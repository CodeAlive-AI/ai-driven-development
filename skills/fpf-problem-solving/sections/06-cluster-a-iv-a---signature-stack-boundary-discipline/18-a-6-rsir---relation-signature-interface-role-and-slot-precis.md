## A.6.RSIR - Relation, Signature, Interface, Role, and Slot Precision Restoration

> **Type:** FPF precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.6.RSIR:0 - Use This When

**Plain name.** Relation-signature-interface-role-slot recovery.

Use this pattern when relation, signature, interface, role, role-holder grammar such as `Holder#Role:Context`, assignment, enactment, slot, field, parameter, argument, endpoint, port, API, protocol, capability, affordance, method, function, concern, interest, Markov-blanket, computational-boundary, or active-inference-boundary wording hides which FPF object or claim kind is current.

**Primary EntityOfConcern.** The EntityOfConcern is one encountered use of an ambiguous engineering phrase together with the claim that this use is intended to carry. RSIR recovers the direct governed object, direct relation and participant meaning, actual participant, declaration-local `SlotSpec` or operation declaration, exact operation application and binding, assertion- or description-side designation, representation position and correspondence, or claim before selecting its governing pattern. The phrase remains wording in an episteme or in speech; it is not the world-side object, occurrence, value, or relation named by the recovered claim.

**Primary working reader.** The first reader is an FPF pattern author, reviewer, or practitioner repairing a phrase before selecting the direct governing pattern. The downstream reader is the engineer, manager, analyst, or steward who needs the repaired phrase to preserve useful project language without minting a shadow ontology.

**First useful move.** Recover the project concern first, then recover the current governed EntityOfConcern or claim kind. Apply the direct governing pattern as soon as it is clear. Keep a reduced-use source label only when no governed value is being asserted.

**What goes wrong if missed.** The same word is used for differently governed objects without saying which claim is current. For example, `interface` may denote an API description, reusable signature, functional port, compatibility claim, or module-boundary relation; `role` may denote a work-facing `U.Role` or be misused for a direct relation-participant meaning, a declaration-local `SlotKind`, or a representation position. A later reader then cannot recover which relation obtains, which actual participant is meant, which `SlotSpec` or operation declaration is current, whether an exact application binds an actual value, or which representation correspondence is intended.

**What this buys.** The reader gets one small recovery move before the direct pattern is applied. The repair preserves useful engineering words while preventing a lexical cue from minting a new root kind or collapsing direct participation, reusable declaration, assertion or description, exact operation application and binding, and representation correspondence.

**Not this pattern when.** Do not use `A.6.RSIR` after the direct governing pattern is already clear. Do not use it for general relation repair after `A.6.P` is selected, for slot discipline after `A.6.5` is selected, for function-like repair after `A.6.F` is selected, for module-interface repair after `A.6.M` is selected, for transformation wording after `A.3.4.P` is selected, or for publication and description repair after `E.17`, `C.2.1`, or `C.2.P.DR` is selected.

### A.6.RSIR:1 - Problem frame

The RSIR cluster sits at a common failure point in FPF texts. A project team sees one word and treats it as if it already selected the ontology:

- "role" in a work assignment, direct relation-participant meaning, declaration-local `SlotKind`, representation argument, RBAC-like status, or evidence use;
- "interface" in a module relation, functional port, API description, protocol, signature, or publication view;
- "slot", "field", "parameter", or "argument" in wording about an actual relation participant, a `RelationSignature` declaration, an A.6.1 argument or result declaration, one actual operation application and bound value, a data, formula, or method-call representation, or ordinary prose;
- "signature" in a law-governed declaration, API shape, interface specification, or plain sign-off phrase;
- "function" in architecture, capability, method, work, mathematical modeling, or quality wording.

`A.6.RSIR` is the first-level recovery pattern for this bounded cluster. It does not decide every neighboring subject ontology. It helps the practitioner recover which object or claim is current and then stop at the direct governing pattern.

### A.6.RSIR:2 - Problem

Without this pattern:

1. **Lexical cues create shadow kinds.** Interface, role, slot, endpoint, and function words become local root kinds because they sound technical.
2. **Participant, declaration, and representation uses become roles.** A direct relation-participant meaning, a declaration-local `SlotKind`, or an argument, field, or endpoint in a selected representation is called a role and then confused with `U.Role`; evidence-use, transformation, and interface claims lose their direct owners.
3. **Role values become declaration or representation labels.** A real `U.Role` is demoted into a declaration-local `SlotKind` or a source-schema field, so the role-taxonomy episteme, effective reference scheme, assignment occurrence, assignment window, role state, and work consequences can no longer be recovered.
4. **Signatures absorb implementations.** A law-governed `U.Signature` is used as if it were a mechanism, method, work-start gate decision, interface conformance proof, or publication.
5. **Participant, declaration, application, and representation boundaries are skipped.** A field or parameter is edited without deciding whether it denotes a direct relation-participant meaning or actual participant, a declaration-local `SlotSpec`, an A.6.1 argument or result declaration, one exact operation application and actual binding, or a position in a selected representation.
6. **Evidence and status uses keep old role grammar.** An episteme, standard, report, publication, or badge is said to have a role instead of being used in an evidence-use, source-use, status-use, publication-use, assurance-use, or gate relation.
7. **Neighboring patterns are copied locally.** A pattern repeats negative catalogues such as "not proof, not permission, not gate" instead of recovering the current object and applying the pattern that governs the claim.

### A.6.RSIR:3 - Forces

| Force | Tension |
|---|---|
| Recognition vs ontology | Engineering words are useful entry cues, but FPF use needs the governed object or claim kind. |
| First-level repair vs overreach | The pattern must recover enough to choose the direct pattern without becoming a second ontology for relation, role, interface, capability, method, function, evidence, or status. |
| Declaration and binding precision vs role ontology | A `U.Role` value may be an actual direct-relation participant or an actual value bound in one exact operation application. A compatible `SlotSpec` or A.6.1 `ArgumentDeclaration` may type the respective reusable use, but participant, declaration content, exact application, binding occurrence, assertion-side designation, and representation position remain distinct. |
| Interface usefulness vs interface-as-kind collapse | Interface words are often useful, but they may point to several different governing patterns. |
| Minimal rewrite vs precision | Ordinary prose can remain ordinary; claim-bearing prose must name the governed object, direct relation use, declaration, or representation correspondence on which it relies. |
| Source label preservation vs misuse | A source label can remain quote-only or reduced-use, but it cannot silently make work, evidence, assurance, gate, publication, or architecture claims admissible. |

### A.6.RSIR:4 - Solution

Use `A.6.RSIR` as a first-level recovery move. `RSIRRepairNote` is optional working support, not a required record, schema, or publication layout. Omit every branch that is not current. The ordinary path may stop after `projectConcern`, `recoveredEntityOfConcernOrClaimKind`, `selectedDirectGoverningPattern`, and one result stated as `retainedSourceLabelUse`, `blockedOverread`, or `nextAdmissibleUse`.

```text
RSIRRepairNote (optional working support; keep only current lines):
  projectConcern:
  recoveredEntityOfConcernOrClaimKind:
  selectedDirectGoverningPattern:
  retainedSourceLabelUse?:
  blockedOverread?:
  nextAdmissibleUse?:
  encounteredWording?:
  currentUse?:
  directParticipantMeaningAndActualParticipant?:
  relationDeclaration?:
  assertionOrDescriptionDesignation?:
  operationDeclaration?:
  exactOperationApplicationAndBinding?:
  representationUseAndCorrespondence?:
  neighboringCandidateValues?:
  stopCondition?:
```

When the optional note is used, it is complete when the current object or claim kind is clear enough to apply the direct governing pattern, keep ordinary prose, keep quote-only wording, or stop the stronger claim. No unused branch is filled for completeness.

#### A.6.RSIR:4.1 - Recovery order

1. **Recover the project concern.** Say what the project is trying to do: assign work responsibility, declare a signature, check an interface, compare functions, name a port, use evidence, assert status, describe a method, or make another claim.
2. **Recover the current governed object or claim kind.** Decide whether the wording points to a direct relation or participant meaning, an actual participant, a reusable `RelationSignature` or `SlotSpec`, an assertion- or description-side participant designation, an A.6.1 argument or result declaration, one exact operation application and actual binding, a representation position and correspondence, a signature, interface claim, role value, role assignment, role description, port, boundary claim bundle, capability, affordance, method, function, concern, interest, publication, source label, or ordinary prose.
3. **Name the direct governing pattern.** Use the table in `A.6.RSIR:4.2` only until the governing pattern is clear.
4. **Separate direct participation, reusable declaration, and assertion or description.** Use `A.6.5` only when one complete `SlotSpec` in one exact `RelationSignature` is current. The direct relation pattern governs participant meaning, actual participants, obtaining, and occurrence identity. If an assertion or description episteme designates a participant, `C.2.1` governs that episteme's identity and content, while the direct assertion, evaluation, evidence-use, or description family governs the exact predicate, polarity, or use relation. When a compatible `SlotSpec` is current, `A.6.5` governs the designation's `ValueKind` and `refMode` discipline; an ordinary assertion may instead name actual participants directly without opening a reusable `RelationSignature`.
5. **Separate operation declaration, actual application and binding, and representation.** `A.6.1` governs declaration-local `ArgumentDeclaration` and `ResultDeclaration` content. Open an actual operation-application binding only after one exact application has been independently identified and its actual bound value matters to a receiving claim. Keep a method-call, formula, tuple, edge, or schema place under `C.29` or its exact representation owner and state correspondence separately.
6. **Keep the source label reduced-use when no governed claim is current.** A word can remain a cue, quotation, title, or local shorthand without being admitted as FPF-governed vocabulary.

Use Tech `position` only for a place in a selected representation, such as a tuple component, formula or method-call argument, graph-edge endpoint, or schema field. Until an explicit correspondence is stated, that position is neither a relation-participant meaning, actual participant, `SlotKind`, `SlotSpec`, nor evidence that the direct relation obtains.

#### A.6.RSIR:4.2 - Direct governing pattern selection

| Recovered object or claim kind | Apply this governing pattern family | RSIR boundary |
|---|---|---|
| direct relation wording | `A.6.P` for recovery, then the direct relation pattern; use `A.6.REL` only when a receiving claim needs explicit occurrence identity or reference | RSIR stops when the direct relation pattern is selected. Ordinary readable assertion may stop before explicit occurrence individuation or identifier assignment. |
| direct relation-participant meaning or actual participant | the direct relation pattern; add `A.6.5` only if a receiving use needs a reusable typed declaration | State the participant meaning and actual participant directly. Neither one is a `SlotKind`, `SlotSpec`, designation, operation binding, or representation position. |
| reusable relation-declaration slot, field, parameter, argument, or endpoint | `A.6.5` for one complete `SlotSpec` inside one exact `RelationSignature`, with `A.6.0` for the containing signature | The `SlotKind` is declaration-local and corresponds to one already recovered participant meaning; the declaration does not make the relation obtain. |
| assertion- or description-side participant designation | `C.2.1` for episteme identity and content; the direct assertion, evaluation, evidence-use, or description family for predicate, polarity, and use; `A.6.5` only when a compatible current `SlotSpec` types the designation | An ordinary assertion may name actual participants directly. A typed designation remains episteme content: it is neither the actual participant nor evidence that the direct predicate obtains. |
| operation argument or result declaration | `A.6.1` and the exact mechanism edition and operation declaration | `ArgumentDeclaration` and `ResultDeclaration` are declaration content. Do not reuse relation `SlotSpec` vocabulary for them. |
| exact operation application or declaration-local argument or result binding | `A.6.1` and the exact mechanism edition and operation declaration | Identify the application occurrence independently; assert a binding only for the exact application and actual bound value under the declared predicate. Do not admit public `OperationApplication`, a universal input/output/result relation, or infer production, a produced entity, result episteme, evidence, or work from a result binding. |
| tuple component, formula or method-call argument, graph-edge endpoint, schema field, or other representation position | `C.29` or the exact representation or publication owner | Keep the position inside that representation and state explicit correspondence when an FPF claim consumes it; do not turn it into a relation participant, declaration, or actual binding by form. |
| signature or law-governed declaration | `A.6.0`; use `A.6.5` only for `SlotSpec` declarations inside a `RelationSignature`, and `A.6.1` for operation argument and result declarations | Do not put mechanisms, methods, work, evidence, actual participants, operation applications or bindings, or representation positions into signature identity-bearing content. |
| role value | `A.2`, role-description and naming patterns in Part F | Do not treat the role as a `SlotKind`, capability, method, or status. |
| role assignment | `A.2.1`, `A.15`, and `A.6.5` only when reusable `SlotSpec`s are current | The four participant meanings are holder system, role value, role-taxonomy episteme, and effective reference scheme; the actual participants retain those direct kinds. A reusable `U.RoleAssignment` `RelationSignature` declares matching `SlotSpec`s with `HolderSystemSlot`, `RoleValueSlot`, `RoleTaxonomyEpistemeSlot`, and `EffectiveReferenceSchemeSlot`. `AssignmentInterval` is assertion- or occurrence-description content; actual extent follows uninterrupted obtaining. A selected model-use structure remains designated only by a receiving assertion or use unless a separately governed relation species makes it a required participant. Evidence, status, capability, and performed work remain direct neighboring claims. |
| role state or role relation structure | `A.2.5`, `A.2.7` | Do not infer role relation structure from ordinary label chains. |
| role description or durable role name | `F.4`, `F.5`, `F.18`, and `F.17` when public or cross-context reuse is current | Do not hide capability, method, or work inside the name. |
| role enactment wording | `A.15.1`, `A.2.1`, and `F.6` | Recover the exact dated `W : U.Work` occurrence and one exact obtaining `RA : U.RoleAssignment`. Use `performedUnderAssignment(W, RA)` or the Plain sentence `S performed W under RA`, where admitted `S : U.System` is `RA.HolderSystemSlot` and is the actual performer. Do not introduce a second enactment object beside work and assignment. |
| module interface or architecture interface | `A.6.M` for module-interface claims; `C.30`, `C.30.ASV`, `C.30.AD`, or `C.30.TFS-REL` for architecture-of, structural-view, architecture-description, or transformation-flow-structure claims; `A.6.0` plus `A.6.5` only for a reusable `RelationSignature` and its complete `SlotSpec`s; `C.29` or the exact representation owner for interface diagrams or schema positions and their correspondence | Do not create generic `U.Interface`. |
| Markov blanket, Markov border, computational boundary, boundary leak, or active-inference boundary | Recover the current claim before choosing a pattern: accepted local Markov dynamics (`A.3.3`), mathematical or probabilistic lens (`C.29`, sometimes `C.26`), viability or measure-model-act envelope (`C.26.3`), holon delimitation or boundary crossing (`A.1` plus the direct governing relation pattern), relation precision (`A.6.P` after a relation-bearing case is recovered), reusable `RelationSignature` and `SlotSpec` declaration (`A.6.0`, `A.6.5`) or representation position and correspondence (`C.29` or the exact representation owner), module-interface or interface-specification claim (`A.6.M`), functional port or functional element (`A.6.F`), physical component (`A.14`, `C.13`, `B.3.5`), boundary description or publication (`C.30.AD`, `E.17`), agency-threshold claim (`A.13`, `A.19`, `C.16`), or boundary-package statement classification (`A.6.B`) only when L, A, D, or E classification is the recovered object. | Do not create `U.MarkovBlanket`, generic `U.Boundary`, generic `U.Interface`, or binary `U.Agent`; do not treat a statistical separation, interface, interface module, physical component, description, and boundary-package classification as the same object. |
| functional port or functional structure | `A.6.F`, `A.3.4`, `E.18`, `C.30.TFS-REL` | Do not equate port, function, module interface, and signature by vocabulary alone. |
| API, protocol, connector, service-access wording | Recover the governed object first: `E.17` for API or interface-description publication; `A.6.0` and `A.6.5` for a reusable `RelationSignature` and its `SlotSpec`s; `C.29` or the exact API-description owner for schema or representation positions and explicit correspondence; `A.6.M` for module-interface claims; `A.6.C` only when recovered protocol, contract, SLA, or agreement-like wording bundles promise, utterance or publication, governance, Work or consequence, or evidence claims; `A.6.P:4.11a` when service or service-access wording still hides its exact referent or direct relation; `A.6.B` only for L, A, D, or E statement classification inside a boundary package. | API may be description, protocol episteme, exact service/access referent or direct relation, signature, publication, module interface, representation, or boundary-package statement classification. |
| capability | `A.2.2`; method, work, evaluation, or gate patterns only when they use an explicit capability criterion | Role labels and interface labels do not establish or demonstrate capability. |
| affordance or action invitation | `A.6.A` | Do not rename affordance as role, interface, or capability until the direct pattern admits it. |
| method, method description, work plan, or dated work | `A.3.1`, `A.3.2`, `A.15`, `A.15.1`, `A.15.2` | Method, description, plan, and work are distinct even when source wording says process. |
| function or functional wording | `A.6.F` | Function-like wording can point to several patterns; `A.6.F` governs that recovery. |
| concern, interest, viewpoint, problem, or characteristic-space selection | `A.7` for EntityOfConcern and description distinction; `C.22` or `C.22.2` for problem-card claims; `E.17.0` or `E.17.2` for viewpoint or view claims; `F.4` or `F.18` for role-description or naming cases; `A.19` or `E.21` for characteristic-space cases | Do not mint generic `U.Concern` or `U.Interest` by wording alone. |
| publication, description, declarative representation, source wording | `C.2.1`, `E.17`, `C.2.P.DR`, `E.10`, `E.10.ARCH` | Do not let description or publication use displace the EntityOfConcern selected by the project concern. |

#### A.6.RSIR:4.2.1 - Relation-defined wording dispatch

When wording derives a qualification, status, or category from participation in a relation, recover the object needed by the next use before naming it:

1. If the claim concerns an actual entity participating under one named relation-participant meaning, state the direct relation, that meaning, and the actual participant. The participant retains its direct kind.
2. If reusable typed declaration is current, use `A.6.5` for the corresponding `SlotSpec` inside one exact `RelationSignature`. Its `SlotKind` is declaration-local and neither is the participant nor makes the relation obtain.
3. If an episteme asserts, evaluates, or describes the participation, `C.2.1` governs the episteme's identity and content, while the direct assertion, evaluation, evidence-use, or description family governs the exact predicate, polarity, or use relation. When a compatible `SlotSpec` is current, `A.6.5` governs the participant designation's `ValueKind` and `refMode` discipline; without reusable declaration, the assertion may designate the actual participants directly.
4. If repeated local quantification over such actual participants is current, use `C.3` and `C.3.1` for the local `U.Kind`, membership rule, and extent rule. Neither the participant-meaning label nor the declaration-local `SlotKind` admits that kind.
5. If the source exposes a tuple component, argument, edge endpoint, schema field, or other representation position, keep it under `C.29` or the exact representation owner and state an explicit correspondence before an FPF claim consumes it. A value shown at that position establishes neither actual participation nor relation obtaining.

For parameter, argument, or result wording, separately recover the A.6.1 declaration content, one independently identified exact operation application and any obtaining declaration-local binding, and the selected representation position. Open the binding only when the actual bound value matters to a receiving claim. Neither the declaration nor representation syntax establishes the binding; a result binding is distinct from production, a produced entity, a result episteme, evidence, and work.

When a receiving use compares or constrains a whole organization of relation occurrences, `A.22` may govern a selected `U.Structure`. One actual participant, corresponding `SlotSpec` or designation, operation binding, or representation position does not by itself establish such a structure.

#### A.6.RSIR:4.3 - Replacement candidate rule

Do not replace one umbrella with another. The minimum admissible repair candidate names:

- the current object or claim kind;
- the governing pattern;
- one result current for the receiving use: a retained reduced-use source label, a blocked stronger reading, or the next admissible use.

Name a direct relation, claim-bearing episteme, declaration-local `SlotSpec`, A.6.1 operation declaration or actual application binding, or representation correspondence only when that exact object is current for the receiving use. Do not fill an unused branch or require both a retained source-label use and a blocked overread. If the minimum cannot be named, leave the phrase in quote-only or reduced-use form and record the blocker.

#### A.6.RSIR:4.4 - Reduced-use source labels

Reduced-use labels are allowed. They are not failures. A source label remains reduced-use when it helps readers find or recognize the case but does not carry FPF-governed content.

Examples:

- "API role" can remain a quoted source phrase while the repair separately names the actual governed claim: a software API description, a provider role assignment, a promise-content episteme under `A.2.3`, a separately obtaining commitment under `A.2.8`, `PromiseContentUse`, a delivery or acceptance relation under its direct owner, another named direct relation, or an interface specification.
- "parameter" can remain ordinary prose while a complete `SlotSpec` is named only for a current reusable relation declaration, an operation `ArgumentDeclaration` or `ResultDeclaration` and any exact application binding stay under `A.6.1`, and a method-call, formula, or other representation position stays under `C.29` or its exact representation owner.
- "function" can remain ordinary engineering language when no architecture, capability, method, work, mathematical, quality, or module claim depends on it.

#### A.6.RSIR:4.5 - Shortcut Cost and Reopen Condition

`A.6.RSIR` is a deliberately weak first-level repair note. The baseline is full use of the direct governing pattern: `A.6.P` for relation repair, `A.6.5` only for reusable `RelationSignature` `SlotSpec` discipline and compatible participant-designation typing, `C.2.1` plus the direct claim family for assertion or description content, `A.6.1` for operation declarations and any exact application binding, `C.29` or the exact representation owner for positions and correspondence, `A.2` and `A.2.1` for role and role assignment, `A.6.M` for module-interface, `A.6.F` for function-like repair, or the evidence, status, publication, architecture, method, work, gate, or problem pattern named by value.

The saved effort is that a practitioner does not run several full patterns before knowing which one is current. The loss budget is narrow: RSIR may select a governing pattern, preserve a reduced-use source label, or record a blocker. It may not decide the role assignment, signature, operation application or binding, evidence-use relation, status assertion, exact service/access referent or direct relation, architecture description, or method relation that belongs to the selected pattern.

Reopen RSIR when the selected pattern shows that the source phrase carried more than one governed object, the object kind was selected too early, a needed slot distinction was missed, or evidence, status, publication, gate, method, work, architecture, capability, or concern claims were folded into one label. The reopened repair splits the phrase into multiple governed values or keeps the excess wording reduced-use.

### A.6.RSIR:5 - Archetypal Grounding

**System case: module interface claim.** A team says "the cooling module exposes the heat-exchanger interface." RSIR first asks what claim is current. If the claim is substitutability or separate change, use `A.6.M`. If a reusable relation declaration for exchanged-medium and boundary-condition participant meanings is current, use `A.6.0` plus `A.6.5` for the `RelationSignature` and complete `SlotSpec`s. If the current use is a diagram, API schema, or other representation, keep its positions under `C.29` or the exact representation owner and state explicit correspondence. If the claim is a functional port in a transformation-flow structure, use `A.6.F`, `A.3.4`, and `E.18`. RSIR does not create `U.Interface`.

**Role case: API provider role.** A source says "the API role is provider." RSIR first recovers what participates in work. If `provider` is a work-facing role, use `A.2.1` to name the holder system, `ProviderRole`, role-taxonomy episteme, effective reference scheme, and assignment window. Add a model-use structure only when an independently selected DDD-style organization changes interpretation. If the API is a publication or protocol description, use `E.17` for publication; use `A.6.P:4.11a` when service or service-access wording hides the concrete subject or relation. Send promise content to `A.2.3` and an accountable provider or consumer commitment to `A.2.8`. For protocol, contract, SLA, or agreement-like boundary wording that bundles several claims, use `A.6.C` to unpack them before sending each recovered object to its direct owner; if module-interface semantics are current, use `A.6.M`; if boundary-package statement classification is current, use `A.6.B`. Do not assign a work role to the API description.

**Evidence case: reviewer evidence role.** A report says "reviewer evidence role approved the gate." RSIR blocks the composite. `ReviewerRole` may be assigned to an admitted `U.System` under `A.2` and `A.2.1`. A report episteme may be used in an evidence-use relation under `A.10`, `B.3`, `F.10`, or `E.17`. A gate approval may be a gate decision under `A.21` or a speech-act case under `A.2.9`. No episteme gets a work role by being evidence.

**Slot case: method parameter.** A method description says "parameter target controls the model." That sentence has no exact governor in this case, so it is not retained as the repaired claim; keep `target` only as a reduced-use source label and write one positive A.6.1 use instead. In the current `recognizeAdmittedHolonCandidate` declaration, `candidate` is an `ArgumentDeclaration` meaning one exact entity being evaluated, with `ValueKind = U.Entity`; `recognitionJudgment` is the declared result meaning. Under A.6.1, the project independently identifies the bounded recognition-evaluation invocation `P-37` by that declaration's application predicate, identity rule, and extent rule. During `P-37`, Pump #37 is actually bound under `candidate`, and the returned value `unknown` is bound under `recognitionJudgment`. In a call representation such as `recognizeAdmittedHolonCandidate(target = Pump-37, ...)`, the named-argument position `target` corresponds to the declared `candidate` meaning but is neither the declaration nor either binding. The practitioner writes: "`target` is the call label; A.6.1 declares `candidate : U.Entity`; during exact application `P-37`, Pump #37 is bound as candidate." Stop there unless the receiving claim needs the result binding or another direct owner.

#### A.6.RSIR:5.1 - Near-Miss Checks

| Source phrase | Positive recovery | Near miss to reject |
|---|---|---|
| "API role is provider" | `ProviderRole` and `U.RoleAssignment` when an admitted `U.System` participates in work; `E.17` when the API phrase names a publication; `A.6.P:4.11a` when service or service-access wording hides the exact referent or direct relation; `A.6.C` only when recovered protocol, SLA, or agreement-like wording bundles promise, utterance or publication, governance, Work or consequence, or evidence claims. | Do not assign a work-facing role to the API description or protocol itself. |
| "endpoint parameter source" | Use the direct relation owner when the phrase hides a participant meaning or actual participant; use `A.6.5` only for a complete `SlotSpec` in a current reusable `RelationSignature`; use `A.6.1` when it names an operation `ArgumentDeclaration`, `ResultDeclaration`, or an actual binding in one independently identified exact application; use `C.29` or `E.17` when it is a representation position or API description, and `A.6.P:4.11a` when a service-documentation label hides the concrete subject or relation; state explicit correspondence whenever the FPF claim consumes the representation. | Do not create an endpoint kind, a work-facing role from the word "source", a parameter ontology, a public application kind, a universal input/output relation, or a world-side participant or binding from representation shape. |
| "`Engineer-7#Verifier:Lab-A`" | Recover `Engineer-7` as the holder `U.System`, `VerifierRole` as the role value, and name the role-taxonomy episteme, effective reference scheme, and assignment window under `A.2.1`. In this case `Lab-A` is the actual facility system in which verification work occurs; state that work relation separately when it is current. | Do not put `Lab-A` into role-assignment identity or keep `Holder#Role:Context` as normative ontology. |
| "function of the pump" | `A.6.F`, `A.3.4`, `E.18`, or `C.30.TFS-REL` when the phrase names functional structure; `A.2.2` when it names a system capability. | Do not treat "function" as the recovered kind before the current claim is known. |
| "standard evidence role" | `A.10`, `B.3`, `F.10`, or `E.17` when a standard episteme is used as evidence, source, status, or publication. | Do not keep `U.EvidenceRole` or put the standard episteme into `U.RoleAssignment`. |

### A.6.RSIR:6 - Bias-Annotation

This pattern has a relation-cluster bias because it sits in A.6. It mitigates that bias by stopping as soon as the direct governing pattern is clear.

It has an interface and software-language stress case because API, endpoint, protocol, and interface wording often enters from software. The pattern deliberately keeps the recovery general: architecture interfaces, physical ports, functional ports, service-access descriptions, and publication forms are all possible, and none is selected by word choice alone.

It resists semio-bias by keeping descriptions, publications, records, reports, standards, and source labels under the patterns that govern those objects and uses: `C.2.1`, `E.17`, `C.2.P.DR`, `A.10`, `B.3`, `F.10`, `C.28`, `E.10`, or `E.10.ARCH` when those objects or uses are current. A source label may help recognition; its presence is not evidence that the denoted object is the current EntityOfConcern or that a proposed action is admissible.

### A.6.RSIR:7 - Conformance Checklist

1. The repair starts with project concern, not with a replacement word.
2. The current EntityOfConcern or claim kind is named before a direct governing pattern is applied.
3. The repair stops at the direct governing pattern once it is clear.
4. When reusable relation declaration is current, slot discipline uses `A.6.5` and states one complete `SlotSpec = <SlotKind, ValueKind, refMode>` inside one exact `RelationSignature`; actual participants and representation positions remain outside it.
5. Role claims preserve the four participants of generic `U.RoleAssignment` and derive occurrence extent from uninterrupted obtaining; claims about role description, role state, selected role relation structure, capability, method, planned work, and performed work exit to their direct patterns.
6. Evidence-use and status-use cases are not represented through `U.RoleAssignment` for epistemes.
7. Interface wording is kept as a recognition cue but is not admitted as generic `U.Interface`.
8. Every neighboring object family selected in the dispatch table exits to its direct governing pattern rather than being redescribed inside RSIR.
9. Relation-defined wording dispatches separately to the direct participant meaning and actual participant; a declaration-local `SlotSpec` when reusable typing is current; an assertion- or description-side designation whose episteme identity and content stay with `C.2.1`, whose predicate, polarity, and use stay with the direct claim family, and whose typing stays with `A.6.5` only when a compatible `SlotSpec` is current; a C.3 local kind when repeated quantification is current; or a representation position plus explicit correspondence. It does not create one umbrella qualification object.
10. Operation wording keeps A.6.1 `ArgumentDeclaration` or `ResultDeclaration` content, one independently identified exact application and obtaining argument or result binding, and any call or formula representation position distinct; it infers neither a public application kind nor production, a produced entity, a result episteme, evidence, or work from the binding.
11. Quote-only or reduced-use labels carry no action-facing claim beyond the claim admitted by the selected governing pattern.

### A.6.RSIR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
|---|---|---|
| Rename `role` to `position` everywhere | It loses real `U.Role` cases and can create a new umbrella. | Recover whether the current use is a `U.Role`, direct relation-participant meaning, actual participant, declaration-local `SlotSpec`, representation position and correspondence, evidence-use relation, status assertion, or ordinary prose. |
| Treat interface as one root kind | It merges module, functional, protocol, API, signature, publication, representation, architecture, and boundary-package claims. | Recover the governing object first; then apply `A.6.M` for module-interface, `A.6.F` for functional port or functional structure, `A.6.0` plus `A.6.5` for a reusable `RelationSignature` and its `SlotSpec`s, `C.29` or the exact representation owner for positions and explicit correspondence, `E.17` for publication or API-description cases, `A.6.C` only when recovered agreement-like, protocol, or SLA wording bundles promise, utterance or publication, governance, Work or consequence, or evidence claims, `A.6.P:4.11a` when service or service-access wording hides its exact referent or direct relation, `A.6.B` only for L, A, D, or E statement classification inside a boundary package, or `C.30`, `C.30.ASV`, `C.30.AD`, or `C.30.TFS-REL` for architecture claims. |
| Put evidence and status into RoleAssignment | It gives epistemes a work-facing role assignment they do not have. | Use evidence-use, source-use, status-use, assurance-use, or publication-use relations under `A.10`, `B.3`, `F.10`, `E.17`, `C.2.1`, or `C.28` when those relations are current. |
| Use `A.6.5` as relation identity | Slot discipline does not say which relation is being asserted. | Apply `A.6.P` or the relation-specific pattern for relation identity; use `A.6.5` only for SlotSpecs. |
| Treat function as the recovered kind | Function-like wording may point to capability, method, work, architecture, mathematical function, quality, or module allocation. | Apply `A.6.F` after RSIR selects function-like recovery. |
| Keep a quoted source label but use it as governing content | Reduced-use wording becomes hidden FPF vocabulary. | State the retained source-label use and blocked overread. |

### A.6.RSIR:9 - Consequences

`A.6.RSIR` adds a small first-level decision before heavy repair. That extra step prevents E.10 from carrying substantive recovery content and prevents each neighboring pattern from repeating the whole RSIR diagnosis.

The pattern also keeps useful source vocabulary alive. Engineers can still say interface, API, role, parameter, function, and endpoint. FPF simply refuses to let those words select ontology by themselves.

The cost is one explicit stop: after the direct pattern is clear, RSIR must stop. Otherwise it becomes the giant repair pattern it was created to avoid.

### A.6.RSIR:10 - Rationale

The RSIR cluster needs a first-level pattern because `E.10` should remain a trigger and lexical-governance pattern, while `A.6.P`, `A.6.5`, `A.6.M`, `A.6.F`, `A.2`, `A.15`, and publication, evidence, and status patterns each govern only their respective objects.

The main ontological principle is participant, declaration, application and binding, assertion and designation, and representation separation. An actual direct-relation participant retains its direct kind under one participant meaning. A corresponding `SlotSpec`, when reusable typed relation declaration is current, states a declaration-local `SlotKind`, exact `ValueKind`, and `refMode`. In an assertion or description, `C.2.1` governs the episteme's identity and content, the direct claim family governs predicate, polarity, or use, and `A.6.5` governs participant-designation typing only against a compatible current `SlotSpec`; an ordinary assertion can name actual participants without one. An A.6.1 `ArgumentDeclaration` or `ResultDeclaration` states reusable operation meaning, while one exact application and obtaining binding relate that independently identified occurrence to an actual bound value. A C.29 representation position may correspond to any of those meanings without becoming the participant, declaration, application, or binding.

The second principle is direct governance. Once the current object is recovered, the pattern that governs that object governs the repair. RSIR only identifies the direct governing pattern.

### A.6.RSIR:11 - SoTA-Echoing

This pattern does not introduce new external SoTA sources beyond the source uses already admitted by E.24 for ontic introduction. It applies those source uses to the narrower RSIR recovery problem.

| Practice or source line | Why it matters for RSIR | FPF adoption in this pattern |
|---|---|---|
| Modular ontology design-pattern work, including MODL, MOMo, and commonsense ontology micropatterns such as Shimizu and Hitzler 2024 and Eells, Dave, Hitzler, and Shimizu 2024. | Current ontology-engineering lesson: use small reusable ontology structures without copying local slot doctrine across patterns. | Adopt and narrow: RSIR does not become an ontic registry. It recovers the current governed object, leaves participant meaning and actual participation with the direct relation owner, uses `A.6.5` only for a current `RelationSignature` `SlotSpec`, uses `C.29` or the exact representation owner for positions and correspondence, and uses `E.24` only for durable ontic decisions. |
| Ontology-interoperability lifecycle work such as Qiang 2025 and 2026. | Current caution that overlapping labels and conflicting local concepts become expensive if not settled before reuse, matching, and validation. | Adapt as prevention: interface, role, slot, function, method, and concern words remain recovery cues until the current EntityOfConcern, direct relation and participant meaning, actual participant, any declaration-local `SlotSpec`, any representation position and correspondence, and the direct governing pattern are named by use. |
| Process-representation ODP work such as Norouzi, Hertling, Waitelonis, and Sack 2025. | Current warning that process and workflow ontologies often hide implicit patterns from domain users. | Adapt for RSIR source labels: "process", "workflow", "method", "function", "parameter", and "interface" may remain useful source labels, but they do not carry FPF-governed content until the direct method, work, transformation-flow, role, slot, publication, or evidence pattern is selected. |
| gUFO, UFO, and OntoUML role, relator, situation, and high-order type practice, including Almeida, Guizzardi, Sales, and Fonseca 2026. | Current foundational-ontology constraint against flattening role values, participant meanings, declaration-local slots, representation positions, status classifications, and evidence uses into one taxonomy. | Adopt the boundary: `U.Role` and `U.RoleAssignment` remain work-facing; direct patterns govern participant meanings and actual participants; `A.6.5` governs declaration-local `SlotSpec`s; `C.29` or the exact representation owner governs positions and correspondence; evidence-use and status-use of epistemes use direct evidence, status, source, publication, assurance, or gate relations rather than `U.RoleAssignment`. |
| Current engineering architecture practice around functions, ports, modules, interfaces, signatures, and views. | Accepted internal-practice constraint from `A.6.M`, `A.6.F`, `A.6.0`, `E.18`, `C.30`, `C.30.ASV`, `C.30.AD`, and `C.30.TFS-REL`: these words are related but do not name one root kind. | Adapt as a positive recovery map: preserve interface and function language as recognition cues, then recover module-interface, signature, functional port, transformation-flow, architecture-of, structural-view, architecture-description, API publication, protocol, or plain source-label use by current claim. |

### A.6.RSIR:12 - Relations

`E.10` detects trigger wording. `E.10.ARCH` states that RSIR is the first-level restoration pattern for this bounded cluster when the direct governing pattern is not already clear.

`A.6.5` governs complete declaration-local `SlotSpec = <SlotKind, ValueKind, refMode>` content inside one exact `RelationSignature` and, only when a compatible `SlotSpec` is current, participant-designation typing. `C.2.1` still governs the assertion or description episteme's identity and content, and the direct claim family governs predicate, polarity, and use. An ordinary assertion may designate actual participants directly without reusable declaration.

`A.6.P` governs relation precision restoration after the recovered object is a relation or relation-bearing claim.

`A.6.0` governs `U.Signature`; `A.6.1` governs operation argument and result declaration content plus any independently identified exact application and declaration-local binding; `E.20` governs mechanism introduction. A.6.1 admits no public `OperationApplication` U-kind or universal input/output/result relation, and its result binding alone establishes none of production, a produced entity, a result episteme, evidence, or work.

`A.2`, `A.2.1`, `A.2.2`, `A.2.5`, `A.2.7`, `A.15`, and Part F role-description and naming patterns govern role, role assignment, capability, role state, role relation structure, role-method-work, and durable role-name claims.

`A.6.M`, `A.6.F`, `A.6.A`, `A.3.4.P`, `E.18`, `C.30`, `C.30.ASV`, `C.30.AD`, and `C.30.TFS-REL` govern module-interface, functional, affordance, transformation, transformation-flow, architecture-of, structural-view, and architecture-description cases.

`C.2.1`, `E.17`, `C.2.P.DR`, `A.10`, `B.3`, `G.6`, `F.10`, and `C.28` govern episteme identity and content, publication, declarative representation, evidence, assurance, provenance, status, and causal-use cases; the exact direct claim family still governs the predicate, polarity, or use asserted through that content.

### A.6.RSIR:End

