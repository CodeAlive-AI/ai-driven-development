## C.3.1 - U.Kind and U.SubkindOf Core

> **Type:** Kind identity, subkind relation, and continuity pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### C.3.1:0 - Use This When

Use this pattern when work must recover one reusable kind, decide whether one kind is a subkind of another, or decide whether the same kind continues across a changed `KindSignature` edition.

**What goes wrong if missed.** A source or practice label becomes an identity key, `U.SubkindOf` carries dependency or construction, a finite sample is mistaken for a universal order, mutually classifying kinds are silently merged, or a changed declaration is treated as automatically new or automatically harmless.

**What this buys.** The user gets an operational kind-continuity test, a replayable subkind test, and a small preorder that remains distinct from declaration identity, current extension, evidence, bridging, and public naming.

**Primary EntityOfConcern.** One `U.Kind` individual recovered through its candidate domain, operative membership condition, intended member/non-member distinction, and continuity rule; or one proposed `U.SubkindOf` relation between exact kind participants within declared applicability.

**First useful move.** Write the ordinary claim first: `CoolingPumpKind is a subkind of PumpKind because every candidate that satisfies the declared cooling-pump condition also satisfies the pump condition.` Then name the exact criteria and applicability that make that statement true. Introduce an occurrence designator or formal equivalence grouping only when a receiver uses it.

**Not this pattern when.** Use C.3.2 for a declaration, admissibility result, candidate classification, or extension; C.3.3 only for a claimed correspondence between independently identified distinct kinds; and `E.24.UK` when admitting another durable public kind rather than using an already admitted `U.Kind` individual.

### C.3.1:1 - Problem Frame

A practice/source boundary is provenance and a comparison cue. It affects the continuity decision only when comparison exposes a real difference in the candidate domain or membership distinction.

`U.SubkindOf` is separately admitted by `E24UK-AR-USUBKINDOF-R5-01` as a same-individual dependent kind under `U.Relation`. Its participants are an exact narrower kind and broader kind. An effective reference scheme and aligned `KindSignature` editions make the criteria interpretable and qualify applicability; they are not relation participants or occurrence-identity discriminators. Candidate state, context slice, declaration edition, kind identity, and one obtaining subkind relation can therefore change for different reasons.

### C.3.1:2 - Problem

The sentence `cooling pump is a pump` is useful only when the membership conditions justify it. A current extension table can hide a bad proposal, and different intensional kinds can happen to classify the same candidates. Conversely, a unit rewrite, source move, or clearer declaration need not create another kind. The core needs an obtaining test for the relation and a before/after test for kind continuity without treating a signature, sample, locality, or extension as the kind.

### C.3.1:3 - Forces

| Force | Tension |
| --- | --- |
| Small typed reasoning vs ontology growth | Projects need reusable kinds without a new public `U.*` name for each distinction. |
| Preorder vs kind identity | Mutual subkind facts may hold for different intensional kinds; classification equivalence must not collapse their identities. |
| Criterion entailment vs observed support | Exact rule entailment or exhaustive evaluation of a closed domain can establish the obtaining condition; a non-exhaustive sample only supports an assertion. |
| Stable kind vs changing declaration | A kind may continue across a compatible change, while a changed membership distinction must not inherit identity silently. |
| Applicability vs uncertainty | A non-applicable classification request is not an `unknown` judgment and cannot establish or refute a subkind fact. |
| Locality vs correspondence | A changed practice or source prompts comparison but does not establish another kind or a bridge. |

### C.3.1:4 - Core Objects

| Object | Meaning | Boundary |
| --- | --- | --- |
| `U.Kind` | The admitted meta-kind whose individuals are reusable intensional classification distinctions. One individual is recovered through its candidate domain, operative membership condition, intended member/non-member distinction, and continuity rule. | A `KindSignature`, label, source boundary, reference scheme, current extension, or receiving use is not the kind. |
| `U.SubkindOf` | The admitted direct relation kind whose occurrences relate exact narrower and broader `U.Kind` participants within declared applicability. Its obtaining facts form a preorder. | It is not a predicate expression, assertion episteme, dependency, part-whole relation, construction, system-role assignment, or admission relation. |
| `SubkindOfObtains(k1, k2)` | The relation-obtaining condition. It holds either because the exact membership criterion for `k1` entails the criterion for `k2` under an aligned interpretation and applicability, or because every candidate in a deliberately closed finite domain has been evaluated and every admissible `true` result for `k1` is also `true` for `k2`. | The first branch is criterion-based. The second is explicitly domain-bounded. Non-exhaustive observations support a separate assertion but do not make the relation obtain. |
| `R_sub : U.SubkindOf` | One obtaining relation occurrence between exact narrower kind `k1` and broader kind `k2`. | Use a designator only when a receiver needs it. The ordered kind participants determine occurrence identity; schemes, signatures, evidence, assertions, and publications do not. |
| subkind assertion episteme | A C.2.1 episteme that affirms, denies, or leaves unresolved the obtaining condition and cites its interpretation, applicability, branch, and support. | The assertion does not make the relation obtain; a negative or unresolved assertion designates no obtaining occurrence. |
| classification equivalence for an alignment | Mutual obtaining `U.SubkindOf` facts between two kinds within the same declared applicability. | It says that the two membership distinctions classify alike there. It does not identify the kinds. A consumer that needs a partial order may order these equivalence groups. |
| `KindSignature` edition | The C.3.2 declaration episteme used to interpret and evaluate one kind. | It is neither the kind nor the subkind relation. |

#### C.3.1:4.1 - Direct U.SubkindOf Relation Boundary

A readable sentence such as `CoolingPumpKind is a subkind of PumpKind for this declared plant use` states that the direct relation obtains. It needs no occurrence identifier when no receiver distinguishes or refers to the occurrence.

The relation obtains under the criterion-entailment branch when the exact narrower membership condition entails the broader one under the aligned interpretation and applicability. Under the closed-domain branch, it obtains only when the candidate domain is deliberately finite and closed, every candidate's admissibility has been checked, and exhaustive evaluation leaves no narrower `true` without a broader `true`. A counterexample refutes either proposal. A missing dependency or `unknown` judgment cannot establish either branch; a `not-applicable` request is outside the comparison.

When a receiver needs one occurrence, `R_sub` is participant-determined by the ordered pair of kind identities. The effective scheme, aligned signatures, and applicability qualify how obtaining is tested and asserted. A scheme-edition change therefore prompts an alignment and renewed test; it does not create another relation occurrence. If the same participants still satisfy the condition, the same relation continues to obtain. If they no longer do, the prior obtaining claim is no longer current; another assertion may record that change without inventing a scheme-keyed occurrence.

### C.3.1:5 - Solution

1. **Recover each kind before comparing it.** For each kind, state the candidate domain, membership condition, intended member/non-member contrast, and continuity rule. Use practice/source provenance to locate the declaration, not to decide identity.
2. **Check admissibility first.** Compare only candidates admissible under both aligned declarations and the stated applicability. `not-applicable` forms no C.3.2 judgment.
3. **Select one obtaining branch.** Use exact criterion entailment when the membership rules can be compared directly. Use exhaustive evaluation only for a deliberately closed finite domain. State which branch and where it applies.
4. **Keep observations in their proper role.** A non-exhaustive sample, test run, or extension can support the subkind assertion and expose a counterexample. It cannot close an open-domain obtaining claim.
5. **Keep a preorder over obtaining facts.** Reflexivity and transitivity apply. Mutual facts between distinct kinds record classification equivalence for that alignment; they do not imply kind identity. Use the equivalence groups only when a receiver needs a partial order.
6. **Separate relation, predicate, and assertion.** Use the readable relation sentence first. Add `R_sub`, a C.2.1 assertion, evidence, or publication only when a named receiver consumes that object.
7. **Diagnose counterexamples at the rule.** Repair a false relation proposal, incompatible declaration alignment, or missing distinct-kind bridge. Do not edit an extension row to make the order appear true.
8. **Decide kind continuity independently.** Apply the before/after test in section 6 whenever criterion, candidate domain, assumptions, dependencies, effective scheme, or locality changes. Another `KindSignature` edition neither proves nor denies kind continuity.
9. **Keep scope and Work outside the kind.** A kind carries no claim scope. An exact `W : U.Work` remains a dated work occurrence under its direct pattern; keep it distinct from a plan, log, label, classification record, or episteme about W.

### C.3.1:6 - Continuity Decision

Compare the old and proposed declarations in this order:

| Question | Continuity consequence |
| --- | --- |
| What candidate domain and operative membership condition did the old kind use? | Write at least one intended member and one relevant non-member or boundary case that exposes the discriminator. |
| What exact criterion, domain, assumption, dependency, or interpretation changed? | Separate a wording, unit, source, or scheme change from a changed membership law. |
| Under an explicit alignment, do the old and new conditions classify the boundary probes alike for the receiving typed use, and does the operative discriminator keep the same meaning? | If yes, the same kind may continue; cite the actual declaration edition in each judgment. If no, identify another kind. |
| Did only the practice, source, team, or publication locality change? | Run the same comparison. Locality alone supplies no result and no `KindBridge`. |
| Are two distinct kinds now being related? | State an obtaining `U.SubkindOf` fact when its criterion or closed-domain branch passes. Use C.3.3 only for a separately justified directional correspondence. |

**Preserving change.** `CoolingPumpSignature-3` replaces litres-per-second with an exactly aligned SI expression, preserves the pump candidate domain, cooling-performance discriminator, intended member and non-member probes, and maintenance use. The same `CoolingPumpKind` continues; new judgments cite edition 3.

**Identity-breaking change.** A proposed edition replaces physical cooling performance with the presence of schema label `CoolingPump`. A physical pump without the row changes from member to non-member and a labelled non-performing row can appear to qualify. The operative distinction and candidate domain changed; identify another kind rather than continuing `CoolingPumpKind`.

**Locality change.** Journal and grant teams may reuse one exact `ReviewerSystemRole` when candidate Systems, required contribution, and acceptance condition remain aligned. If grant review requires a different contribution or admits a materially different candidate boundary, identify another kind. The two labels decide neither case.

### C.3.1:7 - Archetypal Grounding

| Situation | C.3.1 move | Boundary |
| --- | --- | --- |
| `CoolingPumpKind` is below `PumpKind`. | Use criterion entailment: the cooling-pump condition already requires the governed pump condition. State the readable relation and its applicability. | Do not infer a public `U.CoolingPump`, and do not use current extension rows as the truth-maker. |
| A closed inspection lot has five cabinets. | If the declared candidate domain is exactly those five cabinets, check admissibility and evaluate every candidate. The domain-bounded subkind relation from `InspectedCabinetKind` to the proposed broader kind can obtain when every narrower `true` is broader `true`. | The same observations do not establish an open-ended order over all future cabinets. |
| `MorningShiftQualifiedOperatorKind` and `UnionRosteredOperatorKind` happen to select the same people in a closed current roster. | Mutual domain-bounded subkind facts may obtain, giving classification equivalence for this roster. | The kinds remain distinct because their operative membership conditions differ; antisymmetry does not merge them. |
| A signature adds an aligned unit conversion. | Apply section 6, keep the kind, identify the new signature edition, and retain edition-specific judgments. | Do not rewrite earlier judgments as if the new edition had been used. |
| A signature changes from physical cooling performance to a schema label. | The boundary probes expose a changed candidate domain and discriminator; identify another kind. | Do not hide the mismatch by editing the extension. |
| Pump #14 changes state in a later plant slice. | Re-evaluate the admissible candidate and allow the extension to change. | Candidate-state change alone does not create a kind, signature, or relation occurrence. |
| `InspectionWorkKind` is used locally. | Classify only an independently identified `W : U.Work`. | `U.Work`, a plan, or a log row cannot occupy W's candidate position. |
| `WorkPlan` depends on Work. | Use the governing work or E.24.UK relation. | Do not encode dependency as `U.SubkindOf`. |
| `SafetyCriticalFunctionKind` is proposed as a subkind of `FunctionKind`. | First recover both function senses under A.6.F, then use exact criterion entailment or the deliberately closed-domain branch. | The word *function*, a risk label, or current examples establish neither the kinds nor the subkind fact; another public `U.*` name still requires E.24.UK. |
| A project proposes public `U.CoolingPump`. | Take the recovered kind to `E.24.UK`, then apply naming patterns if admitted. | Local typed use and `U.SubkindOf` do not admit or publish another durable kind. |

### C.3.1:8 - Bias-Annotation

C.3.1 counters hierarchy, sample-as-law, assertion-as-world, locality, and table-repair bias. A stronger-looking edge is not automatically an obtaining relation; a sample does not close an open domain; mutual classification does not identify two intensional kinds; a changed source does not split one; and an extension remains an output representation rather than the place to repair the rule.

### C.3.1:9 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C31-1` | Each `U.Kind` individual has a recoverable candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule. Practice/source provenance is a comparison cue, not an automatic identity discriminator. |
| `CC-C31-2` | `U.SubkindOf` cites `E24UK-AR-USUBKINDOF-R5-01`, has exact ordered kind participants, declared applicability, one valid obtaining branch, and participant-determined occurrence identity. |
| `CC-C31-2a` | Predicate content, C.2.1 assertion, evidence item, representation edge, scheme and signature editions, and optional occurrence designator remain distinct; none makes the relation obtain by form. |
| `CC-C31-2b` | Obtaining facts form a preorder. Mutual facts between distinct kinds record classification equivalence for the alignment; a partial order is formed only over equivalence groups when needed. |
| `CC-C31-3` | Criterion entailment compares exact membership rules under aligned interpretation, or exhaustive evaluation covers a deliberately closed finite domain. Non-exhaustive observations support only the assertion. |
| `CC-C31-4` | Only candidates admissible under both declarations enter the comparison. `unknown` neither establishes nor refutes a universal proposal; `not-applicable` forms no judgment. |
| `CC-C31-5` | Reference schemes and declaration editions qualify interpretation, applicability, and assertions but do not identify the relation occurrence. An aligned edition change triggers reevaluation of the same participant-determined relation. |
| `CC-C31-6` | Kind continuity uses before/after candidate-domain, membership-discriminator, member/non-member probes, and receiving-use tests; old judgments retain their cited edition. |
| `CC-C31-7` | A locality change prompts the continuity test; C.3.3 is used only after two distinct kinds and a correspondence proposal exist. |
| `CC-C31-8` | Scope is absent from the kind, and `U.Work`, one `W : U.Work`, and any episteme about W remain distinct. |

### C.3.1:10 - Common Anti-Patterns and How to Avoid Them

* Encoding dependency, part-whole, slot filling, construction, system-role assignment, or admission as `U.SubkindOf`, or treating a predicate expression, assertion, diagram edge, or table row as the obtaining relation occurrence.
* Treating a source hierarchy or public-looking spelling as durable FPF ontology.
* Treating `KindSignature` as the kind or its formality as a property of the kind.
* Assuming every signature edit makes a new kind, or that no signature edit can make one.
* Comparing extensions across incompatible editions and repairing a counterexample by changing rows.
* Storing claim scope on a kind.
* Treating a work label or record as an individual work occurrence.

### C.3.1:11 - Consequences

**Benefits.** Local typed compatibility remains small while its consequences for actual candidate judgments are testable.

**Costs.** A declaration change that matters to later classification needs an explicit edition and a separate continuity decision.

**Risks avoided.** False hierarchy, silent redefinition, retrospective reinterpretation, table-created membership, and kind/individual substitution are blocked.

### C.3.1:12 - Rationale

Kind identity, direct `U.SubkindOf` obtaining, assertion identity, declaration identity, candidate state, and current extension answer different questions and change under different conditions. Their separation lets a kind survive a compatible declaration revision while preventing an assertion or revised criterion from creating an order fact, silently rewriting prior classifications, or hiding a non-obtaining subkind proposal. Keeping the core small also prevents construction, admission, naming, scope, slot discipline, or dependency from being smuggled into one hierarchy relation.

### C.3.1:13 - SoTA-Echoing

Type theory, ontology engineering, and versioned schema practice distinguish intensional identity, preorders, equivalence classes, interpretation editions, and extensions. C.3.1 keeps that distinction but gives practitioners two replayable obtaining branches and a before/after continuity test; C.3.2 owns admissibility and judgment, C.3.3 owns distinct-kind correspondence, and E.24.UK owns the exact public admissions.

### C.3.1:14 - Relations

- **Specializes:** `A.6.REL` for `U.SubkindOf`: exact ordered kind participants, criterion-entailment or exhaustive closed-domain obtaining, applicability, lightweight occurrence use, and participant-determined identity; schemes and declaration editions qualify interpretation and assertion rather than occurrence identity.
- **Builds on:** `C.3`, A.6.0 declaration identity, C.2.1 episteme and assertion identity, A.2.6/USM context-slice and scope discipline, F-G-R, and C.2.3 formality.
- **Coordinates with:** `C.3.2` judgments and extensions, `C.3.3` correspondence between independently identified distinct kinds, `A.2` when one local kind is a system-role kind, `A.6.5` declaration-slot uses that consume an already obtaining subkind relation, `C.29` representations, `E.24.UK` durable U-kind admission, and `A.8`, `A.11`, `F.8`, and `F.5` when public kind governance is current.
- **Other governing patterns:** Use C.2.1 for subkind-assertion epistemes, whether affirmative, negative, or unresolved; candidate features, classification assertions, kind declarations, context bridges, and public naming decisions retain their own governing patterns.

### C.3.1:End

