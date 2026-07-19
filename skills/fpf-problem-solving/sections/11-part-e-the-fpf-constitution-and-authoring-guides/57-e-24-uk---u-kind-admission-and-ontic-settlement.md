## E.24.UK - U-kind Admission and Ontic Settlement

> **Type:** Part E FPF authoring discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### E.24.UK:0 - Use This When

Use this pattern when an FPF text, heading, title, filename, ToC row, table, or source passage presents a candidate `U.*`, type, kind, or subkind distinction and the author must decide whether FPF admits that classificatory distinction as a durable U-kind or instead reuses an already admitted durable U-kind, declares a C.3.2 local kind, or recovers a declaration SlotKind, selected `U.Structure`, episteme or publication form, representation element, or source wording governed elsewhere.

Typical moments:

- a direct relation family has stable occurrence identity and receiving patterns need one common kind for those occurrences;
- a proposed `U.*` name appears in a pattern title, host filename, monolith heading, or ToC row;
- a current pattern uses type, kind, or subkind wording and the governed object is unclear;
- a structural name looks useful for search, but may advertise a false root kind;
- a `RelationSignature` SlotKind, an assertion or description field, a `C.29` representation element, or an `E.24.PUB` reusable form has acquired a `U.*` spelling;
- a single E.24 ontic settlement appears to govern one root U-kind plus several dependent durable U-kinds.

**Primary EntityOfConcern.** The EntityOfConcern is the candidate classificatory distinction: the governed individuals it would classify, their identity or membership rule, the intended extent and non-member boundary, and the claims that would depend on that kind. The admission decision is a claim-bearing episteme recorded through `E.9`; it is not a project-side relation occurrence. A candidate spelling is only a naming input and does not identify or admit the kind.

**Primary working reader.** The first reader is an FPF pattern author or reviewer deciding whether a public FPF name should remain `U.*`. The downstream reader is the practitioner who uses public pattern titles, headings, ToC rows, and names as orientation cues and needs those cues to point to the real governed object.

**First useful move.** Recover the governed individuals, their identity or membership rule, the intended extent and non-member boundary, and the action-facing claim that needs the candidate kind. Then test whether existing U-kinds, direct relations, declaration SlotKinds, C.3 local kinds, or selected structures already preserve that distinction. Judge the public spelling only after the admission disposition is stable.

**What goes wrong if missed.** FPF grows a shadow ontology by punctuation. A slot label becomes a kind, a publication form becomes an ontic, type and kind wording becomes active beside ontic settlement, and a useful title survives because it is searchable rather than because it names the governed object.

**What this buys.** Public `U.*` names become trustworthy. A candidate distinction either passes one explicit root or dependent admission test, or returns to the actual governed object and its direct pattern without creating an umbrella kind.

**Not this pattern when.**

- If the question is whether FPF needs a durable ontic at all, use `E.24`.
- If the question is only detecting an ontic candidate before the durable decision, use `E.24.CD`.
- If the question is the difference among an ontic, its description episteme, publication, and publication form, use `E.24.PUB`.
- If the question is one phrase-level precision issue with no durable name pressure, use `E.10`, `E.10.ARCH`, or the direct precision-restoration pattern.
- If the current governed object is already recovered and only its public label must be chosen, use `F.8`, `F.5`, `F.18`, or `F.17` according to the naming use.

### E.24.UK:1 - Problem Frame

FPF reserves `U.*` names for admitted durable U-kinds. Current source material and older corpus passages can still place that spelling on a declaration-local SlotKind, participant designation, selected structure, publication form, representation element, or unsettled candidate. The spelling is therefore evidence of admission pressure, not evidence of admission.

The current examples in section 4.2 have explicit dispositions. `U.System`, `U.Episteme`, `U.Method`, `U.Work`, `U.Transformation`, `U.Role`, and `U.Relation` are retained root U-kinds under their direct patterns. `U.WorkPlan`, `U.RoleAssignment`, `U.MethodDescription`, `U.Viewpoint`, and `U.View` are retained same-individual dependent kinds; `U.Capability` is retained as an identity-dependent kind under its holder `U.System`. A candidate distinction already covered by an admitted durable U-kind receives `reuse`; a bounded classificatory distinction receives `local-kind` under C.3.2. `U.EpistemePublication` is rejected: Plain `published episteme` is relation-defined wording for contingent participation of one `U.Episteme` in an exact publication occurrence. C.3 `U.Kind` and `U.SubkindOf` remain the governed classification objects and relation used for local typed reasoning; they do not replace ontology-level U-kind admission.

E.24.UK governs this separation. A world-side relation participant keeps its independently governed kind; a `RelationSignature` SlotKind stays declaration-local; an assertion-side designation stays in its claim-bearing episteme; and a publication form or C.29 representation keeps its direct use. It is an E.24 subpattern because U-kind admission depends on ontic settlement, but it is not the head E.24 pattern. E.24 remains the head pattern for `U.Ontic` and ontic introduction. E.24.UK governs the detailed U-kind admission rules.

### E.24.UK:2 - Problem

Without this pattern:

1. **`U.*` spelling substitutes for admission.** A public name is retained because it looks like a kind.
2. **Unsettled type and kind wording competes with U-kind admission rules.** Type, kind, subkind, Concept-Set rows, U-kind names, and E.24 ontics become overlapping ontologies.
3. **A dependent distinction becomes an independent root.** A kind whose individuals retain root identity or depend on one root-kind individual is treated as if it had an independent root settlement.
4. **Structural names over-admit.** Titles, filenames, headings, and ToC rows advertise kindhood more strongly than the pattern body establishes.
5. **Declaration and representation elements become U-kinds.** A participant meaning in a direct relation, a SlotKind in its reusable declaration, an assertion field, or a `C.29` representation element receives a `U.*` spelling even though its governing object is already known.
6. **Naming patterns are asked to do ontology.** F.5, F.8, F.18, or F.17 is used before the governed object has been recovered.

### E.24.UK:3 - Forces

| Force | Tension |
| --- | --- |
| Public mnemonic usefulness vs ontology truth | A `U.*` name can improve discovery; it can also advertise a false governed object. |
| Root stability vs dependent reuse | Some dependent distinctions deserve durable names but retain identity through one root settlement. |
| C.3 typed reasoning vs U-kind governance | C.3 `U.Kind` objects and `U.SubkindOf` occurrences support local typed reasoning, but they are not synonyms for every durable `U.*` distinction. |
| Kernel parsimony vs expressive pattern language | FPF needs useful names, but new U-kinds are expensive and must not replace slots and relations. |
| Host and ToC structure vs prose nuance | A false `U.*` in a title, filename, heading, or ToC row is stronger than a false prose occurrence. |

### E.24.UK:4 - Solution

Treat durable U-kind admission as an ontology decision about one candidate classificatory distinction, not as a relation between a public name and a settlement. Recover the governed individuals, identity or membership rule, intended extent, non-member boundary, and action-facing claims first. Record the decision in a DRR or another claim-bearing episteme under `E.9`; the decision creates no project-side `U.Relation` occurrence.

The compact block below is a publication form for that decision episteme. Its labels prompt decision claims; they are not kind participants, SlotSpecs, or a project-side relation. Treat a filled block as the decision episteme only when its ClaimGraph, exact candidate classificatory distinction as EntityOfConcern, and effective ReferenceScheme are recoverable under C.2.1. Otherwise it remains only a form prompt and no `AdmissionDisposition` may be relied on from it.

Every admitted durable U-kind has one primary E.24-compatible settlement. For a newly admitted durable kind, that settlement establishes exactly one of these forms:

- a root U-kind for a governed subject whose identity and extent are carried by its direct pattern;
- a same-individual dependent U-kind whose direct pattern adds a stable membership condition to individuals already admitted under one root U-kind;
- an identity-dependent U-kind whose direct pattern identifies a distinct individual through an exact dependence on one named root-kind individual plus every additional discriminator.

When no new durable U-kind is admitted, the same decision instead records `reuse` of an exact already admitted durable U-kind, `local-kind` under one exact C.3.2 declaration, or `reject` with the recovered non-kind object and its direct governor.

A public Tech label follows the admission decision through `F.18`. The spelling can improve retrieval, but it supplies neither the classified individuals nor their identity, membership, or extent. `U.Ontic` names the ontology-unit kind and does not replace the subject kind governed by that ontology unit.

Use this compact decision episteme when the admission is contested or load-bearing:

```text
UKindAdmissionDecision:
  DecisionEpistemeIdentity:
    ClaimGraph:
    EntityOfConcern: exact candidate classificatory distinction under decision.
    EffectiveReferenceScheme:
  CandidateGovernedIndividuals:
  CandidateIdentityOrMembershipRule:
  IntendedExtentAndNonMemberBoundary:
  ActionFacingClaimsEnabled:
  ExistingKindAndRelationCoverage:
  E24SettlementRef:
  DirectGoverningPatternRef:
  AdmissionDisposition: root | same-individual-dependent | identity-dependent | reuse | local-kind | reject
  DependentRootUKindRef?:
  SameIndividualMembershipRuleRef?:
  IdentityDependenceRelationAndDiscriminators?:
  ReusedUKindRef?:
  LocalKindDeclarationRef?:
  RejectedCandidateRecoveryRef?:
  CandidateSpelling?:
  NamingPatternIfAdmitted?:
  ReopenCondition:
```

`AdmissionDisposition` is the only disposition field. Supply only the detail required by its value: `DependentRootUKindRef` plus `SameIndividualMembershipRuleRef` for `same-individual-dependent`; `DependentRootUKindRef` plus `IdentityDependenceRelationAndDiscriminators` for `identity-dependent`; `ReusedUKindRef` for `reuse`; `LocalKindDeclarationRef` for `local-kind`; and `RejectedCandidateRecoveryRef` for `reject`. The root case is already completed by `E24SettlementRef` and `DirectGoverningPatternRef`.

The decision episteme describes the selected ontology settlement. It is neither the candidate kind nor any individual classified by that kind. `CandidateSpelling` and `NamingPatternIfAdmitted` remain optional because admission can be settled before the final public name.

#### E.24.UK:4.1 - Positive Test For A Durable U-kind

Test a proposed new durable U-kind against these eight conditions. It may receive `root`, `same-individual-dependent`, or `identity-dependent` only if all eight hold:

1. **Governed individuals.** The candidate classifies identifiable governed individuals, not source expressions, declaration fields, table columns, reference suffixes, publication forms, or mathematical representation elements.
2. **Stable identity or membership.** The direct pattern supplies an identity, grounding, recognition, or membership rule that reidentifies individuals and determines whether they enter the intended extent.
3. **Reviewable witness.** The settlement cites the exact operational witness. For a relation kind, this is the direct relation pattern that governs relation-participant meanings, obtaining, and occurrence identity. For another candidate, use its direct constructive, classificatory, or typed-membership witness. A signature, Concept-Set row, formal declaration, or mathematical trace counts only when its governing pattern states the correspondence to the governed individuals.
4. **Action-facing need.** FPF users need to state, compare, constrain, transform, or otherwise reason about those individuals under this kind; a wording preference alone does not qualify.
5. **Non-duplication.** Existing U-kinds, direct relations, declaration SlotKinds, local C.3 kinds, and selected structures cannot preserve the needed distinction without this durable kind.
6. **Direct governing locus.** One primary governing pattern or accepted governed source set states the kind's identity or membership, intended extent, admissible use, and non-use boundary.
7. **E.24-compatible settlement.** The proposed durable kind has a root, same-individual-dependent, or identity-dependent settlement; the decision names the primary governed subject kind, identity or membership rule, direct governing pattern, named dependent-pattern reliance, and non-use boundary.
8. **By-value dependence.** Current or selected dependent patterns actually rely on the kind by value rather than only repeating its label.

If any positive-admission condition fails, do not force the candidate into a durable root or dependent form. Select `reuse` when an admitted durable kind already covers the distinction, `local-kind` when bounded C.3.2 classification is sufficient, or `reject` when no classificatory distinction remains. Recover the exact direct relation, declaration component, selected structure, episteme, publication form, representation element, or source wording that carries the current claim. Only after disposition is settled may `F.18`, `F.17`, `F.8`, or `F.5` select and expose a public name.

#### E.24.UK:4.2 - Six Admission Dispositions And Current Examples

The typed `AdmissionDisposition` has exactly six values:

1. **`root`.** The candidate classifies individuals whose identity, extent, and recognition are governed by its primary direct pattern.
2. **`same-individual-dependent`.** The candidate classifies individuals already admitted under one root U-kind. The root pattern keeps individual identity; the dependent pattern adds a stable membership condition and an action-facing use.
3. **`identity-dependent`.** The candidate classifies a distinct individual whose identity cannot be stated without one exact dependence on a named root-kind individual. The dependent pattern states that dependence and every additional identity discriminator.
4. **`reuse`.** The needed individuals and distinction are already covered by one admitted durable U-kind. Reuse that exact kind and its direct governing pattern; do not admit a duplicate root or dependent kind.
5. **`local-kind`.** Record this non-admission exit only with one exact current C.3.2 declaration through `LocalKindDeclarationRef`. The distinction remains local under the C.3 family and does not become a root or dependent durable U-kind; E.24.UK does not restate the declaration's internal mechanics.
6. **`reject`.** No durable or local classificatory distinction survives recovery. Keep the exact relation, declaration component, selected structure, episteme, publication object, representation element, or source wording that carries the claim. A contingent qualification whose membership is only temporary participation in a relation belongs here; use Plain relation-defined wording when useful.

Only `root`, `same-individual-dependent`, and `identity-dependent` admit the candidate as a durable U-kind. `reuse`, `local-kind`, and `reject` are distinct exits, not weakened dependent admissions.

The following table is the authoritative disposition for every candidate used as an admission example in this pattern:

| Candidate | `AdmissionDisposition` and constructive form | Governing identity or membership rule | Boundary that preserves the disposition |
| --- | --- | --- | --- |
| `U.System` | `root`; retained root U-kind | `A.1` remains the direct owner of system identity and recognition | role assignment, capability, method enactment, performed work, transformation participation, and evidence remain neighboring relations; none makes an otherwise failing candidate a system |
| `U.Episteme` | `root`; retained root U-kind | `C.2.1` identifies one episteme by exact claim content, exact EntityOfConcern, and effective `U.ReferenceScheme` through `EpistemeConstitutionRelation` | carrier, viewpoint, publication, and dependent-kind membership add no second episteme identity |
| `U.Method` | `root`; retained root U-kind | `A.3.1` governs one semantic way of doing and its method-holarchy identity and composition rules | method description, mechanism, work plan, and dated work remain different governed objects |
| `U.Work` | `root`; retained root U-kind | `A.15.1` is the sole direct owner of the dated performed occurrence and of the judgment that records resolve to it under the declared work-identity tolerances and continuity-policy description | actual change, A.6.1 result-position bindings, domain results, delivery, acceptance, evaluation, and downstream effects retain separate direct owners; none is a work-identity discriminator or a generic work-result relation |
| `U.Transformation` | `root`; retained root U-kind | `A.3.4` identifies one independently grounded actual bounded change through the exact changed referent, temporal extent or formal ordering, boundary conditions, actual pre-boundary, during-boundary, and post-boundary subject facts, and continuity or reidentification rule | a desired, planned, modeled, or asserted change, method, mechanism, work, flow structure, representation, evidence, publication, result, or receiving-use relation remains separately governed; none by itself makes the transformation actual |
| `U.Role` | `root`; retained root U-kind, not an admitted holon kind | `A.2` governs one enactment-facing role value interpreted through one named role-taxonomy episteme and its effective `U.ReferenceScheme` | the holder `U.System`, obtaining `U.RoleAssignment`, taxonomy episteme, reference scheme, selected model-use structure, capability, role state, method admission, work, responsibility, and evidence remain separately governed; a proposed role decomposition returns to A.2.7 and the direct owner of the recovered object or relation |
| `U.Relation` | `root`; retained root U-kind | `A.6.REL` supplies common occurrence discipline and each direct relation pattern supplies participant meanings, obtaining, and occurrence identity | an assertion, description, designator, reference, tuple, or graph edge is not the obtaining occurrence |
| `U.WorkPlan` | `same-individual-dependent` under `U.Episteme`; retained | `A.15.2` recognizes an episteme whose content declares intended `U.Work` over a horizon through plan items and their organization; C.2.1 keeps identity | planned methods, role conditions, windows, budgets, and acceptance targets are plan content or neighboring relations and do not make the intended work occur |
| `U.RoleAssignment` | `same-individual-dependent` under `U.Relation`; retained | `A.2.1` governs an obtaining relation occurrence among holder system, role value, role-taxonomy episteme, and effective reference scheme, continuing while the predicate obtains without interruption for those participants | an interval belongs to an assertion or occurrence description; a model-use structure qualifies only a narrower receiving use unless a direct species makes it required |
| `U.Capability` | `identity-dependent` under the named holder `U.System`; retained | `A.2.2` identifies the holder's ability through holder identity, work family or result class, envelope, measure set, qualification window, and currentness condition | evidence, evaluation, assignment, and actual work remain neighboring relations and do not constitute the capability by record presence |
| `U.MethodDescription` | `same-individual-dependent` under `U.Episteme`; retained | `A.3.2` admits an already identified episteme whose exact EntityOfConcern is one admitted `U.Method` and whose claims, interpreted under the effective `U.ReferenceScheme`, make at least one substantive claim about that method as a way of doing: its transformation or enactment concern, applicability, precondition, effect, bound, or internal method composition; C.2.1 keeps identity | naming the method, giving bibliographic metadata, or stating approval alone does not establish membership; claims about the internal organization of one composite method retain that composite `U.Method` as EntityOfConcern, while claims about an independent relation structure among several methods have the selected `U.Structure` as EntityOfConcern and do not meet this membership rule; adequacy for a receiving use and changes of C.29 representation, publication occurrence, publication form, `U.PresentationCarrier`, approval claim, or work occurrence remain separate |
| `U.Viewpoint` | `same-individual-dependent` under `U.Episteme`; retained | C.2.1 identifies exact episteme P whose EntityOfConcern is one A.22-selected viewpoint-convention `U.Structure`; E.17.0 recognizes membership of that same P only when its fixed claims state the target-kind criterion, exact concerns and stakeholder or audience referents when current, independently admitted episteme kinds, semantic-form and coverage rules, completeness or omission rules, and the describing-use frame; under the effective reference scheme, `ViewpointId i` designates exact P and resolving `U.ViewpointRef r` that uses i yields P, while i, r, and P remain distinct | neither designation nor reference resolution grants `U.Viewpoint` or `U.View` membership; E.17.0 owns membership; `DescriptionContext` is a separate one-viewpoint use qualification whose `viewpointRef` resolves P, selects no view, and establishes no conformance |
| `U.View` | `same-individual-dependent` under `U.Episteme`; retained | E.17.0 recognizes membership of the same episteme E when `EpistemeViewpointConformanceRelation(E,P)` obtains for at least one exact admitted `U.Viewpoint` episteme P; C.2.1 keeps E identity | direct authoring and A.6.3 viewing are construction routes only; selection, rendering, carrier, query execution, publication occurrence, or graphical appearance establishes no view membership |
| `RoleRelationStructure` | `reuse` of admitted `U.Structure`; no new durable U-kind | A.2.7 selects one A.22-governed dependent structure over declared `U.Role` values and exact obtaining role-relation occurrences under the named role taxonomy and effective reference scheme | the selected organization is not a root kind, role holon, role taxonomy, assignment configuration, acting system, or work; participant values and direct relations keep their own governors, and a graph or table remains a representation |
| `MethodRelationStructure@BoundedContext` | `reuse` of admitted `U.Structure`; no new durable U-kind | B.1.5 governs this below-whole-method exit; A.3.1 and A.22 govern the method-side values and the selected context-local structure over their exact direct relations | when actual submethods constitute one composite method, the governed whole is `U.Method` under A.3.1 and the B.1.5 composition rule; description, lens, plan, work, and mechanism remain separate |
| candidate already covered by one admitted durable U-kind | `reuse`; no new durable U-kind | the exact `ReusedUKindRef`, its accepted E.24 settlement, and its current direct governing pattern remain authoritative | reuse creates no rival identity, extent, or public kind; naming work may expose an already admitted name but does not admit another kind |
| classificatory distinction with one exact current C.3.2 declaration reference | `local-kind`; no durable U-kind | `LocalKindDeclarationRef` points to that exact declaration; the C.3 family remains the direct owner | the distinction remains local under the C.3 family and does not become a root or dependent durable U-kind; without the exact reference, `local-kind` does not close by label |
| `U.ActionInvitationPrecisionRestoration` | `reject`; no durable U-kind | A.6.A explicitly governs action-invitation precision restoration as a pattern move and admits no kind with this spelling; recover the exact `actionInvitation(...)` relation and whichever sense, normal form, candidate action, site, would-be enactor, or neighboring governed value is current | rename the public title to the pattern object; relation participants and neighboring method, work, capability, commitment, evidence, gate, and publication values keep their direct owners |
| `U.EpistemePublication` | `reject`; no durable U-kind | an episteme keeps its C.2.1 identity before, during, and after contingent participation as the selected edition in `EpistemePublicationRelation` | use Plain `published episteme` only in a claim that states obtaining participation and identifies or permits recovery of the exact E.24.PUB publication occurrence; Plain wording is neither a reference nor a designator and does not resolve |

Each row carries exactly one of the six dispositions. The retained same-individual kinds do not gain another constitution relation or identity discriminator; their direct patterns judge membership of the already identified root individual. The identity-dependent case identifies a different individual through its declared dependence. The `reuse`, `local-kind`, and `reject` rows remain non-admission exits.

Consumer repair follows the disposition, not one replacement word. Method-description claims retain `U.MethodDescription`; exact viewpoint and view claims retain `U.Viewpoint` and `U.View` only under E.17.0 membership. Every lexical or source use of the rejected spelling `U.EpistemePublication` is recovered by its claim as the selected `U.Episteme`, exact `EpistemePublicationRelation` occurrence, publication form, or `U.PresentationCarrier`; the rejected kind has no occurrences to retype.

Thus `dependent` describes an admission and identity architecture. It is not a shorthand for every object named in a record, every participant of a relation, or every qualifier used to interpret an episteme.

#### E.24.UK:4.2.1 - Accepted Root Settlement For `U.Relation`

FPF has already admitted `U.Relation`; project users do not repeat this ontology decision. The root kind classifies individuable obtaining relation occurrences. A direct relation can obtain before a system explicitly individuates, names, describes, or references one occurrence, but admission under this root requires the direct relation pattern to supply an occurrence-identity rule.

| Admission condition | `U.Relation` settlement by value |
|---|---|
| governed individuals | the extent contains exactly those obtaining relation occurrences for which a direct relation pattern supplies an occurrence-identity rule |
| stable identity or membership | each direct relation pattern states how one occurrence is reidentified and distinguished from another; participant identity, maximal continuous obtaining, constituting work, or another domain discriminator is used only when that pattern selects it |
| reviewable witness | `A.6.REL` supplies the common occurrence discipline; the direct relation pattern supplies relation-participant meanings, the obtaining condition, and the relation-specific identity rule |
| action-facing need | comparisons, qualifications, change claims, nested relations, and receiving direct relations can depend on one occurrence being distinguishable from another |
| non-duplication | relation-kind-specific assertions do not provide one common kind for a relation occurrence used as the EntityOfConcern of an episteme or as a participant of another direct relation |
| direct governing locus | `A.6.REL` governs the root occurrence distinction and progressive individuation; each direct relation pattern governs whether its relation obtains and how its occurrences are identified |
| E.24-compatible settlement | the primary governed subject kind is `U.Relation`; its stable identity criterion is the individuable obtaining relation occurrence under the common `A.6.REL` discipline and the obtaining and occurrence-identity rules of each direct relation pattern; A.6.0, A.6.5, C.2.1, F.18, and C.29 remain neighboring declaration, claim, naming, reference, and representation governors rather than components or extent criteria of this root |
| by-value dependence | A.1 part-relation admission, relation-occurrence descriptions, and direct relations whose participant kind admits `U.Relation` rely on this root by value |

The admission does not force explicit materialization of every obtaining relation. Ordinary engineering prose can stop at the direct relation sentence. A system performs explicit-individuation work only when a named receiving episteme, direct relation, or operation-application assertion depends on occurrence identity. The accepted Tech label `U.Relation` is governed separately through its F.18 NameCard; the label does not establish the extent.

Apply that positive extent rule before classifying a nearby object. A semantic predicate is rule content in the direct relation pattern; participant satisfaction states the criterion for relation obtaining. A relational assertion or relation-occurrence description is a `U.Episteme` under `C.2.1`; its content can claim that the relation obtains or designate one occurrence as its EntityOfConcern. A designator or reference is governed by `F.18` and stands in its exact designation or reference relation to an already individuable occurrence. A filled claim-bearing project record is a `U.Episteme`, while the reusable form of that record remains under `E.24.PUB`. A data-model or diagram element is a `C.29` representation element. Each is connected to the relation occurrence only by its explicit description, publication, designation, reference, or representation relation.

The rule is not lexical. An individuable publication-relation occurrence is itself a `U.Relation` because its own direct publication pattern supplies obtaining and identity. A row that represents that occurrence remains a representation element. Reidentify the current object under its direct pattern instead of inferring membership from words such as relation, edge, link, record, or reference.

#### E.24.UK:4.3 - Combined Admission Order

Use existing rules in this order:

1. Recover the source use and governed EntityOfConcern.
2. If the current question is typed claim quantification, apply C.3, C.3.1, and C.3.2 as needed. When the admission decision under E.24.UK records `local-kind`, `LocalKindDeclarationRef` points to one exact current C.3.2 declaration; the C.3 family remains the direct owner of the local distinction.
3. Recover the identity, grounding, or recognition rule for the candidate: direct governing pattern, C.3 membership and extent rule, Concept-Set witnesses, an A.6 `U.Signature` identified by `<content, EntityOfConcernRef, effectiveReferenceScheme>` and carrying direct `SubjectKind` and `RangedValueKind` declarations plus `ResultKind`, `SliceSet`, or `ExtentRule` when those distinctions are current, an imported symbol bound by that signature, CT2R/Compose-CAL constructive grounding when the claim is structural, formal-substrate/principle-frame declaration, or another accepted operational identity test. For a relation-kind candidate, recover the direct governing relation pattern and its obtaining and occurrence-identity rules as part of the same witness.
4. Test exact existing-kind coverage before proposing a new durable kind. When one admitted durable U-kind and its direct governing pattern already preserve the governed individuals, identity or membership, intended extent, non-member boundary, and action-facing claim, record `reuse` through one exact `ReusedUKindRef` and do not create a rival settlement.
5. If a new durable FPF kind is still claimed, run all eight conditions in section 4.1, including an E.24-compatible candidate settlement. Only when all eight hold, select exactly one of `root`, `same-individual-dependent`, or `identity-dependent`; apply A.11 parsimony and A.8 universal-core testing when kernel-level status is claimed.
6. When durable admission fails, close exactly one remaining exit. Record `local-kind` only when one exact current C.3.2 declaration can be referenced through `LocalKindDeclarationRef`. Otherwise record `reject` and recover the actual object under section 4.6: keep a direct-relation participant's independently governed kind and the direct relation; keep a reusable declaration component as one A.6.5 SlotSpec; keep an assertion or description field inside the receiving `U.Episteme`; and apply `A.22`, `E.24.PUB`, or `C.29` to a selected structure, reusable form, or representation element respectively.
7. Only after the governed object and exactly one admission disposition are stable, use F.8 for mint-or-reuse and F.5, F.18, or F.17 for naming and publication.

The following table summarizes principal cross-pattern contributions; it is not an exhaustive dependency list, and the exact direct owner recovered in steps 1-7 remains authoritative.

| Source | Contribution |
| --- | --- |
| C.3 | Typed claim quantification, intent, extent, membership, kind bridge, and typed guards. |
| C.3.1 | `U.SubkindOf` partial order over `U.Kind`, not dependent-U-kind relation. |
| C.3.2 | Exact current declaration referenced through `LocalKindDeclarationRef`; the C.3 family remains its direct owner. |
| E.14, B.3.5, and C.13 | Working-Model first, CT2R alias-plus-grounding, and Compose-CAL `Γ_m` traces for structural identity claims. |
| A.6.0 and A.6.1 | Construction-facing declaration shape: `SubjectKind`, `RangedValueKind`, `SliceSet`, `ExtentRule`, vocabulary, laws, applicability, realization, and argument-slot discipline. |
| A.8 | Universal-core test for kernel-level U-kind claims. |
| A.11 | Composition and parsimony before adding a new core concept. |
| E.24 | Ontic settlement and distinction among ontic, description episteme, publication, and form. |
| F.8 | Mint-or-reuse decision after recovered kind and use. |
| F.5 | Naming after recovered meaning; naming does not do ontology. |

#### E.24.UK:4.4 - Source Ontology Conversion Guide

Use this short conversion guide when a source ontology, schema, standard, class hierarchy, or top-level ontology uses words such as type, class, category, object type, entity type, kind, or subtype. BFO-style, ISO-style, OWL/RDF, database-schema, programming-language, and discipline-local type systems are source ontologies or representation regimes; they do not become FPF `U.*` names by translation.

First recover the source construct by value:

- source name and source ontology or schema;
- source identity rule, membership rule, extent rule, or recognition rule;
- source relations such as is-a, part-of, realizes, participates-in, depends-on, or equivalent local relations;
- intended source use: classification, query, modeling, exchange, validation, reasoning, implementation, or documentation.

Then select the FPF object:

| Source construct use | FPF recovery |
| --- | --- |
| claim quantification, membership, extent, subkind, kind bridge, or bounded local classification | C.3 `U.Kind`, C.3.1 `U.SubkindOf`, and typed-reasoning rules; record `local-kind` only through one exact current C.3.2 declaration referenced by `LocalKindDeclarationRef` |
| public durable FPF kind needed across patterns | use the E.24.UK admission decision, testing exact existing-kind coverage and recording `reuse` before proposing a new durable kind; only a new admission proceeds to an E.24-compatible settlement |
| a reusable coordination of one primary governed subject kind, its identity rule, core direct relation, named neighboring direct relations, and dependent-pattern reliance | E.24 ontic settlement with explicit reuse of every already governed kind and relation |
| imported formal symbol or declared range in a signature or mechanism | A.6 `U.Signature` identified by `<content, EntityOfConcernRef, effectiveReferenceScheme>` with direct `SubjectKind` and `RangedValueKind` declarations, a symbol bound by that signature, a Concept-Set row, or an admitted durable U-kind |
| source-name alignment across contexts | F.9 bridge, F.17 term row, F.18 naming, and explicit loss notes |
| quoted source construct with no current FPF classificatory, ontic, naming-alignment, or implementation use | retain source wording with its exact local sense and quote-only or reduced-use boundary under E.10 and E.10.ARCH |
| implementation or serialization category | representation, publication form, record field, schema field, or direct implementation artifact governed by the relevant pattern |

A source "type" may become an FPF kind and may require an ontic, but only after these tests. If the source construct only supplies local classification or exchange syntax, keep it as C.3 typed reasoning, bridge material, representation material, or source wording. Do not create a rival FPF type layer beside durable U-kind governance and E.24 ontic settlement.

#### E.24.UK:4.5 - Structural Location Rule

A `U.*` spelling in a pattern title, host filename, monolith heading, or ToC row is stronger than a prose occurrence. Structural locations orient readers to the governed object.

Use this rule:

- **Prose occurrence:** recover the local claim and direct governing pattern.
- **Table row or record field:** recover whether it is one SlotSpec, one assertion or description field, one reusable-form element, or an already governed object.
- **Heading:** retain `U.*` only when the section really governs that object or directly references an already admitted U-kind.
- **Pattern title or host filename:** retain `U.*` only when the pattern's primary EntityOfConcern is that root or dependent U-kind.
- **ToC row:** retain `U.*` only when the row points to a pattern that carries the settlement; otherwise name the direct governed object or repair the wording with E.10.

Do not keep a false `U.*` structural name for memory or search convenience. Use a Plain label, local heading, Name Card, Concept-Set row, relation name, record field, or quoted source wording when that is the actual object.

#### E.24.UK:4.6 - Failed U-kind Admission Dispatch

When a candidate distinction fails the positive test, select one exact non-admission exit. The first two rows below close as `reuse` or `local-kind`; every remaining row closes as `reject` and keeps the actual object under its existing kind and direct governing pattern:

| Candidate actually names | Recovery under its direct owner |
| --- | --- |
| governed individuals and distinction already covered by one admitted durable U-kind | record `reuse` with one exact `ReusedUKindRef`; that kind's accepted E.24 settlement and current direct governing pattern remain authoritative |
| a bounded classificatory distinction with one exact current C.3.2 declaration | record `local-kind` with `LocalKindDeclarationRef`; the C.3 family remains the direct owner and no durable U-kind is admitted |
| an entity participating in one direct relation | keep the entity's independently governed kind; let the direct relation pattern state its participant meaning, obtaining condition, and occurrence identity |
| a reusable relation-declaration component | use `SlotSpec = <SlotKind, ValueKind, refMode>` under `A.6.5`; the SlotKind is local to that declaration |
| a participant designation or another assertion or description field | keep the by-value designation or reference value inside the receiving `U.Episteme`; the field does not become the world-side participant or a U-kind |
| a selected organization of direct relations | classify the selected organization as one `U.Structure` under `A.22`; the relation-specific structure name is not thereby another U-kind |
| a filled record or card presented as claim-bearing | classify the filled object as `U.Episteme` only when its exact ClaimGraph, EntityOfConcern, and effective ReferenceScheme are recoverable under `C.2.1`; otherwise recover its actual form, carrier, record-field, or representation use under the direct owner. Classify a reusable arrangement as the publication-form participant only when `PublicationFormExpressionRelation` obtains; use the exact E.24.PUB publication occurrence and `U.PresentationCarrier` when availability is current |
| a graph, tuple, algebraic, or other formal representation element | use the exact `C.29` mathematical or representation lens and state its correspondence to the represented object when that correspondence matters |
| a measure, metric, or indicator | recover the measured characteristic, scale, evaluation operation, and reading through `C.16.P`, `A.19`, or the direct evaluation pattern |
| a quoted source label or discipline term | retain it as source wording with its local sense and direct FPF recovery under `E.10` and `E.10.ARCH` |
| a desire for a public name | finish object recovery first, then apply `F.8` and the applicable `F.5`, `F.17`, or `F.18` naming pattern |

### E.24.UK:5 - Archetypal Grounding

#### E.24.UK:5.1 - False Structural U-kind Title

A structural title that names an action-invitation precision-restoration move as `U.ActionInvitationPrecisionRestoration` looks like it names a durable U-kind. A.6.A already settles the case: its governed object is the action-invitation precision-restoration move, and no durable kind with this spelling is admitted. Record `reject`, recover the exact `actionInvitation(...)` relation and whichever related governed value is current, and rename the public title to the actual pattern object.

#### E.24.UK:5.2 - Retained Root U-kind

`U.Relation` remains a root U-kind because `A.6.REL` governs individuable obtaining relation occurrences and requires each direct relation pattern to supply obtaining and occurrence identity. The practical need appears when an episteme describes one exact occurrence or another direct relation has that occurrence as a participant. The root admission does not require an occurrence-description episteme for every readable relation assertion.

`U.Work` can remain a root U-kind because A.15.1 is the sole direct owner of the dated performed occurrence and of the judgment that records resolve to it under the declared work-identity tolerances and continuity-policy description. E.24.UK supplies no rival descriptor list as an identity rule. Actual change, A.6.1 result-position bindings, domain results, delivery, acceptance, evaluation, and downstream effects retain their separate direct owners; none is a work-identity discriminator or licenses one generic work-result relation. A heading or title may reference `U.Work` only when that governed occurrence is current.

#### E.24.UK:5.3 - Dependent Durable And Rejected Candidate Cases

**Work plan.** One `U.WorkPlan` is one `U.Episteme` whose content declares intended `U.Work` over a horizon. Its identity follows C.2.1; `A.15.2` adds the stable plan-membership condition and planning use. Changing only a carrier or publication occurrence does not change the plan episteme. Changing its claim content can identify another plan episteme edition.

**Method description.** A pump-maintenance procedure episteme has one exact pump-maintenance `U.Method` as its EntityOfConcern. `A.3.2` recognizes the same episteme individual as `U.MethodDescription` when its claims say something substantive about that method as a way of doing, for example its preconditions, effects, bounds, or internal method composition. An index entry that only names the method and its author fails this positive threshold. A later planning or enactment use evaluates adequacy separately; printing, approving, or enacting neither grants nor removes membership. If the claims describe exact submethods that construct one composite pump-maintenance method, that composite `U.Method` remains the EntityOfConcern. If they instead describe substitution or fallback relations among several independent maintenance methods, the selected `U.Structure` is the EntityOfConcern of an ordinary C.2.1 episteme and the present membership rule does not apply. If claim content, EntityOfConcern, or effective reference scheme changes, C.2.1 identifies the resulting episteme; the dependent kind supplies no second identity.

**Viewpoint.** Maintainability viewpoint episteme P has one exact A.22-selected viewpoint-convention structure as its EntityOfConcern. E.17.0 recognizes the same P as `U.Viewpoint` only when its fixed claim content supplies all positive viewpoint-specification and conformance conditions. Under the effective reference scheme, `ViewpointId i` designates exact P; resolving `U.ViewpointRef r` that uses i yields P. The designator i, reference r, and episteme P remain distinct. Neither designation nor resolution grants `U.Viewpoint` or `U.View` membership; E.17.0 alone owns those membership predicates. `DescriptionContext = <EntityOfConcernRef, BoundedContextRef, ViewpointRef>` is a separate one-viewpoint use qualification: its `viewpointRef` may resolve to P, but it selects no view and establishes no conformance or membership. A library entry, bundle reference, publication, selected use, or structure label likewise does not establish membership. Revising P's identity-bearing claims identifies another episteme edition even when the convention structure is unchanged.

**View.** Architecture episteme E is recognized as `U.View` when `EpistemeViewpointConformanceRelation(E,P)` obtains for exact maintainability viewpoint P. E may be directly authored or may be the receiving episteme of an A.6.3 viewing relation; neither route grants membership. A diagram layout, screen, query execution, current selection, or publication does not establish conformance. If work changes a C.2.1 discriminator, the resulting episteme is identified by that changed discriminator and its view membership is judged anew.

**Published episteme.** The same architecture-view episteme can become available to one audience and use through an E.24.PUB publication occurrence and later cease to be available while keeping its C.2.1 identity and `U.View` membership. Therefore `U.EpistemePublication` is not admitted. Plain `published episteme` is relation-defined wording: the carrying claim states the episteme's obtaining participation as the selected edition and identifies or permits recovery of the exact publication occurrence. The Plain wording is neither a reference nor a designator and does not resolve.

#### E.24.UK:5.4 - Type And Kind Governance Passage

A passage that says a proposed type must pass A.8 or A.11 is a kernel-level U-kind admission question. A passage that says `U.Kind` and `U.SubkindOf` are used for typed reasoning remains under C.3 rules. A naming passage in F.5 or F.8 waits until the governed object and admission decision are stable.

#### E.24.UK:5.5 - Lower-level Heading

A lower-level heading containing `U.*` does not admit kindhood by heading shape. Recover whether the heading names an already admitted root or dependent U-kind, a declaration-local SlotKind, a claim-bearing `U.Episteme`, a relation-defined participant meaning, or a publication object. Keep the recovered object and its direct governing pattern; rename the heading when it advertises a different kind.

### E.24.UK:6 - Bias-Annotation

This pattern blocks punctuation-bias and taxonomy-bias. A `U.*` spelling, title, filename, table row, or imported type word is not enough to create a durable FPF kind. Recover the governed individuals, their direct governing pattern, and their identity or membership rule first. When the candidate instead names participation in a relation, a SlotSpec, an assertion or description field, a selected `U.Structure`, an `E.24.PUB` form, or a `C.29` representation element, retain that exact object and its governing pattern. Only then decide whether any durable U-kind distinction remains.

### E.24.UK:7 - Conformance Checklist

| Check | Closure condition |
| --- | --- |
| `CC-E24UK-1` | The candidate's governed object is recovered before the `U.*` spelling is judged. |
| `CC-E24UK-2` | C.3 `U.Kind` and `U.SubkindOf` are not used as synonyms for all U-kind governance. |
| `CC-E24UK-3` | A root U-kind has a primary E.24-compatible settlement and an identity, grounding, recognition, or membership rule rather than a taxonomic label alone. |
| `CC-E24UK-3a` | Root `U.Relation` classifies only individuable obtaining relation occurrences; `A.6.REL` supplies the common discipline and each direct relation pattern supplies its participant meanings, obtaining condition, and occurrence-identity rule. |
| `CC-E24UK-3b` | The claim-bearing decision episteme records exactly one typed `AdmissionDisposition` value — `root`, `same-individual-dependent`, `identity-dependent`, `reuse`, `local-kind`, or `reject` — and only the detail fields conditional on that value; it creates no project-side relation occurrence, and naming begins only after disposition. |
| `CC-E24UK-3c` | The combined admission order tests exact existing-kind coverage before new admission; a failed new admission closes only as `local-kind` with one exact current C.3.2 declaration or as `reject` with the actual object and direct governor recovered under section 4.6. |
| `CC-E24UK-4` | A dependent durable U-kind states its root U-kind and either a same-individual membership rule that preserves root identity or an identity-dependence relation with every additional discriminator. |
| `CC-E24UK-4a` | `U.MethodDescription` preserves C.2.1 identity and uses the exact stable A.3.2 membership condition: one admitted `U.Method` is the exact EntityOfConcern and at least one substantive claim concerns that method as a way of doing; mention-only content, use adequacy, C.29 representation, publication occurrence, publication form, `U.PresentationCarrier`, approval, and work do not establish membership. `U.Viewpoint` and `U.View` likewise preserve C.2.1 identity and use the exact stable E.17.0 membership predicates; structure selection, bundle membership, DescriptionContext selection, direct authoring, A.6.3 construction, form, carrier, publication, query execution, evaluation, and work do not substitute for those predicates. |
| `CC-E24UK-4b` | `U.EpistemePublication` is rejected; Plain `published episteme` is relation-defined wording in a claim that states obtaining participation and identifies or permits recovery of the exact `EpistemePublicationRelation` occurrence. The Plain wording is neither a reference nor a designator and does not resolve. |
| `CC-E24UK-4c` | Every public example in section 4.2 records exactly one of the six dispositions. `reuse` points to an already admitted kind, `local-kind` points to one C.3.2 declaration, and neither is rewritten as a root or dependent admission. |
| `CC-E24UK-4d` | Under the effective reference scheme, `ViewpointId i` designates exact viewpoint episteme P and resolving `U.ViewpointRef r` that uses i yields P; i, r, and P remain distinct, neither designation nor resolution grants membership, E.17.0 owns membership, and `DescriptionContext` remains a separate one-viewpoint use qualification. |
| `CC-E24UK-5` | Structural locations retain `U.*` only with settlement evidence or direct reference to an already admitted U-kind. |
| `CC-E24UK-6` | A world-side relation participant retains its independently governed kind, while the direct relation pattern states its participant meaning. |
| `CC-E24UK-6a` | A reusable declaration component remains one A.6.5 SlotSpec; its SlotKind does not become a U-kind. |
| `CC-E24UK-6b` | A participant designation or other assertion or description field remains inside the receiving `U.Episteme`. |
| `CC-E24UK-6c` | A selected structure, reusable form, or representation element remains under `A.22`, `E.24.PUB`, or `C.29` respectively. |
| `CC-E24UK-7` | F.8, F.5, F.18, and F.17 are used only after the governed object and admission decision are stable. |
| `CC-E24UK-8` | E.24 remains the head ontic pattern; E.24.UK governs detailed U-kind admission without duplicating that procedure back into E.24. |

### E.24.UK:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| **U-dot by punctuation.** A heading or filename contains `U.` and therefore survives as a kind. | Public spelling outruns admission. | Apply the durable U-kind test; otherwise rename to the governed object. |
| **Participation or SlotKind becomes kind.** An entity receives a new U-kind because it participates in a relation, or a `RelationSignature` SlotKind is read as a world-side kind. | Participation meaning and reusable declaration are collapsed. | Keep the entity's independently governed kind, state the direct relation, and keep the SlotKind only inside its A.6.5 SlotSpec. |
| **Source type import.** A BFO, ISO, OWL, database, or programming-language type is copied as an FPF U-kind. | Source ontology and FPF ontic admission rules become mixed. | Use the source conversion guide and name the FPF governed object. |
| **Searchable title wins.** A memorable heading remains public even though the body governs a record, publication form, relation structure, or local frame. | Discoverability replaces ontology. | Keep the searchable phrase in entry or retrieval material if useful, and put the governed object in the public pattern name. |
| **Dependent kind promoted.** A dependent distinction is admitted as an independent root U-kind. | FPF grows duplicate roots for one governed individual or an identity dependence is hidden. | Name the root U-kind and state either the same-individual membership rule or the exact identity-dependence relation and its discriminators. |
| **Contingent qualification promoted.** Temporary participation in a publication or another direct relation is given a durable U-kind. | The same individual appears to change kind merely because a relation starts or ends. | Keep the exact relation occurrence and use Plain relation-defined wording; for publication use Plain `published episteme` and E.24.PUB. |

### E.24.UK:9 - Consequences

Positive consequences:

- public `U.*` names become reliable orientation signals;
- dependent durable U-kinds can be named without pretending to be independent roots;
- type and kind wording is governed by C.3, E.24.UK, A.8, A.11, F.8, and F.5 rather than preserved as overlapping ontology;
- structural names are settled before they become misleading public names.

Costs:

- pattern authors must read the governed object before keeping a convenient `U.*` spelling;
- some familiar host filenames, headings, and ToC rows must be renamed;
- structural inventory work becomes part of U-kind governance, not an afterthought.

### E.24.UK:10 - Rationale

FPF needs U-kind names to stay rare and load-bearing because they orient many patterns at once. Without a separate U-kind governance rule, ordinary type words, source-ontology classes, slot labels, filenames, and memorable headings create a second ontology beside E.24 ontic settlement and C.3 typed reasoning.

The admission rule keeps the architecture compact. A durable U-kind has an E.24-compatible root settlement or a dependent settlement tied to one named root U-kind. A dependent pattern states either a same-individual membership rule or an exact identity-dependence relation; it does not turn every nearby participant, description field, evidence relation, or qualifier into one generic dependency. Non-U objects keep their direct governing patterns. The public name follows that decision and cannot substitute for identity, membership, or extent.

### E.24.UK:11 - SoTA-Echoing

These reduced SoTA rows remain current for the U-kind admission question while the named practice lines continue to support three premises: classes, individuals, relations, and representation forms remain distinct; modular reuse is preferable to flat taxonomy growth; and a label does not identify or admit the object it labels. Reopen this source-use basis if current best-known practice defeats one of those premises or supplies a more action-capable admission test without worse ontology truth, reader use, or modeling cost.

| Source line | Use in this pattern | Practical implication |
| --- | --- | --- |
| Foundational and applied ontology distinguish classes, individuals, relations, roles, qualities, functions, and representation forms. | Adapt: FPF does not copy one source taxonomy as U-kind admission rules; it recovers the governed object and its admission basis. | A source `type`, `class`, or `category` becomes an FPF U-kind only after FPF admission, not by translation. |
| Modular ontology and ontology-design-pattern practice use reusable fragments rather than one flat taxonomy. | Adopt for E.24 settlement: admitted durable kinds are backed by direct identity or membership rules, ontic settlement, and named dependent-pattern reliance. | A durable U-kind must be usable across patterns without forcing a new taxonomy branch for every declaration SlotKind. |
| Naming and controlled-vocabulary practice separate labels from the objects they label. | Adopt through F.5, F.8, F.17, and F.18 after the governed object is recovered. | A good title can remain searchable while the body names the actual governed object and avoids false U-kind admission. |

### E.24.UK:12 - Relations

- **Specializes:** `E.24` for durable U-kind admission after the governed individuals and ontic settlement are recovered.
- **Uses for relation admission:** `A.6.REL` supplies the common occurrence discipline; each direct relation pattern supplies relation-participant meanings, obtaining, and occurrence identity.
- **Uses for neighboring objects:** `A.6.0` and `A.6.5` govern reusable declarations; `C.2.1` governs admission-decision, assertion, and description epistemes; `F.18` governs the selected Tech label and designators; `C.29` governs mathematical and data-model representations.
- **Coordinates with:** `C.3`, `C.3.1`, and `C.3.2` for local typed reasoning and membership judgments; `E.24.CD` for candidate detection before an E.24 ontic decision, with any resulting U-kind spelling or admission pressure returning here without either pattern selecting the other's disposition; `E.24.PUB` for `EpistemePublicationRelation`, publication form, and carrier distinctions; `A.3.2` for `U.MethodDescription` membership; `E.17.0` for `U.Viewpoint`, `EpistemeViewpointConformanceRelation`, and `U.View` membership; `A.6.3` only for an optional viewing construction; `A.8` and `A.11` for kernel parsimony; and `E.10` for source wording that still hides the governed object.
- **Does not replace:** the direct pattern that governs the classified individuals, their identity or membership, their intended extent, and their action-facing use.

### E.24.UK:End

