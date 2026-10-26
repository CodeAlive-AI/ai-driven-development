## C.31.RSA - Reusable Structure Accounting

> **Type:** Characterization pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.31.RSA:1 - Problem frame

Use this pattern when a practitioner needs to locate where reusable structure lives, where bespoke residue grows, which accounting basis is being used, what can be refactored, and what remains a bounded exception or source-return condition. A report-only share supports a separate use only when that use meets the conditions defined by its applicable pattern.

Claim-use boundary: any use that relies on the RSA account to make a claim beyond reusable-structure accounting is outside RSA. Examples include comparison, publication, evidence validity, assurance or safety-case reliance, gate use, architecture scale preference, causal use, selected-set result declaration, candidate synthesis, and local decision. Record with C.31.RSA only the reusable locus, bespoke residue, accounting basis, report-only share, repair direction, and source-return condition. Add another claim only after naming and applying the pattern that defines and tests it.

First locate the reusable structure and bespoke residue, identify the accounting question, and explain any warranted repair or bounded exception. An adequate ordinary account can finish. `ReusableStructureTriage` can retain these distinctions:

```text
ReusableStructureTriage:
  describedHolonRef:
  reuseQuestion:
  deploymentBoundary?:
  intendedAccountingUse:
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?:
  architectureClaimRef?:
  structureRefs:
  structuralAspectRefs?:
  accountingRelationRefs:
  evidenceRefs:
  whereReusableStructureCurrentlyLives:
  whereBespokeResidueCurrentlyGrows:
  residueRefactoredInto:
    template | interfaceSpecification | methodDescription |
    workStructure | evidencePackage | assuranceArgumentStructure | otherDeclared
  residueAcceptedAsBoundedException:
  sourceReturnCondition?:
  relatedClaimPatternsIfClaimed:
  stopCondition:
```

Use a fuller accounting description when the receiving question needs its structure references and accounting rule. Ordinary use stops when the practitioner knows where reusable structure lives, where bespoke residue grows, what can be refactored and what remains a bounded exception. Retaining or sharing that answer need not create another form.

What goes wrong if C.31.RSA is missed: a reusable share is treated as a proof of modularity; one-off work is hidden under a reuse label; evidence reuse is counted without validity context; hidden residual uncertainty is averaged with reusable templates; and "more reusable structure" is treated as always better.

What C.31.RSA buys in practice: the practitioner can state where structure is reusable, where it is bespoke, what source-side distinctions must remain reachable, and when the result is only report-only accounting.

Not this pattern when the question under repair is source-label recovery, module-interface relation repair, modularity-characteristic selection, measurement or comparability admissibility, architecture scale preference, mathematical-lens use, or any outside-RSA use named above. Use `C.30.STRAT`, `A.6.M`, `C.31`, `C.16`, `A.10`, `B.3`, `G.6`, `C.31.ASAP`, `C.29`, `G.5`, or `C.11` as appropriate; do not treat C.31.RSA as the synthesis or selector pattern.

### C.31.RSA:2 - Problem

Architecture teams often say that structure is reusable, repeated, templated, common, standardized, or bespoke. Those phrases are useful, but they do not say what is being counted, described, or compared. Structure can be selected from functions, flows, control relations, module interfaces, work methods, evidence packages, regulatory arguments, data schemas, deployment constraints, or exception networks.

Functional, flow, control, module-interface, work, evidence, and assurance structures may be included only under their declared `accountingBasisRef`. Name any evidence, assurance, or source relation being claimed by value, and state any source-return condition relied on by the account.

The practical question is: which reusable loci matter, which bespoke residue remains, what source distinctions are lost by accounting, and what repair or source return follows?

### C.31.RSA:3 - Forces

| Force | Tension |
| --- | --- |
| Reuse visibility vs false proof | Reusable loci should be visible, but a share is not proof of quality, assurance, or architecture adequacy. |
| Accounting convenience vs heterogeneous structure | Templates, interface grammars, work methods, and evidence packages do not automatically share one unit. |
| Residue repair vs useful exception | Some bespoke residue should be refactored; some should remain a bounded exception. |
| Compression vs source return | Accounting can summarize structure, but downstream action may require return to source-side records. |
| Local triage vs cross-case comparison | A local report-only share can guide repair; comparison needs declared scale, unit interpretation, admissible comparability relation, and comparator admission named by value. |
| Reuse value vs reuse cost | More reusable structure can increase interface cost, evidence decay, or loss of needed variation. |

### C.31.RSA:4 - Solution

C.31.RSA governs reusable-structure accounting as a typed description over declared structures and structural aspects. Start by locating reuse and residue. Use `ReusableStructureTriage` or `ReusableStructureAccountingDescription@Context` when their fields help the account; a quantitative accounting description still requires its declared basis.

#### C.31.RSA:4.1 - Typed accounting description

```text
ReusableStructureAccountingDescription@Context:
  accountingBasisRef:
  structureRefs: FinSet(U.StructureRef)
  structuralAspectRefs: FinSet(StructuralAspectDescriptionRef)
  reusableStructureSlots:
  bespokeResidueSlots:
  hiddenOrResidualUncertaintySlots:
  slotBasisRefs?:
  admissibleAggregationRuleRef?:
  reportOnlyShares?:
  sourceReturnCondition?:
  admissibleUse:
  nonAdmissibleUse?:
```

`accountingBasisRef` identifies the accounting rule. The rule may concern description length, dependency edges, work items, evidence package count, cost share, template instances, interface variants, regulatory case sections, or another declared basis. The accounting rule is not implied by the word "reuse".

Well-formedness: every slot is over declared `structureRefs`, declared `structuralAspectRefs`, and one declared accounting basis. Slot labels are explanatory; they are not root kinds and are not automatically commensurable.

#### C.31.RSA:4.2 - Explanatory slot labels

A local accounting description may use explanatory slot labels such as:

```text
S_function
S_flow
S_control
S_type
S_interface
S_scale
S_work
S_evidence
S_changePolicy
S_unique
S_crossScopeUnique
H_residual
```

These labels are local slots, not FPF ontology. `H_residual` is residual uncertainty or unmodelled variance under the accounting basis. Its value is not automatically commensurable with counts or other measures of interface grammars, work templates, evidence packages, or regulatory arguments.

#### C.31.RSA:4.3 - Report-only shares

```text
ReusableStructureShare:
  report-only share over declared structureRefs and structuralAspectRefs
  under accountingBasisRef; not an architecture amount

BespokeResidueShare:
  report-only share under accountingBasisRef

HiddenOrResidualShare:
  report-only uncertainty or residue interpretation under accountingBasisRef
```

Every numeric share needs its accounting rule, counted population and scale or unitless-value interpretation, with a unit when relevant. A comparison or ranking additionally needs aligned bases, preference direction when relevant, and its applicable comparator, such as `CG-Spec`, `ComparatorSetRef` or a governing comparator reference. A gate or decision needs that comparator only if its rule relies on such a comparison; it retains its own other requirements. A share with an established counting basis can remain a bounded local report when stronger reliance lacks grounds.

#### C.31.RSA:4.4 - Pseudo-sum boundary

An explanatory decomposition may be useful:

```text
total-described-structure under accountingBasisRef:
  reusable slots
  bespoke residue slots
  hidden or residual uncertainty slots
```

This is a readable decomposition of one declared accounting description, not an equation defining an architecture amount. If the slots do not share a declared accounting basis and comparability rule, they cannot be summed or ranked.

#### C.31.RSA:4.5 - Structure-relocation actions

RSA is useful because it points to relocation and repair actions:

| Situation | Repair direction |
| --- | --- |
| Repeated delivery work contains structure that is not explicit in the work or method description being used. | Move repeated structure into `MethodDescription`, work structure, or reusable work relation. |
| Repeated interface exceptions are handled one by one. | Add or revise interface grammar, variability slots, or substitution policy; use A.6.M when this is a module-interface claim. |
| An undocumented dependency crosses module or view boundaries. | Expose the dependency, revise boundary, add correspondence, or add source-return condition. |
| Evidence is recreated for each instance. | Move repeatable evidence into an evidence package, assurance argument record, or validity-context note. |
| Regulatory or safety-case residue remains one-off. | Split reusable argument structure from context-specific exception; apply B.3 to the assurance claim, including a claim about safety-case support, and G.6 when a citable provenance path is needed. |
| Compression hides needed distinctions. | Reduce compression, add source-return condition, or apply C.29 for lens-governed compression or reduction claims. |
| Bespoke residue protects necessary local variation. | Keep it as a bounded exception with its use conditions and any action-changing limit. |

A high reusable-structure share is not always good. The architecture question is where structure lives—for example, in reusable templates, interfaces, flows, control relations, work methods, evidence packages, or unique exception networks and hidden coupling—and what action follows.

After a relocation or reuse move, ask what got worse:

| Reuse move may improve | Check what may worsen |
| --- | --- |
| Template reuse | Loss of needed variation, hidden local exception, or stale source-return condition. |
| Interface grammar | Interface relation cost, conformance work, change cost, migration cost, or substitution constraint. |
| Work-method reuse | Context mismatch, extra handoff cost, slower local response, or hidden work exception. |
| Evidence-package reuse | Evidence decay, validity-window mismatch, missing context witness, or assurance overread. |
| Assurance-argument reuse | Weakest-link dependency, certification-window mismatch, or unexamined regulatory exception. |
| Compression or lens-backed accounting | Lost source distinction, observer-budget dependency, or C.29 stop-condition breach. |
| Bespoke-residue reduction | Reduced resilience, local-fit loss, or new hidden coupling. |

A conforming RSA move states the reusable locus, the bespoke or residual locus, the accounting basis, the first repair direction, and the first cost, loss, or source-return condition that can make the move inadmissible.

#### C.31.RSA:4.6 - Triage and accounting use boundary

A qualitative account can be sufficient when the practitioner needs to locate reuse, residue and the next warranted repair. Use the triage form if it helps retain that answer.

Develop the accounting rule and structure references when the question depends on a numeric share, comparison of aspects or distinctions hidden by summarization. The fuller description can organize that content. Preserve source-return conditions when they change use. Publication of an adequate account does not require a new form; assurance, scale preference and decisions need the additional grounds of their own claims.

#### C.31.RSA:4.7 - Reopen and lowering conditions

An RSA result retains its declared scope, structure edition and accounting basis, together with source-return and comparator conditions on which its use actually depends. Reopen the triage or lower the admissible use when any of the following changes:

- a hidden source distinction becomes action-relevant;
- the accounting basis changes or proves heterogeneous;
- the selected structure, structural aspect, interface grammar, evidence package, work method, or assurance argument changes edition;
- a comparator set, CG-Spec, or outside-RSA use is added after a report-only share was recorded;
- downstream reliance uses the RSA result for outside-RSA evidence, assurance, gate, causal-use, scale-preference, or decision work that the RSA note did not admit;
- evidence validity, assurance window, or source-return condition decays;
- recurrence changes a bounded exception's cost, conditions or justification;
- a reuse move improves one locus while worsening interface cost, variation loss, evidence decay, assurance work, source-return cost, or hidden bespoke residue.

Block the dependent comparison or ranking when its required comparator or aligned basis is missing; preserve a valid bounded report. For another gate or decision, recover the particular missing premise under its own rule. If the accounting basis is unknown, retain only the qualitative or source-only meaning actually supported. If reuse and residue cannot be distinguished at one locus, mark that part unresolved while preserving independently established parts.

### C.31.RSA:5 - Archetypal Grounding

**Tell.** Account for structure at declared loci under a declared accounting basis.

**Show.** In one architecture, reusable structure may be located in a template and interface grammar. In another, it may be located in a test package, regulatory argument, work method, or flow pattern. In a third, the reusable part may be small, but the bounded exception is exactly what preserves safety or local fit.

**Show.** A share can be useful as a local report. It becomes misleading when it hides which structure was counted, which structure was not counted, and when the reader must return to source records.

Holon and episteme: the structures being accounted over are selected architecture-relevant structures in context. The RSA description describes those structures; it records the local accounting slots, report-only share values, and any source-return condition.

#### C.31.RSA:5.1 - Worked case: reusable evidence package, bespoke delivery work

Situation:

```text
A regulated product line has reusable component templates and a reusable test package.
Each customer delivery still repeats approval work and bespoke integration exceptions.
```

`ReusableStructureTriage`:

```text
describedHolonRef: product-line delivery system
reuseQuestion: which selected structures are reused and where does bespoke residue grow?
deploymentBoundary: regulated customer deployments
intendedAccountingUse: decide the next reusable-structure repair
claimScopeRef: reusable-structure accounting for regulated delivery
qualificationWindowRef: 2026Q3 regulated-delivery review window
architectureClaimRef: C.30 architecture claim for the product-line delivery system and its selected delivery structures
structureRefs:
  component template structure
  interface grammar structure
  evidence package structure
  delivery work structure
accountingRelationRefs:
  reuse, exception, and bespoke-residue relations for the named deployments
evidenceRefs:
  deployment, approval, integration-exception, and reusable-test-package records
whereReusableStructureCurrentlyLives:
  component template structure
  reusable test package
  interface grammar for standard variants
whereBespokeResidueCurrentlyGrows:
  customer-specific approval work
  integration exceptions outside interface grammar
  local evidence witnesses not covered by reusable package
residueRefactoredInto:
  workStructure + evidencePackage + interfaceSpecification
residueAcceptedAsBoundedException:
  customer-specific regulatory clause with declared non-admissible reuse
sourceReturnCondition:
  return to deployment evidence and regulatory exception record before assurance or gate use
relatedClaimPatternsIfClaimed:
  `A.10` for the evidence-validity claim's source-to-use basis; `G.6` when a citable provenance path is needed; `B.3` for assurance reliance; `A.6.M` for interface grammar when a module-interface claim is made; `C.16` for the measurement account; `A.19.CPM` for comparison under a declared comparator
stopCondition:
  report-only accounting; establish comparison, evidence-validity or assurance grounds when that particular further use is made
```

Admissible move: publish the local report-only RSA note and refactor the repeated organization of delivery approval work into reusable work structure and reusable evidence structure. Non-admissible move: claim that the reusable evidence package proves every deployment or that a high reusable share makes the architecture better.

#### C.31.RSA:5.2 - Anti-case: high share hides a bad architecture move

Situation:

```text
A team reports that 85 percent of its architecture is reusable because most screens use one shared template.
The template makes many local exceptions necessary for product teams and side-channel integrations.
```

This is not a successful RSA result. The accounting basis counts template instances but hides interface relation cost, lost variation, hidden bespoke work, and evidence decay. The repair is to mark the share as report-only, add the missing bespoke-residue slots, and apply A.6.M, C.31, or a characteristic pattern governing the claim to the interface relation cost before any comparison or decision use.

Lowering replay: the team tries to use the 85 percent share to rank this template architecture above another product-line variant and approve the template program. The use is lowered to local report-only accounting because the comparator set, accounting-basis alignment, interface-cost measure, source-return condition, and decision record are absent. Recover the interface claim and actual costs, using A.6.M for unresolved module-interface meaning and C.16 for the cost measurement. A.19.CPM governs comparison of admitted profiles; A.19 applies to a CharacteristicSpace or reusable space predicate when one is used, and C.11 to local choice. These grounds can support comparison of the existing variants before any interface is changed. A chosen repair changes the candidate and reopens the affected accounting and comparison.

Stop condition: do not use the 85 percent share for outside-RSA ranking, gate, assurance, or decision. Reopen the RSA note when the interface grammar, exception register, or comparator set changes.

#### C.31.RSA:5.3 - Transfer case: neural-network block replacement

Situation:

```text
A model architecture replaces a repeated attention block with a hybrid SSM-attention block.
The benchmark improves, but cache placement, memory access, and ablation evidence change.
```

RSA can transfer from product-line architecture to neural-network architecture only after `C.30.STRAT` has treated `block`, `cache`, and related terms as source labels unless the reusable locus is already recovered. Then RSA names the declared structures and accounting basis:

- reusable structure may be located in recovered repeated-block topology, dataflow pattern, cache-placement rule, or evaluation harness;
- bespoke residue may be located in model-specific tuning, data distribution dependence, memory-layout exception, or ablation gap;
- benchmark gain is not reusable-structure accounting by itself;
- for evidence claims, use `A.10` for source recovery and bounded reliance, and `G.6` when a citable provenance path is needed; use `C.28` for causal claims and `C.29` for mathematical-lens or compression claims.

Admissible move: record which recovered structural locus was reused, what changed, what source distinctions must remain reachable, and which pattern defines or tests each benchmark, evidence, causal-use, or mathematical-lens claim. Non-admissible move: treat "block replacement improved the architecture" as RSA proof.

### C.31.RSA:6 - Bias-Annotation

| Bias risk | C.31.RSA repair |
| --- | --- |
| Reuse-good bias | Do not treat more reusable structure as automatically better. Ask what repair, cost, or source-return condition follows. |
| Share-proof bias | Do not let `ReusableStructureShare` prove modularity, quality, or any outside-RSA use named in the claim-use boundary. |
| Hidden-unit bias | Do not sum templates, interface variants, work items, and evidence packages without a declared accounting basis. |
| Residue-bad bias | Do not treat every bespoke exception as waste. Some residue is a bounded exception that preserves local fit or safety. |
| Evidence-reuse bias | Do not count evidence reuse without validity context and source-return condition. |
| Compression bias | Do not let accounting hide distinctions needed for action, assurance, causal use, law-domain review, regulatory review, or subsequent decision reopening. |

### C.31.RSA:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| `CC-C31.RSA-1` | The account identifies reusable and bespoke loci and the intended use. Reuse an adequate account; triage and full-description forms are optional. |
| `CC-C31.RSA-2` | An accounting description identifies its structures, aspects, accounting rule, reuse, residue and relevant uncertainty. It states the bounded use and any action-changing restriction. Numeric shares retain the counting and scale basis in section 4.3. |
| `CC-C31.RSA-3` | Report-only shares are marked report-only unless every outside-RSA use being made and named in the claim-use boundary meets the conditions defined by its applicable pattern. |
| `CC-C31.RSA-4` | No text treats RSA as proof of modularity, quality, or any outside-RSA use named in the claim-use boundary. |
| `CC-C31.RSA-5` | Heterogeneous slot labels are not summed unless a declared accounting basis and aggregation rule make the operation admissible. |
| `CC-C31.RSA-6` | Each bespoke residue interpretation states a repair direction, bounded-exception condition, source-return condition, or governing-pattern application. |
| `CC-C31.RSA-7` | For an evidence-validity claim, use `A.10` to recover its source-to-use basis and `G.6` when a citable provenance path is needed; use `B.3` for an assurance claim, including one about safety-case support. |
| `CC-C31.RSA-8` | RSA does not duplicate the C.31 characteristic taxonomy; it uses C.31 only when a modularity characteristic under evaluation, such as bespoke residue, evidence reuse, or residual uncertainty, must govern the accounting interpretation. |
| `CC-C31.RSA-9` | Source-return condition is present when accounting hides action-relevant source distinctions. |
| `CC-C31.RSA-10` | Comparison or ranking uses aligned accounting bases and the applicable comparator. A gate or decision requires that comparator only when its own rule relies on the comparison; other missing grounds block only the dependent use. |
| `CC-C31.RSA-11` | The RSA note names reopen or lowering conditions for source distinction change, accounting-basis change, structure-edition change, implicit-interface change, comparator change, evidence or assurance decay, downstream reliance, repeated bounded exception, and reuse move side effects when those conditions are needed for the record. |
| `CC-C31.RSA-12` | Preserve clear source meanings; use C.30.STRAT when unresolved stratification or structure meaning changes the accounting use. |

### C.31.RSA:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| `ArchitectureAmount` | A reusable share is treated as an amount of architecture. | Restate as report-only share under one declared accounting basis. |
| `ResidueIsWaste` | All bespoke residue is marked bad. | Split repairable residue from bounded exception. |
| `HeterogeneousPseudoSum` | Templates, interface variants, work items, evidence packages, and exceptions are summed as if they shared one unit. | Declare accounting basis or keep the decomposition qualitative. |
| `EvidenceReuseAsAssurance` | Evidence reuse share is treated as assurance. | Recover the evidence-validity claim's source-to-use basis through A.10; use G.6 for a citable provenance path when needed and B.3 for assurance reliance. |
| `RSAAsC31Duplicate` | RSA repeats every modularity characteristic. | Keep RSA to reusable loci, bespoke residue, residual uncertainty, report-only shares, and source-return conditions. |
| `NoSourceReturn` | Accounting hides source distinctions used by downstream action. | Add `sourceReturnCondition` or narrow admissible use. |

### C.31.RSA:9 - Consequences

Benefits:

- Reusable structure and bespoke residue become visible without a false architecture amount.
- Practitioners get a cheap triage before accounting.
- Report-only shares can guide repair without becoming proof.
- Evidence reuse, work repeatability, interface grammar, and bounded exceptions can be separated instead of averaged.

Costs:

- Some attractive reuse reports remain report-only.
- Numeric shares require an explicit counting and scale basis. Comparison needs aligned bases and its comparator; each further claim adds only its own required grounds.
- The pattern raises a source-return question whenever accounting hides distinctions needed by downstream action.

### C.31.RSA:10 - Rationale

C.31.RSA is separate from C.31 because accounting over reusable structure answers a different question from choosing modularity characteristics. C.31 asks which characteristic changes action. C.31.RSA asks where reusable structure and bespoke residue are located under a declared accounting basis.

C.30 distinguishes an architecture relation from its selected structure. RSA does not define `StructureAmount`. A useful accounting description can still report shares, but only under declared structure refs, structural aspects, and an accounting basis.

The pattern also keeps residue ethically and practically neutral until interpreted. Bespoke residue can be a defect, a local necessity, a safety boundary, a regulatory constraint, or a deliberately accepted exception. The repair is to name which one.

### C.31.RSA:11 - SoTA-Echoing

| Source or practice | Currentness or lineage use | Adopt and adapt for C.31.RSA | Rejected overread | Governing-pattern use and action consequence |
| --- | --- | --- | --- | --- |
| C.25 Q-Bundle discipline inside FPF | FPF-local discipline for decomposing quality-family claims. | Adopt separation of scope, measures, mechanisms, windows, evidence, and admissible use. In C.31.RSA this changes `ReusableStructureShare`: the share is report-only accounting under declared `accountingBasisRef` until the relevant outside-RSA use meets the conditions defined by its applicable pattern. | A reusable-structure share does not replace the underlying Q-Bundle, description, evidence relation, or decision record. | Apply `C.25` for quality-family decomposition and `C.16` for a measurement account; the practitioner may report a share locally but must not use it as proof without the governing pattern for that use. |
| ISO/IEC/IEEE 42010:2022 architecture-description, viewpoint, model-kind, and correspondence discipline (`https://www.iso.org/standard/74393.html`; `https://www.iso-architecture.org/ieee-1471/cm/`) | The 2022 international standard and conceptual-model source for architecture-description and view discipline. | Adopt explicit architecture description, source view, viewpoint, model-kind, correspondence, and conformance pressure. In C.31.RSA this changes source-return use: reusable-structure accounting names the structure refs, source view or architecture-description refs, correspondence refs, and source-return condition before any cross-view share is used. | A view, diagram, model kind, or correspondence label is not the reusable structure itself and does not make a share comparable, admissible for decision use, or assurance-bearing. | Apply `C.30` for architecture claims, `C.30.AD` for architecture-description use, `C.30.ASV` for structural-view use, and `E.17.0` for viewpoint conformance; RSA may count only after the selected structure refs and accounting basis are recoverable. |
| Modular Open Systems Approach (MOSA) and open-system acquisition or engineering practice (`https://www.cto.mil/sea/mosa/`; `https://www.cto.mil/wp-content/uploads/2025/03/MOSA-Implementation-Guidebook-27Feb2025-Cleared.pdf`) | Engineering and acquisition practice family for modular interfaces, conformance, replacement, and supplier-diversity pressure. | Adopt the pressure to make reusable interface, conformance, substitution, and supplier-diversity structure explicit. In C.31.RSA this changes interface reuse: a claim about reusable interfaces needs the interface grammar, substitution and version conditions on which it relies. Use A.6.M for unresolved module-interface meaning; establish actual conformance and relied-on source or evidence relations under their direct rules. The supplier-diversity relation likewise needs its direct predicate when that relation is being claimed. | Open interface label, API label, platform label, or supplier-diversity goal is not reusable structure, procurement suitability, assurance, gate passage, or decision authority by itself. | Use A.6.M when the module-interface claim still needs recovery of interface grammar, substitution, version or change conditions, or conformance expectations; keep source or evidence relations and any claimed supplier-diversity relation under their direct patterns before RSA comparison or decision use. Use `G.5` for supplier-set result declaration or `C.11` for a procurement decision when that use is being made. |
| DSM, dependency, and product-architecture practice, including Eppinger and Browning DSM lineage | Architecture-analysis lineage for dependency and product-architecture reasoning, not a complete standard. | Adopt typed dependency structures as possible source for reusable loci and bespoke-residue diagnosis. In C.31.RSA this changes dependency use: dependency counts, partitions, and clusters become candidate source fields only when declared `structureRefs`, structural aspects, and accounting basis are present. | Dependency count, cluster count, or DSM modularity score is not architecture amount, quality proof, or decision verdict. | Apply `C.31` to select modularity characteristics, `C.16` when the count or other result must be interpreted as a measurement, and `A.18` for scale-operation legality; apply `C.29` when a mathematical graph, partition or compression lens is actually used. |
| Goodhart and Campbell proxy-pressure laws | General proxy-risk lineage for report-only shares, reuse scores, and benchmark-like accounting. | Adopt proxy-risk discipline for reusable-share use. In C.31.RSA this changes share use: a reusable-structure share remains report-only until the relevant outside-RSA use meets the conditions defined by its applicable pattern. | Reusable-share improvement, coverage improvement, or benchmark improvement is not value, assurance, evidence sufficiency, gate passage, or architecture decision by itself. | Before a reuse number guides selection or reliance, apply the corresponding measurement, quality-family, set-result, decision, evidence, or assurance pattern identified in section 12. |
| System-evolution, information-hiding, and effective-interface lineage | General holon-architecture lineage for reusable structure that changes over time and hides variation-prone structure. | Adopt evolution and hidden-change discipline. In C.31.RSA this changes residue interpretation: reusable loci, bespoke residue, hidden interface behavior, source-return conditions, and bounded exceptions are reopened when the structure edition, accounting rule, implicit interface, or reliance relation changes. | One-time reusable-share accounting is not sustainable fitness; a stable-looking interface or template does not prove future substitutability. | Reopen or lower the RSA result when hidden variation, implicit dependency, source distinction, or continuing adaptation changes the accounting meaning. |
| Software product-line engineering and variability-management practice, including Pohl, Boeckle, and van der Linden lineage plus product-line and variability work (`https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`) | Product-line variability lineage plus SPLE-review cues for variability slots, product-line reuse, platform extension rules, and reuse-rule discipline. | Adopt variability-slot and reuse-rule pressure. In C.31.RSA this changes product-line use: reusable structure may be located in template, interface, work, evidence, and exception loci, and bespoke residue must name repair direction, bounded exception, or source-return condition instead of being averaged into one share. | Product-line label, shared code base, feature model, or platform name is not enough to infer reusable structure or architecture scale-preference evidence. | Apply A.6.M when platform or interface wording carries a module-interface claim, C.31.ASAP for architecture scale preference, C.11 for choice, or G.5 for selected-set result declaration. |
| GSN Community Standard v3 and assurance-case reuse and safety-case reuse practice (`https://scsc.uk/gsn`; `https://arxiv.org/abs/2506.11023`) | The named assurance-case standard and formalization work; assurance validity remains context-sensitive. | Adopt the distinction between reusable assurance argument structure, reusable evidence structure, and context-specific validity witnesses. In C.31.RSA this changes evidence and assurance reuse: reuse remains accounting until evidence validity, safety-case use, or assurance reliance is governed by its own pattern. | Evidence reuse share or assurance-argument template reuse does not infer assurance, safety-case success, gate passage, or release permission. | Use `A.10` for the evidence-validity claim's source-to-use basis, `G.6` for a citable provenance path when needed, and `B.3` for an assurance claim, including one about safety-case support; add source-return condition and validity-window check before reliance. |
| Architecture-operation language, with neural-network and software-system discussions as source examples, including the GonzoML architecture-operation intake | Practitioner-language source for structural substitution, gating, memory placement, cache placement, routing, ablation, pruning, distillation, and architecture search; not used as a current standard by itself. | Adopt the recognition that replacement and search expose reusable and bespoke structural loci. In C.31.RSA this changes architecture-operation use: recover the structures, aspects and accounting basis actually used, preserving clear local meanings of block, layer, expert, cache, router, gate or pruning mask. Use C.30.STRAT only for a remaining meaning problem. | Block, layer, expert, cache, router, gate, benchmark, ablation, pruning mask, or distillation success is not RSA slot ontology, architecture decision, evidence sufficiency, gate passage, assurance, or architecture adequacy by itself. | Apply `C.30.STRAT` first where source-label recovery is needed, then `C.30` or `C.30.ASV` for architecture claim and structural view, `C.30.TFS-REL` for flow changes, `C.29` for mathematical-lens or compression claims, `A.10` or `G.6` for the evidence-provenance account of a benchmark or evidence claim, and `C.28` for causal claims. |

**Source use and refresh.** Preserve each adopted contribution's scope and assumptions. A dated standard or historical method can support a claim within those conditions; a claim about present requirements or comparative standing needs the applicable current basis. A source row supplies neither actual conformance nor the evidence-validity, assurance or decision grounds of a particular reuse.

Reopen the affected RSA use when a changed source or rule alters its reusable locus, residue, accounting basis, source-return condition or relied-on comparison. For example, a new evidence-validity window can limit reuse of a test package without erasing the count of earlier uses. Preserve unaffected historical accounts, and recover new grounds before stronger reliance.

### C.31.RSA:12 - Relations

| Pattern | Relation |
| --- | --- |
| `C.30.STRAT` | Recovers unresolved stratification or structure meanings when they change the reusable locus, residue, accounting basis or next action. |
| `C.31` | Supplies modularity characteristics under evaluation; RSA does not duplicate the characteristic taxonomy. |
| `A.6.M` | Supplies module-interface claim repair when reusable interface or platform-grammar wording carries such a claim. |
| `C.30`, `C.30.AD`, and `C.30.ASV` | Supply architecture-claim, architecture-description-use, and structural-view context, respectively, for the structures being accounted over. |
| `C.16`, `A.17`, `A.18`, `A.19`, `A.19.CPM` | When RSA shares are used beyond report-only, use C.16 for measurement construction, A.17 for Characteristics, A.18 for scale, unit, and operation legality, including any score used; A.19 for a CharacteristicSpace or reusable space predicate when current; and A.19.CPM for comparison of admitted profiles under a declared comparator. |
| `C.25` | Governs broader quality-family bundles when reusable structure is used in a quality claim. |
| `A.10`, `B.3`, `G.6` | A.10 recovers sources and bounded reliance; G.6 makes an established provenance path citable; B.3 governs assurance claims, including claims about safety-case support. |
| `C.29` | Governs compression, epiplexity, RG, or other mathematical-lens claims when accounting depends on a lens. |
| `C.27`, `C.28`, `C.31.ASAP`, `C.18.1`, `C.19.1` | For claims arising from residue growth or reuse movement, use C.27 for temporal-claim adequacy, C.28 for causal use, C.31.ASAP for architecture alternatives under a declared scale variable and window, C.18.1 for scaling-law lens binding, and C.19.1 for scale-based preference or declared generality policy; a generality preference for architecture structure remains a declared local analogy or policy. |
| `C.32.P2S` | RSA rows may supply reusable structure, bespoke residue, evidence reuse, or source-return pressure to an architecturing flow. Candidate synthesis, selected-set result declaration, and architecture decisions remain outside RSA. |
| `G.5`, `E.17`, `E.24.PUB`, `C.11` | Use `G.5` for selected-set result declaration, `E.17` for a source-backed publication face and source return, `E.24.PUB` for the publication occurrence and audience availability, and `C.11` for local decision. Candidate synthesis stays with `C.32`; RSA defines or tests none of these uses. |

### C.31.RSA:End
