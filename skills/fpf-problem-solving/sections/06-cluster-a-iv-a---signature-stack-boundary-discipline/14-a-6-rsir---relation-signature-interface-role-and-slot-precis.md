## A.6.RSIR - Relation, Signature, Interface, Role, and Slot Precision Restoration

> **Type:** FPF precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.6.RSIR:0 - Use This When

**Plain name.** Relation-signature-interface-role-slot recovery.

Use this pattern when relation, signature, interface, role, role-holder grammar such as `Holder#Role:Context`, assignment, enactment, slot, field, parameter, argument, endpoint, port, API, protocol, capability, affordance, method, function, concern, interest, Markov-blanket, computational-boundary, or active-inference-boundary wording hides which FPF object or claim kind is current.

**Primary EntityOfConcern.** The EntityOfConcern is the RSIR wording-use situation: a source or FPF-governed phrase whose local project concern may point to a relation, relation slot, signature, interface claim, role value, role assignment, role description, port, boundary claim bundle, or plain source label.

**Primary working reader.** The first reader is an FPF pattern author, reviewer, or practitioner repairing a phrase before selecting the direct governing pattern. The downstream reader is the engineer, manager, analyst, or steward who needs the repaired phrase to preserve useful project language without minting a shadow ontology.

**First useful move.** Recover the project concern first, then recover the current governed EntityOfConcern or claim kind. Apply the direct governing pattern as soon as it is clear. Keep a reduced-use source label only when no governed value is being asserted.

**What goes wrong if missed.** The same phrase becomes several ontologies. "Interface" becomes API, signature, port, compatibility evidence, and module boundary. "Role" becomes work role, argument position, evidence status, and access badge. "Parameter" becomes SlotKind, ValueKind, RefKind, and field at once. "Function" becomes capability, method, work, mathematical function, and architecture structure.

**What this buys.** The reader gets one small recovery move before the direct pattern is applied. The repair preserves useful engineering words while preventing a lexical cue from minting a new root kind or hiding a relation slot.

**Not this pattern when.** Do not use `A.6.RSIR` after the direct governing pattern is already clear. Do not use it for general relation repair after `A.6.P` is selected, for slot discipline after `A.6.5` is selected, for function-like repair after `A.6.F` is selected, for module-interface repair after `A.6.M` is selected, for transformation wording after `A.3.4.P` is selected, or for publication and description repair after `E.17`, `C.2.1`, or `C.2.P.DR` is selected.

### A.6.RSIR:1 - Problem frame

The RSIR cluster sits at a common failure point in FPF texts. A project team sees one word and treats it as if it already selected the ontology:

- "role" in a work assignment, relation argument, RBAC-like status, or evidence use;
- "interface" in a module relation, functional port, API description, protocol, signature, or publication view;
- "slot", "field", "parameter", or "argument" in a relation instance, signature declaration, data schema, method call, or ordinary prose;
- "signature" in a law-governed declaration, API shape, interface specification, or plain sign-off phrase;
- "function" in architecture, capability, method, work, mathematical modeling, or quality wording.

`A.6.RSIR` is the first-level recovery pattern for this bounded cluster. It does not decide every neighboring subject ontology. It helps the practitioner recover which object or claim is current and then stop at the direct governing pattern.

### A.6.RSIR:2 - Problem

Without this pattern:

1. **Lexical cues create shadow kinds.** Interface, role, slot, endpoint, and function words become local root kinds because they sound technical.
2. **Relation positions become roles.** Argument positions, evidence-use positions, transformed-entity positions, or interface endpoints are called roles and then confused with `U.Role`.
3. **Role values become schema positions.** A real `U.Role` is demoted into a local field label, losing context, assignment, role description, role state, role relation structure, and work consequences.
4. **Signatures absorb implementations.** A law-governed `U.Signature` is used as if it were a mechanism, method, work-start gate decision, interface conformance proof, or publication.
5. **Slot discipline is skipped.** A field or parameter is edited without saying SlotKind, ValueKind, RefKind, or direct governing relation.
6. **Evidence and status uses keep old role grammar.** An episteme, standard, report, publication, or badge is said to have a role instead of being used in an evidence-use, source-use, status-use, publication-use, assurance-use, or gate relation.
7. **Neighboring patterns are copied locally.** A pattern repeats negative catalogues such as "not proof, not permission, not gate" instead of recovering the current object and applying the pattern that governs the claim.

### A.6.RSIR:3 - Forces

| Force | Tension |
|---|---|
| Recognition vs ontology | Engineering words are useful entry cues, but FPF use needs the governed object or claim kind. |
| First-level repair vs overreach | The pattern must recover enough to choose the direct pattern without becoming a second ontology for relation, role, interface, capability, method, function, evidence, or status. |
| Slot discipline vs role ontology | A role can fill a role-valued slot, and a slot can name a relation position; neither replaces the other. |
| Interface usefulness vs interface-as-kind collapse | Interface words are often useful, but they may point to several different governing patterns. |
| Minimal rewrite vs precision | Ordinary prose can remain ordinary; claim-bearing prose must name the kind, relation, slot, or governed use it relies on. |
| Source label preservation vs misuse | A source label can remain quote-only or reduced-use, but it cannot silently make work, evidence, assurance, gate, publication, or architecture claims admissible. |

### A.6.RSIR:4 - Solution

Use `A.6.RSIR` as a first-level recovery move.

```text
RSIRRepairNote:
  encounteredWording:
  projectConcern:
  currentUse:
  recoveredEntityOfConcernOrClaimKind:
  selectedDirectGoverningPattern:
  slotDisciplineNeeded:
  neighboringCandidateValues:
  retainedSourceLabelUse:
  blockedOverread:
  nextAdmissibleUse:
  stopCondition:
```

The note is complete when the current object or claim kind is clear enough to apply the direct governing pattern, keep ordinary prose, keep quote-only wording, or stop the stronger claim.

#### A.6.RSIR:4.1 - Recovery order

1. **Recover the project concern.** Say what the project is trying to do: assign work responsibility, declare a signature, check an interface, compare functions, name a port, use evidence, assert status, describe a method, or make another claim.
2. **Recover the current governed object or claim kind.** Decide whether the wording points to relation, relation slot, signature, interface claim, role value, role assignment, role description, port, boundary claim bundle, capability, affordance, method, function, concern, interest, publication, source label, or ordinary prose.
3. **Name the direct governing pattern.** Use the table in `A.6.RSIR:4.2` only until the governing pattern is clear.
4. **Use `A.6.5` only when slot discipline is current.** SlotKind, ValueKind, RefKind, SlotSpec, slot content, and operation words belong to `A.6.5`. Relation identity, role ontology, interface semantics, evidence use, status use, work plans, work occurrences, and gate decisions belong elsewhere.
5. **Keep the source label reduced-use when no governed claim is current.** A word can remain a cue, quotation, title, or local shorthand without being admitted as FPF-governed vocabulary.

#### A.6.RSIR:4.2 - Direct governing pattern selection

| Recovered object or claim kind | Apply this governing pattern family | RSIR boundary |
|---|---|---|
| direct relation wording | `A.6.P`, with `A.6.5` for slot discipline | RSIR stops after relation repair is selected. |
| relation slot, field, parameter, argument, endpoint as relation position | `A.6.5`; sometimes `A.6.0` if the position is declared in a signature | Do not turn position labels into U-kinds. |
| signature or law-governed declaration | `A.6.0`, with `A.6.5` for relation or operator positions | Do not put mechanisms, methods, work, or evidence into the signature declaration. |
| role value | `A.2`, role-description and naming patterns in Part F | Do not treat the role as a SlotKind, capability, method, or status. |
| role assignment | `A.2.1`, `A.15`, `A.6.5` for SlotSpecs | `HolderSlot`, `RoleValueSlot`, `BoundedContextSlot`, and `AssignmentWindowSlot` are core; evidence and status uses stay outside. |
| role state or role relation structure | `A.2.5`, `A.2.7` | Do not infer role relation structure from ordinary label chains. |
| role description or durable role name | `F.4`, `F.5`, `F.18`, and `F.17` when public or cross-context reuse is current | Do not hide capability, method, or work inside the name. |
| role enactment wording | `A.15`, `A.15.1`, and `A.2.1` | Use direct work relation or `RoleEnactmentFact`; do not create a root enactment ontic. |
| module interface or architecture interface | `A.6.M` for module-interface claims; `C.30`, `C.30.ASV`, `C.30.AD`, or `C.30.TFS-REL` for architecture-of, structural-view, architecture-description, or transformation-flow-structure claims; `A.6.0` and `A.6.5` for signature or slot claims | Do not create generic `U.Interface`. |
| Markov blanket, Markov border, computational boundary, boundary leak, or active-inference boundary | Recover the current claim before choosing a pattern: accepted local Markov dynamics (`A.3.3`), mathematical or probabilistic lens (`C.29`, sometimes `C.26`), viability or measure-model-act envelope (`C.26.3`), holon delimitation or boundary crossing (`A.1` plus the direct relation owner), relation precision (`A.6.P` after a relation-bearing case is recovered), signature or slot claim (`A.6.0`, `A.6.5`), module-interface or interface-specification claim (`A.6.M`), functional port or functional element (`A.6.F`), physical component (`A.14`, `C.13`, `B.3.5`), boundary description or publication (`C.30.AD`, `E.17`), agency-threshold claim (`A.13`, `A.19`, `C.16`), or boundary-package statement classification (`A.6.B`) only when L, A, D, or E classification is the recovered object. | Do not create `U.MarkovBlanket`, generic `U.Boundary`, generic `U.Interface`, or binary `U.Agent`; do not treat a statistical separation, interface, interface module, physical component, description, and boundary-package classification as the same object. |
| functional port or functional structure | `A.6.F`, `A.3.4`, `E.18`, `C.30.TFS-REL` | Do not equate port, function, module interface, and signature by vocabulary alone. |
| API, protocol, connector, service-access wording | Recover the governed object first: `E.17` for API or interface-description publication; `A.6.0` and `A.6.5` for signature or relation-position claims; `A.6.M` for module-interface claims; `A.6.C` or `A.6.8` for agreement-like, protocol, SLA, service, or service-access cases; `A.6.B` only for L, A, D, or E statement classification inside a boundary package. | API may be description, protocol, service relation, signature, publication, module interface, or boundary-package statement classification. |
| capability | `A.2.2`; method, work, or gate patterns only when they name capability requirements | Role labels and interface labels do not create or demonstrate capability. |
| affordance or action invitation | `A.6.A` | Do not rename affordance as role, interface, or capability until the direct pattern admits it. |
| method, method description, work plan, or dated work | `A.3.1`, `A.3.2`, `A.15`, `A.15.1`, `A.15.2` | Method, description, plan, and work are distinct even when source wording says process. |
| function or functional wording | `A.6.F` | Function-like wording can point to several patterns; `A.6.F` governs that recovery. |
| concern, interest, viewpoint, problem, or characteristic-space selection | `A.7` for EntityOfConcern and description distinction; `C.22` or `C.22.2` for problem-card claims; `E.17.0` or `E.17.2` for viewpoint or view claims; `F.4` or `F.18` for role-description or naming cases; `A.19` or `E.21` for characteristic-space cases | Do not mint generic `U.Concern` or `U.Interest` by wording alone. |
| publication, description, declarative representation, source wording | `C.2.1`, `E.17`, `C.2.P.DR`, `E.10`, `E.10.ARCH` | Do not let description or publication use displace the EntityOfConcern selected by the project concern. |

#### A.6.RSIR:4.3 - Replacement candidate rule

Do not replace one umbrella with another. A repair candidate is admissible only when it names:

- the current object or claim kind;
- any relation or SlotKind that carries the claim;
- the governing pattern;
- the retained use of the source wording;
- the blocked overread.

If those cannot be named, leave the phrase in quote-only or reduced-use form and record the blocker.

#### A.6.RSIR:4.4 - Reduced-use source labels

Reduced-use labels are allowed. They are not failures. A source label remains reduced-use when it helps readers find or recognize the case but does not carry FPF-governed content.

Examples:

- "API role" can remain a quoted source phrase while the repair separately names software API description, provider role assignment, service promise relation, or interface specification.
- "parameter" can remain ordinary prose while SlotKind, ValueKind, and RefKind are named only when a relation or signature claim depends on them.
- "function" can remain ordinary engineering language when no architecture, capability, method, work, mathematical, quality, or module claim depends on it.

#### A.6.RSIR:4.5 - Shortcut Cost and Reopen Condition

`A.6.RSIR` is a deliberately weak first-level repair note. The baseline is full use of the direct governing pattern: `A.6.P` for relation repair, `A.6.5` for slot discipline, `A.2` and `A.2.1` for role and role assignment, `A.6.M` for module-interface, `A.6.F` for function-like repair, or the evidence, status, publication, architecture, method, work, gate, or problem pattern named by value.

The saved effort is that a practitioner does not run several full patterns before knowing which one is current. The loss budget is narrow: RSIR may select a governing pattern, preserve a reduced-use source label, or record a blocker. It may not decide the role assignment, signature, evidence-use relation, status assertion, service relation, architecture description, or method relation that belongs to the selected pattern.

Reopen RSIR when the selected pattern shows that the source phrase carried more than one governed object, the object kind was selected too early, a slot requirement was missed, or evidence, status, publication, gate, method, work, architecture, capability, or concern claims were folded into one label. The reopened repair splits the phrase into multiple governed values or keeps the excess wording reduced-use.

### A.6.RSIR:5 - Archetypal Grounding

**System case: module interface claim.** A team says "the cooling module exposes the heat-exchanger interface." RSIR first asks what claim is current. If the claim is substitutability or separate change, use `A.6.M`. If the claim is only a signature declaration for the exchanged medium and boundary conditions, use `A.6.0` plus `A.6.5`. If the claim is a functional port in a transformation-flow structure, use `A.6.F`, `A.3.4`, and `E.18`. RSIR does not create `U.Interface`.

**Role case: API provider role.** A source says "the API role is provider." RSIR splits the project concern. If "provider" is a work-facing role, recover `ProviderRole`, a `U.RoleAssignment`, `HolderSlot`, bounded context, and assignment window. If the API is a publication or protocol description, use `E.17` for publication and `A.6.8` or `A.6.C` for service, protocol, SLA, or agreement-like boundary wording. If a provider or consumer commitment is current, use `A.2.3` or `A.6.C`; if module-interface semantics are current, use `A.6.M`; if boundary-package statement classification is current, use `A.6.B`. Do not assign a work role to the API description.

**Evidence case: reviewer evidence role.** A report says "reviewer evidence role approved the gate." RSIR blocks the composite. A reviewer may be a role value assigned to a system or acting holon under `A.2` and `A.2.1`. A report episteme may be used in an evidence-use relation under `A.10`, `B.3`, `F.10`, or `E.17`. A gate approval may be a gate decision under `A.21` or a speech-act case under `A.2.9`. No episteme gets a work role by being evidence.

**Slot case: method parameter.** A method description says "parameter target controls the model." RSIR asks whether `target` is a source label, a SlotKind, a ValueKind, or the EntityOfConcern named by the claim. If it is a declared argument position, use `A.6.5` and name `TargetSlot`, ValueKind, and refMode. If it is a method requirement or work input, use method or work patterns.

#### A.6.RSIR:5.1 - Near-Miss Checks

| Source phrase | Positive recovery | Near miss to reject |
|---|---|---|
| "API role is provider" | `ProviderRole` and `U.RoleAssignment` when a team or system participates in work; `E.17`, `A.6.8`, or `A.6.C` when the API phrase names a publication, protocol, SLA, service-access, or agreement-like claim. | Do not assign a work-facing role to the API description or protocol itself. |
| "endpoint parameter source" | `A.6.5` when source is a relation-position SlotKind in a signature or relation; `E.17` or `A.6.8` when it is API or service documentation language. | Do not create an endpoint kind, a work-facing role from the word "source", or a parameter ontology by source wording alone. |
| "`Engineer#Verifier:Lab`" | `A.2.1`, `A.15`, and `A.6.5` when the old notation means holder, role value, bounded context, assignment window, or assignment SlotSpecs. | Do not keep `Holder#Role:Context` as the normative ontology or let it hide holder, role value, context, and window slots. |
| "function of the pump" | `A.6.F`, `A.3.4`, `E.18`, or `C.30.TFS-REL` when the phrase names functional structure; `A.2.2` when it names a system capability. | Do not treat "function" as the recovered kind before the current claim is known. |
| "standard evidence role" | `A.10`, `B.3`, `F.10`, or `E.17` when a standard episteme is used as evidence, source, status, or publication. | Do not keep `U.EvidenceRole` or put the standard episteme into `U.RoleAssignment`. |

### A.6.RSIR:6 - Bias-Annotation

This pattern has a relation-cluster bias because it sits in A.6. It mitigates that bias by stopping as soon as the direct governing pattern is clear.

It has an interface and software-language stress case because API, endpoint, protocol, and interface wording often enters from software. The pattern deliberately keeps the recovery general: architecture interfaces, physical ports, functional ports, service-access descriptions, and publication forms are all possible, and none is selected by word choice alone.

It resists semio-bias by keeping descriptions, publications, records, reports, standards, and source labels under the patterns that govern those objects and uses: `C.2.1`, `E.17`, `C.2.P.DR`, `A.10`, `B.3`, `F.10`, `C.28`, `E.10`, or `E.10.ARCH` when those objects or uses are current. A source label may help recognition, but it does not become the governed EntityOfConcern or make action admissible merely by being present.

### A.6.RSIR:7 - Conformance Checklist

1. The repair starts with project concern, not with a replacement word.
2. The current EntityOfConcern or claim kind is named before a direct governing pattern is applied.
3. The repair stops at the direct governing pattern once it is clear.
4. Slot discipline uses `A.6.5` and states SlotKind, ValueKind, RefKind or `ByValue` when slot claims are current.
5. Role claims keep `U.Role`, `U.RoleAssignment`, role description, role state, role relation structure, capability, method, plan, and work distinct.
6. Evidence-use and status-use cases are not represented through `U.RoleAssignment` for epistemes.
7. Interface wording is kept as a recognition cue but is not admitted as generic `U.Interface`.
8. Neighboring capability, affordance, method, function, concern, interest, publication, and source cases are governed by their direct governing patterns.
9. Any replacement candidate names kind, relation or slot, governing pattern, retained use, and blocked overread.
10. Quote-only or reduced-use labels do not make work, evidence, status, assurance, gate, decision, publication, or architecture claims admissible.

### A.6.RSIR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
|---|---|---|
| Rename `role` to `position` everywhere | It loses real `U.Role` cases and can create a new umbrella. | Recover whether the current object is `U.Role`, SlotKind, evidence-use position, status assertion, or ordinary prose. |
| Treat interface as one root kind | It merges module, functional, protocol, API, signature, publication, architecture, and boundary-package claims. | Recover the governing object first; then apply `A.6.M` for module-interface, `A.6.F` for functional port or functional structure, `A.6.0` and `A.6.5` for signature or relation-position claims, `E.17` for publication or API-description cases, `A.6.C` or `A.6.8` for agreement-like, protocol, SLA, service, or service-access cases, `A.6.B` only for L, A, D, or E statement classification inside a boundary package, or `C.30`, `C.30.ASV`, `C.30.AD`, or `C.30.TFS-REL` for architecture claims. |
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

The main ontological principle is slot discipline without slot overgeneralization. A slot position can admit a role, method, episteme, claim, holon, characteristic, or interface description as filler. That does not turn the filler into a new kind and does not turn the slot label into the filler.

The second principle is direct governance. Once the current object is recovered, the pattern that governs that object governs the repair. RSIR only identifies the direct governing pattern.

### A.6.RSIR:11 - SoTA-Echoing

This pattern does not introduce new external SoTA sources beyond the source uses already admitted by E.24 for ontic introduction. It applies those source uses to the narrower RSIR recovery problem.

| Practice or source line | Why it matters for RSIR | FPF adoption in this pattern |
|---|---|---|
| Modular ontology design-pattern work, including MODL, MOMo, and commonsense ontology micropatterns such as Shimizu and Hitzler 2024 and Eells, Dave, Hitzler, and Shimizu 2024. | Current ontology-engineering lesson: use small reusable ontology structures without copying local slot doctrine across patterns. | Adopt and narrow: RSIR does not become an ontic registry. It recovers the current governed object, then uses `A.6.5` for durable slot discipline, `E.24` for durable ontic decisions, and the direct governing pattern for filled-value claims. |
| Ontology-interoperability lifecycle work such as Qiang 2025 and 2026. | Current caution that overlapping labels and conflicting local concepts become expensive if not settled before reuse, matching, and validation. | Adapt as prevention: interface, role, slot, function, method, and concern words are treated as recovery cues until the current EoC, slot, relation, and governing pattern are named. |
| Process-representation ODP work such as Norouzi, Hertling, Waitelonis, and Sack 2025. | Current warning that process and workflow ontologies often hide implicit patterns from domain users. | Adapt for RSIR source labels: "process", "workflow", "method", "function", "parameter", and "interface" may remain useful source labels, but they do not carry FPF-governed content until the direct method, work, transformation-flow, role, slot, publication, or evidence pattern is selected. |
| gUFO, UFO, and OntoUML role, relator, situation, and high-order type practice, including Almeida, Guizzardi, Sales, and Fonseca 2026. | Current foundational-ontology constraint against flattening role values, relation positions, status classifications, and evidence uses into one taxonomy. | Adopt the boundary: `U.Role` and `U.RoleAssignment` remain work-facing; relation positions use `A.6.5`; evidence-use and status-use of epistemes use direct evidence, status, source, publication, assurance, or gate relations rather than `U.RoleAssignment`. |
| Current engineering architecture practice around functions, ports, modules, interfaces, signatures, and views. | Accepted internal-practice constraint from `A.6.M`, `A.6.F`, `A.6.0`, `E.18`, `C.30`, `C.30.ASV`, `C.30.AD`, and `C.30.TFS-REL`: these words are related but do not name one root kind. | Adapt as a positive recovery map: preserve interface and function language as recognition cues, then recover module-interface, signature, functional port, transformation-flow, architecture-of, structural-view, architecture-description, API publication, protocol, or plain source-label use by current claim. |

### A.6.RSIR:12 - Relations

`E.10` detects trigger wording. `E.10.ARCH` states that RSIR is the first-level restoration pattern for this bounded cluster when the direct governing pattern is not already clear.

`A.6.5` supplies SlotKind, ValueKind, RefKind, SlotSpec, and slot-operation discipline.

`A.6.P` governs relation precision restoration after the recovered object is a relation or relation-bearing claim.

`A.6.0` governs `U.Signature`; `A.6.1` and `E.20` govern mechanism claims.

`A.2`, `A.2.1`, `A.2.2`, `A.2.5`, `A.2.7`, `A.15`, and Part F role-description and naming patterns govern role, role assignment, capability, role state, role relation structure, role-method-work, and durable role-name claims.

`A.6.M`, `A.6.F`, `A.6.A`, `A.3.4.P`, `E.18`, `C.30`, `C.30.ASV`, `C.30.AD`, and `C.30.TFS-REL` govern module-interface, functional, affordance, transformation, transformation-flow, architecture-of, structural-view, and architecture-description cases.

`C.2.1`, `E.17`, `C.2.P.DR`, `A.10`, `B.3`, `G.6`, `F.10`, and `C.28` govern episteme, publication, declarative-representation, evidence, assurance, provenance, status, and causal-use cases.

### A.6.RSIR:End

