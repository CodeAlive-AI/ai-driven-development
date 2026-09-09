## C.31.ASAP - Architecture Scale-Amenability Preference

> **Type:** Characterization pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.31.ASAP:1 - Problem frame

Use this pattern when a practitioner compares architecture alternatives under a declared scale variable or scale window and needs to avoid treating a modularity label, platform label, product-line label, reusable-structure share, or coarse-graining metaphor as an automatic scale-preference claim.

The first useful move is `ScaleClaimTriage`:

```text
ScaleClaimTriage:
  architectureAlternativeSetRef:
  describedHolonRef:
  claimScopeRef:
  selectedContextSliceRefs:
  modelUseStructureRef?:
  scaleVariableRef:
  scaleWindowRef:
  claimedPreferenceUnderScale:
  slopeEvidenceRef, scaleProbeEvidenceRef, or noProbeReason:
  expectedStableOrImprovingStructure:
  exceptionGrowthRisk:
  sourceReturnCondition:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

Ordinary use starts by naming the alternatives and described holon, the exact `U.ClaimScope` and relevant A.2.6 `U.ContextSlice` membership, the scale variable and scale window, the claimed preference under scale, the available slope or scale-probe evidence or no-probe reason, the expected stable or improving structure, and the exception-growth risk. Name `modelUseStructureRef` only when one independently selected `BoundedModelUseStructure` changes this receiving interpretation; it never replaces the claim scope. Use `ArchitectureScaleAuditRecord@Project` only when the scale preference is being used to affect a comparison, selected set, publication, assurance input, or architecture decision.

What goes wrong if C.31.ASAP is missed: "modular", "platform", "product line", "reusable", "general", "open", "coarse-grained", or "RG-like" becomes a shortcut for a scale-preference claim; a locally hand-engineered solution is called debt even when safety, law-domain, or mission constraints justify it; exception growth is hidden until the architecture is already expensive to change; and coarse descriptions keep losing lower-scope safety or semantic distinctions without a source-return condition.

What C.31.ASAP buys in practice: the practitioner can say what is being scaled, where the scale claim holds, what structure is expected to remain stable or improve, what exceptions are allowed, what evidence or no-probe reason exists, which scale-preference claim stays in C.31.ASAP, and which pattern defines or tests any lens-use, evidence, assurance, selection, or decision claim being made.

Not this pattern when the question under repair is only module-interface relation repair, modularity-characteristic selection, reusable-structure accounting, mathematical-lens use, scale-law adequacy, method preference under general BLP, candidate architecture generation, selected-set return, or final local choice. Use `A.6.M`, `C.31`, `C.31.RSA`, `C.29`, `C.18.1`, `C.19.1`, `C.32`, `G.5`, or `C.11` as appropriate. C.31.ASAP governs architecture scale-preference claims; it does not select the architecture, prove the scale law, or certify the project.

### C.31.ASAP:2 - Problem

Architecture work often asks whether one structure will scale better than another: a product-line architecture rather than bespoke variants, an open interface rather than a closed integration, a stable flow topology rather than repeated project exceptions, or a reusable evidence package rather than repeated assurance work.

These claims are useful only after the scale relation is declared. "Scales better" can mean fewer interface grammar variants, lower exception growth, better learning transfer, more reusable templates, more stable control relations, less source-return cost, fewer regulatory exceptions, or more freedom of action. Those are not the same claim.

C.31.ASAP turns architecture scale-preference talk into a declared scale variable or window, a preference claim, evidence or no-probe reason, expected stable or improving structure, exception-growth risk, and source-return condition. It does not turn scale preference into proof, selection, assurance, causal use, or a universal law.

### C.31.ASAP:3 - Forces

| Force | Tension |
| --- | --- |
| Fast architecture choice vs scale evidence | Practitioners often need a scale-aware preference before a full scale study exists. |
| Reusable structure vs useful exception | Reuse can improve scale behavior, but some bespoke residue is justified by safety, law-domain, mission, or context constraints. |
| Platform label vs scale mechanism | A platform or product-line name does not say which variability slots, extension rules, exception curve, or refactor trigger makes scale behavior better. |
| Coarse view vs source distinctions | Coarse-grained architecture descriptions can expose stable structure, but they can also hide lower-scope hazards. |
| Preference guidance vs selection authority | A scale preference can inform a candidate set or decision, but selection and choice remain with their governing patterns. |
| Architecture scope vs method BLP | Architecture scale amenability resembles BLP, but C.31.ASAP governs architecture alternatives and selected structures, not general method-family policy. |

### C.31.ASAP:4 - Solution

C.31.ASAP specializes scale-amenability preference for architecture alternatives. It applies when an architecture alternative set, scale variable or scale window, and claimed preference under scale are named.

#### C.31.ASAP:4.1 - Applicability fields

C.31.ASAP applies only when all of the following are present:

1. a declared architecture alternative set, described holon, exact `U.ClaimScope`, and relevant A.2.6 `U.ContextSlice` membership;
2. a declared scale variable or scale window;
3. a claimed preference under scale;
4. slope evidence, scale-probe evidence, or a no-probe reason;
5. an expected stable or improving structure, exception-growth risk, or source-return condition that changes the next architecture move.

If those fields are absent, keep the claim in `C.31` as a temporal or scale-sensitive characteristic cue, in `C.31.RSA` as report-only accounting, in `C.29` as a bounded lens-use output, or in ordinary architecture prose.

#### C.31.ASAP:4.2 - `ScaleClaimTriage`

Use `ScaleClaimTriage` before any heavier scale audit:

```text
ScaleClaimTriage:
  architectureAlternativeSetRef:
  describedHolonRef:
  claimScopeRef:
  selectedContextSliceRefs:
  modelUseStructureRef?:
  architectureClaimRef?:
  scaleVariableRef:
  scaleWindowRef:
  claimedPreferenceUnderScale:
  slopeEvidenceRef?:
  scaleProbeEvidenceRef?:
  noProbeReason?:
  expectedStableOrImprovingStructure:
  exceptionGrowthRisk:
  sourceReturnCondition:
  admissibleUse:
  nonAdmissibleUse?:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

The triage is complete enough when it states the next admissible architecture move and the stop or return condition. Include `nonAdmissibleUse?` only when it passes F.19's plausible-reader test; `groundedScaleShortcut?` is an alias for that same optional value. It may stop at local guidance when no comparison, publication, assurance, selected-set, or decision use is being made.

`claimScopeRef` designates one exact `U.ClaimScope`; `selectedContextSliceRefs` records the A.2.6 membership relevant to this use. A scale window is the range of the scale variable for which the preference is claimed, not a substitute for either scope object. `modelUseStructureRef` is optional and is filled only when an independently selected A.1.1 `BoundedModelUseStructure` changes the interpretation of this exact preference use.

#### C.31.ASAP:4.3 - Architecture scale-preference rule

When architecture alternatives satisfy the same safety boundary, law-domain boundary, and assurance boundary, prefer the alternative whose reusable functional-structure, flow-structure, control-structure, module-interface, work-template, and evidence-package structure and learning-transfer slopes remain stable or improve over the declared scale window, unless an `ArchitectureScaleAuditRecord@Project` records a bounded exception.

C.31.ASAP defines the scale-preference claim and its boundary. Use `G.9` for a parity claim and `A.21` for a gate claim; the candidate, comparison, set-declaration, and choice uses are distinguished below.

A scale-preference claim may inform `C.32` candidate generation or supply one input to an `A.19.CPM` comparison by naming the scale variable, scale window, expected stable or improving structure, exception-growth risk, and source-return condition for candidate alternatives. Use `C.32` to construct the candidate architecture palette, `A.19.CPM` to compare alternatives, `G.5` to declare a selected-set result, `C.11` to make a final local choice, and `C.32.PAD` to record a project architecture decision. When audience availability is current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. Apply the relevant evidence, assurance, gate, or release definition and test only when that claim is current.

When the same scale-sensitive pressure must also become a project criterion, `C.32.ACS` creates a separate row for the exact characteristic or Q-Bundle slot, bearer, scale form, and use class. That row may supply declared input to an ASAP preference. Use C.31.ASAP to state which alternative is preferable under the scale window; use C.32.ACS to admit and classify the criterion row as an optimization indicator, guardrail, or context-only row. Keep the preference record and criterion row separately referenced.

#### C.31.ASAP:4.4 - Scale variables

Typical architecture scale variables include:

| Scale variable | Reading |
| --- | --- |
| `N_units` | repeated units or instances |
| `N_scopeCount` | aggregation scopes, coarse-graining scopes, or typed LCA control scopes |
| `N_sites` | deployments, sites, markets, or jurisdictions |
| `N_interfaceTypes` | distinct interface grammar variants |
| `N_requiredTransformationKinds` | distinct transformation kinds in the selected functional-structure view |
| `N_flowRelationKinds` | flow-relation or crossing variants in the selected flow-structure view |
| `N_moduleTypes` | module type library size |
| `N_workRepetitions` | delivery, operation, or test repetitions |
| `N_supplierOrVendorClasses` | substitutability or vendor class dimension |
| `N_regulatoryInstances` | approval, safety, or certification repeats |
| `freedomOfAction` | allowed design, search, or control variation |

The scale variable is not enough by name. The claim being made also needs a scale window, expected stable or improving structure, exception-growth risk, and source-return condition.

#### C.31.ASAP:4.5 - Scale audit outputs

Use the heavier audit only when the scale preference changes comparison, publication, selected-set, assurance-input, or decision use:

```text
ArchitectureScaleAuditRecord@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureScaleAuditProjectUseRelationRef?: U.RelationRef governed by the exact audit-use or work-use pattern
  architectureAlternativeSetRef:
  claimScopeRef:
  selectedContextSliceRefs:
  modelUseStructureRef?:
  scaleVariableRefs:
  scaleWindowRef:
  ArchitectureSlopeVector:
  IsoScaleParityNote?:
  ASAPWaiverReason?:
  ArchitectureHeuristicDebt?:
  BespokeResidueRegisterRef?:
  SourceReturnCondition:
  admissibleUse:
  nonAdmissibleUse?:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

For `ArchitectureScaleAuditRecord@Project` and `BespokeResidueRegister@Project`, `@Project` is a compatibility and retrieval cue. An audit local to one actual project names both the exact composite `U.Work` in `projectWorkOccurrenceRef` and the obtaining direct audit-use relation in `architectureScaleAuditProjectUseRelationRef`. `BespokeResidueRegisterRef` may cite the register episteme. Assert that register's project locality only after a separate direct register-to-work relation is governed, and cite that exact occurrence; the audit-use relation remains about the audit. Otherwise retain only retrieval use and make no audit or residue-register project-locality claim.

| Output | Meaning |
| --- | --- |
| `ArchitectureSlopeVector` | Slopes for reusable structure, interface variation, flow stability, control stability, work repeatability, bespoke residue, exception growth, and learning transfer. |
| `IsoScaleParityNote` | Comparison under equalized scale budgets where possible; if parity is not possible, the loss is named. |
| `ASAPWaiverReason` | Declared reason for not choosing the scale-amenable alternative. |
| `ArchitectureHeuristicDebt` | Report-only note for knowingly accepting a locally hand-engineered solution with less scale-amenable slope profile under the declared scale window. |
| `BespokeResidueRegister@Project` | Pattern-local exception inventory with expiry or refactor triggers. |
| `ScaleWindow` | Declared range where the preference claim holds. |
| `SourceReturnCondition` | Condition for returning from a compressed, coarse, extracted, indexed, or accounting representation to source-side structural evidence, source records, or a related source or evidence record with higher declared validation boundary. |

`ArchitectureScaleAuditRecord@Project` records the triage of an architecture scale-preference claim. An assurance proof, gate record, selected-set result declaration, publication occurrence, local decision, or work plan remains a separate result under its own pattern; use A.15.2 for the work plan.

#### C.31.ASAP:4.6 - Waiver discipline

```text
ASAPWaiverReason:
  deontic constraint
  safety or law-domain boundary
  scale-probe overturn
  assurance infeasibility
  context-specific bounded exception
```

A deontic constraint, safety boundary, law-domain boundary, mission constraint, assurance infeasibility, or scale-probe overturn can justify a bounded exception without creating `ArchitectureHeuristicDebt`.

`ArchitectureHeuristicDebt` remains report-only unless tied to a decision, risk, work, evidence, assurance, or selected-set record through its governing pattern.

#### C.31.ASAP:4.7 - Scale-refactoring moves

Before scale-preference guidance becomes action-guiding, name at least one possible repair or stop:

| Scale symptom | Possible architecture move | Boundary |
| --- | --- | --- |
| interface variants grow without payoff | reduce interface alphabet or introduce interface grammar | A.6.M governs interface relation repair. |
| product-line or platform variants lack explicit variation points | introduce variability slots or extension rules | Platform label alone is not scale-preference evidence. |
| one aggregation scope hides lower-scope hazards | split the declared aggregation scope or architecture boundary | C.29 supplies lens-use fields only when coarse-graining is mathematical-lens use. |
| repeated work contains reusable structure | reuse a method template for subsequent work | Use `A.3.1` for a Method claim, `A.15` for Method–Work alignment, and `A.15.1` for actual Work. Use `A.15.4` only while appearance hides a work-relevant prerequisite. |
| regulatory or safety residue remains local and repeated | isolate regulatory residue or safety-specific exception register | Use `A.10` for source recovery and bounded reliance, `G.6` for addressable provenance, `B.3` when a named assurance claim is current, and `A.21` for a gate claim. |
| coarse representation loses safety, semantic, or source distinctions | return to lower-scope source-side evidence or narrow the scale window | Source-return condition is mandatory. |

#### C.31.ASAP:4.8 - C.29 lens relation

When a scale preference depends on an RG, coarse-graining, epiplexity, graph, multilevel-learning, or frustration lens, use `C.29` for the mathematical-lens recovery and keep the architecture scale-preference claim in C.31.ASAP. Use C.18.1 for any scale-law claim.

For architecture use, the C.29 output should name `MLU.Description@RGArchitecture`, `MLU.Description@MultilevelLearningFrustration`, or another local MathLensUse output only when the lens changes the next admissible use. The C.31.ASAP side records the scale variable, scale window, slope or scale-probe evidence, exception-growth risk, and source-return condition. C.29 records candidate mathematical object, mapping mode, preserved structure, lost structure, visible payoff, declared use, stop condition, and any blocked overread justified through F.19.

### C.31.ASAP:5 - Archetypal Grounding

| Archetype | Without C.31.ASAP | With C.31.ASAP |
| --- | --- | --- |
| Product-line platform | Platform name is treated as scale-preference evidence. | Variability slots, extension rules, exception curve, and refactor triggers are declared before preference use. |
| Neural architecture block library | Reusing blocks is treated as reusable architecture by itself. | The alternative set names scale variable, interface grammar variants, exception growth, and source-return condition. |
| Safety or certification reuse | Reusable evidence package is counted without validation boundary. | Evidence reuse remains tied to source-return. An evidence-validity or safety claim is tested under its applicable domain rule. Use `A.10` for source recovery and bounded reliance, `G.6` for addressable provenance, and `B.3` when a named assurance claim is current. |
| Cross-scope residual | A frustration or complexity label is treated as scale mathematics. | C.31.ASAP names the scale window and residual slope; C.29 records the lens-use fields if the mathematical-lens use is being claimed. |

#### C.31.ASAP:5.1 - Filled triage slice

```text
ScaleClaimTriage:
  architectureAlternativeSetRef: product-line platform alternative vs bespoke customer-specific variants
  describedHolonRef: the regulated deployment platform and its site-specific variants
  claimScopeRef: preference claim for 5 to 40 named regulated deployment sites inside the current qualification boundary
  selectedContextSliceRefs: the named site, jurisdiction, and qualification-window slices admitted by that claim scope
  modelUseStructureRef?: absent; no independently selected bounded-model-use structure changes this use
  scaleVariableRef: N_sites
  scaleWindowRef: 5 to 40 regulated deployment sites inside the current qualification window
  claimedPreferenceUnderScale: platform alternative is preferred if interface variants and approval exceptions grow slower than bespoke variants
  slopeEvidenceRef, scaleProbeEvidenceRef, or noProbeReason: scale-probe evidence from six deployments; no universal scale law claimed
  expectedStableOrImprovingStructure: interface grammar, reusable test package, deployment work template
  exceptionGrowthRisk: jurisdiction-specific clauses and side-channel integrations may grow faster than sites
  sourceReturnCondition: return to exception register, interface variant log, and deployment evidence before publication, selected-set, assurance, or decision use
  relatedClaimGovernanceIfClaimed: C.31 for the characteristic; C.31.RSA for reusable-structure share; C.16 for measurement; A.19.CPM for comparison; G.5 for selected-set declaration; G.9 for parity; C.11 for local decision; A.10 for source recovery and bounded reliance; G.6 for addressable provenance; B.3 for a named assurance claim
  stopCondition: stop at local scale-preference guidance unless comparator admission, evidence validity, and decision or selected-set governance are present
```

Admissible move: prefer the platform alternative as a local scale-preference guide and start interface-grammar repair before deployment spread increases. Stop at local guidance; open the direct selected-set, evidence-sufficiency, assurance, gate, or decision pattern only when that downstream claim is current.

#### C.31.ASAP:5.2 - Near-miss lowering slice

Near-miss: a team says the platform architecture should win because it has an 82 percent reusable-structure share, an RG-like coarse description, and "less bespoke debt" than the local variant.

Lowering replay:

- The platform label is a source cue, not scale-preference evidence; recover variability slots, extension rules, exception curve, and source-return condition first.
- The 82 percent reusable-structure share stays report-only under C.31.RSA until the scale variable, scale window, accounting basis, comparator admission, and admissible comparison relation are declared.
- The RG-like phrase stays with C.29 unless the mathematical-lens fields, preserved structure, lost structure, payoff, admissible use, and stop condition are recoverable.
- The "bespoke debt" label is lowered to waiver review when safety, law-domain, mission, assurance, or scale-probe overturn reasons may justify the local variant.

Stop C.31.ASAP use when the scale window, probe evidence or no-probe reason, comparator admission, or source-return condition is absent. Reopen it only after those fields are recoverable and the platform-label, share, lens, and waiver claims have their governing patterns.

### C.31.ASAP:6 - Bias-Annotation

| Bias risk | C.31.ASAP correction |
| --- | --- |
| **Platform label bias** | Platform or product-line wording names a possible source context, not scale-preference evidence. Recover variability slots, extension rules, exception curve, refactor triggers, and source-return condition. |
| **Modularity-means-scalability bias** | A module count, interface count, or reusable-structure share is not a scale preference. Use C.31 and C.31.RSA first, then C.31.ASAP only when scale variable and scale window are named. |
| **Debt inflation bias** | A locally hand-engineered solution is called debt without checking deontic, safety, law-domain, mission, assurance, or scale-probe waiver reasons. |
| **RG proof bias** | RG, coarse-graining, fixed-point, or universality wording is treated as scale-preference proof. Use C.29 for lens recovery and keep scale preference in C.31.ASAP. |
| **Selection laundering** | The scale-preference claim is used as if it selected the architecture. Use `G.5` for selected-set declaration and `C.11` for local choice; use `G.9` when parity is current. |

### C.31.ASAP:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| `CC-C31.ASAP-1` | A C.31.ASAP use being made names the architecture alternative set, described holon, exact `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership, scale variable or scale window, and claimed preference under scale. | Prevents generic "scales better" and generic-context wording. |
| `CC-C31.ASAP-2` | `ScaleClaimTriage` names slope evidence, scale-probe evidence, or a no-probe reason. | Prevents preference claims without declared evidence or no-probe reason. |
| `CC-C31.ASAP-3` | Expected stable or improving structure and exception-growth risk are stated. | Keeps the pattern about architecture structure rather than scale vocabulary. |
| `CC-C31.ASAP-4` | Source-return condition is present when any compressed, coarse, extracted, indexed, or accounting representation drops source-side distinctions. | Prevents unsafe coarse descriptions. |
| `CC-C31.ASAP-5` | Waiver reason is one of deontic constraint, safety or law-domain boundary, scale-probe overturn, assurance infeasibility, or context-specific bounded exception. | Prevents false debt labels. |
| `CC-C31.ASAP-6` | `ArchitectureHeuristicDebt` remains report-only unless a decision, risk, work, evidence, assurance, or selected-set record is being used under its governing pattern. | Prevents shadow project authority. |
| `CC-C31.ASAP-7` | Platform, product-line, modularity, reuse, open-interface, RG, and coarse-graining labels do not establish scale preference by themselves. | Blocks source-label overread. |
| `CC-C31.ASAP-8` | Mathematical-lens claims name C.29 output fields; C.31.ASAP governs only the architecture scale-preference side. | Keeps C.29 and C.31.ASAP distinct. |
| `CC-C31.ASAP-9` | Comparison, selected-set, local choice, evidence, assurance, gate, work, or release claims name the governing pattern. | Prevents scale preference from becoming selection or assurance. |
| `CC-C31.ASAP-10` | SoTA rows mutate at least one solution line, checklist item, boundary, relation, or worked slice. | Keeps source use non-decorative. |
| `CC-C31.ASAP-11` | Project-local audit use names both `projectWorkOccurrenceRef` and `architectureScaleAuditProjectUseRelationRef`; a residue register remains retrieval-only unless its own governed direct relation to the exact composite Work is cited. | Prevents an `@Project` suffix, work reference, or borrowed audit relation from fabricating locality. |
| `CC-C31.ASAP-12` | When an ACS criterion row and an ASAP preference are both current, each is separately referenced and neither substitutes for the other. | Keeps criterion admission and alternative preference distinct. |

### C.31.ASAP:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| `ModularThereforeScalable` | The text says modular or platform architecture scales without scale variable, window, slope evidence, or exception curve. | Add `ScaleClaimTriage` or downgrade to C.31 characteristic cue. |
| `GenericScaleAudit` | Audit fields appear with no architecture alternative set or preference use. | Return to `ScaleClaimTriage`; remove audit apparatus until preference use is being made. |
| `AllExceptionsAreDebt` | Any non-scale-amenable choice becomes debt. | Test waiver reasons and keep justified bounded exceptions out of `ArchitectureHeuristicDebt`. |
| `RGAsScaleProof` | Coarse-graining or RG wording is used as a scale-preference claim. | Apply C.29 for lens use and C.31.ASAP for preference claim; require source-return condition. |
| `ShareAsScalePreferenceEvidence` | `ReusableStructureShare` or `BespokeResidueShare` is used to prefer one alternative. | Keep the share report-only in C.31.RSA until scale variable, window, and admissible comparison are declared. |

### C.31.ASAP:9 - Consequences

| Positive consequence | Cost or trade-off |
| --- | --- |
| Scale preference becomes inspectable before selection or decision. | The practitioner must name a scale variable and window instead of relying on a label. |
| Platform and product-line claims gain usable refactor triggers. | Some source language becomes only a recognition cue until variability slots and exception curves are declared. |
| C.29 lens use stays useful without turning into scale proof. | RG claims and coarsening claims need preserved and lost structure plus source-return condition. |
| Report-only debt notes remain bounded. | Decisions or risk records must use their governing patterns when reliance use is being made. |

### C.31.ASAP:10 - Rationale

`C.31` and `C.31.RSA` can expose scale-sensitive characteristics and reusable-structure residue, but they should not themselves decide which architecture alternative is preferable under scale. C.31.ASAP governs this architecture scale-preference claim family; it is narrower than general BLP and broader than one measurement card.

The pattern adapts BLP-style scale-amenability to architecture: prefer the alternative that preserves or improves reusable structure over a declared scale window when safety, law-domain, and assurance boundaries are comparable. Treat modularity, reuse, platform practice, and mathematical coarse-graining as candidate cues. Base the preference on the named scale variable and window, expected stable or improving structure, exception-growth risk, and available slope or scale-probe evidence or no-probe reason.

### C.31.ASAP:11 - SoTA-Echoing

| Source family | Source-use relation | C.31.ASAP contribution | Practitioner use |
| --- | --- | --- | --- |
| Software product-line and variability-management practice (`https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`) | Mature variability lineage plus current SPLE-review cues. | Adopt variability slots, product-line reuse, exception inventory, and refactor triggers as architecture scale-preference fields. | Treat a product-line label, shared code base, feature model, or platform name as a cue. Before preferring the product-line alternative, name the scale window, variability slots, exception curve, and source-return condition. |
| Product-platform and modular product-architecture practice (`https://link.springer.com/article/10.1007/s00163-023-00427-1`; `https://arxiv.org/abs/2510.11089`) | Current engineering-design source line for modular product architecture, assembly orientation, product-family reuse, and manufacturing-aware modularity. | Adopt the product-family commonality and variety trade-off as an architecture scale-preference pressure: reusable structure needs declared variation points, interface rules, assembly or realization constraints, exception curve, and source-return condition. | Treat a product-platform name, common-module count, or modular-product label as a cue; establish any module-interface or manufacturing claim separately. Before preferring a product-platform alternative, state which product-family variation is scaled, which structure remains stable, and which assembly, safety, law-domain, or mission exception is allowed. |
| Platform-engineering maturity practice (`https://tag-app-delivery.cncf.io/fr/whitepapers/platform-eng-maturity-model/`) | Current platform-practice source for platform service set, extension-rule, substitution-policy, and maturity-pressure claims. | Adapt platform practice into extension-rule, substitution-policy, conformance-expectation, and exception-growth checks. | Treat platform maturity as a source cue until the architecture scale variable and exception behavior are declared. Establish any architecture selection or reusable-structure claim through its own pattern. |
| C.19.1 BLP in FPF | FPF-local preference discipline for general scale-amenable methods. | Specialize the preference idea to architecture alternatives, selected structures, scale variables, and architecture slope vector. | Use C.19.1 for method-family policy and C.31.ASAP for architecture scale preference; selector policy and decision records remain with their governing patterns. |
| C.29 RG and coarse-graining lens use in FPF | FPF-local mathematical-lens discipline. | Require scale window, coarse-graining rule, preserved structure, lost structure, and source-return condition when RG-like architecture scale reasoning is being claimed. | Use `MLU.Description@RGArchitecture` or `MLU.Description@MultilevelLearningFrustration` only when the lens changes the next admissible use. Establish any physical-RG, scale-proof, causal-proof, assurance, or selected-architecture claim through its own source basis and governing pattern. |

### C.31.ASAP:12 - Relations

- **Builds on:** `C.31`, `C.31.RSA`, `C.16`, `A.2.6`, `A.17`, `A.18`, `A.19`, `C.18.1`, `C.19.1`, and `C.29`; uses A.1.1 only when a selected `BoundedModelUseStructure` changes the receiving interpretation.
- **Coordinates with:** `A.6.M` for module-interface relation repair; `C.30`, `C.30.ASV`, `C.30.LCA`, and `C.30.ILC` for architecture and selected-structure questions; `C.33` and `C.34` when scale-amenability material needs captured-structure, lost-structure, preservation, or correspondence adequacy before candidate use; `C.35` for the generated or discovered result's kind and adequacy for candidate use; `C.32.P2S` when scale-amenability pressure must continue through problem-to-structure architecturing; `C.32.ACS` when the pressure is represented as a distinct project criteria row; `C.32` when scale preference informs candidate architecture generation; `A.19.CPM` when it supplies one input to explicit comparison; `A.10` for source recovery and bounded reliance, `G.6` for addressable provenance, and `B.3` for a named assurance claim; `G.5`, `G.9`, and `C.11` for selected-set, parity, and choice claims.
- **Boundary:** `C.31.ASAP` governs architecture scale-preference claims. `C.32.ACS` governs criteria-set and criteria-row construction; `A.19.CPM` governs explicit comparison. `C.31`, `C.31.RSA`, `C.29`, `C.18.1`, `C.19.1`, `G.5`, `G.9`, and `C.11` govern modularity-characteristic, reusable-structure accounting, mathematical-lens, scale-law, general method preference, selected-set, parity, and local-choice claims when those claims are being made.
- **Precision-restoration relation:** source wording recovered by `E.10`, `E.10.ARCH`, or `C.30.STRAT` is governed by C.31.ASAP only when the recovered claim being made is architecture scale preference over a declared alternative set, scale variable, and scale window.

### C.31.ASAP:End

