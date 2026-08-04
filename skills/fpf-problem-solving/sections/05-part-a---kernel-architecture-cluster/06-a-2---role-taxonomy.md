## A.2 - Role Taxonomy

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.2:0 - Use This When

**Plain name.** Enactment-facing role value.

Use this pattern when the same admitted `U.System` can participate in different work, transformation, functioning, or method enactments without becoming a different system kind, and a project must state what that system is being in the current participation.

Typical moments:

- the same pump is a cooling circulator in plant operation and a test article in qualification work;
- a relied-on claim names a role but omits the role vocabulary, interpretation scheme, holder, or assignment window;
- ordinary wording says that an episteme, capability, method, or value filling a relation participant slot "plays a role", while the direct FPF relation is still hidden;
- a proposed "part of a role" may instead be a separate role value, role relation, role-state predicate, capability-fit condition, responsibility, commitment, or method or work structure.

**Primary EntityOfConcern.** The EntityOfConcern is `U.Role`: an enactment-facing role value interpreted through one named role-taxonomy episteme and its effective `U.ReferenceScheme`. It says what an admitted `U.System` holder is being for a current participation claim. `U.Role` is a root U-kind but not an admitted holon kind; proposed decompositions are dispatched to the direct patterns governing the recovered objects and relations.

**Primary working reader.** The first reader is an engineer-manager, analyst, or FPF author who must keep system identity stable while making role meaning and role assignment inspectable. A later reader must be able to recover the role vocabulary and scheme, the holder, the assignment window, and the separate work or method claim that relied on the assignment.

**First useful move.** Name the role value, the role-taxonomy episteme, and its effective reference scheme. Add `U.RoleAssignment` when holder or assignment-window identity matters. Then state capability, role state, method admission, performed work, responsibility, evidence, or episteme use through its direct governing pattern.

**Concern-word boundary.** *Concern* is Plain reader- or viewpoint-facing wording; it does not admit `U.Concern` or replace the exact EntityOfConcern, viewpoint episteme, role-taxonomy interpretation, assignment, or receiving relation needed by the claim.

**What goes wrong if missed.** One system's different participations become artificial system kinds, or one role label silently absorbs the holder, local meaning, assignment window, capability, method, and work claim. At the opposite extreme, every contribution is called a role even when no system holds one. Both failures make it impossible to tell who participated, under which interpretation, and what actually happened.

**What this buys.** A small role vocabulary can be reused without type explosion or a universal context object. The same system may hold several roles through distinct assignments; identical labels under different role taxonomies or reference schemes do not establish identical role meanings; epistemes remain participants in their own use and evidence relations rather than becoming role holders.

**Not this pattern when.**

- Use `A.2.1` when the current object is the assignment relation and its occurrence identity.
- Use `A.2.2` for a holder's capability and `A.2.5` for a current role state.
- Use `A.2.7` for selected substitution, incompatibility, qualification, or bundle relations among role values.
- Use `A.15` and its method and work neighbors for method admission, planned work, and performed work.
- When the current participant is an episteme rather than a system holder, recover the direct use, evidence, publication, external-rule, currentness, or reliance relation. `C.2.1`, `A.10`, `E.17`, `F.10`, and `A.15.4` are common exits.
- If only the word `role` is unclear, use `A.6.RSIR` until the governed object or relation is recovered.

### A.2:1 - Problem Frame

One system can participate differently while retaining its system identity. `PumpUnit-3` remains the same pump while it holds `CoolingCirculatorRole` in plant operation and `TestArticleRole` in qualification work. A person remains the same person while holding author and verifier roles in different assignments. Role values let a project name these differences without inventing a new system kind for each participation.

Role meaning is not global. A role-taxonomy episteme contains the vocabulary and relation claims through which a role value is interpreted, and an effective `U.ReferenceScheme` fixes the current interpretation. `U.RoleAssignment` then states which admitted system holds the role and during which uninterrupted occurrence. When a selected `BoundedModelUseStructure` changes one receiving interpretation, the receiving assertion or work use may designate that structure; it is not an optional participant of the generic role relations.

Ordinary language also uses `role` to mean contribution. A design method may use a standard publication as the source for a constraint claim, a report may participate in an evidence relation, and a value may fill a participant slot of another relation. Those are useful claims, but none makes the episteme or slot filler a role holder. The direct relation must be recovered before the wording becomes relied-on FPF content.

### A.2:2 - Problem

Without this pattern:

1. one system's different participations are modeled as different system kinds;
2. identical role labels are treated as identical meanings even when their role taxonomies or reference schemes differ;
3. the role value, holder, assignment window, and relied-on work claim are compressed into one label;
4. capability, method admission, role state, responsibility, evidence, or performed work is treated as a property or part of the role value;
5. a proposed role decomposition creates false role mereology instead of recovering the direct role relations or neighboring objects;
6. an episteme or a value filling a relation participant slot is made a role holder merely because ordinary wording says it "plays a role".

### A.2:3 - Forces

| Force | Tension |
| --- | --- |
| Stable system identity vs varied participation | The holder remains one system while assignments and participation claims change. |
| Semantic locality vs vocabulary reuse | Role values need an explicit role taxonomy and reference scheme, but each local use must not become a new system kind. |
| Role value vs assignment occurrence | `U.Role` states what kind of participation is meant; `U.RoleAssignment` states who holds it and when. |
| Useful factorization vs false role mereology | Responsibilities, qualifications, role states, capability-fit conditions, and method relations may be selected separately without becoming role parts. |
| Ordinary contribution wording vs direct relation discipline | The word `role` can help recognition, but a relied-on claim must recover the system-held role or the actual episteme-use, slot, capability, method, or work relation. |

### A.2:4 - Solution

Use `U.Role` for an enactment-facing role value interpreted through one role-taxonomy episteme and effective reference scheme. Ask: **which role value, under which role vocabulary and interpretation scheme, is assigned to this admitted system during the current window?**

Then keep three moves distinct. Interpret the role value. State `U.RoleAssignment` when holder or window identity matters. Add only the direct role-state, capability, method-admission, work, transformation, responsibility, evidence, or reliance relations needed by the current claim.

A selected `BoundedModelUseStructure` can qualify one receiving interpretation. Designate it in the receiving assertion or work use only when an independently established DDD-style organization changes that interpretation; it is not an optional participant of a generic role relation and does not assign, hold, or enact the role.

#### A.2:4.1 - Core Definitions

**`U.Role`.** A `U.Role` is an enactment-facing role value. Its meaning is recovered from a named role-taxonomy episteme under an effective `U.ReferenceScheme`; the value names what an admitted `U.System` holder is being when assignment, method admission, transformation or functioning participation, work attribution, or role-state checking is current. A role value is not the holder, assignment relation, taxonomy episteme, reference scheme, or selected model-use structure.

Plain gloss: a role says what one system is being in a particular participation without turning that participation into a new system kind. The role vocabulary and scheme make that statement interpretable; the assignment says who holds it and when.

**`U.RoleAssignment`.** A `U.RoleAssignment` is an assignment relation governed by `A.2.1`. Its four participants are an admitted `U.System` holder, one `U.Role` value, the role-taxonomy episteme that states its local vocabulary, and the effective reference scheme. Its actual assignment extent is the maximal continuous period during which the assignment predicate obtains; an assertion or occurrence description may state the currently known extent separately. A.2 explains the distinction; A.2.1 governs the complete SlotSpecs and relation-occurrence identity.

**Role holder.** A holder of `U.RoleAssignment` is an admitted `U.System`. A current method-admission, work, transformation, or functioning relation cites that assignment when system participation matters. Motors, pumps, organisms, teams, services, and people can therefore be holders without implying consciousness, social agency, legal responsibility, or ethical responsibility. An episteme remains a participant in the direct relation through which a system uses it to describe, constrain, evidence, or inform work.

**Role description.** A role description is a `U.Episteme` whose EntityOfConcern is a role value, role assignment, or selected role relation. It may contain claims about role admission, use, or interpretation. Systems may teach from it or store it, and a publication relation may expose it; those uses do not make the description the role value.

**No role mereology.** `U.Role` is not an admitted holon kind. If a proposed role decomposition matters, identify what the proposed element actually is. A narrower role value, a substitution or incompatibility relation, a role-state predicate, a holder-eligibility or capability-fit condition, a responsibility or commitment relation, and a method or work structure are governed separately. Rich slots in an assignment or a role description do not make those values parts of the role.

**Relations around a role value.** These direct relations make a role usable without becoming slots or parts of `U.Role`:

| Current claim | Governing pattern | Kept distinct |
| --- | --- | --- |
| Role interpretation and description | `A.2`, `C.2.1`, `F.4`, `F.5` | Role value, role-taxonomy episteme, effective reference scheme, and description episteme. |
| Role assignment | `A.2.1`, `A.6.5` | Four participants: holder system, role value, taxonomy episteme, and scheme; the separately described assignment extent. |
| Role state | `A.2.5` | The exact `U.RoleAssignment` occurrence and by-value `RoleStatePredicate` from A.2.5's two-participant relation; its maximal continuous joint-truth extent is derived from obtaining history. Target evaluation window, assertion polarity, evidence, and reliance remain separate. |
| Holder capability | `A.2.2` | Capability instance, envelope, measures, currentness, and fit predicate. |
| Method admission | `A.15`, `A.3.1`, `A.3.2` | Method, method description, and role-admission condition. |
| Work or transformation participation | `A.15`, `A.15.1`, `A.3.4` | Holder assignment, dated work occurrence, transformation relation, and their separately governed results. |
| Evidence or reliance concerning a role claim | `A.10`, `A.15.4`, `C.2.1`, `F.10` | Episteme, evidenced claim, reliance relation, provenance, and currentness. |

Select only the rows needed by the current claim. A long relation neighborhood is not a larger role.

#### A.2:4.2 - Role Assignment Boundary

Begin with a readable sentence: an admitted system holds a named role, interpreted through a named role taxonomy and reference scheme, during a stated assignment interval.

`A.2.1` directly governs `U.RoleAssignment`. It alone owns the relation's `RelationSignature`, four participant `SlotSpec` declarations, obtaining condition, and occurrence-identity rule. The relation connects the admitted holder system, enactment-facing role value, role-taxonomy episteme, and effective reference scheme; its actual assignment extent follows uninterrupted obtaining. Any selected model-use structure belongs to the receiving assertion or use, not this signature.

The role-taxonomy episteme and effective reference scheme make local interpretation explicit without introducing a universal context object. The optional model-use structure neither holds nor assigns the role. Assignment authority, role state, capability, method admission, performed work, responsibility, evidence, reliance, and publication remain separate claims under their direct governing patterns.

When another claim relies on assignment identity, cite the exact `U.RoleAssignment` occurrence declared under `A.2.1`; do not recreate its signature in this taxonomy pattern.

#### A.2:4.3 - Recover the Direct Relation behind Contribution Wording

In ordinary language, `the role of X` often means that X contributes to some use. First ask whether X is an admitted `U.System` being something in work, transformation, functioning, or method participation. If yes, recover `U.Role` and, when relied on, `U.RoleAssignment`. If no, keep X in its actual kind and name the direct relation that makes its contribution matter.

| Ordinary wording | Governed repair |
| --- | --- |
| `RFC 9110 plays a normative role in this design` | Keep the RFC publication as an episteme and state the current external-rule, constraint, source-use, or publication relation selected by the design claim. The engineering system holding the design role remains separate. |
| `this dataset plays the benchmark role` | Keep the dataset as an episteme and state the current evidence, measurement, benchmark, source-use, or currentness relation. |
| `this parameter has the control role` | Recover the method or model parameter, or an `A.6.5` relation SlotSpec, according to the direct declaration. |
| `this interface plays the integration role` | Recover the selected module-interface, port, signature, or protocol relation under its governing architecture or interface pattern. |

The alternatives in a row are triage questions, not a union kind. Select the one relation that the relied-on claim actually uses. If that relation is still unclear, apply `A.6.RSIR` and stop before minting a role value.

#### A.2:4.4 - Role Taxonomy Episteme and Role Relation Structure

A role-taxonomy episteme contains the role vocabulary and selected role-relation claims interpreted under one effective `U.ReferenceScheme`. The episteme does not assign a role. A `U.RoleAssignment` relates the holder system to one role value and declares participant SlotSpecs for the taxonomy episteme and scheme needed to interpret that value.

`A.2.7` governs a selected role relation structure made from exact substitution, incompatibility, qualification, and role-bundle relation occurrences. A receiving check may use an assertion about one of those occurrences alongside separately governed `U.RoleAssignment`, `RoleStateRelation`, or capability-fit claims. Those neighboring relations remain direct-owner objects; they are not A.2.7 relation participants, role parts, or system-kind subsumption.

Algebraic, graph, matrix, embedding, or neural representations are mathematical lenses over that selected role relation structure when a project declares such a lens use. A `BoundedModelUseStructure` remains a separate `U.Structure`; when it changes one receiving interpretation, the receiving assertion or use designates it without extending generic role-relation signatures.

| Role value | Recognition case | Boundary |
| --- | --- | --- |
| `CoolingCirculatorRole` | A pump circulates coolant under a plant-operations role taxonomy. | The pump is the holder; circulation capability and performed work remain separate claims. |
| `TestArticleRole` | The same pump participates in qualification work under a test role taxonomy. | The test assignment does not change pump identity. |
| `VerifierRole` | A person, team, or service performs verification work under a named assignment. | The verification report is an episteme, not the role holder. |
| `TransformerRole` | A system changes an EntityOfConcern through work under a method or transformation relation. | The holder performs work; the role value does not act. |

#### A.2:4.5 - Reduced Use and Stronger Claims

A role-like word may remain Plain when it only helps people recognize a local conversation and no decision, attribution, admission, or reliance depends on its identity. Do not materialize `U.Role` or `U.RoleAssignment` merely to improve wording.

When a stronger claim appears:

- name the role-taxonomy episteme and effective reference scheme when role meaning matters;
- add `U.RoleAssignment` when holder or assignment-window identity matters;
- add the direct role-state, capability-fit, method-admission, work, transformation, evidence, or reliance relation when that relation carries the claim;
- use `A.2.7` for selected role relations inside one interpretation; when a proposed comparison, substitution, translation, or reuse crosses role taxonomies or reference schemes, use `F.9` and `A.6.9` to establish the exact Bridge, then state a separate `C.2.1` assertion about that Bridge naming the bounded use, direction, correspondence rule, tolerated semantic loss, polarity, and effective scheme; recover current reliance through `A.10` or `B.3` before acting.

The earlier Plain mention is not evidence for any stronger claim. Complete only the smallest direct relation needed by the current use.

### A.2:5 - Archetypal Grounding

#### A.2:5.1 - Pump in a Cooling Loop

Plant operation relies on a current assignment. The four values under `participantDesignations` designate the direct relation participants; `assignmentInterval` is assertion content describing the currently known extent of the uninterrupted occurrence.

```text
RoleAssignmentAssertion@PumpUnit3:
  participantDesignations:
    HolderSystemSlot: PumpUnit-3
    RoleValueSlot: CoolingCirculatorRole
    RoleTaxonomyEpistemeSlot: PlantOperationsRoleTaxonomy-2026
    EffectiveReferenceSchemeSlot: Plant-A-Operations-Scheme
  assignmentInterval: [2026-06-01, open]
```

`PumpUnit-3` is the holder system. `PlantOperationsRoleTaxonomy-2026` contains the role-vocabulary claims, and `CoolingCirculatorRole` is interpreted under `Plant-A-Operations-Scheme`. Plant A is an actual plant system and work locus, not a context slot. No selected model-use structure is needed because none changes interpretation of this assignment.

The world-side assignment occurrence continues only while its predicate obtains without interruption for the same four participants. Closing the open assertion interval later refines the same description when continuity holds; the declared interval neither makes the relation obtain nor becomes a fifth participant.

The assignment does not prove that the pump can circulate coolant throughout every operating region, that circulation work occurred, or that a maintenance method was followed. Those claims use `A.2.2`, `A.15.1`, and the applicable method, transformation, measurement, and evidence relations.

#### A.2:5.2 - A Standard Used in Design Work

An engineering team uses the RFC 9110 publication while designing an HTTP service. Keep three claims separate:

1. `DesignTeam-2` holds `ProtocolDesignerRole` under `EngineeringRoles-2026`, interpreted through `HTTP-Design-Scheme`, during one current uninterrupted assignment episode.
2. The RFC publication is the source episteme in a source-use relation whose receiving use is the HTTP-semantics constraint set in the team's design method description.
3. The dated design work is performed by `DesignTeam-2` and may produce a method description or system description.

The team uses the publication as the named source for those constraints. The publication neither holds the design role nor performs the work.

#### A.2:5.3 - The Same Label under Two Role Taxonomies

An editorial team and a safety-assurance team both use `ReviewerRole`. Their role-taxonomy epistemes contain different admission, independence, evidence, and completion claims, each interpreted under its effective reference scheme. The shared label establishes neither one role meaning nor a Bridge.

Suppose a staffing dashboard proposes `u-reviewer-display`: show assignments from both taxonomies in one `Reviewer` column. First recover the exact F.17 sense cells and establish the exact obtaining F.9 Bridge between them. Then state a separate affirmative C.2.1 assertion about that Bridge: direction `d-safety-to-editorial-display`; rule `r-preserve-reviewer-differences`, which keeps each taxonomy's admission, independence, evidence, and completion claims in separate fields; and tolerance `t-shared-label-only`, which permits the shared display label but no assignment, eligibility, capability, substitution, or performed-work inference. Its effective reference scheme interprets those designations.

For this ordinary display use, the exact current A.10 evidence-provenance graph relation and `RelianceDisposition=pass` support only `u-reviewer-display`. They do not justify putting a safety-assurance reviewer into an editorial assignment. That substitution would be another bounded-use assertion with its own direction, rule, tolerance, polarity, and reliance. If an assurance claim is being made or B.3's material-reliance threshold is met, first ask whether a current positive B.3 assurance claim exists: only one that carries the same use with a sufficient minimum reliance safety assurance record supports it; otherwise an explicit no-assurance, insufficient-record, narrowed, rejected, withdrawn, abstaining, or blocked disposition stops or narrows the use.

A Bridge Card may package the Bridge, bounded-use assertion, evidence, and disposition, but neither the card nor the Bridge alone establishes use suitability, assigns either role, or proves that dashboard or substitution work occurred. Any actual assignment, comparison, or work remains under its direct owner. If an independently selected DDD-style model-use structure changes one receiving interpretation, designate it in that receiving assertion or use. A genuinely structure-dependent relation species requires its own direct pattern, required structure participant, stronger predicate, and occurrence-identity rule; it is not an optional extension of a generic role relation.

#### A.2:5.4 - Relation Participant Slot Named Role

An external relation notation may label one participant as `role`. In FPF the declaration first recovers one participant SlotKind and its SlotSpec. The ValueKind is `U.Role` only when the filler is genuinely an enactment-facing role value. Otherwise the ValueKind remains the direct kind of the actual participant. The external label alone creates neither a `U.Role` value nor a `U.RoleAssignment`; an admitted system holds a role only through the separately obtaining assignment relation.

### A.2:6 - Bias Annotation

| Bias risk | Failure | Repair |
| --- | --- | --- |
| Semio-bias | A role description or taxonomy publication is treated as the role value. | Keep the episteme and its publication relations separate from `U.Role`. |
| Global-label bias | Matching role labels are taken as matching meanings or sufficient permission for cross-scheme use. | Compare the role-taxonomy claims and exact sense cells. For a proposed cross-scheme use, require an obtaining F.9 Bridge, a separate C.2.1 bounded-use assertion, and current A.10 or B.3 reliance; infer neither role identity nor authorization. |
| Episteme-as-agent drift | A standard, report, dataset, or model is said to perform work. | Name the holder system and work occurrence; keep the episteme in its direct evidence, reliance, external-rule, or publication relation. |
| Slot-role drift | A value filling a relation participant slot is treated as a system-held role because the external notation labels that participant `role`. | Declare the exact SlotKind and ValueKind under `A.6.5`; use `U.Role` only for an actual enactment-facing role value. |
| Capability-role drift | Assignment is treated as proof of ability. | Use `A.2.2` and a separately stated capability-fit condition. |
| Method-role drift | A role value is treated as the method of work. | Keep method, method description, admission condition, and work occurrence under `A.3` and `A.15`. |

### A.2:7 - Working Guidance

1. Identify the candidate holder. `U.Role` applies only when an admitted `U.System` is what the current participation claim classifies.
2. Name the role value, the role-taxonomy episteme, and the effective reference scheme that interprets it.
3. When another claim relies on who holds the role or when, state `U.RoleAssignment` under `A.2.1`.
4. State role state, capability fit, method admission, responsibility, commitment, work, transformation, evidence, and reliance through their direct patterns; do not put them inside the role value.
5. When a proposed subrole appears, use `A.2.7` only for substitution, incompatibility, qualification, or joint-admission bundle relations among role values. Use A.2 for another role value, and send role state, capability fit, responsibility, commitment, method, or work to its direct owner. Do not assume `partOf`.
6. When an independently selected `BoundedModelUseStructure` changes a receiving interpretation, designate it in that receiving assertion or use rather than in a generic role relation.
7. For a cross-scheme role use, establish the exact F.9 Bridge, state the separate C.2.1 bounded-use assertion, and recover current A.10 or B.3 reliance; a matching label, profile, Bridge, or card alone grants no use.
8. If the source phrase only says that a non-system entity contributes, recover the direct relation with `A.6.RSIR` and stop before creating `U.Role`.

### A.2:8 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-A2.1 | The current role claim names an enactment-facing `U.Role` value held by an admitted `U.System`. |
| CC-A2.2 | Role interpretation names the role-taxonomy episteme and effective `U.ReferenceScheme`. |
| CC-A2.3 | A relied-on assignment claim uses `U.RoleAssignment` with holder system, role value, role-taxonomy episteme, and effective reference scheme as its four participants; the assignment extent is described separately. |
| CC-A2.4 | Role-state, capability-fit, method-admission, work, transformation, responsibility, evidence, and reliance claims remain direct neighboring relations. |
| CC-A2.5 | An episteme is not made a role holder because a system uses it in a description, constraint, evidence, reliance, or publication relation. |
| CC-A2.6 | A relation participant uses an exact SlotSpec; an external participant label does not create `U.Role` or a role assignment. |
| CC-A2.7 | A proposed role decomposition is resolved through `A.2.7` and direct neighboring patterns; `U.Role` is not placed in a `partOf` chain. |
| CC-A2.8 | Matching labels under different taxonomies or schemes are not treated as identity evidence. |
| CC-A2.9 | Any selected model-use structure is designated by the receiving assertion or use; no optional `ModelUseStructureSlot` is added to a generic role relation. |
| CC-A2.10 | A selected model-use structure, when current for a receiving interpretation, neither holds nor assigns the role and does not replace the role taxonomy or effective scheme. |
| CC-A2.11 | Any cross-scheme role use cites the exact obtaining F.9 Bridge, states a separate C.2.1 assertion with its bounded use, direction, rule, tolerance, polarity, and effective scheme, and recovers current A.10 or B.3 reliance; a Bridge Card is not a use licence and any use that occurred remains under its direct owner. |

### A.2:9 - Common Anti-Patterns

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| `PumpAsCoolingCirculator` as a system subtype | It turns one assignment into system identity. | Keep the pump kind stable and state `CoolingCirculatorRole` through `U.RoleAssignment`. |
| `PumpUnit-3#CoolingCirculatorRole:Plant-A@Window` | The compact token hides taxonomy, scheme, and the kind of `Plant-A`, while suggesting a mandatory context participant. | Use the `U.RoleAssignment` SlotSpecs governed by `A.2.1`; keep Plant A as the actual plant system or work locus. |
| `AssistantReviewerRole partOf ReviewerRole` | No constructive role whole or role-part relation has been established. | Determine whether the exact claim is an A.2.7 qualification, substitution, incompatibility, or bundle relation, or another role value under A.2; send responsibility, capability, method, and work claims to their direct governing patterns. |
| `The PDF enforced the rule` | An episteme is substituted for the system that performed enforcement work. | Name the holder system and work occurrence; state the PDF's direct external-rule, evidence, or reliance relation separately. |
| `Same role label, therefore same role` | Labels establish neither semantic identity, an obtaining Bridge, nor suitability for a proposed use. | Compare the role claims and exact sense cells. If a cross-scheme action is proposed, establish the F.9 Bridge, separate bounded-use assertion, and current A.10 or B.3 reliance; otherwise stop without identity or permission inference. |

### A.2:10 - Consequences

| Gain | Cost or tradeoff |
| --- | --- |
| Systems retain stable identity while their participations change. | Relied-on role use must name a taxonomy episteme and reference scheme. |
| Assignment identity becomes inspectable through holder, role value, taxonomy, scheme, and window. | A compact role label may need a short typed assignment when attribution matters. |
| Role decomposition no longer creates unsupported holonhood. | Factorization work must classify each proposed element through `A.2.7` or a neighboring pattern. |
| Ordinary assignments need no constructed bounded-context object or optional model-use participant. | A DDD receiving assertion or work use designates its selected model-use structure when that structure actually changes interpretation. |
| Episteme use, capability, method, and work remain independently testable. | Everyday contribution wording must be resolved before it carries a stronger claim. |

### A.2:11 - Rationale

Roles solve a participation problem, not a system-identity problem. The pump does not become a new system because it is used as a cooling circulator, and the person does not become a new system kind because a verification assignment starts. `U.Role` names what the holder is being; `U.RoleAssignment` states who holds that role and when.

The selected ontology keeps three levels separate:

1. the role value interpreted through a role-taxonomy episteme and effective reference scheme;
2. the obtaining `U.RoleAssignment` relation occurrence linking holder, role value, taxonomy episteme, and scheme, with its actual extent derived from uninterrupted obtaining and described separately;
3. direct neighboring relations for role state, capability, method admission, responsibility, commitment, work, transformation, evidence, reliance, description, and publication.

This separation explains why `U.Role` is not a holon. Proposed role "parts" do not pass a constructive assembly and meta-holon transition test for the role value. They repeatedly resolve into relation occurrences, predicates, other role values, method or work structures, or parts of description epistemes. The useful structure is therefore the selected role relation structure governed by `A.2.7`, not role mereology.

Semantic locality also does not require a universal bounded context. The role-taxonomy episteme and reference scheme ordinarily suffice. A receiving assertion or use may designate a selected `BoundedModelUseStructure` only in the narrower case where an actual model-use organization changes that interpretation.

### A.2:12 - SoTA-Echoing

| Practice line | Source and status | FPF mutation | Practical consequence |
| --- | --- | --- | --- |
| Current foundational-ontology work keeps role-like classification, relation-participant distinctions, relation aspects, and situations from collapsing into one taxonomy. | Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint; used as a current comparator, not as an imported category hierarchy. | Keep `U.Role`, `U.RoleAssignment`, A.6.5 participant SlotKinds, role-state relations, and episteme-use relations distinct. FPF additionally applies its own constructive holon-admission test and does not admit `U.Role` as a holon. | A practitioner can model different assignments without creating system subtypes or role parts. |
| DDD makes model applicability local and describes Context Mapping as a method applied to actual model-use boundaries. | Eric Evans, [Domain-Driven Design Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf), 2015 mature reference; Evans, [Context Mapping with an AI-based Component](https://www.domainlanguage.com/articles/context-mapping-an-ai-based-component/), 2026 current worked practice. | Translate the action-facing DDD object to a selected `BoundedModelUseStructure`; keep Context Mapping as `U.Method` and its intended and performed work separate; designate the structure only in the receiving assertion or use whose interpretation it changes. | A pump assignment needs taxonomy and scheme; a DDD integration use names the selected structure without extending generic assignment identity. |
| FPF relation and episteme discipline keeps description and publication epistemes distinct from evidence, reliance, source-use, and publication relations and from the systems that perform work. | Current `C.2.1`, `A.6.REL`, `A.10`, `A.15.4`, and `E.17` pattern line. | Require a system holder for enactment-facing role assignment and keep each episteme in the direct relation that makes its use relevant. | A team can use a standard as the source for constraints and a report as evidence without either becoming the doer of work. |

### A.2:13 - Relations

**Builds on:** `A.1` for system and holon grounding; `C.2.1` for the role-taxonomy episteme and effective reference scheme; `A.6.0`, `A.6.5`, and `A.6.REL` for assignment RelationSignature, participant SlotSpecs, and occurrences; `E.24` for U-kind discipline.

**Governs with:** `A.2.1` for role assignment; `A.2.2` for capability; `A.2.5` for role state; `A.2.7` for selected role relation structure; `A.15` for role-method-work alignment; `F.4` and `F.5` for role description and naming.

**Crosses semantic-locality boundaries through:** `F.9` and `A.6.9` for the exact Bridge between scheme-local sense cells; `C.2.1` for the separate bounded-use assertion; and `A.10` or `B.3` for current reliance. `A.1.1` plus the receiving assertion or use pattern governs any selected `BoundedModelUseStructure` that changes interpretation. An actual assignment, comparison, substitution, translation, publication, or work occurrence remains under its direct owner.

**Keeps separate from:** direct episteme-use, evidence, reliance, publication, external-rule, currentness, and assurance patterns. Apply `A.6.RSIR` only until the actual object or relation behind contribution wording is recovered, then continue with that governing pattern.

### A.2:End

