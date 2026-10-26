## D.2 - Recognize Ethical Concerns Across Levels and Scopes (Multilevel Ethics)

> **Type:** D-family ethical entry pattern
> **Status:** Stable


**Use this when.** Use this pattern when an action or arrangement may benefit one affected entity while harming another across levels or scopes, or when responsibility is assigned across levels.

**Not this pattern when.** If only the value frame is missing, use `D.1`. If `D.3` has already described the conflict, use that result. If the conflict has to be mediated or used in a decision, use `D.4`. If the current concern is bias, fairness, impact audit, causal-fairness audit consumption, or ethical assurance, use `D.5`.

**What goes wrong if missed.** A local improvement is treated as ethically sufficient while another declared level, scope, or affected holon carries the harm.

**What this buys.** Identify who or what may bear a loss, explain how the affected scopes are related, and choose the question to examine next.

### D.2:1 - Problem Frame

Ethical trouble in system-holon work often appears because the current action is good for one level and bad for another. A person may benefit while a team is damaged. A project may benefit while a community pays the cost. A standard may improve coordination while excluding a minority case. A model may improve one metric while moving harm to a less visible scope.

Do not force these cases into a fixed ladder such as local, group, ecosystem, planetary. Declare the levels and scopes present in the situation and explain who or what may be affected.

### D.2:1.0 - Problem

A change can benefit one affected entity while imposing harm, exclusion or risk elsewhere, or change who is responsible for its consequences. The failure is to infer ethical sufficiency from the local gain without examining consequences for others. When responsibility matters, state its basis; a kind or assignment does not by itself establish that responsibility. Use `E.10.ROLE` to clarify role wording.

### D.2:1.1 - Forces

| Force | Tension |
| --- | --- |
| Local benefit vs. cross-level harm | A change can improve one declared scope while imposing cost, risk, or exclusion elsewhere. |
| Situation-defined levels vs. fixed ladders | Multilevel ethics needs declared levels and scopes from the case, not a universal moral hierarchy. |
| Affected entities and their descriptions | Identify the affected entity, whether a system or an episteme such as a standard, and explain whose use or interests make the change an ethical concern. |
| Early recognition vs. premature mediation | Use D.2 to make the conflict visible, D.3 to describe its sides and tension, and D.4 for mediation. |
| Ethical concern vs. architecture residual | Cross-scope residuals can be architectural, ethical, or both; choose the method for the question that needs answering. |

### D.2:2 - Solution

Name the local gain, who or what may bear a loss, and the levels or scopes that make this an ethical concern. State the next question to settle. Recognition is complete when those sides and the next use are clear; an already qualified `D.3` conflict or `D.4` decision question can be used directly.

Use `MultilevelEthicsEntry@Context` when the practitioner or a recipient needs to recover these connections for comparison or revision. Keep its content in the existing answer or working note when that suffices. Add evidence, value-frame editions, and supporting relations where the stated concern actually relies on them:

```text
MultilevelEthicsEntry@Context:
  ethicalConcernRef
  affectedEntityOfConcernRef
  valueFrameEditionRefs?
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  declaredLevelOrScopeRefs
  affectedHolonRefs
  affectedEpistemeRefs?
  roleWordRecoveryRefs?: E.10.ROLE results when role wording occurs
  localSystemRoleKindRefs?: FinSet(U.KindRef)
  systemRoleClassificationAssertionRefs?: FinSet(U.EpistemeRef)
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
  evidenceRefs?
  uncertaintyOrCurrentnessCondition?
  nextSubjectPatternLocator
```

The entry has one job: make the multilevel concern recognizable and choose its next use. It does not require a separate dossier or new inquiry before the concern can be discussed. A proposed inquiry goes through `C.11.DUA` when its receiving contribution or feasibility is unresolved; conflict description and decision use remain with `D.3` and `D.4`.

Material systems and epistemes can be affected EntitiesOfConcern. For an episteme such as a standard, state which uses and interests make its change ethically relevant.

### D.2:3 - Recognition Matrix

| Working situation | What to recover | Next pattern to apply |
| --- | --- | --- |
| A Method helps one team meet its target while increasing risk for another team or for users. | Affected holons, any independently current assignment, Method, actual Work when present, expected consequences, evidence, and each responsibility, commitment, permission, authority, or participation relation that the concern relies on. | `D.3` conflict description |
| A public policy helps a city-level goal while making one neighborhood or profession worse off. | Declared scopes, value concerns, responsibility claims, evidence, uncertainty. | `D.3` conflict description |
| A technical standard improves interoperability but excludes a minority device, language, publication form, or data source. | Standard or episteme whole, affected systems, publication and use relations, consequence horizon. | `D.3`, with `C.2.1` and `E.17` as needed |
| A model or metric looks fair at one aggregate level but hides subgroup harm. | Metric, affected groups, causal claim, evidence set, audit condition. | `D.5`, with `C.28` when causal fairness is claimed |
| An architecture move reduces residual at one holon level while creating cross-scope residual elsewhere. | Architecture structure, selected scopes, residual, affected value concerns. | `C.30.ILC`; use `D.3` if ethical conflict is live |

### D.2:4 - Boundaries

D.2 recognizes ethical concerns across levels and scopes. Use the corresponding subject method to judge a conflict, mediate it or conduct an audit.

`D.2` does not create `U.Level`, `U.Frustration`, `U.Emergence`, or a fixed moral scale. Levels and scopes are declared relations in the current situation. If a mathematical lens is needed for scale, frustration, optimization, Pareto comparison, or renormalization-like reasoning, use `C.29` and the applicable pattern for the current object.

### D.2:5 - Archetypal Grounding (Worked Slice)

A product team wants to reduce service cost by making a medical device harder to service outside authorized centers. At the first discussion, the team expects better manufacturer quality control and lower liability risk, while patients in regions without authorized service may lose timely access. Name those sides and their scopes, then return the next question: which service restriction, if any, addresses the particular hazard without imposing avoidable access harm? This is a useful `D.2` result. `D.3` can describe the tension in a short note from the available account.

Now suppose a release decision depends on whether a proposed servicing method can leave calibration outside the declared tolerance. A qualified test team can perform the discriminating check before the release window closes, and the release authority needs its result under the applicable rule. Preserve that focused investigation and the rule's actual force. Use `C.11.DUA` to compare the restriction's protective contribution with access harm, feasible alternatives, delay, and displaced work; a safety label settles none of those merits. `D.4` carries the resulting decision, including the authority needed to change a requirement or accept a residual. If the required basis cannot be obtained, the proposed release remains unsupported; a narrower continuation must meet its own conditions.

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
| CC-D2-2 | Affected holons, epistemes, Methods, actual Work, and consequences are named when current. Role wording is recovered through `E.10.ROLE`; a local kind and a C.2.1 System-classification assertion episteme remain separate. Every assignment recovers its directly declared species and obtaining occurrence. Participation or affected-party status, responsibility, commitment, permission, and authority each use their own direct relation or exact `missing-governor`. | Keeps the entry usable without making assignment imply participation or responsibility. |
| CC-D2-3 | The result identifies the next live question and `D.3`, `D.4`, `D.5`, `C.30.ILC`, or another subject pattern that answers it. The entry record is used only when its recoverable content contributes to that use. | Keeps D.2 as entry recognition, not conflict solver. |
| CC-D2-4 | Mathematical scale, threshold, optimization, or Pareto reasoning uses `C.29` or the direct measurement pattern. | Prevents math wording from becoming ethics ontology. |

### D.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| One-level ethics | The case is treated as good because one declared level improves. | Name every affected level or scope that changes the ethical claim. |
| Ladder import | A fixed level list is imported before the case is understood. | Recover the situation-defined scopes first. |
| Entry as solution | D.2 is used to decide the conflict. | Name the concern and select D.3, D.4, D.5, C.30.ILC, or another subject pattern for its next use. |
| Hidden episteme harm | A standard, model, policy, or architecture description is treated only as a document, not as an affected episteme with use consequences. | Separate the episteme, its publication relation, use relation, and affected systems or people. |

### D.2:7 - Consequences

Making cross-scope concerns explicit lets the practitioner choose the next useful question, such as an ethical conflict, an architectural consequence or a need for audit.

### D.2:9 - Rationale

A change can look technically local while shifting costs, risks or responsibilities across affected entities. Recovering those relations lets the practitioner formulate the ethical question before choosing mediation, an audit or an architectural response.

### D.2:10 - SoTA-Echoing

| Source line | Practical implication for this pattern |
| --- | --- |
| Multilevel selection and holonic systems thinking | Ethical effects often appear across nested, overlapping, or situation-defined scopes; the case must declare the levels or scopes it uses instead of importing a fixed moral ladder. |
| Applied ethics and responsibility practice | Trace responsibility and harm across the scopes where the action has consequences. |
| FPF holon and episteme ontology | Affected systems, collections, work occurrences, disciplines, and epistemes may be current; value-frame editions, ClaimScope, and qualification windows delimit the ethical claim, while descriptions and publication use remain separate from the affected in-life object. |
| Architecture residual discipline | A cross-scope residual can require architecture repair, a D.3 conflict description, or both; D.2 names the next pattern to apply instead of treating architecture shape as ethical proof or ethics as architecture by default. |

### D.2:11 - Relations

- Builds on `D.1` for ethical value frame boundary.
- Builds on `A.1`, `B.1`, and `C.13` for holon, level, scope, and part-whole grounding.
- Coordinates with `D.3` for the interlevel ethical conflict description and with `D.4` for mediation or decision use.
- Coordinates with `D.5` for bias, fairness, impact audit, causal-fairness audit consumption, and ethical assurance.
- Coordinates with `C.11.DUA` when a proposed inquiry or disputed protective requirement needs contribution, feasibility, and burden appraisal.
- Coordinates with `A.15`, `A.3.4`, `C.16`, `C.29`, and `C.30.ILC` when method, work, transformation, measurement, mathematical lens, or architecture residual claims are current.

### D.2:End
