## D.2 - Multilevel Ethics For Holon Work

> **Type:** D-family ethical entry pattern
> **Status:** Stable
> **Pattern role:** This compact MethodDescription helps a practitioner recognize multilevel ethical concern and identify the next exact subject assertion and predicate; it does not settle conflict or supply a fixed level ladder.

**Use this when.** Use this pattern when a system, holon, method, work plan, work occurrence, policy, recommendation, architecture move, or publication use may improve one declared level or scope while harming another, or when responsibility is assigned across levels.

**Not this pattern when.** If only the value frame is missing, use `D.1`. If the conflict structure is already current, use `D.3`. If the conflict has to be mediated or used in a decision, use `D.4`. If the current concern is bias, fairness, impact audit, causal-fairness audit consumption, or ethical assurance, use `D.5`.

**What goes wrong if missed.** A local improvement is treated as ethically sufficient while another declared level, scope, or affected holon carries the harm.

**What this buys.** The practitioner names the affected levels or scopes, the current value frame, and the next pattern to apply before mediation, assurance, bias audit, or architecture return.

### D.2:1 - Problem Frame

Ethical trouble in system-holon work often appears because the current action is good for one level and bad for another. A person may benefit while a team is damaged. A project may benefit while a community pays the cost. A standard may improve coordination while excluding a minority case. A model may improve one metric while moving harm to a less visible scope.

Do not force these cases into a fixed ladder such as local, group, ecosystem, planetary. Declare the levels and scopes present in the situation—for example, a person, team, organization, community, polity, economy, built asset, project, environment, episteme family, standard, publication, AI-enabled system, or another admitted holon or declared scope.

### D.2:1.0 - Problem

A change can be beneficial at one declared level or scope while imposing harm, exclusion, or risk elsewhere, or while changing a direct responsibility relation. The failure is to treat the local gain as ethically sufficient before the affected levels, scopes, holons, epistemes, Methods, actual Work, evidence, and next subject pattern are named. Recover role wording through `E.10.ROLE`; do not infer responsibility from a kind or assignment.

### D.2:1.1 - Forces

| Force | Tension |
| --- | --- |
| Local benefit vs. cross-level harm | A change can improve one declared scope while imposing cost, risk, or exclusion elsewhere. |
| Situation-defined levels vs. fixed ladders | Multilevel ethics needs declared levels and scopes from the case, not a universal moral hierarchy. |
| Holons in life vs. descriptions | The affected object may be a system, episteme, publication use, policy, or architecture move; the entry must not collapse these into one document concern. |
| Early recognition vs. premature mediation | Use D.2 to make the conflict visible, D.3 for its structure, and D.4 for mediation. |
| Ethical concern vs. architecture residual | Cross-scope residuals can be architectural, ethical, or both; the next pattern to apply must be named by value. |

### D.2:2 - Solution

Open a `MultilevelEthicsEntry@Context`:

```text
MultilevelEthicsEntry@Context:
  ethicalConcernRef
  affectedEntityOfConcernRef
  valueFrameEditionRefs
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  declaredLevelOrScopeRefs
  affectedHolonRefs
  affectedEpistemeRefs?
  roleWordRecoveryRefs?: E.10.ROLE results when role wording occurs
  localSystemRoleKindRefs?: FinSet(U.KindRef)
  systemRoleClassificationJudgmentRefs?: FinSet(U.RelationRef)
  systemRoleAssignmentRows?: FinSet({
    assignmentSpeciesRef: U.RelationKindRef constrained under U.SystemRoleAssignment
    assignmentOccurrenceRef: U.RelationRef constrained to an obtaining occurrence of assignmentSpeciesRef, with actual participants, holder, applicability, and extent recoverable
  })
  participationOrAffectedPartyRelationRefs?: exact direct relation refs
  participationOrAffectedPartyMissingGovernorRefs?: exact A.6.RCD results
  responsibilityRelationRefs?: exact direct relation refs
  responsibilityMissingGovernorRefs?: exact A.6.RCD results
  commitmentRelationRefs?: exact direct relation refs
  commitmentMissingGovernorRefs?: exact A.6.RCD results
  permissionRelationRefs?: exact direct relation refs
  permissionMissingGovernorRefs?: exact A.6.RCD results
  authorityRelationRefs?: exact direct relation refs
  authorityMissingGovernorRefs?: exact A.6.RCD results
  interestOrConcernRefs
  capabilityOrFunctioningConcernRefs?
  methodRefs?
  workRefs?
  transformationRefs?
  expectedConsequenceRefs
  evidenceRefs
  uncertaintyOrCurrentnessCondition
  nextSubjectPatternLocator
```

The entry record has one job: recognize that multilevel ethics is live and choose the next pattern to apply. It does not itself resolve the conflict.

For this pattern, holon work includes material systems and epistemes when they are the affected EntityOfConcern. An architectural description, standard, model card, policy publication, or research program may be the affected episteme; the pattern still asks which levels, scopes, affected holons, interests, responsibilities, and consequences are live.

### D.2:3 - Recognition Matrix

| Working situation | What to recover | Next pattern to apply |
| --- | --- | --- |
| A Method helps one team meet its target while increasing risk for another team or for users. | Affected holons, any independently current assignment, Method, actual Work when present, expected consequences, evidence, and each responsibility, commitment, permission, authority, or participation relation that the concern relies on. | `D.3` conflict structure |
| A public policy helps a city-level goal while making one neighborhood or profession worse off. | Declared scopes, value concerns, responsibility claims, evidence, uncertainty. | `D.3` conflict structure |
| A technical standard improves interoperability but excludes a minority device, language, publication form, or data source. | Standard or episteme whole, affected systems, publication and use relations, consequence horizon. | `D.3`, with `C.2.1` and `E.17` as needed |
| A model or metric looks fair at one aggregate level but hides subgroup harm. | Metric, affected groups, causal claim, evidence set, audit condition. | `D.5`, with `C.28` when causal fairness is claimed |
| An architecture move reduces residual at one holon level while creating cross-scope residual elsewhere. | Architecture structure, selected scopes, residual, affected value concerns. | `C.30.ILC`; use `D.3` if ethical conflict is live |

### D.2:4 - Boundaries

`D.2` is an entry pattern, not a general ethics doctrine and not a conflict solver. It keeps ethics from being omitted when levels and scopes of holons matter. It also keeps multilevel ethics from replacing architecture, assurance, causal, evidence, or publication patterns before the ethical EntityOfConcern is clear.

`D.2` does not create `U.Level`, `U.Frustration`, `U.Emergence`, or a fixed moral scale. Levels and scopes are declared relations in the current situation. If a mathematical lens is needed for scale, frustration, optimization, Pareto comparison, or renormalization-like reasoning, use `C.29` and the applicable pattern for the current object.

### D.2:5 - Archetypal Grounding (Worked Slice)

A product team wants to reduce service cost by making a medical device harder to service outside authorized centers. The move may improve manufacturer quality control and reduce liability risk, but harm patients in regions where authorized service is unavailable. `D.2` opens the entry: manufacturer, patients, service organizations, and device fleet are named as affected holons; the applicable regulatory and project value-frame editions delimit the claim; the regional and service scopes are explicit; value concerns include safety, access, responsibility, and maintainability; and the work plan and expected consequences are named. `D.3` then maps the conflict; `D.4` handles mediation or decision use.

### D.2:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Local optimum becomes ethical sufficiency | A benefit at one level is treated as enough while another scope carries harm. | Declare affected levels, scopes, holons, value concerns, and next subject pattern. |
| Fixed ladder bias | A generic hierarchy such as individual, team, and society replaces the levels present in the case. | Derive levels and scopes from the affected EntityOfConcern, named holons and Work, value frames, and responsibility relations that are current. |
| System-only bias | Multilevel ethics is limited to material systems and misses epistemes, standards, publications, or descriptions. | Treat affected systems and epistemes as admitted holons when the case makes them current. |
| Architecture absorbs ethics | A cross-scope residual is treated only as architecture because it has a structural shape. | Use `C.30.ILC` for architecture residual and `D.3` and `D.4` when value, harm, responsibility, or admissible sacrifice is live. |

### D.2:6 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-D2-1 | Declared levels or scopes come from the situation and are named by value. | Prevents fixed moral ladders and false `U.Level`. |
| CC-D2-2 | Affected holons, epistemes, Methods, actual Work, and consequences are named when current. Role wording is recovered through `E.10.ROLE`; a local kind and a System-classification judgment remain separate. Every assignment recovers its directly declared species and obtaining occurrence. Participation or affected-party status, responsibility, commitment, permission, and authority each use their own direct relation or exact `missing-governor`. | Keeps the entry usable without making assignment imply participation or responsibility. |
| CC-D2-3 | `nextSubjectPatternLocator` is `D.3`, `D.5`, `C.30.ILC`, or another subject pattern named by value. | Keeps D.2 as entry recognition, not conflict solver. |
| CC-D2-4 | Mathematical scale, threshold, optimization, or Pareto reasoning uses `C.29` or the direct measurement pattern. | Prevents math wording from becoming ethics ontology. |

### D.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| One-level ethics | The case is treated as good because one declared level improves. | Name every affected level or scope that changes the ethical claim. |
| Ladder import | A fixed level list is imported before the case is understood. | Recover the situation-defined scopes first. |
| Entry as solution | D.2 is used to decide the conflict. | Use D.2 only to open the entry and select D.3, D.4, D.5, C.30.ILC, or another subject pattern. |
| Hidden episteme harm | A standard, model, policy, or architecture description is treated only as a document, not as an affected episteme with use consequences. | Separate the episteme, its publication relation, use relation, and affected systems or people. |

### D.2:7 - Consequences

This pattern makes ethical level structure visible early. It prevents two opposite errors: treating ethics as a late bias audit only, and treating every interlevel residual as architecture without first asking whether value, harm, responsibility, or admissible sacrifice is being claimed.

### D.2:9 - Rationale

`D.2` makes multilevel ethical concern visible before the work jumps to conflict mediation, bias audit, assurance, or architecture. This matters because many cases look technically local but ethically cross-level: a method, standard, architecture move, publication, or work plan can improve one scope while pushing cost, risk, exclusion, or responsibility elsewhere.

The pattern deliberately avoids a fixed ladder. It asks for declared levels and scopes from the situation, then selects the next pattern to apply. That keeps FPF holon-aware without making every cross-scope case an architecture residual or every ethical case a bias audit.

### D.2:10 - SoTA-Echoing

| Source line | Practical implication for this pattern |
| --- | --- |
| Multilevel selection and holonic systems thinking | Ethical effects often appear across nested, overlapping, or situation-defined scopes; the case must declare the levels or scopes it uses instead of importing a fixed moral ladder. |
| Applied ethics and responsibility practice | Responsibility and harm cannot be assigned only at the most local level when a method, work plan, policy, standard, architecture move, or recommendation moves consequences across scopes. |
| FPF holon and episteme ontology | Affected systems, collections, work occurrences, disciplines, and epistemes may be current; value-frame editions, ClaimScope, and qualification windows delimit the ethical claim, while descriptions and publication use remain separate from the affected in-life object. |
| Architecture residual discipline | A cross-scope residual can require architecture repair, ethical conflict structure, or both; D.2 names the next pattern to apply instead of treating architecture shape as ethical proof or ethics as architecture by default. |

### D.2:11 - Relations

- Builds on `D.1` for ethical value frame boundary.
- Builds on `A.1`, `B.1`, and `C.13` for holon, level, scope, and part-whole grounding.
- Coordinates with `D.3` for interlevel ethical conflict structure and with `D.4` for mediation or decision use.
- Coordinates with `D.5` for bias, fairness, impact audit, causal-fairness audit consumption, and ethical assurance.
- Coordinates with `A.15`, `A.3.4`, `C.16`, `C.29`, and `C.30.ILC` when method, work, transformation, measurement, mathematical lens, or architecture residual claims are current.

### D.2:End

