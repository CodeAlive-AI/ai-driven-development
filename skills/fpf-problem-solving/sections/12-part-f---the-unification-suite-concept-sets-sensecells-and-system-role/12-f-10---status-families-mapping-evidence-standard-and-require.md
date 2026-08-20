## F.10 - Status Families Mapping: Evidence, Standard, and Requirement Status

> **Type:** Boundary and relation-use pattern
> **Status:** Stable
> **Normativity:** Normative

### F.10:1 - Problem frame

**Use this when.** Use F.10 when a receiving use depends on a word such as *observed*, *measured*, *validated*, *approved*, *deprecated*, *satisfied*, *violated*, *waived*, *pending*, *current*, or *ready*, and the exact status value, governed target, scope, window, source, rule, or use is still implicit.

Use it especially when evidence, standards, and requirements are being mixed: a dashboard says a service is ready, a standard says a method is approved, a measurement is cited as requirement satisfaction, a model card says a model is validated, or a requirement register says a clause is waived.

**Primary EntityOfConcern.** The live object is one exact status-use relation around an already governed bearer or target, one local status value, one ClaimScope/use scope, one validity window, and one intended receiving use. F.10 does not define or create the target and does not turn a display, source, list membership, approval act, evaluation rule, result, or evidence item into the status-use relation.

**First useful move.** Recover the exact target and its direct domain result first. Then name the status-value SchemeSenseCell and family under the effective ReferenceScheme, status scope/window, exact source and provenance/currentness constraints, intended use, and stronger use not carried. If a rule must be applied, name the dated evaluation work, rule application, and result separately.

**What goes wrong if missed.** One compact word does the work of domain result, evidence standing, standard approval, requirement satisfaction, gate passage, release readiness, permission, and assurance at once. A dashboard list or traffic-light cell is treated as actual status use. An F.9 Bridge or family edge is treated as the explanation or evaluation rule. Design approval becomes runtime satisfaction.

**What this buys.** Status words remain local, typed, comparable, and usable without hiding the target or the work that justified the status. Evidence status says only what evidential standing is being asserted for a claim; standard status says only what a named governing source sanctions; requirement status says only what is being asserted about an exact clause after its direct evaluation. Cross-local vocabulary and cross-modality interpretation remain explicit and loss-aware.

**Not this pattern when.** Use the subject's direct pattern for its target and domain result; `A.2.4` for first evidence/status-use classification; `A.10`/`G.6` for source recovery, provenance, and bounded reliance; `G.11` for currentness; `B.3` for assurance; `C.28` for causal use; `A.21` for a gate; the direct permission, commitment, requirement, standard, acceptance, release, or decision pattern for those results; `E.17`/`E.24.PUB` for publication; and `A.15.1`/`A.6.1` for performed evaluation work and actual bindings.

### F.10:2 - Problem

Status vocabulary is useful because it is compact. It is dangerous because the same label often hides different objects and claims:

1. **Modality collapse.** *Validated* is read as evidence standing, standard approval, requirement satisfaction, and release permission at once.
2. **Target collapse.** The status does not say whether it concerns a claim, quantity, method description, standard edition, clause, system-role assignment, work result, publication, gate record, or another exact target.
3. **Result collapse.** A measurement, proof, conformance verdict, requirement-evaluation result, or assurance result is renamed as a generic status instead of retained under its direct governor.
4. **Window and scheme loss.** Status is asserted without the effective ReferenceScheme, ClaimScope, conditions, edition, or relevance window that makes contradiction and freshness checkable.
5. **Source and display collapse.** A badge, list row, dashboard tile, screenshot, certificate view, or generated summary becomes the status source or status use by visibility.
6. **Design-run substitution.** Standard approval is read as runtime satisfaction, or runtime evidence as approval, without an exact interpretation relation and evaluation rule.
7. **Bridge overread.** Shared spelling, a common family label, an F.17 row, an F.18 NameCard, or an F.9 Bridge is treated as the direct explanation, status application, or target result.
8. **Episteme use drift.** A report, standard, model card, dashboard cell, or requirement document is said to hold an “evidence role”, “status role”, or “standard role” rather than participate in an evidence-use, status-use, source-use, standard-use, or requirement-use relation.

### F.10:3 - Forces

| Force | Tension this pattern resolves |
| --- | --- |
| Local fidelity versus reuse | Status meaning is local to an effective ReferenceScheme, yet projects must explain or compare statuses across schemes. |
| Compact label versus recoverable relation | A quick display is useful, while target, value, scope, window, source, rule, and use must remain recoverable before reliance. |
| Evidence versus standard versus requirement | Evidence standing is epistemic; standard and requirement statuses are deontic in different ways. |
| Direct result versus status | A domain result may justify a status assertion, but the result and status remain different objects. |
| Design stance versus runtime standing | Approval of a description or profile does not show what happened in one run. |
| Cue versus actual use | Display and list membership aid retrieval but do not establish source, evaluation, currentness, status use, or downstream reliance. |
| Ordinary speech versus kind discipline | “The role of this status” is repaired as an exact use relation, not as a work-facing role held by an episteme. |

### F.10:4 - Solution

Recover the governed target and direct result before applying a local status. Treat status value, status-use occurrence, status assertion, source, evaluation, display, and receiving use as distinct.

#### F.10:4.1 - Three status families

F.10 supplies a small set of three status families—`EvidenceStatus`, `StandardStatus`, and `RequirementStatus`—for common project use. A family classifies local status values; it is not a universal result kind and does not create its targets.

| Status family | Modality | Typical exact target | What the family permits one status-use assertion to say |
| --- | --- | --- | --- |
| `EvidenceStatus` | epistemic | exact target-claim episteme or claim-bearing result episteme | The asserted evidential standing of that claim for one scope, polarity, window, and use, after exact A.2.4 evidence-use and direct input results are recovered. It is not the measurement/proof/causal result or evidence relation itself. |
| `StandardStatus` | deontic and curatorial | exact standard/profile edition, method description, governed configuration, or other admitted standard target | What the exact governing source sanctions, discourages, or supersedes for one scheme, edition, scope, window, and use. It is not an approval speech act, permission, runtime result, or requirement satisfaction. |
| `RequirementStatus` | deontic and compliance-facing | exact requirement, duty, constraint, acceptance, or obligation clause | What is asserted about applicability, satisfaction, violation, waiver, or pending evaluation for that clause under its direct rule, scope, conditions, and window. It is not the clause, evaluation work, result, gate, or assurance. |

A project may define local sublevels or labels, but each label resolves under one effective ReferenceScheme to one exact local sense and maps to one of these three families—`EvidenceStatus`, `StandardStatus`, or `RequirementStatus`—or to another status family defined by its own pattern. Adding a family row creates neither a system-role kind nor a global synonym.

#### F.10:4.2 - Status value, use occurrence, assertion, and display

A local status value is designated through an exact F.17 `SchemeSenseCell`:

```text
<EffectiveReferenceScheme, LocalExpression, LocalSenseClaim>
```

An F.18 NameCard may govern its selected public designation. An F.17 row may collect one or more cells for a named unification use; one-cell rows are valid. Neither the cell, card, row, spelling, nor family membership applies the value to a target.

One `StatusUseRelation` candidate names:

```text
StatusUseRelation:
  StatusBearerRef:
  StatusTargetRef:
  DirectTargetAndResultGovernor:
  DirectResultRef:                 # when a domain result is consumed
  StatusValueCellRef:
  StatusFamilyRef:
  EffectiveReferenceScheme:
  StatusScope:
  StatusWindow:
  IntendedStatusUse:
  SourceClaimEpistemeRef:
  SourceRelationOrRegisterRef:
  EvaluationWorkRef:               # when a rule is applied
  EvaluationRuleAndApplicationRef: # when a rule is applied
  EvaluationResultClaimRef:        # when a result is produced
  ProvenancePathRef:
  CurrentnessRef:
  NotCarried:
```

For an F.10-family status, `StatusUseRelation(B,T,V,G,W,U)` obtains only when: `B` and `T` resolve to admitted governed objects; exact cell `V` has the required F.10 family/local sense under its effective ReferenceScheme; the family-specific source and any direct result/evaluation basis support applying `V` to `T`; `G` and `W` bound that application; and `U` is the named intended use without a stronger inference. Unknown or missing basis yields no positive occurrence and a `Pending`, `Inconclusive`, or explicit unresolved disposition only when that value's own rule is satisfied. Absence of evidence is never target falsity.

One F.10 occurrence is identified by the exact ordered tuple `<B,T,V,G,W,U>`. Repeated evaluations, assertions, displays, rows, records, or citations create no duplicates. A changed bearer, target, value cell, scope, window, or intended use identifies another candidate. A changed source, evidence path, evaluation, or currentness fact can change whether the fixed candidate is warranted or obtains; it is not silently copied into relation identity. A status under another exact predicate keeps its own subject assertion and defining or constraining `ClaimGraph` instead of inheriting this predicate by family resemblance.

A distinct C.2.1 status-assertion episteme states affirmative or negative polarity for the exact `StatusUseRelation`. A separate display or publication form may render that assertion. The assertion does not perform evaluation, and the display does not become the assertion, source, or actual receiving use.

#### F.10:4.3 - Recover the target and result first

Use this order:

1. name the receiving question and exact target;
2. recover the target's identity and direct governor;
3. recover any measurement, formal, causal, conformance, diagnostic, comparison, acceptance, requirement-evaluation, gate, assurance, permission, or decision result under its own pattern;
4. identify the C.2.1 episteme that states that result;
5. resolve the local status expression to its exact F.17 cell and F.10 family;
6. recover the source, edition, scheme, scope, conditions, window, provenance, and currentness required by this status use;
7. when a rule is needed, identify dated evaluation work, enacted method, exact direct/A.6.1 application, and evaluation-result claim;
8. assert the status-use relation and its C.2.1 status-assertion episteme; then separately recover publication/display and any actual later premise, decision-use, status-use, gate-use, or operation-argument relation.

Status never defines or constitutes the target. A changed status may change a receiving disposition without changing target identity or the earlier domain result. Conversely, a changed target or direct result requires the status application to be re-evaluated; copying the old value is not continuation proof.

#### F.10:4.4 - A.2.4 status-use positions

When an A.2.4 first-use classification is current, retain its positions by value:

| Position | F.10 use |
| --- | --- |
| `StatusBearerSlot` | Bearer from which the status is asserted or read. This is not a system-role-holder position and does not by itself make the bearer an assignment holder. The same bearer may separately be admitted as a `U.System` and be the holder in an occurrence of a declared assignment species. |
| `StatusTargetSlot` | Exact governed target; required when different from the bearer. |
| `StatusScopeSlot` | Claim, requirement, admission, or use scope; not a generic context object. |
| `StatusValueSlot` | Exact local status-value cell or value governed here or by another direct status pattern. |
| `StatusWindowSlot` | Validity, edition, freshness, or source window. |
| `StatusUseSlot` | Named intended use; actual later use still needs its dated work and direct relation. |
| `StatusProvenanceConstraintSlot` | Exact source order, authority source, publication, proof, verification, register, or provenance condition. |

These are relation positions, not system-role-kind qualifier slots, a record schema that applies status, or a new generic status ontic.

#### F.10:4.5 - Family value sets

**EvidenceStatus** local values:

1. `Observed` — seen or recorded once under declared observation conditions.
2. `Measured` — supported by a declared measurement method, model, calibration basis, value, and uncertainty.
3. `Corroborated` — supported by more than one independent source, procedure, or observation line.
4. `Replicated` — repeated by independent work or under varied declared conditions.
5. `Refuted` — counter-evidence defeats positive evidential standing inside the same scope and window.
6. `Inconclusive` — available input results and evidence-use relations are insufficient or mixed for the target claim.

These values classify evidential standing; they do not replace the observation, measurement, proof, causal, or other direct result, and `Inconclusive` is not target falsity.

**StandardStatus** local values:

1. `Candidate` — proposed and not yet normative for the named scheme/use.
2. `Draft` — worked text or profile, not yet the governing edition.
3. `Approved` — sanctioned by the exact governing source for the named scheme, edition, scope, window, and use.
4. `Deprecated` — discouraged, conditionally allowed, or being phased out.
5. `Superseded` — replaced by another named edition, profile, or governing source.

`Approved` does not mean that an approval act occurred unless its direct speech-act/decision relation is separately recovered; it grants no permission and proves no runtime satisfaction.

**RequirementStatus** local values:

1. `Applicable` — the exact clause binds under its governed scope, conditions, and window.
2. `Inapplicable` — the clause does not bind under those conditions.
3. `Satisfied` — a direct requirement/acceptance evaluation result says the clause is met for the exact target, scope, conditions, and window.
4. `Violated` — the direct evaluation result says it is not met there.
5. `Waived` — binding is suspended or excepted by an exact authorized source/relation and window.
6. `Pending` — the status application awaits a needed source, input result, evaluation, decision, or currentness repair.

`Satisfied`, `Violated`, `Waived`, and `Pending` do not replace the clause, evaluation work/result, waiver act or permission, gate decision, assurance result, or action.

#### F.10:4.6 - Bridge and interpretation discipline

Status meanings do not travel by label. When two local status senses under different ReferenceSchemes must be compared, use the actual F.9 Bridge occurrence between the exact F.17 SchemeSenseCells, with direction, bridge kind, tolerance/loss, and bounded use. Its Card or description is separate and optional; optional F.9 `CL` remains evidence-strength shorthand, not a use threshold. The Bridge makes no status-use occurrence obtain and produces no target result.

When one status-use occurrence is used to explain or evaluate a status question of another family, scheme, or modality, recover an exact `StatusInterpretationRelation`:

```text
StatusInterpretationRelation:
  SourceStatusUseOccurrenceRef:
  TargetStatusQuestionRef:
  Direction:
  InterpretationRuleRef:
  EffectiveReferenceScheme:
  ClaimScopeAndWindow:
  BridgeRef:                    # only when local senses cross schemes
  IntendedUse:
```

It obtains only when the named interpretation rule admits that source occurrence for the exact target question, direction, scope, window, and use. Its occurrence identity is the exact ordered `<SourceStatusUseOccurrenceRef, TargetStatusQuestionRef, Direction, InterpretationRuleRef, ClaimScopeAndWindow, IntendedUse>` tuple; a Bridge ref is a separate qualifying premise when local senses cross schemes. A family edge, shared word, Bridge, table row, or source order is not this relation. Applying the rule is separate dated evaluation work; its result claim is separate again. Even a positive interpretation relation does not by itself produce `RequirementStatus=Satisfied`, `StandardStatus=Approved`, a gate result, permission, assurance, or actual later reliance.

#### F.10:4.7 - Design-run discipline

Keep three questions separate:

* What do exact observation, measurement, proof, causal, or other input results warrant as evidence standing for this target claim and window?
* What does an exact governing source sanction for this method description, profile, standard edition, or configuration and use?
* What does direct requirement-evaluation work conclude about this exact clause, target, scope, conditions, and runtime/design window?

A standard-approved method description may be admissible for selection under that profile. It does not show that the method was enacted or that a runtime clause was satisfied. Runtime evidence may become an admitted input to requirement evaluation through an exact evidence-use and status-interpretation relation. It does not approve the method, standard, gate, or release.

### F.10:5 - Archetypal grounding

#### F.10:5.1 - Service acceptance from runtime evidence

July uptime is first recovered as an exact C.16 measurement result, stated by a distinct C.2.1 episteme. A.2.4 classifies that episteme for the uptime claim, and F.10 may assert `EvidenceStatus=Measured` for that exact claim, scheme, scope, and July window.

The SLO clause and service target are independently recovered. Dated evaluation work applies the SLO rule to the measurement result through exact bindings and produces a requirement-evaluation result claim. Only that basis can support a separate `RequirementStatus=Satisfied` occurrence. If monitoring and service-management senses differ, an F.9 Bridge handles the cells and a `StatusInterpretationRelation` handles the admitted explanatory/evaluation use. The measurement, evidence status, bridge, interpretation, evaluation work/result, requirement status, dashboard display, gate, assurance, and release decision remain distinct.

#### F.10:5.2 - Approved method description

One exact safety-controller MethodDescription is `StandardStatus=Approved` only under the named standard/profile edition, source relation, scheme, scope, window, and selection use. That status neither creates the MethodDescription nor proves an approval speech act, permission, method enactment, or response-time satisfaction.

A particular controller run is separate `U.Work`. Its response-time measurement result and evidence-use relation can enter direct clause-evaluation work. A separate requirement status may follow from that evaluation; it does not inherit `Approved` by label or family edge.

#### F.10:5.3 - Model card and fairness requirement

A model card reports high cross-validation AUC. Recover the exact predictive-performance result and claim episteme first; the card is a publication/display. F.10 may assert an `EvidenceStatus` for that predictive claim under its validation scheme and window. It cannot decide the different policy clause “demographic parity delta ≤ 0.1”. That branch needs production-window fairness measurement, its result episteme/evidence use, the policy clause, dated evaluation work, the exact policy rule application, and its own requirement-status assertion.

#### F.10:5.4 - Status display cue

A release dashboard cell shows `Ready`. The cell is only a cue until exact source assertion, target, value cell, scheme, scope, window, provenance/currentness, and intended use are recoverable. Display or list membership does not establish a status-use occurrence or actual reliance. If the status is consumed for a gate, release, assurance, admission, permission, or decision, the subject pattern must admit the separate use and result.

### F.10:6 - Bias-Annotation

F.10 blocks five recurring biases:

* **label-authority bias:** familiar wording is treated as source authority;
* **target-by-status bias:** assigning a value is treated as defining or creating its target;
* **display/list bias:** visibility, row membership, or dashboard aggregation is treated as application or actual use;
* **family/bridge explanation bias:** a family edge, shared spelling, row, Card, or Bridge replaces the exact interpretation relation and rule; and
* **system-role drift:** an evidence, status, standard, or requirement use is treated as proof that its bearer is a `U.System`, has a local system-role classification, or holds a system-role assignment.

The repair is to recover target and direct result first, then the exact local value, relation occurrence, assertion, evaluation basis, display, and receiving use. None of those use facts establishes System admission, a local system-role classification, or an assignment. The same bearer may have those neighbouring facts only when it independently passes System admission and is the holder of an assignment occurrence whose declared species is known.

### F.10:7 - Conformance checklist

| Check | Pass question |
| --- | --- |
| `CC-F10-01` Target and direct result | Are the exact target, target identity, direct governor, and any consumed domain result/result episteme recovered before status is applied? |
| `CC-F10-02` Local value | Does the status expression resolve to an exact F.17 SchemeSenseCell under an effective ReferenceScheme and to one family/direct status pattern? |
| `CC-F10-03` Use occurrence | Are bearer, target, value, scheme, scope, window, intended use, and direct obtaining basis explicit? |
| `CC-F10-04` Source | Are source assertion/register, edition/order rule, provenance path, and G.11 currentness result recovered when they decide use? |
| `CC-F10-05` Assessment | If a rule is applied, are dated evaluation work, enacted method, exact application/bindings, and evaluation-result claim separate? |
| `CC-F10-06` Assertion/display | Is the C.2.1 status-assertion episteme distinct from publication occurrence, form, rendering, carrier, row, and dashboard cell? |
| `CC-F10-07` Modality | Are evidence status, standard approval, requirement status, and every direct result kept distinct? |
| `CC-F10-08` Bridge | Does cross-scheme vocabulary use cite an actual F.9 occurrence between exact cells, while Card/description remains separate? |
| `CC-F10-09` Interpretation | Does cross-family or cross-modality explanation name the exact `StatusInterpretationRelation`, direction, rule, scope/window, and use? |
| `CC-F10-10` Design-run | Are standard approval, runtime evidence, requirement evaluation, and runtime satisfaction separate? |
| `CC-F10-11` Receiving use | Is any actual premise/gate/assurance/permission/release/decision use grounded in dated work and its direct relation rather than intended use or display? |
| `CC-F10-12` No creation | Does status neither define/create its target nor turn evidence absence into target falsity? |
| `CC-F10-13` No system-role drift | Does evidence, status, standard, or requirement use refrain from establishing System admission, a local system-role classification, or an assignment? When a receiving claim needs an assignment, does it name the occurrence and its declared species? Does the occurrence carry every required participant value and have the independently admitted System as holder? |
| `CC-F10-14` Subject-pattern boundary | Do evidence provenance, assurance, causal use, publication, gate, permission, commitment, work, requirement evaluation, approval act, and decision remain with direct governors? |

### F.10:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| `Validated -> approved -> compliant` | One label carries evidence, standard, requirement, and release status. | Split the target/result/status occurrences; add exact Bridge, interpretation relation, evaluation work, and rule only where current. |
| Approved method means SLO satisfied | Design approval becomes runtime result. | Keep MethodDescription approval, method enactment, runtime result, and clause evaluation separate. |
| Evidence status as domain result | `Measured`, `Corroborated`, or `Refuted` replaces measurement, proof, causal, or diagnostic result. | Recover the direct result and result episteme first; evidence status only classifies evidential standing for the named use. |
| Status defines target | A `Ready` or `Approved` row is treated as constituting a service, method, clause, person/team state, or product. | Recover target identity under its direct governor before status application. |
| Status badge or list membership as use | Display, list, or row membership is treated as source, status application, gate passage, or reliance. | Recover assertion/source and the separate actual receiving-use relation. |
| Clause-less compliance | *Compliant* is asserted without an exact clause, target, rule, scope, conditions, and window. | Recover the clause and direct evaluation result. |
| Bridge-free roll-up | A dashboard aggregates local labels as global synonyms. | Use exact cells and F.9 occurrences, or downgrade to local explanation. |
| Bridge/family edge as explanation | A Bridge or `EvidenceStatus -> RequirementStatus` arrow is treated as direct reason. | Name the `StatusInterpretationRelation`, exact rule, evaluation application, and result. |
| Evidence escalation without independence | One repeated lab result is called replicated. | Keep it measured/corroborated until independent replication conditions and results are recovered. |
| Status role for episteme | A report, standard, or requirement is said to ‘hold a role’. | Use the A.2.4 and F.10 use relations. They establish neither System admission, local system-role classification, nor an assignment. If the receiving claim needs an assignment, name the admitted System, declared assignment species and occurrence, and that System as its holder. |
| Tool-state explosion | Every local tool state becomes a durable status kind. | Keep tool labels local; create a durable cell/family mapping only for a receiving use that needs it. |

### F.10:9 - Consequences

F.10 adds a small amount of relation recovery before status can be relied on. The user names exact target/result, local value, scheme, scope, window, source, rule, and use instead of letting a word decide everything.

The payoff is practical: teams can compare statuses across disciplines, explain why a status was asserted or rejected, locate bridge/interpretation loss, and stop a display from becoming target truth, permission, assurance, gate passage, or work evidence.

The cost is that F.10 cannot decide neighboring results. It does not perform measurement or evaluation, compute assurance, approve a standard by speech act, satisfy a clause, pass a gate, authorize work, prove causal effect, decide currentness, or establish actual downstream use.

### F.10:10 - Rationale

Status words sit at the meeting point of evidence, norms, and action, so they are tempting shortcuts. The shortcut remains safe only when target, direct result, local sense, scope/window, source, evaluation rule, and intended/actual use stay visible.

The small set of three status families—`EvidenceStatus`, `StandardStatus`, and `RequirementStatus`—supports quick recognition without becoming a common result algebra. F.17/F.18 govern local sense and designation; F.9 governs cross-local sense bridges; F.10 governs the status-use and interpretation questions; direct subject, evidence, work, result, assurance, gate, permission, and decision patterns retain their own objects.

### F.10:11 - SoTA-Echoing

| Practice question | Exact source and source-use status | F.10 adoption and rejected overread | Currentness and reopen condition |
|---|---|---|---|
| How should a requirement status stay attached to an exact clause and evaluation use? | [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html), confirmed current in 2024, is a **current standard reference** for requirements-engineering processes and information items. It does not supply F.10's status algebra. | **Adapt.** `RequirementStatus` targets one requirement or clause under explicit scope, conditions, window, and a direct evaluation result. Reject *compliant* without the clause, applicable rule, and result; neither a requirement document nor its lifecycle label proves satisfaction or waiver. | Reopen when 29148 is revised or a stronger cross-domain requirements source changes which clause, applicability, evaluation, or result distinctions must remain visible. |
| How should a standard's edition and lifecycle standing remain distinct from approval of a method or configuration? | ISO's [international harmonized stage codes](https://www.iso.org/stage-codes.html) and [standards-development stages](https://www.iso.org/stages-and-resources-for-standards-development.html) are **current primary ISO process references** for publication, review, confirmation, revision, and withdrawal states. | **Adapt only the separation between an edition and its status.** `StandardStatus` names the exact source edition, target, scheme, window, and use. Reject the inference from a source's publication or confirmation state to enactment, runtime satisfaction, permission, compliance, or project approval. | Reopen when ISO changes the stage model or when another governing source family used by FPF needs a materially different distinction between edition and currentness. |
| What does provenance establish, and what does it not establish about evidence standing? | W3C [PROV-O](https://www.w3.org/TR/prov-o/) (2013) is a stable Recommendation retained as **provenance lineage and reference**; it distinguishes entities, activities, agents, and qualified provenance relations. | **Adapt the separation, not a truth claim.** Recover the exact observation or result, source, provenance relation, and evidence-use relation before assigning `EvidenceStatus`. Reject provenance presence as target truth, corroboration, assurance, or sufficient evidence by itself. | Reopen if W3C supersedes PROV or a current evidence standard changes the provenance-to-evidence-use boundary consumed by F.10. |
| How should cross-local status words remain local rather than becoming global synonyms? | [ISO 704:2022](https://www.iso.org/standard/79077.html) is a **current terminology standard** linking objects, concepts, definitions, and designations; F.9 supplies FPF's current relation between exact local senses. | **Adapt.** Recover each local value cell and use an exact F.9 Bridge plus a separate interpretation rule when cross-local use is intended. Reject shared spelling, a family edge, or a mapping card as explanation, evaluation, substitution, or global identity. | Reopen when ISO 704 or the F.9 relation model changes the distinction between designations and concepts or the cross-local mapping used here. |
| Why are a credential or dashboard view, its status, and a relying decision different objects? | W3C [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) (2025) is a **current W3C Recommendation** that separates issuer, subject, holder, verifier, credential, presentation, and credential-status information, and leaves authorization decisions outside the data model. | **Adapt.** A visible credential, register row, or dashboard cell is a cue or presentation. Recover the source assertion, target, status value, currentness, and actual receiving use separately. Reject display, verification, or credential status as permission, gate passage, assurance, system-role assignment, or relying decision. | Reopen when the VC Recommendation or its status standards change the boundaries among issuer, status information, presentation, and verifier that this example uses. |

### F.10:12 - Relations

**Builds on:** `F.17` for exact SchemeSenseCells and local-sense rows; `F.18` for designation NameCards; `F.9` for actual cross-local Bridge occurrences; `A.2.4` for first status-use positions; `C.2.1` for target-result and status-assertion epistemes; `A.15.1`/`A.6.1` for evaluation work and applications; and the exact subject pattern of every target/result used.

**Coordinates with:** `A.10`/`G.6` for provenance and bounded reliance; `G.11` for currentness; `B.3` for assurance-result claims; `C.28` for causal use; `E.17`/`E.24.PUB` and C.29 for publication/representation; and the direct standard, requirement, acceptance, gate, permission, commitment, release, and decision patterns for their own results and uses.

**Precision-restoration exit.** When wording such as *status role*, *approved role*, *validated means compliant*, *green means ready*, or a family arrow hides target, result, value, scheme, window, source, interpretation rule, or actual use, recover those exact objects here and apply the pattern that defines each neighboring claim. Do not repair the phrase by minting a generic status, evidence, or result relation.

### F.10:End

