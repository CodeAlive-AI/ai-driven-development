## D.5 - Bias Audit and Ethical Assurance

> **Type:** D-family bias-audit and ethical-assurance boundary pattern
> **Status:** Stable
> **Pattern role:** This compact pattern owns bias, fairness, impact-audit, causal-fairness audit consumption, and ethical-assurance boundary use; it does not replace D.1 through D.4.

**Use this when.** Use this pattern when a model, metric, policy, publication, decision system, recommendation, method, work plan, system, holon, or FPF claim may create bias, unfairness, human or group impact, causal-fairness overclaim, or ethical assurance risk.

**Not this pattern when.** If the ethical value frame is missing, use `D.1`. If the current question is multilevel ethics entry, use `D.2`. If the current question is to describe the sides and tension of an interlevel ethical conflict, use `D.3`. If the current question is mediation or decision use of that conflict, use `D.4`. If the current question is only evidence, causality, assurance, measurement, or architecture residual without bias, fairness, human or group impact, or ethical assurance, use the direct owner.

**What goes wrong if missed.** A model, metric, policy, publication, or decision system passes ordinary evidence or assurance checks while representation, proxy, visibility, metric, language, or human-impact bias remains hidden.

**What this buys.** Bias, fairness, human-impact, causal-fairness, and ethical-assurance concerns become auditable without replacing `D.1` through `D.4`, evidence, causal, measurement, or architecture owners.

### D.5:1 - Problem Frame

Bias and fairness failures often survive ordinary verification. A metric may be accurate while hiding subgroup harm. A model may be predictive while reproducing past exclusion. A policy may look neutral while moving cost to people or groups who were not represented in the evidence. A publication may look technically clear while licensing a harmful use.

`D.5` keeps this audit and assurance question explicit. It does not replace multilevel ethics. It asks whether the current object and its intended use are ethically unsafe because of bias, unfairness, impact, causal fairness without the required C.28 evidence value, or assurance without the required assurance relation.

### D.5:1.0 - Problem

Bias, fairness, human-impact, causal-fairness, and ethical-assurance concerns can remain invisible after ordinary technical verification. The failure is to let the model, metric, policy, publication, method, work plan, system, or holon be treated as admissible for use while the audited EntityOfConcern, intended use, affected people or groups, evidence, mitigation, and residuals are not explicit.

### D.5:1.1 - Forces

| Force | Tension |
| --- | --- |
| Ordinary verification vs. subgroup harm | Evidence or accuracy can look strong while representation, proxy, metric, visibility, language, or impact bias remains current. |
| Bounded answer vs. stronger reliance | A current concern may need only a qualified answer; a release or assurance claim can need a fuller account of the basis, mitigations, and residuals it relies on. |
| Fairness wording vs. causal claim | Metric disparity, associative fairness, interventional fairness, and counterfactual fairness are different claims. |
| Assurance relation vs. ethical permission | Assurance can record examined evidence and residuals, but cannot turn unresolved bias or harm into moral authorization. |
| Audit frame vs. neighboring owners | D.5 must keep bias and ethical assurance visible without replacing evidence, causality, measurement, architecture, or D.1 through D.4. |

### D.5:2 - Solution

Identify the object, the bias or fairness concern, and the use the answer must support. Give the result warranted by the available basis, with the affected groups and limitations that change that use. A metric comparison can finish at its qualified measurement result; recognizing a value conflict returns to `D.3` or `D.4`.

An intended audit, fairness, or assurance conclusion must satisfy its own evidence conditions. A missing basis leaves that conclusion unsupported. Select further investigation and the record it needs for that particular claim or decision, using §3.1.

Use `BiasAuditAssuranceFrame@Context` to organize an audit whose recipient needs to inspect the connection among claims, evidence, constraints, and residuals. The applicable content may already be present in the result being used:

```text
BiasAuditAssuranceFrame@Context:
  auditedEntityOfConcernRef
  intendedUseRef
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  affectedPopulationRefs?
  affectedSystemRefs?
  affectedHolonRefs?
  metricOrModelRefs?
  policyOrPublicationRefs?
  biasConcernRefs
  ethicalClaimRefs?
  fairnessClaimRef?
  impactClaimRef?
  causalFairnessUseRef?
  causalUseSupportResultRef?: CausalUseSupportResultRef
  evidenceRefs?
  assuranceClaimRefs?
  assuranceUseRef?
  mitigationOrConstraintRefs?
  acceptedResidualRefs?
  admissibleUse
  inadmissibleOverread?
  strongerSourceReturnCondition?
```

The frame organizes the audit account. It is neither the object being audited nor evidence that its use is fair. Include relied-on evidence and any stronger-source return needed by the particular conclusion.

### D.5:3 - Bias and Fairness Recognition

| Current claim | What D.5 requires | Neighboring owner |
| --- | --- | --- |
| "This metric shows the system is fair." | Distinguish metric disparity, proxy choice, subgroup impact, and intended use. | `C.16` for metric construction |
| "This intervention makes outcomes fair." | Declare the causal fairness use, C.28 support components and causal-use support result. | `C.28` |
| "The model is unbiased." | Name represented and missing groups, data-generation limits, model-use limits, and evidence. | `A.10`, `C.16`, `D.5` |
| "The release is ethically assured." | Separate audit findings, mitigations, accepted residuals, and the assurance or evidence relation. | `B.3`, `D.5` |
| "The policy is acceptable because it helps the whole." | Check whether a multilevel conflict is live. | `D.2`, `D.3`, `D.4` |

#### D.5:3.1 - Optional Audit Records And Depth

D.5 may use a compact `BiasRegister@Context` when the live need is to keep concerns visible during ordinary work:

```text
BiasRegister@Context:
  auditedEntityOfConcernRef
  intendedUseRef
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  affectedPopulationRefs?
  affectedSystemRefs?
  biasConcernCode
  evidenceRefs
  mitigationOrConstraintRef?
  acceptedResidualRef?
  nextReviewTrigger?
```

Choose depth from the claim and consequence that the recipient needs to judge. A bounded finding, corrected metric statement, or identified conflict can complete the present use, including when it concerns an affected group or appears in a publication. Retain the limitation that prevents that result from being read as a wider fairness or assurance claim.

Use a fuller `BiasAuditReport@Context` when the receiving decision needs to inspect the combined evidence, mitigations, and residuals behind an audit or assurance conclusion. A consequential or reusable causal-fairness audit retains this report and the C.28 support it consumes. A release that relies on a particular protective claim needs the evidence and audit account required to support that claim. Reuse a matching existing account; after a material change, reopen the claims whose basis or use changed. The report is a Description episteme or publication-use object, with scope and depth set by that reliance.

A concrete indication of harm, a missing basis for an intended claim, or an applicable assurance requirement can make further investigation necessary before that use. Name what its result could change, who can obtain it, and whether its contribution warrants its full cost and delay; use `C.11.DUA` when this appraisal is unresolved. If the needed basis remains unavailable, state which intended claim remains unsupported and give any feasible narrower use, mitigation, or stop with its conditions. Neither a short record nor a large report supplies missing evidence.

Exposure, repetition, automation, publication, and changed populations are cues to examine the actual use and consequence. They do not by themselves prescribe a full audit or a separate explanation for omitting one. When a protective or documentation requirement is disputed, use `C.11.DUA` to examine its hazard, threshold basis, protective contribution, feasibility, and distributed burden, while keeping its current force and amendment authority explicit.

#### D.5:3.2 - Compact Bias Concern Taxonomy

| Code | Concern | Typical question |
| --- | --- | --- |
| REP | Representation, coverage, sampling, proxy choice, missing group, or shifted population. | Who or what is missing, over-weighted, proxied, or moved out of scope? |
| ALG | Algorithmic, modeling, objective, ranking, optimization, or threshold behavior. | Which model or optimization choice changes outcomes for whom? |
| VIS | Visibility, interface, dashboard, presentation, or publication framing. | What becomes easy to see, hard to see, or too authoritative by display? |
| MET | Metric, measurement, scale, comparator, normalization, or threshold. | What does the metric count, hide, compare, or turn into a pass or fail claim? |
| LNG | Language, naming, category, definition, group label, or claim wording. | Which words change what can be asserted, counted, blamed, or done? |

The codes are only concern locators. They do not replace the governed object, affected people or groups, intended use, evidence, mitigation, or accepted residual.

### D.5:4 - Causal Fairness Boundary

A fairness claim may be associative, interventional, or counterfactual. C.28 supplies the causal-use question, rung, estimand, separate support components, common-threat result, and `CausalUseSupportResultRef`. D.5 keeps the bias/fairness audit and its conclusion.

When counterfactual fairness is consequential, reusable, published, or used for assurance, the cited C.28 components expose the additional counterfactual-identifiability assumptions required for that question. If the audit relies on an estimated fairness result, they also expose the estimate and its estimation-consistency result. Missing identification or consistency lowers the C.28 result to `bounded` or `unsupported`; more of the same data does not repair either gap.

Cite the C.28 result from the existing `BiasAuditReport@Context`. Do not open a separate C.28 fairness card; D.5 defines no such output. Metric-only fallback remains cheaper: when only metric disparity is claimed, record the metric or evaluation result and stop. An interventional proxy may support a bounded interventional fairness statement, but it does not establish counterfactual fairness without the required estimand and support components.

The C.28 result is one evidence basis. It does not certify fairness, approve a release, or supply ethical assurance; D.5 and any downstream decision or assurance pattern make those separate conclusions.

### D.5:5 - Ethical Assurance Boundary

Ethical assurance is not a stamp of moral permission. It is an assurance claim that bias, fairness, impact, and accepted residuals have been examined for the current use.

Use `B.3` for the assurance relation. Use `A.10` for evidence provenance and source currentness. Use `D.3` to describe an interlevel ethical conflict and `D.4` to mediate or use it in a decision. Use `C.30.ILC` when the issue is an architecture residual rather than a bias or fairness audit.

### D.5:6 - Archetypal Grounding (Worked Slice)

A hiring-screening model has high aggregate accuracy and an internal note says it is "fair." D.5 first asks what fairness claim is being made. If the claim is only a metric disparity comparison, give the metric or evaluation result with its affected groups, intended use, and material limits, then stop. A recipient can reuse or publish that bounded comparison without treating it as a conclusion that hiring is fair. An intended stronger conclusion reopens its actual missing basis. If the team claims counterfactual fairness, C.28 must expose the causal estimand, additional counterfactual-identifiability assumptions, and an estimate with its consistency result when that estimate is relied on. Missing conditions lower the C.28 support result before D.5 decides its audit use. If the audit exposes a conflict between company efficiency and applicant harm across declared scopes, D.3 describes that conflict and D.4 guides its decision use.

### D.5:6.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Audit as document ritual | A register or report exists but does not change intended use, residuals, or constraints. | Tie each concern to audited EntityOfConcern, intended use, evidence, mitigation, and accepted residual. |
| Metric fairness overclaim | A metric comparison is published as causal or counterfactual fairness. | Recover the fairness claim kind. For counterfactual fairness, require C.28 identification assumptions and estimation consistency when an estimate is used before D.5 consumes the support result. |
| Assurance as authorization | Ethical assurance is treated as permission to proceed. | Record assurance as assurance or evidence relation and keep `D.4` and `D.5` use separate. |
| Bias category replaces object | REP, ALG, VIS, MET, or LNG code is treated as the governed object. | Use codes only as concern locators; keep audited EntityOfConcern and intended use explicit. |

### D.5:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-D5-1 | The result names the audited EntityOfConcern, intended use, affected populations or Systems, and the bias, fairness, impact, or ethical concern being answered. Relied-on evidence and material limitations qualify its warranted use. Assurance use, repair return, ClaimScope, and qualification window are explicit when they delimit the audit; record and investigation depth follow the particular reliance in §3.1. | Keeps audit scope inspectable. |
| CC-D5-2 | Metric, causal fairness, evidence, assurance, publication, and architecture-residual claims use their direct owners. | Prevents D.5 from swallowing neighboring patterns. |
| CC-D5-3 | Ethical assurance is recorded as assurance or evidence relation, not moral permission. | Keeps assurance from becoming ethical authorization. |
| CC-D5-4 | If the audit exposes interlevel conflict, use D.3 for the conflict description and D.4 for mediation or decision use. | Keeps D.5 connected to the D cluster without replacing it. |

### D.5:3.3 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Ethics ghetto | Bias or fairness is left in a separate ethics note while the model, metric, release, publication, or work plan keeps operating unchanged. | Put the concern on the audited EntityOfConcern and its intended use, then name the mitigation, constraint, or accepted residual. |
| Checklist charade | A checklist is completed without answering the concern about affected people, evidence, use, or residuals. | Return the bounded finding or judgement; use a register or report when its content is needed for tracking or reliance. |
| Bias whack-a-mole | One disparity is patched while proxy, representation, metric, visibility, or language concerns move elsewhere. | Keep REP, ALG, VIS, MET, and LNG concerns visible until the admissible use and accepted residual are explicit. |

### D.5:8 - Consequences

This pattern keeps bias, fairness, impact, causal-fairness audit consumption, and ethical assurance from being scattered across technical patterns. It also prevents D.5 from swallowing all ethics. The cost is that teams must say which bias or fairness claim they are making. The gain is that ethical assurance becomes a typed assurance or evidence claim rather than a comforting label.

### D.5:9 - Rationale

`D.5` exists because bias, fairness, human-impact, causal-fairness audit consumption, and ethical assurance often survive ordinary technical checks. It keeps those concerns in one audit frame while preserving direct owners: metrics and measurement remain with measurement patterns, causal fairness remains with causal-use patterns, assurance remains an assurance relation, and multilevel ethical conflict remains with D.2 through D.4.

Audit depth follows what a particular claim or decision needs from the result. A compact account can carry a useful finding; a stronger audit or assurance conclusion needs its supporting evidence and the record required for that reliance. Material changes reopen the affected basis, and a disputed requirement remains open to substantive appraisal without losing its present force.

### D.5:10 - SoTA-Echoing

| Source line | Practical implication for this pattern |
| --- | --- |
| Fairness and bias audit practice | Representation, proxy, metric, visibility, language, and impact concerns must be tied to intended use, affected groups, source-currentness, and accepted residuals. |
| Causal fairness and causal inference | Associative, interventional, and counterfactual fairness claims need different evidence values and cannot be interchanged by wording. |
| Assurance and governance practice | An assurance record can support bounded reliance, but does not grant moral permission under unresolved residual harm or replace D.3 and D.4 when interlevel conflict is exposed. |
| FPF episteme and publication discipline | Bias registers and reports are descriptions or publication-use objects; they do not make the audited object fair by existing. |

### D.5:11 - Relations

- Builds on `D.1` and coordinates with `D.2`, `D.3`, and `D.4` for value frame, multilevel entry, conflict description, and mediation or decision use.
- Coordinates with `A.10` for evidence and source currentness.
- Coordinates with `C.11.DUA` for the contribution and feasibility of further inquiry and the merits and current force of disputed audit or protective requirements.
- Coordinates with `B.3` for assurance relation and reliance.
- Coordinates with `C.16` for metric and measurement construction.
- Coordinates with `C.28` for causal fairness, including counterfactual-identification assumptions, estimation consistency when an estimate is used, and the bounded causal-use support result.
- Coordinates with `E.17` when publication or publication-use relation changes admissible use.

### D.5:End
