## C.31.ASAP - Which Architecture Is Preferable Under Scale? (Scale Amenability)

> **Type:** Characterization pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### C.31.ASAP:1 - Problem frame

Use this pattern when a practitioner compares architecture alternatives under a declared scale variable or scale window and needs to avoid treating a modularity label, platform label, product-line label, reusable-structure share, or coarse-graining metaphor as an automatic scale-preference claim.

First identify the alternatives, the scale variable and its window, and the grounds and limits of the proposed preference. An adequate ordinary account can finish; `ScaleClaimTriage` can retain it:

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
  slopeEvidenceRef, scaleProbeEvidenceRef, comparisonBasisRef, or noProbeReason:
  expectedStableOrImprovingStructure?:
  exceptionGrowthRisk?:
  sourceReturnCondition?:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

Ordinary use starts by naming:

- the alternatives and described holon;
- the `U.ClaimScope` and relevant A.2.6 `U.ContextSlice` membership;
- the scale variable and scale window;
- the claimed preference under scale and whose price, effort or other outcome the commission asks you to compare;
- the observations or derivation supporting the proposed scale behavior, or what remains open in their absence;
- the structural feature or exception behavior on which that preference depends, when it calls for either.

Name `modelUseStructureRef` only when one independently selected `BoundedModelUseStructure` changes this receiving interpretation; it never replaces the claim scope.

Use `ArchitectureScaleAuditRecord@Project` when those distinctions help retain or examine the preference for its receiving use. Sharing an already adequate account needs no new form.

What goes wrong if C.31.ASAP is missed:

- "modular", "platform", "product line", "reusable", "general", "open", "coarse-grained", or "RG-like" becomes a shortcut for a scale-preference claim;
- a locally hand-engineered solution is called debt even when safety, law-domain, or mission constraints justify it;
- exception growth is hidden until the architecture is already expensive to change; and
- coarse descriptions keep losing lower-scope safety or semantic distinctions without a source-return condition.

A practitioner can use the resulting account to say which architecture is preferable for the planned scale and criterion, which conditions support that judgement, and what could reverse it.

For questions limited to the following concerns, use the corresponding patterns instead of C.31.ASAP:

| Question | Pattern |
| --- | --- |
| Module-interface relation repair | `A.6.M` |
| Modularity-characteristic selection | `C.31` |
| Reusable-structure accounting | `C.31.RSA` |
| Mathematical-lens use | `C.29` |
| Scale-law adequacy | `C.18.1` |
| Method preference under general BLP | `C.19.1` |
| Candidate architecture generation | `C.32` |
| Selected-set return | `G.5` |
| Final local choice | `C.11` |

C.31.ASAP governs architecture scale-preference claims; it does not select the architecture, prove the scale law, or certify the project.

### C.31.ASAP:2 - Problem

Architecture work often asks whether one structure will scale better than another: a product-line architecture rather than bespoke variants, an open interface rather than a closed integration, a stable flow topology rather than repeated project exceptions, or a reusable evidence package rather than repeated assurance work.

These claims are useful only after the scale relation is declared. "Scales better" can mean fewer interface grammar variants, lower exception growth, better learning transfer, more reusable templates, more stable control relations, less source-return cost, fewer regulatory exceptions, or more freedom of action. Those are not the same claim.

C.31.ASAP connects a declared scale variable and window to a preference claim, its evidence or no-probe reason, the behavior or exception risk on which it depends, and any needed source return. It does not turn scale preference into proof, selection, assurance, causal use, or a universal law.

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

C.31.ASAP specializes scale-amenability preference for architecture alternatives. It applies when an architecture alternative set, scale variable with its window, and claimed preference under scale are named.

#### C.31.ASAP:4.1 - Applicability fields

C.31.ASAP applies only when all of the following are present:

1. a declared architecture alternative set, described holon, `U.ClaimScope`, and relevant A.2.6 `U.ContextSlice` membership;
2. a declared scale variable and its window;
3. a claimed preference under scale;
4. the observed scale behavior, a derivation from applicable conditions, evidence from a scale probe, or a reason why the claim remains hypothetical;
5. the grounds relating the architecture alternatives to that comparison. These may include an applicable quotation for the required service, or differences in structure and local exceptions where those affect the claimed advantage.

If those fields are absent, keep the claim in `C.31` as a temporal or scale-sensitive characteristic cue, in `C.31.RSA` as report-only accounting, in `C.29` as a bounded lens-use output, or in ordinary architecture prose.

#### C.31.ASAP:4.2 - `ScaleClaimTriage`

Recover the following content before a heavier scale audit. Reuse an adequate account; the triage form is optional:

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
  comparisonBasisRef?:
  noProbeReason?:
  expectedStableOrImprovingStructure?:
  exceptionGrowthRisk?:
  sourceReturnCondition?:
  admissibleUse:
  nonAdmissibleUse?:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

A supported preference can finish a comparison. If the evidence still permits different rankings, identify the condition that changes the ordering. An inquiry to resolve it can itself be the deliverable when that inquiry was commissioned.

Include `nonAdmissibleUse?` only for an independently grounded alternative that is plausible here and whose rejection changes understanding or action; `groundedScaleShortcut?` is an alias for that optional value.

Retaining or publishing the bounded answer preserves its limits. A stronger comparison, assurance, selected-set or decision claim needs its own grounds.

`claimScopeRef` designates one `U.ClaimScope`; `selectedContextSliceRefs` records the A.2.6 membership relevant to this use. A scale window is the range of the scale variable for which the preference is claimed, not a substitute for either scope object.

`modelUseStructureRef` is optional and is filled only when an independently selected A.1.1 `BoundedModelUseStructure` changes the interpretation of this preference use.

#### C.31.ASAP:4.3 - Architecture scale-preference rule

When the commission values stable reusable structure, compare how well the alternatives preserve it over the declared scale window, subject to safety, law-domain and assurance requirements. If the question concerns another characteristic, carry the alternatives through the permitted operating conditions and compare them on that characteristic. Select the functional, flow, control, interface, work-template or evidence structure and any learning-transfer characteristic relevant to that comparison.

Define the advantage that would change the recommendation and for whom. A supplier’s engineering effort, the purchaser’s price and the installer’s work can change independently. For a combined cost, include the work the arrangement transfers to others within the stated scope and count shared work once. Compare both alternatives for the same deliveries under the conditions that affect that advantage. Separate a one-time investment from work repeated at each installation or each new interface type. When deciding whether to commission a shared design, count the preparation it requires. When deciding whether to keep using one already built, compare future costs and commitments that the choice can still change. The original expense remains part of the investment history. More deployments at an established site may require none of the qualification work that a first deployment in a new jurisdiction requires. Check where the two alternatives tie or change order. When different admissible mixes of sites give different recommendations, state which mix supports each and what is known about the proposed rollout.

Observations can support a comparison for the conditions examined. A binding rate, an engineering bound or a supported construction can also establish an answer for the entire stated range under its assumptions. Record the observations or the applicable derivation and its assumptions. A quotation or bound that orders the alternatives throughout a window can be cited in `comparisonBasisRef` even when neither slope is known. An advantage in price throughout a window establishes which quote is cheaper. To claim its price grows more slowly, compare the changes in price. When an untested premise could reverse the preference, state what depends on it. A reason for skipping a probe supplies no evidence about its outcome. An applicable derivation can already settle the question. Conflicting characteristics need the preference or decision rule for the work in question.

C.31.ASAP defines the scale-preference claim and its boundary. Use `G.9` for a parity claim and `A.21` for a gate claim; the candidate, comparison, set-declaration, and choice uses are distinguished below.

A scale-preference claim may inform `C.32` candidate generation or supply one input to an `A.19.CPM` comparison by naming the scale variable and window, the grounds for ordering the alternatives, and any structural uncertainty or exception that could reverse that order.

Use:

- `C.32` to construct the candidate architecture palette;
- `A.19.CPM` to compare alternatives;
- `G.5` to declare a selected-set result;
- `C.11` to make a final local choice; and
- `C.32.PAD` to record a project architecture decision.

For audience availability, use `E.24.PUB` for the publication occurrence, form, carrier, audience and bounded use; use `E.17` when a source-backed face and return are needed.

Apply the relevant evidence, assurance, gate, or release definition and test only when that claim is current.

When the same scale-sensitive pressure must also become a project criterion, `C.32.ACS` creates a separate row for the characteristic or Q-Bundle slot, bearer, scale form, and use class. That row may supply declared input to an ASAP preference. Use C.31.ASAP to state which alternative is preferable under the scale window; use C.32.ACS to admit and classify the criterion row as an optimization indicator, guardrail, or context-only row. Keep the preference record and criterion row separately referenced.

#### C.31.ASAP:4.4 - Scale variables

Typical architecture scale variables include:

| Scale variable | Reading |
| --- | --- |
| `N_units` | repeated units or instances |
| `N_scopeCount` | aggregation scopes, coarse-graining scopes, or typed LCA control scopes |
| `N_sites` | Distinct deployment sites. Deployment events, markets and jurisdictions can have different counts and costs. Name and count the one that drives the work in question. |
| `N_interfaceTypes` | distinct interface grammar variants |
| `N_requiredTransformationKinds` | distinct transformation kinds in the selected functional-structure view |
| `N_flowRelationKinds` | flow-relation or crossing variants in the selected flow-structure view |
| `N_moduleTypes` | module type library size |
| `N_workRepetitions` | delivery, operation, or test repetitions |
| `N_supplierOrVendorClasses` | substitutability or vendor class dimension |
| `N_regulatoryInstances` | approval, safety, or certification repeats |
| `freedomOfAction` | allowed design, search, or control variation |

Name the scale variable, its window and the characteristic whose behavior matters to the comparison. Add a source-return condition when omitted distinctions could change the receiving action. Increasing the number of sites changes a quantity in the model. Abstracting the model can leave the jurisdiction of a site open. The same disciplinary model can compare five and forty sites. Use B.5.MR:4.2 when asking which conclusions still follow after leaving a distinction open.

#### C.31.ASAP:4.5 - Scale audit outputs

Use a fuller audit when unresolved behavior, exceptions or comparison grounds could change the receiving use. An existing adequate account can carry the necessary content:

```text
ArchitectureScaleAuditRecord@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureScaleAuditProjectUseRelationRef?: U.RelationRef governed by the audit-use or work-use pattern
  architectureAlternativeSetRef:
  claimScopeRef:
  selectedContextSliceRefs:
  modelUseStructureRef?:
  scaleVariableRefs:
  scaleWindowRef:
  ArchitectureSlopeVector?:
  comparisonBasisRef?:
  IsoScaleParityNote?:
  ASAPWaiverReason?:
  ArchitectureHeuristicDebt?:
  BespokeResidueRegisterRef?:
  SourceReturnCondition?:
  admissibleUse:
  nonAdmissibleUse?:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

For `ArchitectureScaleAuditRecord@Project` and `BespokeResidueRegister@Project`, `@Project` is a compatibility and retrieval cue.

An audit local to one project names both the composite `U.Work` in `projectWorkOccurrenceRef` and the obtaining direct audit-use relation in `architectureScaleAuditProjectUseRelationRef`. `BespokeResidueRegisterRef` may cite the register episteme. Assert that register's project locality only after a separate direct register-to-work relation is governed, and cite that occurrence; the audit-use relation remains about the audit. Otherwise retain only retrieval use and make no audit or residue-register project-locality claim.

| Output | Meaning |
| --- | --- |
| `ArchitectureSlopeVector` | Slopes for the selected characteristics, such as reusable structure, interface variation, flow or control stability, work repeatability, residue, exception growth or learning transfer. Keep missing estimates, uncertainty and incomparable dimensions visible. |
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

A deontic constraint, safety boundary, law-domain boundary, mission constraint, assurance infeasibility or scale-probe result can justify departing from the scale preference. If the baseline is a recommendation, a different choice may already be within the decision maker’s authority. For a binding condition, establish whether the operative rule permits a departure in this case and scope. Where it reserves a decision, identify who may grant it and whether the required decision took effect. An analyst can establish the case for requesting that decision. A binding constraint that admits no waiver continues to apply.

`ArchitectureHeuristicDebt` remains report-only unless tied to a decision, risk, work, evidence, assurance, or selected-set record through its governing pattern.

#### C.31.ASAP:4.7 - Scale-refactoring moves

Name at least one possible repair or stop before using the scale preference to guide action:

| Scale symptom | Possible architecture move | Boundary |
| --- | --- | --- |
| interface variants grow without payoff | reduce interface alphabet or introduce interface grammar | A.6.M governs interface relation repair. |
| product-line or platform variants lack explicit variation points | introduce variability slots or extension rules | Platform label alone is not scale-preference evidence. |
| one aggregation scope hides lower-scope hazards | split the declared aggregation scope or architecture boundary | Recover the consequential distinction. Use C.29 when the mathematical representation, transfer or limits of reliance remain unresolved. |
| repeated work contains reusable structure | reuse a method template for subsequent work | Use `A.3.1` for a Method claim and `A.15` for Method–Work alignment. For a dated Work, recover A.13 and independent A.15.1 admission, with F.6 only for precise assignment-bound attribution. Use `A.15.4` only while appearance hides a work-relevant prerequisite. |
| regulatory or safety residue remains local and repeated | isolate regulatory residue or safety-specific exception register | Establish the relied-on source grounds; use `A.10` for a needed replayable source-to-use account, `G.6` for needed addressable provenance, `B.3` when a named assurance claim is current, and `A.21` for a gate claim. |
| coarse representation loses action-changing safety, semantic or source distinctions | return to source-side evidence or narrow the scale window | Preserve the return condition needed by this reliance. |

#### C.31.ASAP:4.8 - C.29 lens relation

A scale preference may use an RG, coarse-graining, epiplexity, graph, multilevel-learning or frustration model. Establish the assumptions and correspondence needed by that inference; an adequate domain treatment can suffice. Use `C.29` when choosing or transferring the representation, or relying on its result, leaves an unresolved question. Keep the architecture scale-preference claim in C.31.ASAP and use C.18.1 for a scale-law claim.

The account retains its scale variable, window and the basis for the comparison, including any variation in exceptions that can change the answer. State where to recover an omitted fact when the answer depends on it. When a C.29 account is needed, it can use `MLU.Description@RGArchitecture`, `MLU.Description@MultilevelLearningFrustration` or another local account to explain the representation, correspondence, preserved and lost distinctions, payoff and limits. A separately named output is needed only when the receiving use requires it.

### C.31.ASAP:5 - Archetypal Grounding

| Archetype | Without C.31.ASAP | With C.31.ASAP |
| --- | --- | --- |
| Product-line platform | A team treats a platform name as grounds for lower rollout cost. | Compare the work or price for the planned varieties and volumes. Investigate a variation or exception when it can change that comparison. |
| Neural architecture block library | Reusing blocks is treated as reusable architecture by itself. | The alternative set names scale variable, interface grammar variants, exception growth, and source-return condition. |
| Safety or certification reuse | Reusable evidence package is counted without validation boundary. | Evidence reuse remains tied to source-return. An evidence-validity or safety claim is tested under its applicable domain rule. Establish the relied-on source grounds; use `A.10` for a needed replayable source-to-use account, `G.6` for needed addressable provenance, and `B.3` when a named assurance claim is current. |
| Cross-scope residual | A frustration or complexity label is treated as scale mathematics. | C.31.ASAP names the scale window and residual slope; establish the mathematical basis of the interpretation; use C.29 if representation choice, transfer or reliance is unresolved. |

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
  scaleProbeEvidenceRef: six platform deployments using the ordinary interface within one qualification regime. The records identify the interface, local exceptions and work completed at those sites.
  expectedStableOrImprovingStructure: interface grammar, reusable test package, deployment work template
  exceptionGrowthRisk: jurisdiction-specific clauses and side-channel integrations may grow faster than sites
  sourceReturnCondition: return to exception register, interface variant log and deployment evidence when a wider window or stronger use needs distinctions omitted from this account
  relatedClaimGovernanceIfClaimed: C.31 for the characteristic; C.31.RSA for reusable-structure share; C.16 for measurement; A.19.CPM for comparison; G.5 for selected-set declaration; G.9 for parity; C.11 for local decision; A.10 for source recovery and bounded reliance; G.6 for addressable provenance; B.3 for a named assurance claim
  stopCondition: retain the supported local guidance and the untested-window hypothesis; establish comparison, evidence-validity or decision grounds for that further use
```

The six platform deliveries show which interfaces and exceptions occurred there. Predicting a lower growth rate than the bespoke alternative calls for comparable grounds for that alternative and for the future mix of sites. Identify the change in configuration or jurisdiction that could reverse the preference.

Suppose both suppliers offer the same required service for five to forty sites during the quotation period. The shared platform costs 18 units to prepare the common interface and 2 per ordinary site. The bespoke offer costs 5 per site. At five ordinary sites the quoted totals are 28 and 25. At six they tie. From seven through forty ordinary sites the platform costs less. This follows from the two binding offers for that range. The six installations alone would not establish those prices.

At eight sites the ordinary prices are 34 and 40. Under the same offers one site needing a different connector adds a one-time charge of 12 to the platform total and is included in the bespoke price. The comparison then favors the bespoke offer at 40 against 46. If the eighth site's connector is unknown and the other seven are ordinary, its interface specification settles which offer is less expensive. An assertion about actual expenditure still needs the charges incurred. An architecture choice can also depend on service or assurance conditions beyond price. At twelve sites with at most one such surcharge, the platform quote is either 42 or 54 against 60. Its price advantage then holds with either connector. These binding totals settle the purchaser’s quoted price. If the cheaper offer leaves local rewiring to site technicians, ask whose budget bears that work. Include it when comparing the purchaser’s full rollout cost or total delivery effort. A higher supplier cost that is covered by the fixed price need not change which invoice is lower.

#### C.31.ASAP:5.2 - Near-miss lowering slice

Near-miss: a team says the platform architecture should win because it has an 82 percent reusable-structure share, an RG-like coarse description, and "less bespoke debt" than the local variant.

Lowering replay:

- Identify the feature of the proposed platform on which the preference depends. For a preference based on exception-handling effort, recover which variants require an exception and how much work it adds.
- The team's reported 82 percent gives a starting point for checking the claim. Recover the counting unit, population and records to establish the share. Even an established share can correspond to 41 of 50 or 82 of 100. It supplies an absolute count only with an adequate denominator and precision. For a scale preference, establish how the counted reuse affects the characteristic compared over the proposed deployments.
- An RG-like phrase alone supplies no mathematical correspondence or scale-preference evidence. Recover the model and its relevant preservation and loss; use C.29 if representation choice, transfer or reliance remains unresolved.
- The "bespoke debt" label is lowered to waiver review when safety, law-domain, mission, assurance, or scale-probe overturn reasons may justify the local variant.

Report the 82 percent as the team's statement until its basis is established. Preserve a verified accounting result within that basis. If compatible rollout plans favor different alternatives, identify the conditions for each preference and what the present decision requires.

### C.31.ASAP:6 - Bias-Annotation

| Bias risk | C.31.ASAP correction |
| --- | --- |
| **Platform label bias** | Identify what would give the platform its claimed advantage. Recover the interface variations, exception costs or coverage limits on which that advantage depends. |
| **Modularity-means-scalability bias** | A count or reusable share alone does not establish scale preference. Use C.31 or C.31.RSA when the characteristic or accounting meaning remains unresolved; proceed directly to C.31.ASAP when the alternatives, variable, window and relevant grounds are recoverable. |
| **Debt inflation bias** | A locally hand-engineered solution is called debt without checking deontic, safety, law-domain, mission, assurance, or scale-probe waiver reasons. |
| **RG proof bias** | RG, coarse-graining, fixed-point, or universality wording is treated as scale-preference proof. Establish the mathematical inference and the distinct scale preference; use C.29 when its representation or reliance question is unresolved. |
| **Selection laundering** | The scale-preference claim is used as if it selected the architecture. Use `G.5` for selected-set declaration and `C.11` for local choice; use `G.9` when parity is current. |

### C.31.ASAP:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| `CC-C31.ASAP-1` | A C.31.ASAP use being made names the architecture alternative set, described holon, `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership, scale variable and its window, and claimed preference under scale. | Prevents generic "scales better" and generic-context wording. |
| `CC-C31.ASAP-2` | Identify what the observations or applicable derivation establish for the stated alternatives and scale window. State an unsupported extension as a hypothesis. | A price schedule can settle a quoted cost over the whole window. A reason for skipping a test supplies no measured slope. |
| `CC-C31.ASAP-3` | Identify the structure expected to remain stable or change, and the relevant exceptions, when the preference depends on that behavior. | Applicable price bounds can order two offers while leaving their internal engineering effort unknown. |
| `CC-C31.ASAP-4` | Source-return condition is present when a compressed, coarse, extracted, indexed or accounting representation drops distinctions on which the receiving action depends. | Prevents unsafe coarse descriptions. |
| `CC-C31.ASAP-5` | Classify the reason for departure under §4.6. When an effective waiver is claimed, identify the rule that covers this case or the decision made under the authority it delegates. A justified request can complete an advisory commission. | Prevents false debt labels. |
| `CC-C31.ASAP-6` | `ArchitectureHeuristicDebt` remains report-only unless a decision, risk, work, evidence, assurance, or selected-set record is being used under its governing pattern. | Prevents shadow project authority. |
| `CC-C31.ASAP-7` | Platform, product-line, modularity, reuse, open-interface, RG, and coarse-graining labels do not establish scale preference by themselves. | Blocks source-label overread. |
| `CC-C31.ASAP-8` | Mathematical inferences retain their model, correspondence and use conditions. Use C.29 for unresolved representation choice, transfer or reliance; C.31.ASAP governs the distinct scale preference. | Keeps the mathematical and preference grounds explicit without requiring a separate lens output for an adequate domain treatment. |
| `CC-C31.ASAP-9` | Comparison, selected-set, local choice, evidence, assurance, gate, work, or release claims name the governing pattern. | Prevents scale preference from becoming selection or assurance. |
| `CC-C31.ASAP-10` | A source-dependent preference retains the adopted contribution, its assumptions and limits. | Makes the grounds of the preference recoverable. |
| `CC-C31.ASAP-11` | Project-local audit use names both `projectWorkOccurrenceRef` and `architectureScaleAuditProjectUseRelationRef`; a residue register remains retrieval-only unless its own governed direct relation to the composite Work is cited. | Prevents an `@Project` suffix, work reference, or borrowed audit relation from fabricating locality. |
| `CC-C31.ASAP-12` | When an ACS criterion row and an ASAP preference are both current, each is separately referenced and neither substitutes for the other. | Keeps criterion admission and alternative preference distinct. |

### C.31.ASAP:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| `ModularThereforeScalable` | The text claims an advantage without saying what changes as use grows. | Identify the alternatives, relevant quantity, range and grounds for the advantage. Retain an untested hypothesis where the comparison is open. |
| `GenericScaleAudit` | Audit fields appear with no architecture alternative set or preference use. | Recover the architecture question and retain only the content needed to answer it. |
| `AllExceptionsAreDebt` | Any non-scale-amenable choice becomes debt. | Test waiver reasons and keep justified bounded exceptions out of `ArchitectureHeuristicDebt`. |
| `RGAsScaleProof` | Coarse-graining or RG wording is used as a scale-preference claim. | Establish the mathematical grounds and C.31.ASAP preference conditions. Use C.29 for an unresolved representation or reliance question; retain source return when the inference depends on omitted distinctions. |
| `ShareAsScalePreferenceEvidence` | `ReusableStructureShare` or `BespokeResidueShare` is used to prefer one alternative. | Keep the share report-only in C.31.RSA until scale variable, window, and admissible comparison are declared. |

### C.31.ASAP:9 - Consequences

| Positive consequence | Cost or trade-off |
| --- | --- |
| Scale preference becomes inspectable before selection or decision. | The practitioner must name a scale variable and window instead of relying on a label. |
| Product-line comparisons expose which changes in the customer mix could reverse the preference. | The effect of an unfamiliar variation can remain uncertain until its cost or technical consequence is established. |
| C.29 lens use stays useful without turning into scale proof. | RG and coarsening inferences need their relevant preservation and loss grounds, with source return when omitted distinctions can change the use. |
| Report-only debt notes remain bounded. | Decisions or risk records must use their governing patterns when reliance use is being made. |

### C.31.ASAP:10 - Rationale

`C.31` and `C.31.RSA` can expose scale-sensitive characteristics and reusable-structure residue, but they should not themselves decide which architecture alternative is preferable under scale. C.31.ASAP governs this architecture scale-preference claim family; it is narrower than general BLP and broader than one measurement card.

The pattern adapts BLP-style scale-amenability to architecture: when continued reuse is the criterion, prefer an alternative with a demonstrated advantage over the declared scale window under comparable safety, law-domain and assurance conditions. Treat modularity, reuse, platform practice, and mathematical coarse-graining as candidate cues. Base the preference on the named scale variable and window, relevant structural behavior, exception-growth risk and the reach of available evidence. A comparison can follow from applicable rates or constraints throughout a range. A preference that still depends on an untested extrapolation remains provisional.

### C.31.ASAP:11 - SoTA-Echoing

| Source family | Source-use relation | C.31.ASAP contribution | Practitioner use |
| --- | --- | --- | --- |
| Software product-line and variability-management practice (`https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`) | Variability lineage and SPLE-review cues. | Adopt variability slots, product-line reuse, exception inventory, and refactor triggers as architecture scale-preference fields. | Treat a product-line label, shared code base, feature model, or platform name as a cue. Recover the variation and exception behavior that matters to the proposed preference in its scale window. A comparative quotation can settle acquisition price while leaving future integration effort open. |
| Product-platform and modular product-architecture practice (`https://link.springer.com/article/10.1007/s00163-023-00427-1`; `https://arxiv.org/abs/2510.11089`) | Engineering-design source line for modular product architecture, assembly orientation, product-family reuse, and manufacturing-aware modularity. | Product-family commonality and variety can change assembly and qualification work as deployment grows. | If the preference depends on assembly or qualification, identify the variations, interfaces and operating constraints that affect it. A covered price comparison can settle the purchaser's cost without settling who does the engineering work. |
| Platform-engineering maturity practice (`https://tag-app-delivery.cncf.io/fr/whitepapers/platform-eng-maturity-model/`) | Platform-practice source for platform service set, extension-rule, substitution-policy, and maturity-pressure claims. | Adapt platform practice into extension-rule, substitution-policy, conformance-expectation, and exception-growth checks. | Treat platform maturity as a source cue until the architecture scale variable and exception behavior are declared. Establish any architecture selection or reusable-structure claim through its own pattern. |
| C.19.1 BLP in FPF | FPF-local preference discipline for general scale-amenable methods. | Specialize the preference idea to architecture alternatives, selected structures, scale variables, and architecture slope vector. | Use C.19.1 for method-family policy and C.31.ASAP for architecture scale preference; selector policy and decision records remain with their governing patterns. |
| C.29 RG and coarse-graining lens use in FPF | FPF-local mathematical-lens discipline. | Establish the scale window, coarse-graining rule and relevant preservation or loss for the inference; retain source return when needed. | Use C.29 when representation choice, transfer or reliance is unresolved; its local account can use `MLU.Description@RGArchitecture` or `MLU.Description@MultilevelLearningFrustration` when that form serves the receiving use. Establish any physical-RG, scale-proof, causal-proof, assurance, or selected-architecture claim through its own source basis and governing pattern. |

### C.31.ASAP:12 - Relations

- **Builds on:** `C.31`, `C.31.RSA`, `C.16`, `A.2.6`, `A.17`, `A.18`, `A.19`, `C.18.1`, `C.19.1`, and `C.29`; uses A.1.1 only when a selected `BoundedModelUseStructure` changes the receiving interpretation.

**Coordinates with:**

| Need or use condition | Coordinating pattern |
| --- | --- |
| Module-interface relation repair. | `A.6.M` |
| Architecture and selected-structure questions. | `C.30`, `C.30.ASV`, `C.30.LCA`, and `C.30.ILC` |
| Scale-amenability material needs captured-structure, lost-structure, preservation, or correspondence adequacy before candidate use. | `C.33` and `C.34` |
| The generated or discovered result's kind and adequacy for candidate use. | `C.35` |
| Scale-amenability pressure must continue through problem-to-structure architecturing. | `C.32.P2S` |
| The pressure is represented as a distinct project criteria row. | `C.32.ACS` |
| Scale preference informs candidate architecture generation. | `C.32` |
| Scale preference supplies one input to explicit comparison. | `A.19.CPM` |
| Source recovery and bounded reliance; addressable provenance; a named assurance claim. | `A.10`; `G.6`; `B.3`, respectively |
| Selected-set, parity, and choice claims. | `G.5`, `G.9`, and `C.11`, respectively |


**Claim boundaries:**

| Claim being made | Governing pattern |
| --- | --- |
| Architecture scale preference | `C.31.ASAP` |
| Criteria-set and criteria-row construction | `C.32.ACS` |
| Explicit comparison | `A.19.CPM` |
| Modularity characteristic | `C.31` |
| Reusable-structure accounting | `C.31.RSA` |
| Mathematical lens | `C.29` |
| Scale law | `C.18.1` |
| General method preference | `C.19.1` |
| Selected set | `G.5` |
| Parity | `G.9` |
| Local choice | `C.11` |

- **Precision-restoration relation:** source wording recovered by `E.10`, `E.10.ARCH`, or `C.30.STRAT` is governed by C.31.ASAP only when the recovered claim being made is architecture scale preference over a declared alternative set, scale variable, and scale window.

### C.31.ASAP:End
