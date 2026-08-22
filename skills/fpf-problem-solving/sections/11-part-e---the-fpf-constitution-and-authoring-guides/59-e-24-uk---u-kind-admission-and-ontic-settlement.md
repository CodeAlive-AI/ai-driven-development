## E.24.UK - U-kind Admission and Ontic Settlement

> **Type:** Part E FPF authoring discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### E.24.UK:0 - Use This When

Use this pattern when a public FPF expression proposes a `U.*`, type, kind, or subkind and the author must choose among four outcomes: reuse an admitted durable kind, declare a bounded C.3.2 local kind, admit a genuinely needed durable kind, or recover a non-kind object under the rule that defines or tests it. A title, filename, ToC row, table, or source spelling opens the question but never answers it.

Typical moments:

- a direct relation family has stable occurrence identity and patterns for the next questions need one common kind for those occurrences;
- a proposed `U.*` name appears in a pattern title, host filename, monolith heading, or ToC row;
- a current pattern uses type, kind, or subkind wording and the governed object is unclear;
- a structural name looks useful for search, but may advertise a false root kind;
- a `RelationSignature` SlotKind, an assertion or description field, a `C.29` representation element, or an `E.24.PUB` reusable form has acquired a `U.*` spelling;
- a single E.24 ontic settlement appears to govern one root U-kind plus several dependent durable U-kinds.

**Primary EntityOfConcern.** Identify the exact object the admission decision is about before filling the shared E.24-family decision: an already recoverable C.3 `U.Kind`, the proposal episteme for an unadmitted distinction, or the source-construct entity being translated. Put the proposed criterion, candidate individuals, intended extent and non-member boundary, spelling, and dependent claims in the decision's ClaimGraph. If no decision subject is identifiable, keep the inquiry open. An extension, member list, rule bundle, title, or spelling cannot fill this position.

**Primary working reader.** The first reader is an FPF pattern author or reviewer deciding whether a public FPF name should remain `U.*`. The downstream reader is the practitioner who uses public pattern titles, headings, ToC rows, and names as orientation cues and needs those cues to point to the real governed object.

**First useful move.** First name the exact local kind, proposal episteme, or source-construct entity that the decision is about; if no such object is identifiable, retain the inquiry and stop. Then recover the proposed governed individuals, identity or membership rule, intended extent and non-member boundary, and the action-facing claim that needs the kind. Test whether existing U-kinds, direct relations, declaration SlotKinds, C.3 local kinds, or selected structures already preserve that distinction. Judge the public spelling only after the admission disposition is stable.

**What goes wrong if missed.** FPF grows a shadow ontology by punctuation. A slot label becomes a kind, a publication form becomes an ontic, type and kind wording becomes active beside ontic settlement, and a useful title survives because it is searchable rather than because it names the governed object.

**What this buys.** Public `U.*` names become trustworthy. A candidate distinction either passes one explicit root or dependent admission test, or stays with the actual governed object and uses its defining or testing rule, with the PatternID kept only as a locator, without creating an umbrella kind.

**Not this pattern when.**

- If the question is whether FPF needs a durable ontic at all, use `E.24`.
- If the question is only detecting an ontic candidate before the durable decision, use `E.24.CD`.
- If the question is the difference among an ontic, its description episteme, publication, and publication form, use `E.24.PUB`.
- If the question is one phrase-level precision issue with no durable name pressure, use `E.10`, `E.10.ARCH`, or the direct precision-restoration pattern.
- If the current governed object is already recovered and only its public label must be chosen, use `F.8`, `F.5`, `F.18`, or `F.17` according to the naming use.

### E.24.UK:1 - Problem Frame

FPF reserves `U.*` names for admitted durable U-kinds. Current source material and older corpus passages can still place that spelling on a declaration-local SlotKind, participant designation, selected structure, publication form, representation element, or unsettled candidate. The spelling is therefore evidence of admission pressure, not evidence of admission.

Section 4.2 separates exact accepted admission-result references from open prerequisites, blocked candidates, and non-admission exits. A public spelling, owner citation, or orientation row supplies no admission by itself. Existing root and same-individual-dependent kinds remain usable only through the exact accepted result reference recorded there; `U.Capability` remains blocked on its missing dependence governor, and unresolved prerequisite kinds remain `unsettled` rather than being inherited by assertion.

E.24.UK governs this separation. A world-side relation participant keeps its independently governed kind; a `RelationSignature` SlotKind stays declaration-local; an assertion-side designation stays in its claim-bearing episteme; and a publication form or C.29 representation keeps its direct use. It is an E.24 subpattern because U-kind admission depends on ontic settlement, but it is not the head E.24 pattern. E.24 remains the head pattern for `U.Ontic` and ontic introduction. E.24.UK governs the detailed U-kind admission rules.

### E.24.UK:2 - Problem

Without this pattern:

1. **`U.*` spelling substitutes for admission.** A public name is retained because it looks like a kind.
2. **Unsettled type and kind wording competes with U-kind admission rules.** Type, kind, subkind, Concept-Set rows, U-kind names, and E.24 ontics become overlapping ontologies.
3. **A dependent distinction becomes an independent root.** A kind whose individuals retain root identity or depend on one root-kind individual is treated as if it had an independent root settlement.
4. **Structural names over-admit.** A title, filename, heading, ToC row, bounded-context label, system, team, subsystem, view, diagram, publication, or named use is treated as if it created a base `U.Structure` identity or specialization membership.
5. **Declaration and representation elements become U-kinds.** A participant meaning in a direct relation, a SlotKind in its reusable declaration, an assertion field, or a `C.29` representation element receives a `U.*` spelling even though its governing object is already known.
6. **Naming patterns are asked to do ontology.** F.5, F.8, F.18, or F.17 is used before the governed object has been recovered.

### E.24.UK:3 - Forces

| Force | Tension |
| --- | --- |
| Public mnemonic usefulness vs ontology truth | A `U.*` name can improve discovery; it can also advertise a false governed object. |
| Root stability vs dependent reuse | Some dependent distinctions deserve durable names but retain identity through one root settlement. |
| C.3 typed reasoning vs U-kind governance | `U.Kind` is an admitted meta-kind and C.3 kinds are its individuals; this does not give each such individual its own public `U.*` subject-kind name. `U.SubkindOf` is separately admitted as a same-individual dependent relation kind under `U.Relation`. Every other durable subject-kind proposal still needs its own E.24.UK result. |
| Kernel parsimony vs expressive pattern language | FPF needs useful names, but new U-kinds are expensive and must not replace slots and relations. |
| Host and ToC structure vs prose nuance | A false `U.*` in a title, filename, heading, or ToC row is stronger than a false prose occurrence. |

### E.24.UK:4 - Solution

Treat durable U-kind admission as a claim-bearing decision about one identified entity, not as a relation between a public name and a settlement and not as a bundle of future members, rules, boundaries, and uses. Select the decision's EntityOfConcern by the entry rule above; keep the proposed kind criterion, extent, spelling, and use-enabling claims in its ClaimGraph. Record the decision in a DRR or another claim-bearing episteme under `E.9`; the decision creates no project-side `U.Relation` occurrence.

Do not fill a second E.24.UK decision card. `E.24:4.0a` is the sole editable `E24FamilySettlementDecision` schema. The short view below helps a practitioner find its U-kind fields; it is a read-only projection and cannot omit, weaken, rename, or override any claim required by the shared decision.

| Practitioner question | Exact place in the shared decision |
| --- | --- |
| What is being decided, and under which scheme? | `DecisionEpistemeIdentity`, including the independently identified pre-judgment EntityOfConcern, its identity governor, and the effective ReferenceScheme |
| Which practical use needs a visible result? | `CandidateInputs.ReceivingUseAndVisibleResult` |
| What subject and identity rule are already current? | `PrimaryGovernedSubjectKind` and `SubjectIdentityConstitutionOrRecognitionRule` |
| What durable kind is proposed? | `ProposedDurableUKindIfAny`, including governed individuals, membership rule and scheme, intended extent and nearest non-members, plus the root-inclusion or exact identity-dependence rule when that branch needs one |
| What public spelling is proposed, if any? | `CandidatePublicSpellingIfAny`; it remains naming pressure, not admission evidence |
| What existing rule already covers the need? | `ExistingGovernorAndNonDuplicationResult` |
| Which relations and declarations does the receiving use actually consume? | `MinimalGovernedRelationSet`, `IdentityBearingDirectRelationIfSelected`, and `ReusableDeclarationsActuallyConsumed`; inactive entries are omitted only from the display, never from the underlying decision when they are required |
| Who will rely on the result, and where does it stop? | `NamedDependentPatternReliance`, `NonUseBoundary`, and `ReopenCondition` |
| What was decided? | `Outputs.UKindAdmissionResult`, including the result reference, one of the six dispositions, subject-pattern locator, positive membership-and-extent result when current, branch-specific result, and non-use/reopen boundary |
| Was an ontic result reused or created beside it? | `Outputs.OnticSettlementResult` and `DecisionMode`; `U-kind-only` cites an already accepted ontic settlement, while `atomic ontic-plus-U-kind` creates two sibling outputs from the same inputs |

A short view is therefore valid only when every displayed answer resolves back to that one shared decision. An inactive field may disappear from the view; a required field may not disappear from the decision. The `UKindAdmissionResultRef` identifies the result, not the decision episteme. In an atomic decision, the ontic and admission results remain provisional together and neither is evidence for the other.

The shared decision selects exactly one positive form—`root`, `same-individual-dependent`, or `identity-dependent`—or one non-admission exit—`reuse`, `local-kind`, or `reject`. Every positive result cites its durable membership rule and scheme. Same-individual dependence also states the root and the implication to root membership for the same individual. Identity dependence instead cites an already governed relation to a distinct root-kind individual plus every discriminator. The three non-admission exits cite the exact reused kind, local C.3.2 declaration, or recovered non-kind object.

A public Tech label follows the accepted result through F.18 and F.17. Spelling improves retrieval but supplies neither membership nor extent. The decision, its output result, the proposed or admitted kind, and individuals classified by that kind remain different objects.

#### E.24.UK:4.1 - Positive Test For A Durable U-kind

Test a proposed new durable U-kind against these eight conditions. It may receive `root`, `same-individual-dependent`, or `identity-dependent` only if all eight hold:

1. **Governed individuals.** The candidate classifies identifiable governed individuals, not source expressions, declaration fields, table columns, reference suffixes, publication forms, or mathematical representation elements.
2. **Stable identity or membership.** Cite an identity, grounding, recognition, or membership rule that reidentifies individuals and determines whether they enter the intended extent.
3. **Reviewable witness.** Cite the direct operational test. For a relation-kind candidate, cite the pattern passage that defines the relation; that passage must state participant meanings, obtaining, applicability, and occurrence identity. If no current direct relation closes the claim, an `A.6.RCD` application may record a derived or primitive candidate with a proposed direct subject settlement; its local-claim and predicate-definition exits are not kind witnesses. Every other candidate cites its direct constructive, classificatory, or membership test. A signature, row, declaration, or mathematical trace counts only when its declaration or defining rule states the correspondence to the governed individuals.
4. **Action-facing need.** FPF users need to state, compare, constrain, transform, or otherwise reason about those individuals under this kind; a wording preference alone does not qualify.
5. **Non-duplication.** Existing U-kinds, direct relations, declaration SlotKinds, local C.3 kinds, and selected structures cannot preserve the needed distinction without this durable kind.
6. **Defining locus.** One primary rule passage or accepted governed source set states the kind's identity or membership, intended extent, admissible use, and non-use boundary.
7. **Shared E.24-family settlement.** Fill `E.24:4.0a` with the subject kind and identity rule, the smallest governed relation set needed by the named use, any identity-bearing relation selected by the current settlement decision, declarations actually reused, direct defining or testing rules, receiving use, and non-use and reopen boundaries. Also cite the durable-membership rule and scheme, the same-individual inclusion law or identity-dependence relation when applicable, and the exact result references. If both ontic and public kind are new, one atomic co-decision returns separate provisional outputs without circular premises.
8. **By-value dependence.** Current or selected downstream uses cite the kind by value rather than only repeating its label.

If any positive-admission condition fails, do not force the candidate into a durable root or dependent form. Select `reuse` when an admitted durable kind already covers the distinction, `local-kind` when bounded C.3.2 classification is sufficient, or `reject` when no classificatory distinction remains. Recover the exact direct relation, declaration component, selected structure, episteme, publication form, representation element, or source wording that carries the current claim. Only after disposition is settled may an author apply F.8, F.5, and F.18 naming criteria and constitute any public F.17 row.

#### E.24.UK:4.2 - Six Admission Dispositions

The typed `AdmissionDisposition` has exactly six values:

1. **`root`.** The candidate classifies individuals identified by one cited identity or membership rule whose extent and recognition conditions are explicit.
2. **`same-individual-dependent`.** The candidate classifies individuals already admitted under one root U-kind. The root pattern keeps individual identity; the dependent pattern adds a stable membership condition and an action-facing use. The accepted settlement also states the implication: if that same individual satisfies the dependent condition, it is a member of the named root kind.
3. **`identity-dependent`.** The candidate classifies a distinct individual whose identity cannot be stated without one named root-kind individual. The exact dependence relation between those two individuals and every additional discriminator must already have a defining rule. A holder or root reference without that relation does not close admission.
4. **`reuse`.** The needed individuals and distinction are already covered by one admitted durable U-kind. Reuse that exact kind and its cited identity or membership rule; do not admit a duplicate root or dependent kind.
5. **`local-kind`.** Record this non-admission exit only with one exact current C.3.2 declaration through `LocalKindDeclarationRef`. The distinction remains local under the C.3 family and does not become a root or dependent durable U-kind; E.24.UK does not restate the declaration's internal mechanics.
6. **`reject`.** No durable or local classificatory distinction survives recovery. Keep the exact relation, declaration component, selected structure, episteme, publication object, representation element, or source wording that carries the claim. A contingent qualification whose membership is only temporary participation in a relation belongs here; use Plain relation-defined wording when useful.

Only `root`, `same-individual-dependent`, and `identity-dependent` admit the candidate as a durable U-kind. `reuse`, `local-kind`, and `reject` are distinct exits, not weakened dependent admissions.

Read kind, individual, dependence, and part separately:

- `U.WorkPlan` is a kind name. `MaintenancePlan_Q3` is one individual that may be classified by that kind. The name is not the plan individual, and neither is a declaration slot or record field.
- Same-individual dependence adds membership, not another object. C.2.1 first identifies `MaintenancePlan_Q3` as one `U.Episteme`; when A.15.2's plan-membership predicate holds, that same episteme is also a `U.WorkPlan`. No second plan individual and no parthood claim follow.
- Identity dependence concerns two distinct individuals joined by a governed relation that contributes to one individual's identity. A capability and its holder system would need that relation. Current A.2.2 supplies a holder-indexed identity tuple but not the required capability-to-holder relation, so `U.Capability` remains blocked; a holder field or reference is not the missing relation.
- Dependence does not imply parthood. Even if a capability-to-holder dependence relation is governed later, that fact alone does not make the capability a part or characteristic of the holder system. A parthood conclusion needs its own direct part relation under A.1 and that relation's obtaining rule.

None of a kind name, membership, identity dependence, or parthood follows from another. When the contrast is kind versus instance, say **kind**, **individual**, **instance**, or **concrete governed object**, not bare **value**. Reserve slot-filler wording for actual declaration slots and record-field wording for records.

#### E.24.UK:4.2a - Durable Membership and C.3 Projection

Durable U-kind membership and C.3 classification remain distinct, but C.3 now relies on an admitted meta-kind. `E24UK-AR-UKIND-R5-01` admits `U.Kind`; its individuals are reusable intensional classification distinctions recovered through candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule. A `KindSignature`, source or practice label, scheme, extension, assertion, or publication is not that kind individual.

For an independently identified candidate `x`, membership in an admitted durable subject kind `K` still follows the direct predicate `M_K` under the accepted settlement. A C.3 `U.Kind` individual may declare or reuse that predicate for typed reasoning without admitting another public `U.*` kind. A row, spelling, record, or unresolved evaluation changes neither the direct predicate nor the world-side extent.

`E24UK-AR-USUBKINDOF-R5-01` separately admits `U.SubkindOf` as a same-individual dependent kind under `U.Relation`. Its individuals are the same relation occurrences already admitted under `U.Relation` whose exact ordered kind participants satisfy C.3.1's criterion-entailment branch or exhaustive deliberately closed-domain branch within declared applicability. Scheme and signature editions qualify the obtaining test and assertion; they are not participants or occurrence-identity discriminators.

For any other `same-individual-dependent` admission, the settlement states `M_Kd(x) -> M_Kr(x)` and the same individual keeps root identity. For `identity-dependent`, the cited rule defines or constrains a two-place dependence relation from the distinct dependent individual to one exact root-kind individual and supplies every additional discriminator. A root reference alone closes neither form.

The current capability candidate still stops at the exact missing-governor result in section 4.2c; do not invent a dependence relation to make that example pass.
`U.Structure` follows the accepted A.22 architecture instead. A.22 identifies one context-independent selected organization from four and only four discriminators: exact independently identified constituents, exact selected obtaining relation occurrences, exact constraints as applied, and one named selection-use frame. `E24UK-AR-USTRUCTURE-R12-01` records the root admission. A bounded-context label, system, team, subsystem, model, method, work occurrence, result episteme, description, view, graph, table, representation, publication, or use does not supply that identity.

`BoundedModelUseStructure` and A.22's conditional crossing-analysis specialization are same-individual dependent predicates over already identified `U.Structure` values. The same structure individual keeps its A.22 identity; satisfying the corresponding A.22:4.1c condition adds the specialization and implies `U.Structure` membership. The bounded-model-use name has a current F.17 row. The crossing-analysis condition is strictly conditional on independently governed exact obtaining crossing occurrences plus all four A.22 base discriminators; because no positive member exists, its NameCard label remains local and pending and is not consumed here as public vocabulary. Neither condition adds a second structure individual, root identity, ambient-context discriminator, holonhood, agency, description identity, or view identity. An A.2.6 claim-scope value or membership fact affects the selection only when an exact applied constraint refers to it; that applied constraint, not the bare scope or membership outcome, occupies the third discriminator. A scope, context, label, view, publication, representation, or selected use alone creates neither the base structure nor specialization membership.

The three A.1.1 relation-kind designations consumed by the bounded-model-use test are current through `UTS.ModelApplicabilityRelation.FPFCore.2026-07-25`, `UTS.ModelUseRelation.FPFCore.2026-07-25`, and `UTS.ModelExpressionCoherenceRelation.FPFCore.2026-07-25`. Those F.17 rows publish only the names. A.1.1 defines each relation; the corresponding passage states its predicate, participants, obtaining condition, and occurrence-identity rule. A row, NameCard, matching token, or appearance in this registry makes no occurrence obtain and grants no `BoundedModelUseStructure` membership.


A project that needs bounded quantification may use an admitted `U.Kind` individual through C.3.2. If the kind's membership criterion cites an already governed durable subject-kind predicate, that projection neither admits another durable kind nor creates an automatic `U.SubkindOf` fact. A project-specific kind remains an individual of `U.Kind` without acquiring its own public `U.*` label; proposing such a label reopens E.24.UK for that subject kind.

#### E.24.UK:4.2b - Accepted Admission-Result Registry

Each `E24UK-AR-*` reference identifies one accepted `UKindAdmissionResult`, not the decision episteme that produced it. The registry is a navigation index. The two R5 references resolve to the complete shared decisions and separate outputs in sections 4.2.2 and 4.2.3; the bootstrap resolves to `E24-CO-UONTIC-BOOT-01` and sibling result `E24-OS-UONTIC-BOOT-01`. A row marked `RG` is a reconstructed by-value result whose exact subject-pattern passage and this row together state the disposition, membership test, reliance, and boundary; it does not pretend that a new shared decision was run. No result reference gains a second result by appending a suffix.

Each R5 or bootstrap result is a C.2.1 episteme about the pre-judgment subject construct. Its own ClaimGraph states the exact shared decision reference, disposition, membership or identity basis, subject-pattern locator, branch result, reliance, and non-use/reopen boundary under `FPFCoreReferenceScheme`. An `RG` result instead uses the reconstructed basis stated above and carries no fabricated shared-decision or sibling-output reference. The decision episteme has its own ClaimGraph and identity. A consumer relies on the result reference and follows it to the decision when it needs common inputs or decision mode.

`RG` means reconstructed and grandfathered. The exact result reference, not the row wording, is the reliance point. Every row reopens if its direct membership or identity predicate, intended extent or named reliance, nearest non-use boundary, or shared E.24 settlement law changes; carrier, layout, and spelling changes alone do not reopen it.

`E24-CO-UONTIC-BOOT-01` takes the E.24 source construct, shared settlement rule, receiving use, and non-use boundary without presupposing `U.Ontic`. It returns `E24-OS-UONTIC-BOOT-01` and `E24UK-AR-UONTIC-BOOT-01`; neither the schema, pattern, decision, nor kind thereby becomes an ontology-unit individual.

| Result | U-kind and disposition | Subject pattern and decisive test | Named reliance; nearest non-member |
| --- | --- | --- | --- |
| `E24UK-AR-UENTITY-RG-01` | `U.Entity`; `root`, RG | `A.1:4.1`; individuable and referenceable | all subject-pattern references; a label or row is not thereby an entity |
| `E24UK-AR-UHOLON-RG-01` | `U.Holon`; `root`, RG | `A.1:4.2`; six-part constructive holon criterion | recognition of the four root holon kinds; a collection or part list is not a holon by form |
| `E24UK-AR-UONTIC-BOOT-01` | `U.Ontic`; `root`, bootstrap | `E.24:4` plus `E24-OS-UONTIC-BOOT-01`; connected action-facing ontology unit | E.24-family and dependent ontology reuse; a topic cluster, form, or registry row is not the unit |
| `E24UK-AR-USYSTEM-RG-01` | `U.System`; `root`, RG | `A.1:4.4`; constructively recognized acting holon | A.2 and A.15; a local system-role kind, system-role-assignment occurrence, relation-participant position, declaration or representation position, Method, capability record, work record, or ordinary organizational title is not a System by that fact alone |
| `E24UK-AR-UEPISTEME-RG-01` | `U.Episteme`; `root`, RG | `C.2.1:4.1`; ClaimGraph, EntityOfConcern, and scheme constitute one episteme | A.3.2, A.15.2, E.17.0, and this registry; carrier, publication, or view use adds no second identity |
| `E24UK-AR-UMETHOD-RG-01` | `U.Method`; `root`, RG | `A.3.1:4`; one semantic way of doing | method-description and enactment uses; a description, plan, or dated work occurrence is not the method |
| `E24UK-AR-UWORK-RG-01` | `U.Work`; `root`, RG | `A.15.1:4`; one dated performed occurrence | A.15 and P2W; a plan, log, result, delivery, or effect is not the Work occurrence |
| `E24UK-AR-UTRANSFORMATION-RG-01` | `U.Transformation`; `root`, RG | `A.3.4:4`; one grounded actual bounded change | transformation and production uses; a planned, modeled, asserted, or represented change is not actual change |
| `E24UK-AR-URELATION-R11-01` | `U.Relation`; `root`, reconstructed | `A.6.REL:4` plus the direct relation pattern; obtaining occurrence with identity rule | occurrence-bearing epistemes and relations; predicate, assertion, designator, tuple, or edge is not the occurrence |
| `E24UK-AR-UKIND-R5-01` | `U.Kind`; `root`, R5 | `C.3:4` and `C.3.1:4`, through atomic decision `E24-CO-UKIND-R5-01` and sibling ontic result `E24-OS-UKIND-R5-01`; one reusable intensional classification distinction recovered through candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule | C.3 typed reasoning and durable kind settlement; a `KindSignature`, locality, scheme, current extension, label, assertion, or publication is not the kind individual |
| `E24UK-AR-USUBKINDOF-R5-01` | `U.SubkindOf`; `same-individual-dependent` under `U.Relation`, R5 | `C.3.1:4.1`, through atomic decision `E24-CO-USUBKINDOF-R5-01` and sibling ontic result `E24-OS-USUBKINDOF-R5-01`; the exact ordered `U.Kind` participants satisfy criterion entailment or exhaustive evaluation over a deliberately closed finite domain within declared applicability | subkind comparison and typed compatibility; a hierarchy edge, mutual classification equivalence, sample, assertion, scheme/signature edition, or source boundary does not create the occurrence or identify the kinds |
| `E24UK-AR-USTRUCTURE-R12-01` | `U.Structure`; `root`, R1.2 | `A.22:4.1`; one selected organization identified only by exact constituents, selected obtaining relation occurrences, applied constraints, and one named selection-use frame | selected-structure and specialization uses; context, label, system, team, subsystem, method, work, result, description, view, representation, publication, or use alone is not the structure |
| `E24UK-AR-BMUS-R12-01` | `BoundedModelUseStructure`; `same-individual-dependent` under `U.Structure`, R1.2 | `A.22:4.1c` with `A.1.1` and `A.2.6`; the same already identified structure is selected over one exact model episteme, exact admitted model-use holons, and the required obtaining A.1.1 relation occurrences under applied constraints for the named bounded-model-use frame | bounded model-use reasoning; a bounded-context or model-use label, model episteme, team, subsystem, scope, description, view, graph, table, or publication alone grants no membership |
| `E24UK-AR-A22-CROSSING-RULE-R12-01` | A.22 conditional crossing-analysis specialization; `same-individual-dependent` rule under `U.Structure`, R1.2; public term pending | `A.22:4.1c`; the same already identified structure must have several bounded model-use structures as exact constituents and exact selected obtaining crossing occurrences among them under applied constraints for one named crossing-analysis use | the rule may support future crossing analysis; no current member, context-map label, mapping method or work, view, diagram, publication, shared participant, or selected use grants membership or a public specialization name |
| `E24UK-AR-UWORKPLAN-RG-01` | `U.WorkPlan`; `same-individual-dependent` under `U.Episteme`, RG | `A.15.2:4`; intended-work membership plus root inclusion | planning and readiness; a calendar image, possible work, method description, or performed Work is not a WorkPlan |
| `E24UK-AR-USYSTEMROLEASSIGNMENT-RPR-01` | `U.SystemRoleAssignment`; `same-individual-dependent` under `U.Relation`, RPR | `A.2.1:4`; the same identified relation occurrence has family membership through one declared assignment species. That species declares `HolderSystemSlot`, a declaration-local assigned-kind slot limited to one local system-role kind, its own predicate and applicability, maximal uninterrupted occurrence identity, and every commission, position, installation, or other participant on which its identity depends. Membership implies `U.Relation` for that same occurrence. | attribution and work-facing assignment use; the family has no permissive binary root signature, and a stronger species is not a generic holder-kind occurrence plus another occurrence. A holder-kind pair, interval, assertion, responsibility claim, or generic `U.Kind` domain is not an assignment occurrence. |
| `E24UK-AR-UMETHODDESCRIPTION-RG-01` | `U.MethodDescription`; `same-individual-dependent` under `U.Episteme`, RG | `A.3.2:4`; substantive claims about one admitted method | method use and planning; mention, metadata, approval, publication, or representation is not membership |
| `E24UK-AR-UVIEWPOINT-RG-01` | `U.Viewpoint`; `same-individual-dependent` under `U.Episteme`, RG | `E.17.0:4`; fixed viewpoint-convention membership claims | E.17.0; an identifier, reference, describing use, selected viewpoint, carrier, or structure does not grant membership |
| `E24UK-AR-UVIEW-RG-01` | `U.View`; `same-individual-dependent` under `U.Episteme`, RG | `E.17.0:4`; `EpistemeViewpointConformanceRelation(E,P)` obtains | E.17.0 and A.6.3; authoring, rendering, query execution, or publication does not grant membership |

#### E.24.UK:4.2c - Open Prerequisites, Blocked Candidates, and Non-admission Results

The shared decision can also encounter public kind names that do not yet have a resolvable accepted admission result. They remain explicit prerequisites rather than being smuggled into the accepted registry. Existing by-value use of an exact current value may continue under its subject pattern, but no new admission may cite the unsettled kind itself as already accepted.

| Exact result or blocker reference | Current disposition | Exact missing or closing basis |
| --- | --- | --- |
| `E24UK-OPEN-UREFERENCESCHEME-01` | `U.ReferenceScheme` prerequisite unsettled | F.18 identifies the current `FPFCoreReferenceScheme` value and C.2.1 consumes an effective scheme, but no current subject pattern and accepted result state the kind's identity, extent, and non-use boundary |
| `E24UK-OPEN-UCLAIMGRAPH-01` | `U.ClaimGraph` prerequisite unsettled | C.2.1 consumes exact claim content and distinguishes it from graph representations, but no current accepted admission result and direct kind-admission pattern are resolvable from this host set |
| `E24UK-BLK-U-CAPABILITY-01` | `U.Capability` identity-dependent candidate blocked | A.2.2 supplies the holder-indexed identity tuple but not the exact governed capability-to-holder identity-dependence relation, its obtaining condition, and its identity effect |
| `E24UK-NAR-AIPR-01` | `U.ActionInvitationPrecisionRestoration`; `reject` | A.6.A governs a pattern move and the exact `actionInvitation(...)` relation; the title does not admit another kind |
| `E24UK-NAR-EPUB-01` | `U.EpistemePublication`; `reject` | an episteme keeps C.2.1 identity while an exact `EpistemePublicationRelation` may obtain; Plain `published episteme` names that participation and not another kind |

Generic `reuse` and `local-kind` are decision exits, not accepted example results. Close `reuse` only with an exact `ReusedUKindRef` that resolves to this registry; close `local-kind` only with one exact current C.3.2 `LocalKindDeclarationRef`. If either reference is absent, keep the candidate unsettled.

Consumer repair follows the disposition, not one replacement word. Method-description claims retain `U.MethodDescription`; exact viewpoint and view claims retain `U.Viewpoint` and `U.View` only under E.17.0 membership. Every lexical or source use of the rejected spelling `U.EpistemePublication` is recovered by its claim as the selected `U.Episteme`, exact `EpistemePublicationRelation` occurrence, publication form, or `U.PresentationCarrier`; the rejected kind has no occurrences to retype.

Thus `dependent` describes an admission and identity architecture. It is not a shorthand for every object named in a record, every participant of a relation, or every qualifier used to interpret an episteme.

#### E.24.UK:4.2.1 - Accepted Root Settlement For `U.Relation`

FPF has already admitted `U.Relation`; project users do not repeat this ontology decision. The root kind classifies individuable obtaining relation occurrences. A direct relation can obtain before a system explicitly individuates, names, describes, or references one occurrence, but admission under this root requires the direct relation pattern to supply an occurrence-identity rule.

| Admission condition | `U.Relation` settlement by value |
|---|---|
| governed individuals | the extent contains exactly those obtaining relation occurrences for which a direct relation pattern supplies an occurrence-identity rule |
| stable identity or membership | A.6.REL supplies the common discipline, and each exact direct relation pattern states how one occurrence is reidentified and distinguished from another. Participant identity, maximal continuous obtaining, constituting work, or another domain discriminator is used only when that defining passage selects it. |
| reviewable witness | `A.6.REL` supplies the common occurrence discipline; the direct relation pattern supplies relation-participant meanings, the obtaining condition, and the relation-specific identity rule |
| action-facing need | comparisons, qualifications, change claims, nested relations, and receiving direct relations can depend on one occurrence being distinguishable from another |
| non-duplication | relation-kind-specific assertions do not provide one common kind for a relation occurrence used as the EntityOfConcern of an episteme or as a participant of another direct relation |
| direct governing locus | `A.6.REL` governs the root occurrence distinction and progressive individuation; each direct relation pattern defines or constrains whether its relation obtains and how its occurrences are identified |
| shared E.24-family settlement | `E24UK-AR-URELATION-R11-01` is the accepted reconstructed root result. This by-value settlement records primary subject kind `U.Relation`, A.6.REL plus each needed direct relation pattern as the minimal rule set, named receiving reliance, and the non-use boundary below. `IdentityBearingDirectRelationIfSelected = none`: admission invents no relation among the `U.Relation` kind, a relation kind, or another relation occurrence. Because this result predates separate output identifiers, the registry does not fabricate an `OnticSettlementResult` suffix; reopen it into the current shared schema if a receiving use requires a separately identified ontic output. |
| by-value dependence | A.1 part-relation admission, relation-occurrence descriptions, and direct relations whose participant kind admits `U.Relation` rely on this root by value |

The admission does not force explicit materialization of every obtaining relation. Ordinary engineering prose can stop at the direct relation sentence. A system performs explicit-individuation work only when a named receiving episteme, direct relation, or operation-application assertion depends on occurrence identity. The accepted Tech label `U.Relation` is governed separately through its F.18 NameCard; the label does not establish the extent.

Apply the positive extent rule before classifying a nearby object. Predicate content is a rule; an assertion or occurrence description is a C.2.1 episteme; a designator or reference stays under F.18; a reusable form stays under E.24.PUB; and a row, graph edge, or diagram element stays under C.29. None is the obtaining occurrence. Connect it to the occurrence only through its explicit assertion, description, designation, reference, publication, or representation relation.

The rule is not lexical. An individuable publication-relation occurrence is itself a `U.Relation` when E.24.PUB defines that relation and states its obtaining and identity conditions. A row that represents the occurrence remains a representation element. Reidentify the current object by the rule that defines or tests it instead of inferring membership from words such as relation, edge, link, record, or reference.

#### E.24.UK:4.2.2 - Accepted Root Settlement for `U.Kind`

The subject of this decision is the still-unsettled C.3 proposal for reusable intensional classification distinctions—not `U.Kind` assumed in advance. One atomic decision evaluates the connected C.3 ontology unit and the public root kind from the same evidence.

| Shared field | Exact value |
| --- | --- |
| decision identity | `E24-CO-UKIND-R5-01`; C.2.1 identifies this decision episteme by its own ClaimGraph, EntityOfConcern, and scheme. Its EntityOfConcern is the exact pre-judgment source construct at C.3:4–6, identified before admission by that located passage and its candidate-domain, membership, boundary, and continuity content. The decision ClaimGraph is the common-input and output claims in this section; its scheme is `FPFCoreReferenceScheme`. |
| receiving use and visible result | C.3 typed judgments, C.3.1 kind continuity and subkind comparison, and E.24.UK admission need one reusable kind individual rather than a signature, label, extension, or assertion |
| primary subject and rule | candidate public subject kind `U.Kind`, not yet admitted in the inputs; C.3:4–6 and C.3.1:4–6 recover a kind through candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule |
| candidate public spelling | `U.Kind`; this is naming pressure carried by the decision, not admission evidence |
| proposed durable kind | governed individuals are exactly those reusable intensional distinctions; the durable membership and extent rule is the cited C.3/C.3.1 rule under `FPFCoreReferenceScheme`; one-off groupings, declaration components, source labels, schemes, extensions, assertions, and forms are nearest non-members |
| existing coverage | no admitted kind, direct relation, `KindSignature`, source class, or local extension supplies this cross-pattern meta-kind; a project-specific kind may still be one member without gaining its own public `U.*` name |
| relation and declaration input | `MinimalGovernedRelationSet = none`, because the membership rule itself identifies this root and no direct relation is needed for its identity; `IdentityBearingDirectRelationIfSelected = none`; no reusable declaration is consumed to admit the root |
| reliance and boundary | C.3.1–C.3.4 and E.24.UK rely on the exact kind individual; reopen when the candidate domain, operative membership distinction, member/non-member probes, continuity rule, named reliance, or shared settlement law changes |
| ontology output | `E24-OS-UKIND-R5-01`, an `OnticSettlementResult` selecting the connected C.3 kind-reasoning ontology unit through local exact ref `C3KindReasoningOntic.R5` (not a public Tech label), primary subject kind `U.Kind`, the cited identity rule, an empty minimal relation set, named reliance above, and the same non-use/reopen boundary |
| admission output | `E24UK-AR-UKIND-R5-01`, a `UKindAdmissionResult` with `AdmissionDisposition = root`, `SubjectPatternLocator = C.3`, membership-and-extent result `C.3:4–6` plus continuity result `C.3.1:4–6`, and `BranchSpecificResultRef = E24-OS-UKIND-R5-01` |
| decision mode | `atomic ontic-plus-U-kind`; both outputs are evaluated from these common inputs and accepted together |

The decision and its two outputs are three distinct C.2.1 epistemes. Each output has the same pre-judgment source construct as EntityOfConcern, its own ClaimGraph consisting of the applicable output claims above plus the exact decision reference, and `FPFCoreReferenceScheme`. The sibling ontic result is recorded in the admission result for navigation; it was not a premise used to admit `U.Kind`.

A project-specific kind can now be an individual of `U.Kind` without becoming another durable public subject kind. Proposing a public `U.*` name for that individual requires another E.24.UK decision.

#### E.24.UK:4.2.3 - Accepted Same-individual Dependent Settlement for `U.SubkindOf`

The subject here is the still-unsettled C.3.1 proposal for an ordered kind-participant relation—not `U.SubkindOf` assumed in advance. The accepted relation occurrence keeps its `U.Relation` identity and gains the dependent membership only when C.3.1's obtaining rule holds.

| Shared field | Exact value |
| --- | --- |
| decision identity | `E24-CO-USUBKINDOF-R5-01`; C.2.1 identifies this decision episteme by its own ClaimGraph, EntityOfConcern, and scheme. Its EntityOfConcern is the exact pre-judgment source construct at C.3.1:4.1–6, identified before admission by that located passage and its participant, obtaining, applicability, and occurrence-identity content. The decision ClaimGraph is the common-input and output claims in this section; its scheme is `FPFCoreReferenceScheme`. |
| receiving use and visible result | typed compatibility, monotonic classification use, bridge order-preservation claims, and declaration constraints need an exact obtaining relation rather than a hierarchy edge or assertion |
| primary subject and rule | admitted root subject kind `U.Relation`; the ordered narrower and broader participants are exact `U.Kind` individuals admitted through `E24UK-AR-UKIND-R5-01`. C.3.1 defines criterion-entailment or exhaustive deliberately closed-domain obtaining, declared applicability, and participant-determined occurrence identity. |
| candidate public spelling | `U.SubkindOf`; this is naming pressure carried by the decision, not admission evidence |
| proposed durable kind | `U.SubkindOf`; governed individuals are the same obtaining relation occurrences already under `U.Relation`; membership uses the C.3.1 rule under `FPFCoreReferenceScheme`, and every positive member is that same root relation occurrence |
| existing coverage | root `U.Relation` supplies common occurrence identity but not the narrower/broader predicate; a hierarchy edge, implication expression, current extension, sample, assertion, scheme/signature edition, or `KindBridge` does not supply the obtaining occurrence |
| minimal relation set | direct kind candidate `U.SubkindOf`; participant meanings are exact narrower and broader `U.Kind` individuals; obtaining and occurrence identity are stated in C.3.1:4.1–6; direct governor C.3.1; enabled uses are the receiving uses above |
| other inputs | `IdentityBearingDirectRelationIfSelected = none`; the candidate relation is the governed subject, not an extra edge that identifies the ontology unit. No reusable `RelationSignature` is consumed. |
| reliance and boundary | C.3.1–C.3.4 rely on the exact occurrence; reopen when participant meanings, obtaining branch, applicability, occurrence identity, root inclusion, named reliance, or shared settlement law changes |
| ontology output | `E24-OS-USUBKINDOF-R5-01`, an `OnticSettlementResult` selecting the C.3.1 subkind-reasoning ontology unit through local exact ref `C3SubkindReasoningOntic.R5` (not a public Tech label), primary subject kind `U.Relation`, the C.3.1 direct rule, the one-relation minimal set above, named reliance, and the same non-use/reopen boundary |
| admission output | `E24UK-AR-USUBKINDOF-R5-01`, a `UKindAdmissionResult` with `AdmissionDisposition = same-individual-dependent`, `SubjectPatternLocator = C.3.1`, membership-and-extent result `C.3.1:4.1–6`, root inclusion through `E24UK-AR-URELATION-R11-01`, and `BranchSpecificResultRef = E24-OS-USUBKINDOF-R5-01` |
| decision mode | `atomic ontic-plus-U-kind`; both outputs are evaluated from these common inputs and accepted together |

The decision and its two outputs are three distinct C.2.1 epistemes. Each output has the same pre-judgment source construct as EntityOfConcern, its own ClaimGraph consisting of the applicable output claims above plus the exact decision reference, and `FPFCoreReferenceScheme`. The sibling ontic result is recorded for navigation, not used as prior evidence. Scheme and signature editions qualify interpretation, applicability, and assertions; they are neither participants nor occurrence-identity discriminators.

#### E.24.UK:4.3 - Practitioner-first Admission Tree

1. **Recover the candidates and criterion.** Identify the decision subject, candidate individuals, stable membership or identity rule, intended extent, nearest non-member, and named action-facing use. For a relation kind, use the rule that defines its participant meanings, obtaining, applicability, and occurrence identity, and cite the PatternID that locates that rule; an `A.6.RCD` application may record a derived or primitive candidate only with a proposed direct subject settlement. If no subject or criterion is recoverable, keep the inquiry open.
2. **Try an admitted durable kind.** If one accepted result already preserves those individuals, the criterion, extent, boundary, and use, record `reuse` through that exact result and stop.
3. **Try bounded classification.** If one project or context needs only typed membership or quantification, record `local-kind` through one exact C.3.2 declaration and stop.
4. **Test the need for a new durable kind.** Continue only when repeated cross-pattern use needs one stable membership law that existing durable kinds and direct relations cannot preserve. Run the eight tests and name each downstream question, its defining or testing rule, and the PatternID that locates that rule.
5. **Choose the positive form.** Use `root` for independently identified individuals, `same-individual-dependent` when one root individual gains an additional stable membership predicate and inclusion law, or `identity-dependent` when a distinct individual has an already governed dependence relation to one root individual plus all discriminators. Fill the shared E.24-family settlement; use one atomic co-decision if ontic and kind are both new. Apply A.11 and A.8 when kernel status is claimed.
6. **Close or reject, then name.** A missing branch law or positive-test condition blocks admission. Otherwise record `reject` and recover the non-kind object under the rule that defines or tests it. Only after one disposition and governed object are stable may F.8, F.5, F.18, or F.17 expose a public name.

The subject pattern remains a locator, not an authority: C.3 states the membership and continuity rules for kinds; A.6.REL states the common relation-occurrence discipline; each direct relation pattern states participant meanings, obtaining, applicability, and occurrence identity; A.6.0/A.6.5 define reusable declarations; E.24 defines ontic-settlement predicates; and F.8/F.5/F.18/F.17 constrain names after ontology is settled.

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
| public durable FPF kind needed across patterns | use E.24.UK with the shared `E.24:4.0a` settlement; reuse an accepted ontic settlement when present, and use one atomic co-decision with separate settlement and admission outputs when both ontic and kind are new |
| a reusable coordination of one primary governed subject kind, its identity rule, minimal independently governed relation set, optional identity-bearing direct relation selected by the exact subject predicate and occurrence-identity rule, declarations actually reused, and dependent-use reliance | use the `E.24:4.0a` ontic settlement; do not invent a universal core relation or a relation whose participants are kinds, patterns, declarations, or the ontic |
| imported formal symbol or declared range in a signature or mechanism | A.6 `U.Signature` identified by `<content, EntityOfConcernRef, effectiveReferenceScheme>` with direct `SubjectKind` and `RangedValueKind` declarations, a symbol bound by that signature, a Concept-Set row, or an admitted durable U-kind |
| source-name alignment between exact F.17 cells | F.9 Bridge, F.17 term row, F.18 naming, and explicit loss notes |
| quoted source construct with no current FPF classificatory, ontic, naming-alignment, or implementation use | retain source wording with its exact local sense and quote-only or reduced-use boundary under E.10 and E.10.ARCH |
| implementation or serialization category | representation, publication form, record field, schema field, or direct implementation artifact handled under the rule that defines or tests its use |

A source "type" may become an FPF kind and may require an ontic, but only after these tests. If the source construct only supplies local classification or exchange syntax, keep it as C.3 typed reasoning, bridge material, representation material, or source wording. Do not create a rival FPF type layer beside durable U-kind governance and E.24 ontic settlement.

#### E.24.UK:4.5 - Structural Location Rule

A `U.*` spelling in a pattern title, host filename, monolith heading, or ToC row is stronger than a prose occurrence. Structural locations orient readers to the governed object.

Use this rule:

- **Prose occurrence:** recover the local claim, the rule that defines or tests it, and that rule's PatternID locator.
- **Table row or record field:** recover whether it is one SlotSpec, one assertion or description field, one reusable-form element, or an already governed object.
- **Heading:** retain `U.*` only when the section's primary EntityOfConcern is that object or the heading directly references an already admitted U-kind.
- **Pattern title or host filename:** retain `U.*` only when the pattern's primary EntityOfConcern is that root or dependent U-kind.
- **ToC row:** retain `U.*` only when the row points to the passage that carries the accepted settlement; otherwise name the direct governed object or repair the wording with E.10.

Do not keep a false `U.*` structural name for memory or search convenience. Use a Plain label, local heading, Name Card, Concept-Set row, relation name, record field, or quoted source wording when that is the actual object.

#### E.24.UK:4.6 - Failed U-kind Admission Dispatch

When positive admission fails, take the first truthful exit: `reuse` with one accepted result, `local-kind` with one C.3.2 declaration, or `reject` with the actual object handled under its defining or testing rule. A participating entity keeps its intrinsic kind; a declaration component stays an A.6.5 SlotSpec; a designation or claim field stays in its episteme; a structure, publication form, or representation stays under A.22, E.24.PUB, or C.29; and a measure or source expression stays with its measurement or wording-use rule. Public naming waits until that recovery is complete.

### E.24.UK:5 - Archetypal Grounding

#### E.24.UK:5.0 - Five Replays Through One Decision Sequence

Use the same five steps in every replay: (1) identify the decision's EntityOfConcern and named use; (2) test an existing durable kind, direct relation, and bounded C.3 classification; (3) state governed individuals, membership or identity, intended extent, and the nearest non-member; (4) run all eight conditions, the shared E.24-family settlement, and the A.11/A.8 branch when current; (5) record one result reference, naming result, non-use boundary, and reopen condition. A future genuinely new candidate must complete this sequence before its public name is admitted.

In each closed replay, the `E24UK-*` reference identifies the exact admission-result episteme or reconstructed result. The five steps summarize that result and, when a current shared decision exists, point to its separate ClaimGraph; the effective reference scheme is `FPFCoreReferenceScheme`. A stopped replay names the exact blocker instead of pretending that an admission result exists.

**Reconstructed root — `U.Relation`.**

1. **Subject and use.** The EntityOfConcern is the A.6.REL source construct for the common kind of individuable obtaining relation occurrences. C.2.1 and receiving direct relations need to refer to one exact occurrence without turning an assertion, row, or graph edge into that occurrence.
2. **Coverage.** No other admitted durable kind covers all and only those occurrences. A bounded C.3 kind would not supply the cross-pattern root used by direct relation patterns.
3. **Membership.** An individual enters the extent only when its direct relation pattern establishes obtaining and supplies an occurrence-identity rule under A.6.REL. Predicate content, an assertion, description, designator, reference, tuple, or edge is the nearest non-member.
4. **Eight tests and settlement.** Governed individuals, stable occurrence identity, direct-pattern witness, action-facing occurrence use, non-duplication, A.6.REL plus the direct relation pattern, accepted result `E24UK-AR-URELATION-R11-01`, and by-value reliance are all present. A.11 retains one common root rather than duplicating it for every direct relation; A.8 does not promote relation-specific names into additional universal roots. This reconstructed result has no fabricated settlement suffix.
5. **Result and flip.** `E24UK-AR-URELATION-R11-01` records `root`; `NC-U-RELATION` retains the Tech label `U.Relation`. Reopen when the common occurrence criterion, direct identity discipline, dependent use, or settlement law changes. If an already admitted kind is found with the same governed extent and use, the disposition changes to `reuse`.

**Same-individual dependent — `U.WorkPlan`.**

1. **Subject and use.** The EntityOfConcern is A.15.2's WorkPlan kind-source construct; `MaintenancePlan_Q3` is a member witness, not the decision subject. Planning and readiness patterns need one durable way to recognize substantive intended-work epistemes.
2. **Coverage.** `U.Episteme` already supplies individual identity, but it does not by itself distinguish epistemes that substantively coordinate intended work. A one-project classification would be tested under C.3 before durable admission.
3. **Membership.** C.2.1 identifies `MaintenancePlan_Q3`; A.15.2's plan-membership predicate classifies that same individual as `U.WorkPlan` and implies its root `U.Episteme` membership. A calendar image or ticket title without substantive intended-work claims is the nearest non-member.
4. **Eight tests and settlement.** Identified epistemes, C.2.1 identity, the A.15.2 membership witness, planning use, non-duplication, A.15.2 as direct locus, accepted reconstructed result `E24UK-AR-UWORKPLAN-RG-01`, and by-value A.15 reliance are present. Under A.11's test, the result is a same-individual dependent kind rather than a second root or plan object; no new A.8 universal root is claimed. This replay does not invent a separate settlement identifier.
5. **Result and flip.** `E24UK-AR-UWORKPLAN-RG-01` records `same-individual-dependent`; the existing Tech label `U.WorkPlan` is retained and this replay mints no new name. Reopen when C.2.1 identity, A.15.2 membership, the planning use, or settlement law changes. If only one bounded project needs the distinction and one exact C.3.2 declaration suffices, the disposition changes to `local-kind`.

**Same-individual structure specializations — `BoundedModelUseStructure` and the A.22 conditional crossing-analysis rule.**

1. **Subject and use.** The decision subjects are the A.22 source constructs for base `U.Structure` and its two model-use specializations. A.1.1 and crossing-analysis consumers need durable membership without turning a context, team, subsystem, description, or view into another structure individual.
2. **Coverage.** `U.Structure` supplies the one base identity. The two specialization conditions add stable action-facing membership to that same individual; neither needs an independent root or an identity-dependence relation to a context-like bearer.
3. **Membership and near-misses.** A.22 first identifies `PressControlUse_S` from exact constituents `PressControlModel-5`, `Press-3`, and `PressControllerCode-17`; selected obtaining `ModelApplicabilityRelation`, `ModelUseRelation`, and `ModelExpressionCoherenceRelation` occurrences; an exact applied safety-control constraint claim whose proposition refers to the claim scope used by that selection; and the named use “decide whether operating use and controller-code maintenance belong to one bounded model-use organization.” That claim may state a proposition about the scope or its A.2.6 membership predicate; neither the bare scope nor the membership outcome is the constraint claim. Only then may the same `PressControlUse_S` satisfy `BoundedModelUseStructure`. The supplier-to-billing material currently supplies only a proposed six-part crossing organization—source `SupplierUse_S`, target `BillingUse_S`, direction, required fit, permitted loss, and claim scope. `SupplierToBillingTranslation_R` and `SupplierBillingCrossing_S` are not asserted: no compatible exact crossing predicate and current facts make the crossing obtain, so the A.22 relation-occurrence discriminator and base identity are unavailable. Only after that predicate is defined, current facts satisfy it, and all four A.22 discriminators are established may the same identified structure satisfy the conditional crossing-analysis specialization. `PressControlTeam`, a `BillingContext` label, `ContextMap_v3` as a `U.View`, its diagram, and its publication occurrence identify none of those structures and grant no specialization membership.
4. **Eight tests and settlement.** Governed base-structure and bounded-model-use individuals, A.22 identity and positive bounded-model-use membership witnesses, action-facing model-use needs, non-duplication, A.22 as direct locus, the relevant settlements, and by-value reliance are present. For the conditional crossing-analysis specialization, this replay settles only the same-individual-dependent membership rule and its action-facing need; it has no positive witness and no public F.17 row while the direct crossing governor is absent. A.2.6 contributes only when an applied constraint refers to an exact claim scope. That constraint, not the bare scope, membership outcome, or its representation, occupies the third discriminator.
5. **Result and flip.** `E24UK-AR-USTRUCTURE-R12-01` records `root`; `E24UK-AR-BMUS-R12-01` records the current named `same-individual-dependent` specialization; `E24UK-AR-A22-CROSSING-RULE-R12-01` records only the conditional `same-individual-dependent` crossing-analysis rule without asserting a current member or public term. Each specialization implies `U.Structure` membership only for the same individual that satisfies its exact A.22 condition. If the four base discriminators cannot be recovered, stop at the exact description or representation. If base identity is established but one specialization condition fails, retain only the base `U.Structure`; do not repair the failure with a context label, another structure identity, holonhood, or view typing. Reopen only when the A.22 identity or specialization condition, the A.2.6 applied-scope interface, the named reliance, or the shared settlement law changes.

**Identity-dependent candidate — blocked by a missing identity-dependence relation.**


1. **Subject and use.** The EntityOfConcern is A.2.2's capability kind-source construct; `Pump37MaintenanceCapability_2026` would be one capability individual distinct from holder system `Pump37`. The intended use is reidentifying the capability through its holder while evidence, assignment, and work change.
2. **Coverage.** `U.System` cannot classify the distinct capability individual, and a local kind would not replace a missing identity rule.
3. **Membership and missing relation.** A.2.2 contains a holder-indexed tuple, but no rule for a two-place capability-to-holder identity-dependence relation, obtaining condition, or identity effect. A holder field or reference is not that relation.
4. **Failed tests.** Stable identity, reviewable witness, and shared-settlement condition 7 fail at the same missing governor. The A.11 and A.8 tests are not run, and naming does not begin.
5. **Result and flip.** `E24UK-BLK-U-CAPABILITY-01` is the resolvable result; there is no accepted identity-dependent admission to reconstruct. Reopen only when A.2.2 defines the exact dependence relation and its identity effect. If recovery shows only a capability assertion, evidence item, fit assessment, or record field rather than a distinct governed individual, the disposition changes to `reject`.

**Rejected near-miss — `U.EpistemePublication`.**

1. **Subject and use.** The EntityOfConcern is the proposed kind source construct for an episteme made available to an audience; the use is to speak plainly about that availability.
2. **Coverage.** `U.Episteme` already identifies the episteme, while E.24.PUB defines the exact publication occurrence, selected edition, audience, use, and publication-form boundary.
3. **Failed membership.** Publication participation can begin and end without reidentifying the episteme and supplies neither a stable dependent-membership predicate nor a distinct individual. An unpublished edition of the same episteme is the discriminating near-miss.
4. **Failed tests and settlement.** Stable membership and non-duplication fail; `E24-OS-EPISTEME-ONTIC-01` and the E.24.PUB rules already identify the needed objects and publication relation. Applying the A.11 duplicate-kind test records rejection; do not apply A.8 or begin naming.
5. **Result.** `E24UK-NAR-EPUB-01` records `reject`. Use Plain **published episteme** only in a claim that identifies or permits recovery of the obtaining `EpistemePublicationRelation`; admit no `U.EpistemePublication` name. Reopen only if a later cited rule defines a stable classificatory distinction not reducible to publication participation.

#### E.24.UK:5.3 - Broad rule-content provision/support candidate

A proposal groups phrases such as "this pattern defines or constrains the result", "the framework supports the claim", and "service provision" under one public kind. The phrases do not identify common individuals: one locates defining claim content, another may describe evidence or source use, and the third may designate dated Work, a Method, promise content, or an operational bearer. They share neither an identity or membership rule nor a receiver that needs the proposed instances as one kind.

Recover each material occurrence first under C.2.1 and its exact subject relation. Then return `reject` for the broad candidate. Each result cites the corresponding assertion through `RejectedCandidateRecoveryRef`; it does not cite the shared word list or migration table. Genuine Work, source, evidence, publication, authority, access, and direct-relation claims survive unchanged in their own meanings. An unrecovered occurrence stays unchanged. The rejection admits no `U.Provision`, `U.Support`, generic `SupportRelation`, governance occurrence, or rule-locus description kind.

#### E.24.UK:5.4 - Type And Kind Governance Passage

A passage that says a proposed type must pass A.8 or A.11 is a kernel-level U-kind admission question. A passage that says `U.Kind` and `U.SubkindOf` are used for typed reasoning remains under C.3 rules. A naming passage in F.5 or F.8 waits until the governed object and admission decision are stable.

#### E.24.UK:5.5 - Lower-level Heading

A lower-level heading containing `U.*` does not admit kindhood by heading shape. Recover whether the heading names an already admitted root or dependent U-kind, a declaration-local SlotKind, a claim-bearing `U.Episteme`, a relation-defined participant meaning, or a publication object. Keep the recovered object and the rule that defines or tests it; rename the heading when it advertises a different kind.

### E.24.UK:6 - Bias-Annotation

This pattern blocks punctuation-bias and taxonomy-bias. A `U.*` spelling, title, filename, table row, or imported type word is not enough to create a durable FPF kind. Recover the governed individuals, their identity or membership rule, and the PatternID that locates that rule first. When the candidate instead names participation in a relation, a SlotSpec, an assertion or description field, a selected `U.Structure`, an `E.24.PUB` form, or a `C.29` representation element, retain that exact object and its defining or testing rule. For a structure specialization, first recover the same base individual through A.22's four discriminators; a context, system, team, subsystem, label, scope, method, work, result, view, representation, publication, or use creates neither that base identity nor dependent membership. Only then decide whether any durable U-kind distinction remains.

### E.24.UK:7 - Conformance Checklist

| Check | Closure condition |
| --- | --- |
| `CC-E24UK-1` | Before the shared E.24-family decision is filled, one exact local kind, proposal episteme, or source-construct entity is selected as its EntityOfConcern; if none is identifiable, the work remains inquiry and stops before an admission disposition. |
| `CC-E24UK-1a` | The proposed criterion, governed individuals, intended extent and non-member boundary, public spelling, and dependent claims remain in the decision ClaimGraph. An extension, member list, rule bundle, title, or spelling never substitutes for the EntityOfConcern. |
| `CC-E24UK-2` | Durable membership follows the admitted kind's direct predicate and reference scheme; its extent contains exactly the independently identified candidates for which that predicate holds. |
| `CC-E24UK-2a` | A C.3 local projection cites the durable predicate in its own `KindSignature` criterion and creates neither durable admission nor an automatic `U.SubkindOf` edge. |
| `CC-E24UK-2b` | `U.Kind` is admitted only through atomic decision `E24-CO-UKIND-R5-01` and its separate outputs `E24-OS-UKIND-R5-01` and `E24UK-AR-UKIND-R5-01`. Its individuals have a recoverable candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule; locality, spelling, scheme, declaration, current extension, assertion, and publication decide neither kind identity nor membership by themselves. |
| `CC-E24UK-2c` | `U.SubkindOf` is admitted only through atomic decision `E24-CO-USUBKINDOF-R5-01` and its separate outputs `E24-OS-USUBKINDOF-R5-01` and `E24UK-AR-USUBKINDOF-R5-01`. It is a same-individual dependent kind under `U.Relation`; its occurrence has exact ordered kind participants and obtains only by exact criterion entailment or exhaustive evaluation over a deliberately closed finite domain. A hierarchy edge, sample, or assertion is not the occurrence. |
| `CC-E24UK-3` | Every positive result created under the current `E.24:4.0a` schema cites one exact accepted `OnticSettlementResult`, plus the kind's direct membership, extent, and branch-specific law. A reconstructed `RG` result remains at its exact admission-result reference and by-value basis; before a new consumer requires a separately identified ontic output, replay it through the current schema rather than inventing a suffix. No owner label or universal head relation substitutes for either basis. |
| `CC-E24UK-3a` | Root `U.Relation` classifies only individuable obtaining relation occurrences. `A.6.REL` supplies the common discipline; each admitted direct or derived relation kind has a direct subject settlement for participant meanings, obtaining, applicability, and occurrence identity. An `A.6.RCD` local-claim or predicate-definition result does not count as kind admission; only a derived or primitive candidate that carries the proposed direct subject settlement can be tested by the E.24/E.24.UK admission rules. |
| `CC-E24UK-3b` | The claim-bearing decision episteme records exactly one typed `AdmissionDisposition` value — `root`, `same-individual-dependent`, `identity-dependent`, `reuse`, `local-kind`, or `reject` — and only the detail fields conditional on that value; it creates no project-side relation occurrence, and naming begins only after disposition. |
| `CC-E24UK-3c` | The practitioner-first admission tree tests exact existing-kind coverage and bounded C.3 classification before new admission; a failed new admission closes only as `local-kind` with one exact C.3.2 declaration or as `reject` with the actual object and direct governor recovered under section 4.6. |
| `CC-E24UK-3d` | When both a new ontic and a new public U-kind are needed, one atomic `E24FamilySettlementDecision` returns separate settlement and admission result refs from common inputs. Neither output is prior evidence for the other, and neither is accepted while the other branch remains unresolved. |
| `CC-E24UK-4` | A same-individual dependent kind states its root kind, direct membership predicate, and the implication from dependent to root membership for the same individual. An identity-dependent kind states an already governed two-place dependence relation to one exact root-kind individual plus every additional discriminator; a root reference alone never closes either case. |
| `CC-E24UK-4a` | `U.MethodDescription` preserves C.2.1 identity and uses the exact stable A.3.2 membership condition: one admitted `U.Method` is the exact EntityOfConcern and at least one substantive claim concerns that method as a way of doing; mention-only content, use adequacy, C.29 representation, publication occurrence, publication form, `U.PresentationCarrier`, approval, and work do not establish membership. `U.Viewpoint` and `U.View` likewise preserve C.2.1 identity and use the exact stable E.17.0 membership predicates; structure selection, bundle membership, a describing use or its selected viewpoint, direct authoring, A.6.3 construction, form, carrier, publication, query execution, evaluation, and work do not substitute for those predicates. |
| `CC-E24UK-4b` | `U.EpistemePublication` is rejected; Plain `published episteme` is relation-defined wording in a claim that states obtaining participation and identifies or permits recovery of the exact `EpistemePublicationRelation` occurrence. The Plain wording is neither a reference nor a designator and does not resolve. |
| `CC-E24UK-4c` | Every retained public example resolves through one exact `E24UK-AR-*` admission-result reference. The registry row is navigation: an R5 result follows to its complete shared decision and sibling output; a reconstructed result follows to its cited direct subject passage and by-value row. Neither kind is accepted from a label, row shape, or unresolved decision. |
| `CC-E24UK-4d` | Under the effective reference scheme, `ViewpointId i` designates exact viewpoint episteme P and resolving `U.ViewpointRef r` that uses i yields P; i, r, and P remain distinct, and neither designation nor resolution grants membership. Membership follows only from E.17.0's predicate. A named describing use may select P, but the use and selection remain separate from designation, reference resolution, conformance, and membership. |
| `CC-E24UK-4e` | Bootstrap co-decision `E24-CO-UONTIC-BOOT-01` returns distinct outputs `E24-OS-UONTIC-BOOT-01` and `E24UK-AR-UONTIC-BOOT-01` without presupposing an admitted `U.Ontic` or making the schema, pattern, decision episteme, or kind an ontology-unit instance. Any prerequisite kind without a resolvable accepted result remains in the open table. |
| `CC-E24UK-4f` | Base `U.Structure` identity is context-independent and comes only from the four A.22 discriminators. `BoundedModelUseStructure` and A.22's conditional crossing-analysis specialization are same-individual dependent predicates over an already identified structure and add no second root identity. Only the bounded-model-use name currently has an F.17 public row. An A.2.6 scope or membership outcome affects identity only through an exact applied constraint that refers to it; the bare value or outcome is not a discriminator. A context, system, team, subsystem, label, scope, method, work, result, description, view, representation, publication, or use alone creates neither the base structure nor specialization membership. |
| `CC-E24UK-5` | Structural locations retain `U.*` only with settlement evidence or direct reference to an already admitted U-kind. |
| `CC-E24UK-6` | A world-side relation participant retains its independently governed kind. The cited direct relation pattern states what that participant means in the relation; a relation kind or occurrence does not own a ClaimGraph. |
| `CC-E24UK-6a` | A reusable declaration component remains one A.6.5 SlotSpec; its SlotKind does not become a U-kind. |
| `CC-E24UK-6b` | A participant designation or other assertion or description field remains inside the receiving `U.Episteme`. |
| `CC-E24UK-6c` | A selected structure, reusable form, or representation element remains under `A.22`, `E.24.PUB`, or `C.29` respectively. |
| `CC-E24UK-7` | F.8, F.5, F.18, and F.17 are used only after the governed object and admission decision are stable. |
| `CC-E24UK-8` | E.24 remains the head ontic pattern; use E.24.UK for detailed U-kind admission without duplicating that procedure back into E.24. |

### E.24.UK:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| **U-dot by punctuation.** A heading or filename contains `U.` and therefore survives as a kind. | Public spelling outruns admission. | Apply the durable U-kind test; otherwise rename to the governed object. |
| **Participation or SlotKind becomes kind.** An entity receives a new U-kind because it participates in a relation, or a `RelationSignature` SlotKind is read as a world-side kind. | Participation meaning and reusable declaration are collapsed. | Keep the entity's independently governed kind, state the direct relation, and keep the SlotKind only inside its A.6.5 SlotSpec. |
| **Source type import.** A BFO, ISO, OWL, database, or programming-language type is copied as an FPF U-kind. | Source ontology and FPF ontic admission rules become mixed. | Use the source conversion guide and name the FPF governed object. |
| **Searchable title wins.** A memorable heading remains public even though the body governs a record, publication form, relation structure, or local frame. | Discoverability replaces ontology. | Keep the searchable phrase in entry or retrieval material if useful, and put the governed object in the public pattern name. |
| **Dependent kind promoted.** A dependent distinction is admitted as an independent root U-kind, or a root reference is treated as proof of dependence. | FPF grows duplicate roots, hides the root-inclusion law, or claims an unidentified dependence. | For the same individual, state the dependent membership predicate and its implication to root membership. For a distinct individual, cite an already governed exact dependence relation and its discriminators; otherwise stop admission at the missing governor. |
| **Structure specialization re-rooted.** A context, system, team, subsystem, model-use label, scope, method, work result, view, diagram, publication, or named use is treated as if it created a base structure or one of its specializations. | The A.22 four-discriminator identity is bypassed, and description, representation, use, or a pending label is mistaken for structure membership. | Identify the exact `U.Structure` under A.22 first. Add `BoundedModelUseStructure` only when its A.22:4.1c condition holds; apply the conditional crossing-analysis rule only after independently governed crossings and all four base discriminators exist. Otherwise retain the actual context-like, epistemic, representational, publication, or use object under its defining or testing rule. |
| **Contingent qualification promoted.** Temporary participation in a publication or another direct relation is given a durable U-kind. | The same individual appears to change kind merely because a relation starts or ends. | Keep the exact relation occurrence and use Plain relation-defined wording; for publication use Plain `published episteme` and E.24.PUB. |

### E.24.UK:9 - Consequences

Positive consequences:

- public `U.*` names become reliable orientation signals;
- dependent durable U-kinds can be named without pretending to be independent roots;
- model-use structure specializations can be named without duplicating A.22 base identity or collapsing contexts, systems, views, representations, publications, or uses into structures;
- type and kind wording is handled through C.3, E.24.UK, A.8, A.11, F.8, and F.5 rather than preserved as overlapping ontology;
- structural names are settled before they become misleading public names.

Costs:

- pattern authors must read the governed object before keeping a convenient `U.*` spelling;
- some familiar host filenames, headings, and ToC rows must be renamed;
- structural inventory work becomes part of U-kind governance, not an afterthought.

### E.24.UK:10 - Rationale

FPF needs U-kind names to stay rare and load-bearing because they orient many patterns at once. Without a separate U-kind governance rule, ordinary type words, source-ontology classes, slot labels, filenames, and memorable headings create a second ontology beside E.24 ontic settlement and C.3 typed reasoning.

The admission rule keeps durable classification connected to direct ontology without making every local class public. E.24 and E.24.UK share one settlement; C.3 handles bounded classification. A same-individual dependent kind adds one membership predicate and root-inclusion law to an existing individual. An identity-dependent kind instead requires a governed relation to a distinct root-kind individual plus all discriminators. Missing branch evidence blocks admission, and no public name, reference field, or owner label substitutes for it.

### E.24.UK:11 - SoTA Decision for Durable Kind Admission

The bounded question is practical: **when should a reusable distinction become a durable public kind, when is a local classifier or direct relation enough, and what identity commitment does each choice add?** Compare alternatives at the effort of repairing or authoring one FPF pattern—not at the effort of adopting a whole enterprise ontology.

| Current line | Strong contribution | Failure mode or extra effort for this question | FPF decision and receiving locus |
| --- | --- | --- | --- |
| [gUFO, 2026](https://arxiv.org/abs/2603.20948), with its current type typology, intrinsic and relational aspects, situations, and higher-order types; standardization is still at ISO/IEC CD 21838-5 | Rich distinctions expose whether one bearer gains a classification or a distinct dependent individual needs grounding. | Using the whole typology first adds a foundational-ontology mapping and can choose an imported category before the FPF receiving use and local alternative are known. | **Adapt** the same-individual/distinct-individual question in the admission tree and the WorkPlan, capability, role, phase, and quality cases. **Reject** automatic import of the taxonomy or its labels as FPF admission. |
| Current [BFO 2020 artifacts](https://github.com/BFO-ontology/BFO-2020), maintained for the ISO 21838 top-level-ontology line | Strong formal separation of dependence, continuant mereology, process, role, and disposition. | Adopting the whole upper ontology is expensive for a bounded FPF authoring decision, and its categories do not decide whether one FPF name deserves durable public reliance. | **Adopt** the warning that dependence is not parthood and require an exact dependence rule for the capability case. **Reject** BFO classification or official status as the admission gate. |
| Modular ontology-design-pattern work, including [MODL](https://arxiv.org/abs/1904.05405), and the emerging [LLM-assisted ontology-engineering direction](https://arxiv.org/abs/2411.09601) | Reusable small modules reduce duplicated modeling; the newer direction makes modularity important when assisted changes become cheap and frequent. | Pattern discovery and adaptation still cost work. The LLM paper states a research direction, not evidence that this pattern's eight conditions or result architecture is best. | **Adopt** existing-governor reuse and bounded modules in steps 2–4. Treat LLM assistance as a reopen pressure only, never as the load-bearing admission basis. |
| Current operational [OBO Foundry principles](https://obofoundry.org/principles/fp-000-summary.html) | Scope, versioning, textual definition, reuse, identifiers, and operational conformance make shared ontologies maintainable. | These governance and publication checks do not by themselves settle world-side kind identity, membership, dependence, or the difference between a local classifier and durable FPF kind. | **Adapt** explicit scope, reuse, version, and reopen boundaries in the decision and registry. **Reject** conformance to a publication regime as proof of admission. |
| [OWL 2 semantics](https://www.w3.org/TR/owl2-direct-semantics/) and [ISO 704:2022](https://www.iso.org/standard/79077.html) | OWL cleanly separates classes, individuals, properties, and semantics-free labels; ISO 704 separates objects, concepts, definitions, and designations. | These are mature lineage baselines, not a current low-effort method for deciding FPF's durable/local/non-kind boundary or its identity dependence. | **Adopt** class/individual/property separation, same-individual inclusion, and naming-after-object recovery. **Reject** a class axiom, label, definition, or designation as sufficient admission. |

**Selected non-dominated contribution.** None of these lines supplies the same progressive cost boundary. E.24.UK first reuses an accepted kind, then tries one bounded C.3 classification, then recovers a direct relation or other non-kind object, and only then admits a new durable kind for repeated cross-pattern reliance with an exact membership or dependence rule. At comparable authoring effort, this reduces ontology commitment while preserving exact identity, non-member, reliance, and reopen tests. The gain is not universal superiority over a foundational ontology; it is a better effort/traceability trade for FPF pattern repair.

The shared E.24 decision is part of that gain. It prevents the ontic and public-kind questions from being answered by two incompatible cards. In the `U.Kind` and `U.SubkindOf` cases, one atomic decision returns two sibling results. In the capability case, the missing dependence rule stops only that admission. In the WorkPlan case, the same episteme gains dependent membership without a second plan. A role or phase near-miss stays with a direct relation or local kind; `HighRiskPump@Turnaround2026` stays a local C.3 distinction; and public spelling waits for F.18 after the object is settled. A source may model a pressure quality or an obligation-bearing relation as a separate dependent individual. FPF does so only when a direct rule identifies that individual and its exact dependence. A measurement value, assertion, participant pair, agreement document, or relation record cannot admit it by representation alone.

The main remaining failure risks are also explicit. The progressive route can under-admit a distinction if a bounded use hides later cross-pattern reliance, or over-admit it if repeated wording is mistaken for stable membership. Reopen when a stronger current alternative offers the same identity assurance at lower effort, when an admitted kind loses its member/non-member or continuity test, or when a worked counterexample changes the same-individual, identity-dependent, local-kind, or non-kind decision.

### E.24.UK:12 - Relations

- **Shares settlement with:** `E.24` through the one `E24FamilySettlementDecision` schema in `E.24:4.0a`. E.24.UK records the `UKindAdmissionResult`; E.24 records the `OnticSettlementResult`. An existing result may be reused, while a case needing both new outputs is one atomic co-decision with neither output used as prior evidence.
- **Uses for relation admission:** `A.6.REL` states the common occurrence discipline. Each direct relation pattern states participant meanings, obtaining, applicability, and occurrence identity. An `A.6.RCD` application may record a residual claim or a derived-or-primitive candidate with its proposed direct subject settlement; local-claim and predicate-definition results remain claim content and do not admit a relation kind.
- **Uses for neighboring objects:** `A.6.0` defines reusable signature identity; `A.6.5` defines `SlotSpec` declarations; `C.2.1` defines admission-decision, assertion, and description episteme identity; `F.18` supplies the naming rule for selected Tech labels and designators; `C.29` defines mathematical and data-model representation use.
- **Coordinates with:** `A.22` for admitted structure identity and dependent structure predicates; `A.1.1` for bounded model-use relations; `A.2.6` for claim-scope membership; `C.3`, `C.3.1`, and `C.3.2` for admitted `U.Kind` individuals, the admitted `U.SubkindOf` direct species, declaration, admissibility, and judgment; `E.24.CD` for candidate detection; `E.24.PUB` for publication distinctions; direct kind patterns for every other admission; and `E.10`, F.8, F.17, and F.18 for wording and naming after settlement.
- **Does not replace:** the rule that defines or constrains the classified individuals, their identity or membership, intended extent, and action-facing use, or the PatternID that locates that rule.

### E.24.UK:End

