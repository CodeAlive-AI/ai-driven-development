## A.2.4 - Episteme Evidence-Use and Status-Use Relations

> **Type:** Boundary and relation-use pattern
> **Status:** Stable
> **Normativity:** Normative

### A.2.4:1 - Problem Frame

Use this pattern when a report, proof, dataset, measurement file, standard, requirement, dashboard cell, model card, publication face, generated explanation, or other `U.Episteme` is being used as evidence, source, status bearer, assurance input, or causal-use input for a claim.

Use it when the working question is:

* which episteme is being used;
* which claim, theory statement, status assertion, use, or causal-use question the episteme is being used for;
* which bounded context, claim scope, grounding holon, polarity, relevance window, assurance use, weight model, and provenance constraints are current;
* whether source wording such as "evidence role", "status role", "standard role", or "the report plays a role" hides an evidence-use, status-use, source-use, publication-use, assurance-use, gate-use, or causal-use relation;
* whether the evidence-use or status-use relation is sufficiently specified for the intended reliance, or only enough for orientation, source-finding, a reversible probe, or a narrowed use.

**Primary EntityOfConcern.** The `EntityOfConcern` is the evidence-use relation or status-use relation around an episteme. It is not `U.Role`, not `U.RoleAssignment`, and not a system performing work.

**First useful move.** Name the episteme, the bounded context, the claim or status being addressed, and the direct governing pattern that owns the use: usually `A.10`, `B.3`, `C.2.1`, `C.28`, `F.10`, `G.6`, `E.17`, `E.10.D2`, or a direct gate, source, requirement, definition, explanation, or publication-use pattern.

**What goes wrong if missed.** A document starts acting like an agent, a dataset is treated as if it held a work-facing role, a dashboard status becomes permission, a proof becomes global evidence without a theory fence, or a simulation-only counterfactual output is relabelled as realized causal evidence.

**What this buys.** The project can use epistemes as evidence, status bearers, sources, standards, requirements, definitions, explanations, publications, or assurance inputs without creating a second role ontology for epistemes and without losing claim scope, polarity, freshness, provenance, or assurance-use distinctions.

**Not this pattern when.** If the current claim is a system or acting holon holding a work-facing role, use `A.2` and `A.2.1`. If the current claim is performed work, use `A.15.1`. If the current claim is the full evidence-provenance graph relation, use `A.10`. If the current claim is assurance, use `B.3`. If the current claim is causal use, use `C.28`. If the current claim is a status family or status mapping, use `F.10`. If the current claim is publication-use or source-use, use `E.17` and `E.10.D2` as needed.

### A.2.4:2 - Problem

Source text may name `U.EvidenceRole` or evidence-like role labels for a real need: an episteme can be used as evidence for a claim inside a bounded context, with scope, polarity, time, assurance use, weight, and provenance constraints. The FPF repair is to model that use as an evidence-use relation, not as a non-behavioral role held by the episteme through `U.RoleAssignment`.

That creates several failures:

1. **Episteme-as-holder drift.** A paper, proof, dataset, standard, or dashboard cell is treated as if it held a work-facing role.
2. **Evidence role ontology drift.** `ModelFitEvidenceRole`, `MeasurementEvidenceRole`, or `AxiomaticProofRole` look like role kinds instead of evidence-use relation classifications or local evidence-use labels.
3. **Claim relation collapse.** Target claim, grounding holon, claim scope, polarity, relevance window, assurance use, weight model, and provenance constraints are hidden behind one role name.
4. **Evidence and status collapse.** A status badge, standard reference, approval-looking display, publication face, or requirement source is treated as evidence, status assertion, gate passage, permission, and assurance at once.
5. **Work confusion.** The work that produced an episteme and the later use of that episteme as evidence are folded into one relation.
6. **Causal-use laundering.** Observational association, intervention, realized counterfactual sample, identified counterfactual estimate, and simulation-only output are relabelled by evidence-wording instead of being governed by `C.28`.
7. **Cross-context leakage.** Evidence accepted in one context is reused in another without an explicit bridge, source-currentness relation, or assurance-use statement.

### A.2.4:3 - Forces

| Force | Tension this pattern resolves |
| --- | --- |
| Episteme identity versus episteme use | The same episteme can be used for several claims without becoming several epistemes or several role-assignment holders. |
| Compact evidence statement versus full evidence graph | Users need a small evidence-use statement first; `A.10` still owns full evidence-provenance graph detail. |
| Formal proof versus empirical evidence | A proof can be stable inside one theory version; empirical evidence usually needs relevance windows, freshness, and provenance constraints. |
| Status display versus status assertion | A visible badge, cell, or label can cue status but does not by itself create permission, gate passage, assurance, or work evidence. |
| Local acceptance versus cross-context reuse | Evidence and status use are context-bound; reuse needs bridge, source-currentness, publication-use, or assurance-use relations. |
| Causal evidence classes versus ordinary evidence relation | Causal-use evidence classes need `C.28`; A.2.4 only keeps the evidence-use relation from becoming a role assignment. |

### A.2.4:4 - Solution

Do not create or use `U.EvidenceRole` as a durable role kind. Do not place an episteme in `U.RoleAssignment` merely because it is used as evidence, source, standard, requirement, definition, explanation, publication, status bearer, or assurance input.

Use direct relation patterns instead:

| Current claim | Use |
| --- | --- |
| one episteme is used as evidence for one claim, effect, or bounded reliance use | `A.10`, with the A.2.4 evidence-use SlotKinds below |
| evidence use contributes to assurance, trust, readiness, compliance, safety, release confidence, `F`, `G`, `R`, or `CL` | `B.3`, consuming A.10 evidence-use relations |
| the episteme itself is being identified, versioned, or distinguished from publication faces and publication carriers | `C.2.1` |
| the use is causal, counterfactual, intervention-facing, or simulation-only | `C.28`, with A.10 evidence-provenance graph relation and the A.2.4 evidence-use relation as input |
| the source says "status", "approved", "current", "valid", "stale", "ready", or another status-like value | `F.10`, A.10, B.3, a gate pattern, or a direct status pattern |
| the source is a publication face, view, description, source citation, standard, requirement, explanation, or specification-use case | `E.17`, `E.17.0`, `E.17.2`, `E.17.EFP`, `E.10.D2`, or the direct source-use pattern |
| a system, person, team, organization, or acting holon holds a role and performs or prepares work | `A.2`, `A.2.1`, `A.15`, `A.15.1`, or `A.15.2` |

#### A.2.4:4.1 - Evidence-Use Relation Slots

An evidence-use relation is a relation around an episteme and a claim or effect. It is not a role assignment.

| SlotKind | ValueKind | Identity and currentness discipline |
| --- | --- | --- |
| `EvidenceEpistemeSlot` | `U.Episteme` used as evidence | Identity slot for the evidence-use relation. |
| `EvidenceTargetClaimSlot` | claim or theory statement | Identity slot whenever the relation is claim-bound; a missing value blocks claim-bound evidence use. |
| `EvidenceClaimGroundingHolonSlot` | `U.Holon` grounding the target claim, mirroring C.2.1 `GroundingHolonSlot` | Identity or currentness-required when changing the grounding holon changes the evidence relation or the claim being evidenced. |
| `EvidenceClaimScopeSlot` | claim-scope value governed by `B.3`, `A.10`, `C.28`, or a direct evidence pattern | Identity qualifier when changing scope changes the relation; currentness-required when scope changes admissible use. |
| `EvidencePolaritySlot` | evidential polarity value such as supports, refutes, constrains, or neutral when that value set is current | Identity qualifier when changing polarity changes which evidence-use relation is asserted. |
| `EvidenceRelevanceWindowSlot` | temporal relevance window, theory-version fence, freshness policy, or decay policy | Identity or currentness-required when time, version, or freshness changes the evidence use; consideration slot for formal uses where the theory-version fence already carries the boundary. |
| `EvidenceAssuranceUseSlot` | typing, verification, validation, reliance, gate, release, or another assurance-use value governed by `B.3`, `A.10`, or a direct pattern | Identity qualifier only when changing assurance use changes the relation; currentness-required for reliance-bearing use. |
| `EvidenceWeightModelSlot` | weight, confidence, reliability, likelihood, or scoring model reference | Consideration slot; currentness-required when weighted evidence is claimed. |
| `EvidenceProvenanceConstraintSlot` | provenance constraints over external work, source, publication, method description, proof check, measurement, publication carrier, or evidence-provenance graph relation | Currentness-required when provenance decides admissible use or a rival explanation. |

These SlotKinds are evidence-use relation positions. They are not work-role qualifier slots, not `U.Role` names, and not new U-kinds by themselves.

#### A.2.4:4.2 - Status-Use Relation Slots

A status-use relation is a relation around a bearer, status value, scope, window, source, and use. It is not a status role held by an episteme.

| SlotKind | ValueKind | Use |
| --- | --- | --- |
| `StatusBearerSlot` | episteme, claim, method description, publication, role assignment, work occurrence, clause, gate record, or another governed bearer admitted by the direct pattern | The value whose status is being asserted or read. |
| `StatusTargetSlot` | claim, method, episteme, publication, work result, clause, bearer, or another governed status target | Required when the status is not simply about the bearer itself. |
| `StatusScopeSlot` | bounded-context scope, claim scope, admission scope, requirement scope, or use scope | Currentness-required when scope changes the status assertion. |
| `StatusValueSlot` | status value governed by `F.10` or a direct pattern | Required for a status assertion. |
| `StatusWindowSlot` | temporal validity window, freshness policy, status-currentness relation, or source-currentness relation | Currentness-required for time-sensitive status. |
| `StatusUseSlot` | gate use, assurance use, admission use, source-currentness use, work-plan readiness use, or another direct use | Required when the status is consumed for that use. |
| `StatusProvenanceConstraintSlot` | source order, authority source, publication, proof, verification, register, or provenance constraint | Currentness-required when provenance decides status use. |

These names do not create a generic status ontic. They are repair vocabulary for status-use relations in the current role and relation-slot settlement. Durable status families remain governed by `F.10` or a direct status pattern.

#### A.2.4:4.3 - Minimal Evidence-Use Statement

For ordinary use, write only the fields needed for the current reliance question:

```text
Episteme evidence-use statement:
  EvidenceEpisteme:
  BoundedContext:
  EvidenceTargetClaim:
  EvidenceClaimGroundingHolon:
  EvidenceClaimScope:
  EvidencePolarity:
  EvidenceRelevanceWindow:
  EvidenceAssuranceUse:
  EvidenceWeightModel:
  EvidenceProvenanceConstraint:
  DirectGoverningPattern:
  UnsupportedOverread:
```

`UnsupportedOverread` names the stronger claim not carried by this relation, such as approval, permission, gate passage, performed work, assurance, causal identification, release confidence, or global truth.

#### A.2.4:4.4 - Minimal Status-Use Statement

For status-like cases, write the smallest relation that keeps status from becoming role assignment, gate passage, or assurance by display alone:

```text
Episteme status-use statement:
  StatusBearer:
  StatusTarget:
  StatusScope:
  StatusValue:
  StatusWindow:
  StatusUse:
  StatusProvenanceConstraint:
  DirectGoverningPattern:
  UnsupportedOverread:
```

If the status is used for a gate, release, work-plan readiness, assurance, or admission decision, apply the direct governing pattern for that use. A.2.4 only keeps the status-use relation typed and prevents role-holder grammar from returning where an episteme-use relation is needed.

#### A.2.4:4.5 - Formal, Empirical, and Causal Evidence Uses

Source labels such as `AxiomaticProofRole`, `ObservationEvidenceRole`, `MeasurementEvidenceRole`, `ModelFitEvidenceRole`, `ReplicationEvidenceRole`, `CalibrationEvidenceRole`, and `BenchmarkEvidenceRole` become evidence-use classifications or local evidence-use labels, not `U.Role` values.

Formal line:

* the evidence episteme is a proof, derivation, counterexample, theory note, proof-check result, or formal publication;
* `EvidenceTargetClaimSlot` names the theorem or theory statement;
* `EvidenceClaimScopeSlot` names the theory domain or declared scope;
* `EvidenceRelevanceWindowSlot` usually names a theory-version fence rather than an empirical expiry date;
* `EvidenceProvenanceConstraintSlot` names proof checks, source publications, theory version, and dependency conditions when current.

Empirical line:

* the evidence episteme is a dataset, observation record, measurement report, replication report, calibration result, benchmark result, model-fit report, or similar episteme;
* `EvidenceClaimScopeSlot`, `EvidenceRelevanceWindowSlot`, `EvidenceWeightModelSlot`, and `EvidenceProvenanceConstraintSlot` usually decide whether the use is admissible;
* the producing work remains `U.Work` under `A.15.1`, performed by a system or acting holon under `U.RoleAssignment` where that trace is current.

Causal-use line:

* the causal-use question belongs to `C.28`;
* A.2.4 keeps the evidence-use relation typed so the episteme is not relabelled by vocabulary alone;
* exact `C.28` values such as `observationalAssociationSupportBasis`, `interventionalActionSupportBasis`, `realizedCounterfactualSampleSupportBasis`, `identifiedCounterfactualEstimateSupportBasis`, and `simulationOnlyCounterfactualOutputBasis` remain `C.28` values, not role names.

#### A.2.4:4.6 - Work, Source, and Publication Boundary

The producing work and the later evidence use are different relations.

* A lab run, proof-checking session, calibration run, benchmark run, review, model evaluation, or data extraction can be `U.Work`.
* The report, proof file, dataset, benchmark table, or publication produced by that work can be a `U.Episteme`.
* A later project can use that episteme as evidence through an evidence-use relation.
* A publication face, view, source citation, credential view, dashboard display, or generated explanation can cue evidence or status use, but it does not become the evidence-use relation by itself.

When the source-currentness, publication-use, view, explanation, or specification-use question is current, use `E.17`, `E.17.0`, `E.17.2`, `E.17.EFP`, `E.10.D2`, `A.10`, or the direct source-use pattern before relying on the evidence-use or status-use relation.

#### A.2.4:4.7 - Shortcut Cost and Reopen Condition

The baseline is the direct governing pattern: full `A.10` for evidence-provenance graph relations, full `B.3` for assurance, full `C.28` for causal use, full `F.10` for status families, full `E.17` or `E.10.D2` for publication-use and description-use cases, and full `A.15.1` when the producing work is current.

A.2.4 is the weaker first-use representation. It saves effort by writing only the relation positions needed to stop role-like source wording from collapsing evidence, status, work, assurance, source, and publication claims. The loss budget is narrow: A.2.4 may name the evidence-use or status-use relation, preserve the named direct governing pattern, and state unsupported overread. It may not decide assurance value, gate passage, causal identification, source-currentness order, publication interpretation, or performed-work truth.

Open the direct governing pattern when the attempted use depends on assurance, safety, release, compliance, causal effect, gate decision, permission, performed work, source freshness, publication use, status currentness, or a contested provenance relation.

### A.2.4:5 - Archetypal Grounding

#### A.2.4:5.1 - Proof Used as Evidence

`Lemma-12.proof` is an episteme used as evidence for `Theorem-12` in `GraphTheory_v3.1`.

The evidence-use relation names:

* `EvidenceEpistemeSlot = Lemma-12.proof`;
* `EvidenceTargetClaimSlot = Theorem-12`;
* `EvidenceClaimScopeSlot = finite DAGs inside GraphTheory_v3.1`;
* `EvidencePolaritySlot = supports` or an entailment-specific polarity when the local value set declares one;
* `EvidenceRelevanceWindowSlot = theory-version fence GraphTheory_v3.1`;
* `EvidenceAssuranceUseSlot = verification use`;
* `EvidenceProvenanceConstraintSlot = proof publication, proof-check result, dependency list, and theory version`.

No episteme holds `AxiomaticProofRole`. The proof episteme is used in a claim-bound evidence-use relation.

#### A.2.4:5.2 - Calibration Dataset Used as Evidence

`Trial-R3.csv` is an episteme used as evidence for `Sensor S accuracy +/-0.3 C in [0,70] C under lab conditions L`.

The evidence-use relation names the claim scope, polarity, relevance window, weight model, producing work runs, method description, measurement traceability, and freshness policy. If a later assurance claim is made, `B.3` consumes this relation. If the calibration run itself is being discussed, use `A.15.1` for the work occurrence.

#### A.2.4:5.3 - Dashboard Status Cell

A release dashboard shows `Ready`.

That visible cell can be:

* a status cue;
* a status assertion if the source, status value, scope, window, and provenance constraints are recoverable;
* evidence for a gate or release claim only when `A.10` and the gate pattern recover the source relation;
* no evidence-use relation if it is stale, copied, unauthenticated, or disconnected from the decision source.

It is not a status role held by the dashboard episteme.

#### A.2.4:5.4 - Standard Used as Requirement or Evidence

An ISO/IEC/IEEE standard clause can be an episteme used as a requirement source, definition source, status source, or evidence source depending on the current claim.

Do not write "the standard has a normative role" as live FPF ontology. Recover the relation governed by the current claim: standard-use, requirement-use, definition-use, source-use, evidence-use, status-use, or assurance-use.

#### A.2.4:5.5 - Simulation-Only Counterfactual Output

A simulation output mentions a counterfactual. That output may be an episteme used in an evidence-use relation. The causal-use class still belongs to `C.28`.

If the current `C.28` value is `simulationOnlyCounterfactualOutputBasis`, the evidence-use relation cannot be relabelled as `realizedCounterfactualSampleSupportBasis` or `interventionalActionSupportBasis` by evidence wording, validation wording, or role wording alone.

### A.2.4:6 - Bias-Annotation

This pattern mainly blocks six biases:

* **episteme-as-role-holder bias**: an episteme is placed in `U.RoleAssignment` because it is useful as evidence or status;
* **evidence-name-as-kind bias**: local evidence-use labels become `U.Role` names;
* **status-display-as-authority bias**: a visible badge or status cell becomes gate passage, permission, or assurance;
* **work-as-evidence-use collapse**: producing work, produced episteme, and later evidence use are treated as one relation;
* **scope-free evidence bias**: target claim, grounding holon, claim scope, polarity, time, assurance use, or provenance constraints are omitted;
* **causal laundering bias**: causal evidence classes are changed by source vocabulary rather than by `C.28` causal-use reasoning.

The repair is to recover the episteme first, then recover the evidence-use, status-use, source-use, publication-use, assurance-use, or causal-use relation that is current.

### A.2.4:7 - Conformance Checklist

| Check | Pass condition |
| --- | --- |
| `CC-A2.4-1` Episteme boundary | The evidence or status bearer is identified as `U.Episteme`, publication face, claim, status bearer, or another direct-pattern bearer; no episteme is placed in `U.RoleAssignment` merely because it is used. |
| `CC-A2.4-2` Target relation | Evidence use names the target claim or effect when claim-bound; status use names the status bearer, status value, and target when needed. |
| `CC-A2.4-3` Grounding and scope | Claim grounding holon, claim scope, status scope, or use scope is named when changing it would change the relation or admissible use. |
| `CC-A2.4-4` Polarity and value | Evidence polarity or status value is explicit when the use depends on it. |
| `CC-A2.4-5` Time and freshness | Relevance window, theory-version fence, freshness policy, status window, or source-currentness relation is explicit when the use is time-sensitive. |
| `CC-A2.4-6` Provenance | External producing work, source, publication, proof check, measurement, method description, register, or evidence-provenance relation is named when it decides admissible use. |
| `CC-A2.4-7` Assurance boundary | Assurance, readiness, safety, compliance, release confidence, trust, `F`, `G`, `R`, or `CL` claims go to `B.3`; A.2.4 only supplies typed evidence-use or status-use relation positions. |
| `CC-A2.4-8` Causal boundary | Causal-use and counterfactual claims go to `C.28`; A.2.4 does not mint causal evidence kinds. |
| `CC-A2.4-9` Work boundary | The producing work remains `U.Work`; the episteme use remains evidence-use or status-use. |
| `CC-A2.4-10` Publication boundary | Publication face, source citation, generated explanation, credential view, or dashboard display is not treated as evidence-use or status-use until the relation is recoverable. |
| `CC-A2.4-11` No evidence/status role ontology drift | Live prose does not teach `U.EvidenceRole`, status role for epistemes, episteme role holder, or evidence-role assignment through `U.RoleAssignment`. |
| `CC-A2.4-12` Direct governing pattern | The statement names the direct pattern that owns the current use: `A.10`, `B.3`, `C.2.1`, `C.28`, `F.10`, `G.6`, `E.17`, `E.10.D2`, or another governing pattern named by value. |

### A.2.4:8 - Common Anti-Patterns and How to Avoid Them

| Source wording | Failure | Repair |
| --- | --- | --- |
| "The report has EvidenceRole for Claim A." | Puts an episteme into role ontology. | Use an evidence-use relation with `EvidenceEpistemeSlot`, `EvidenceTargetClaimSlot`, scope, polarity, window, and provenance constraints when current. |
| "Dataset X proves safety." | Treats dataset presence as proof, assurance, and safety claim. | Use `A.10` for evidence, `B.3` for assurance or safety assurance, and name unsupported attempted use. |
| "The standard has normative role." | Role word hides standard-use, requirement-use, source-use, or publication-use. | Recover the relation governed by the current claim and apply `E.10.D2`, `E.17`, `F.10`, or the direct requirement pattern. |
| "The badge is current, so release is allowed." | Status display becomes gate passage or permission. | Use status-use relation plus gate or release governing pattern; dashboard display alone is not a decision. |
| "Simulation output is counterfactual evidence." | Simulation-only output is promoted to realized or interventional causal evidence. | Use `C.28`; keep `simulationOnlyCounterfactualOutputBasis` distinct unless the causal-use pattern admits another value. |
| "The work run is the evidence role." | Work occurrence and evidence-use relation are collapsed. | Use `A.15.1` for the work occurrence, `C.2.1` for the produced episteme, and `A.10` plus A.2.4 slots for later evidence use. |

### A.2.4:9 - Consequences

The positive consequence is a simpler role ontology. Systems and acting holons hold work-facing roles; epistemes are used through evidence-use, status-use, source-use, publication-use, requirement-use, definition-use, explanation-use, assurance-use, and causal-use relations.

The cost is explicit relation recovery. A phrase such as "evidence role", "status role", "standard role", "proof role", or "benchmark role" no longer closes the claim. The user needs to recover which episteme, claim, scope, status, time window, provenance constraint, and direct pattern are current.

The payoff is that one episteme can be reused honestly across many claims. Each use can have a different target claim, grounding holon, scope, polarity, relevance window, assurance use, weight model, or provenance constraint without multiplying role kinds.

### A.2.4:10 - Rationale

Evidence-use and status-use are kept as relation positions because an episteme can support, constrain, display, attest, or refresh different claims without becoming a work-facing role holder. This avoids multiplying role kinds for every publication, credential, dataset, proof, status display, source, and explanation use.

### A.2.4:10.1 - SoTA-Echoing

| SoTA line | Adopted or adapted move | FPF consequence |
| --- | --- | --- |
| Current digital provenance, content-credential, verifiable-credential, and attestation practice, including C2PA 2.4, W3C Verifiable Credentials 2.0, SLSA Provenance 1.2, and in-toto Statement v1. | Adopt the separation of subject, issuer or producing work, proof or status check, time, verifier or relying context, and claim. Adapt it to FPF `U.Episteme`, `U.Work`, role-assignment, source-currentness, and publication-use distinctions. | A.2.4 uses evidence-use and status-use relation slots instead of an episteme role assignment; credential or provenance display does not become truth, permission, gate passage, or assurance by itself. |
| Assurance-case and trust-calculus practice separates evidence presence from assurance, safety, readiness, compliance, and release confidence. | Adopt the separation between evidence-use and assurance-use. | A.2.4 supplies relation positions; `B.3` computes or states assurance and names limits, scope, decay, and reopen conditions. |
| Current causal-inference, target-trial, counterfactual, and simulation-evaluation practice separates observational, interventional, realized-counterfactual, identified-estimate, and simulation-only evidence classes. | Adopt the separation of causal evidence classes; use exact value names from `C.28`. | Causal evidence-use wording cannot relabel simulation-only output as realized or interventional evidence. |
| Foundational-ontology and relation-slot practice, including gUFO, UFO, and OntoUML role, relator, situation, and high-order type work, separates role-assignment holders, relation positions, status assertions, and object use. | Adopt the anti-collapse principle: a value may fill a relation position without becoming a new kind or role-assignment holder. | `U.RoleAssignment` stays work-facing, while episteme evidence, status, source, publication, requirement, definition, explanation, and assurance uses stay in direct relations. |

Refresh this pattern's source use when those provenance, credential, attestation, assurance, causal-use, or foundational-ontology practices change the separation between evidence presence, status display, assurance, provenance, causal class, and role assignment.

### A.2.4:11 - Relations

* **Builds on:** `A.2` for `U.Role`, `A.2.1` for `U.RoleAssignment`, `A.6.5` for SlotSpec discipline, and `C.2.1` for episteme slot relation and episteme identity.
* **Coordinates with:** `A.10` for evidence-provenance graph relation; `B.3` for assurance; `C.28` for causal-use evidence classes; `F.10` for status families; `G.6` for evidence graph and provenance ledgers; `E.17`, `E.17.0`, `E.17.2`, and `E.17.EFP` for publication, view, and explanation-use cases; `E.10.D2` for EntityOfConcern, description episteme, and specification-use discipline.
* **Separates from:** `A.15.1` for producing work; `A.15.2` for planned work; gate patterns for gate passage; `A.2.8` and `A.2.9` for commitments and speech acts; source-currentness patterns for source freshness and source order.
* **Precision-restoration owners:** When source wording says "evidence role", "status role", "standard role", or another role-shaped phrase around an episteme, use `A.6.RSIR` for relation-slot or role-like slot recovery and `E.10.ARCH` for ontology-first repair architecture.

### A.2.4:12 - Lowering, Repair, and Refresh

Lower an attempted A.2.4 use when the episteme is known but the target claim, scope, polarity, status value, time window, or provenance constraints are not recoverable. The lowered result may be source-finding, orientation, an evidence-needed note, a status-source request, or a narrowed reliance use.

Repair the use when a neighboring relation is actually current: performed work, assurance, causal use, gate passage, permission, commitment, publication-use, source-currentness, requirement-use, definition-use, or explanation-use.

Refresh the use when the episteme edition, target claim, grounding holon, claim scope, theory version, relevance window, source-currentness relation, status source, proof check, measurement trace, method description, or assurance-use relation changes.

### A.2.4:End

