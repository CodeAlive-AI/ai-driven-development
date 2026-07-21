## A.7.CP - Constructive-Premise Compact and Reasoning-Basis Use

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative

### A.7.CP:0 - Use this when

Use this pattern when reasoning, ontology analysis, choice, or reconciliation actually relies on a broad constructive claim and another person must be able to recover which claim, posture, context, work occurrence, and interval carried that reliance.

The first useful move is to name the dated reasoning work, its declared use, the exact `A7CP-*` claim IDs it relies on, and whether each use is an `adoptedPremise` or `conditionalAssumption`. Leave the other compact claims latent.

**Not this pattern when.** Citation, publication, shared vocabulary, ordinary `A.7` category-error repair, source currentness, or a domain/evidence problem that uses no compact claim in reasoning creates no relation occurrence. This support pattern is not a method, performer, work plan, catalogue-reading episode, or problem-facing result.

The primary reader is an author or reviewer who must make one load-bearing constructive premise use recoverable. The governed object is one `ClaimUsedAsReasoningBasisRelation@Context` occurrence and the exact compact claim content it cites.

### A.7.CP:1 - Problem frame

FPF methods can depend on broad claims such as “a publication does not create world-side obtaining” or “a method episteme does not perform work”. When those claims are copied into every method, they drift. When they remain implicit, reviewers cannot tell whether a result depended on an adopted premise, a conditional branch, or no common claim at all.

The compact publishes twelve stable claim contents once. Consumers cite only actual uses, so ordinary work does not acquire a foundation checklist.

### A.7.CP:2 - Problem

Three conflations make premise use unreliable:

1. claim content is confused with the posture in which one work occurrence uses it;
2. citation or co-location is confused with actual reliance in reasoning; and
3. a support owner is treated as a method that performs or governs the consuming work.

The result is either hidden premises or a copied catalogue that becomes a second ontology authority. Both failures obscure occurrence identity and reopen behavior.

### A.7.CP:3 - Forces

| Force | Tension |
|---|---|
| Stable claims vs local use | Claim content should be durable, while posture, work, context, and interval vary per use. |
| Recoverability vs cheap first use | Load-bearing use needs a trace; ordinary method use should not traverse twelve claims. |
| Shared support vs direct ownership | Common claims coordinate patterns without absorbing evidence, currentness, construction, work, or kind admission. |
| Adopted premise vs conditional assumption | Both can support reasoning, but their defeaters and reopen conditions differ. |
| Reuse vs copied variants | One owner prevents drift; consumers still need locally intelligible action guidance. |

### A.7.CP:4 - Solution

#### A.7.CP:4.1 - Publish the compact once

The compact carries these stable claim contents:

1. **`A7CP-01 Existence and obtaining`.** World-side obtaining is not created by a claim, database row, predicate, or publication merely representing it.
2. **`A7CP-02 Constructive settlement`.** When identity, constitution, dependence, or obtaining changes a consequence, name the construction or direct governing relation that grounds it; a reconstructible trace is not itself the world construction.
3. **`A7CP-03 Constitution and social objects`.** Constituting acts, admitted systems, and the relations they institute remain distinct from descriptions of those acts and relations.
4. **`A7CP-04 Epistemic openness and fallibility`.** Evidence and reliance may remain unresolved without turning unresolved evidence into a third world-side obtaining mode.
5. **`A7CP-05 Representation boundary`.** Descriptions, logical forms, database rows, graphs, and publications represent or carry claims under exact relations; their form does not prove the represented ontic.
6. **`A7CP-06 Agency and work attribution`.** A method episteme describes a way of working; an admitted system under a role assignment performs dated work and produces results.
7. **`A7CP-07 Kind discipline`.** Use direct existing kinds and local admission before proposing a universal kind, root relation, or role-like surrogate.
8. **`A7CP-08 Scoped pluralism`.** Different source traditions or apparatuses may be useful for different receiving claims; compatibility is tested by consequences, not achieved through prestige hierarchy.
9. **`A7CP-09 Structure and wholeness`.** A description of structure is not the structure; not every construction is mereology, and `C.13` remains the owner of constructional mereology only.
10. **`A7CP-10 Time, identity, and currentness`.** World-side temporal qualification, occurrence identity, claim/publication currentness, and source supersession are separate questions.
11. **`A7CP-11 Direct-owner separation`.** Capability, state, architecture, role, method, work, evidence, permission, and relation families retain their direct owners even when an ontology method diagnoses a conflict among them.
12. **`A7CP-12 Formal projection non-reversal`.** CT2R and formalization may preserve, collapse, or omit structure. Logical validity or representation form does not reverse-infer a unique world construction.

The twelve IDs form a stable closed compact in this pattern. They are not steps, completeness criteria for every ontology use, or twelve intrinsic premise kinds.

#### A.7.CP:4.2 - Record actual reasoning-basis use

`Premise` and `assumption` name postures of exact claim use, not disjoint claim kinds.

```text
ClaimUsedAsReasoningBasisRelation@Context <: U.Relation

RelationSignature:
  BasisClaimSlot:
    SlotKind: BasisClaimSlot
    ValueKind: U.Episteme
    refMode: U.EpistemeRef
  ReasoningWorkSlot:
    SlotKind: ReasoningWorkSlot
    ValueKind: U.Work
    refMode: WorkRef

semanticDirection: BasisClaimSlot -> ReasoningWorkSlot
ReasoningBasisPostureValue ::= adoptedPremise | conditionalAssumption

RelationOccurrenceQualifiers:
  basisClaimIdRef: ClaimIdRef
  boundedContextRef: U.BoundedContextRef
  declaredReasoningUseRef: U.EntityRef
  posture: ReasoningBasisPostureValue
  relianceInterval: QualificationWindowPolicy
```

`BasisClaimSlot` is the exact claim-bearing episteme and exact compact claim ID used. `ReasoningWorkSlot` is the dated reasoning, choice, ontology-analysis, or reconciliation work that relies on it. `WorkRef` resolves to `U.Work`; the work's `performedBy` role assignment supplies the admitted system. The words “premise” and “assumption” are not relation participants.

The relation obtains during the maximal interval in which the named work actually relies on the exact claim in an inference, comparison, or choice for the declared context and use. Access, citation, publication, or co-location alone is insufficient. It applies only to reasoning-basis use; source currentness, evidence, publication, and work method remain with their owners.

One occurrence is identified by exact claim episteme and claim ID, exact work occurrence, bounded context and declared use, posture, and maximal continuous reliance interval. A change to claim edition, work occurrence, context/use, posture, or interval ends or splits the occurrence.

#### A.7.CP:4.3 - Keep posture and transition explicit

`adoptedPremise` means the work presently proceeds on the claim as accepted basis in its declared scope. `conditionalAssumption` means the work uses the claim in a narrower model, scenario, proof, or branch with an explicit test, defeater, or reopen condition. Every conditional assumption actually used can function as a premise inside that bounded subargument; not every adopted premise is conditional. Neither posture changes the claim episteme's intrinsic kind.

The same claim can be adopted in one work and conditional in another. It can also change posture within one work through two relation occurrences. Such a transition reopens only results that depended on the changed use; it does not trigger corpus-wide synonym or claim rewriting.

#### A.7.CP:4.4 - Use the cheapest truthful path

1. Name the exact reasoning work and declared use.
2. Cite only the compact IDs that are load-bearing.
3. Record one relation occurrence per exact claim/posture/continuous-use identity.
4. Keep evidence, currentness, source use, kind admission, subject construction, and work method with their direct owners.
5. Stop when the result and its premise uses are recoverable. Do not inspect unused compact entries.

### A.7.CP:5 - Archetypal Grounding

**Relation-occurrence repair.** Ontology-analysis work splits one support relation into two occurrences after removal and reinstallation. It relies on `A7CP-01` and `A7CP-10`, so two reasoning-basis occurrences are recorded for that work. The other ten claims stay latent.

**Role/chart reconciliation.** Reconciliation work distinguishes assignment constitution from a chart that evidences the assignment. It uses `A7CP-01`, `A7CP-03`, `A7CP-05`, and `A7CP-06`. The source-use and evidence relations stay under their direct owners.

**No compact use.** Missing telemetry blocks a state claim while the relevant state and evidence distinctions are already clear. Work returns to measurement/evidence. No compact claim is load-bearing, so no reasoning-basis occurrence is created.

### A.7.CP:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: cross-pattern constructive premise support and actual reasoning-basis use.

The main biases are foundation maximalism, premise-kind inflation, and trace-by-citation. The mitigation is one compact owner, exact claim IDs, two context-local postures, actual work participation, and a non-use rule that keeps ordinary reasoning cheap.

### A.7.CP:7 - Conformance Checklist

| ID | Check |
|---|---|
| `CC-A7CP-1` | Every relation occurrence names one exact claim episteme/ID, dated work occurrence, context/use, posture, and reliance interval. |
| `CC-A7CP-2` | The work actually relies on the claim; citation, access, or publication alone is insufficient. |
| `CC-A7CP-3` | `adoptedPremise` and `conditionalAssumption` are use postures, not intrinsic claim kinds. |
| `CC-A7CP-4` | A posture or identity change splits the relation occurrence and reopens only dependent results. |
| `CC-A7CP-5` | Consumers cite only load-bearing claim IDs and do not copy the compact. |
| `CC-A7CP-6` | The support pattern is not described as a method, performer, work plan, result, or mandatory catalogue traversal. |
| `CC-A7CP-7` | Evidence, currentness, source use, subject construction, kind admission, and work method remain with direct owners. |
| `CC-A7CP-8` | The twelve compact claims retain their stable IDs and contents as one closed support set. |

### A.7.CP:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Require every ontology use to check all twelve claims. | Cite only actual load-bearing claims; unused entries remain latent. |
| Treat a citation as a premise-use occurrence. | Name the dated work and inference/comparison that actually relies on the claim. |
| Define “premise” and “assumption” as separate episteme kinds. | Keep one exact claim episteme and record the context-local posture. |
| Let the compact perform or govern consuming work. | Keep the method and performer under the consuming pattern; this host supplies claim content and relation semantics. |
| Copy the compact into `A.7`, `A.7.1`, or `A.7.2`. | Keep one owner and use exact claim-ID references. |
| Hide evidence or currentness inside the relation. | Cite direct evidence/currentness results without turning them into relation fields. |

### A.7.CP:9 - Consequences

The compact makes broad constructive reliance recoverable without enlarging current `A.7` or creating copied foundation variants. Ordinary users pay nothing unless a claim is actually load-bearing. The cost is precise claim/work/posture identity in consequential reasoning; the benefit is stable content ownership and bounded reopen.

### A.7.CP:10 - Rationale

Claim content and reasoning posture vary on different axes. Publishing the content once and recording use through a direct relation prevents both hidden premises and premise-kind inflation. Work participation makes the relation ontologically honest: an episteme can be used by reasoning work but cannot reason or act by itself.

**Use only the premise the work actually relies on.**

### A.7.CP:11 - SoTA-Echoing

| Practice question | Current practice and source | FPF alignment | Disposition |
|---|---|---|---|
| Can exact claim content be reduced to possible-world equivalence? | Fine 2017 argues for exact truthmaker content beyond coarse modal equivalence. | Compact claims retain exact contents and IDs; FPF does not merge them into one modality field. | **Comparator only.** No truthmaker ontology is imported. |
| How should formal claims preserve typed behavior? | Homotopy type theory and related typed proof practice preserve exact proposition/type roles (Rijke, Shulman & Spitters 2020). | Reasoning-basis use cites an exact claim episteme and does not infer world ontology from formal form. | **Adapt as formal comparator.** Direct formal owners keep proof semantics. |
| Do bearer and realization distinctions matter for capability claims? | Applied-ontology capability work retains bearer and realization conditions (Toyoshima et al. 2022). | `A7CP-11` routes capability claims back to `A.2.2` rather than importing a compact capability ontology. | **Comparator only.** The external hierarchy is not imported. |
| Do weak permission, strong permission, and action satisfiers have the same content? | Moltmann 2024 distinguishes those contents and their use. | `A7CP-11` protects direct permission owners; exact claim IDs can support analysis without becoming permission objects. | **Adapt as separation pressure.** No modal-object U-kind is added. |

The current-practice implication is practical: exact claim use and direct-owner boundaries matter more than a large premise catalogue. The worked cases demonstrate when two, four, or zero compact claims are used.

### A.7.CP:12 - Relations

- **Defines:** the twelve `A7CP-*` constructive claim contents and `ClaimUsedAsReasoningBasisRelation@Context`.
- **Is consumed by:** `A.7.1` and `A.7.2`, which cite exact claims directly and expose relation occurrences only when use is load-bearing. Neither method depends on the other for the compact.
- **Coordinates with:** current `A.7` for its existing strict distinctions without broadening its EntityOfConcern, first move, Solution, or cases.
- **Preserves direct ownership in:** `A.10` and `G.11` for evidence/currentness, `E.24`/`E.24.UK` for ontology admission, subject construction patterns for constructive settlement, and `A.7.2` for ontology source-use relations.
- **Does not define:** a premise method, source authority, evidence relation, work plan, performer kind, common realism checklist, or universal foundation ontology.

### A.7.CP:End

