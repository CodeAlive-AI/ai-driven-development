## A.7.2 - FPF Ontology-Premise Reconciliation

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative

### A.7.2:0 - Use this when

Use this pattern when two or more dated applications of current FPF methods or patterns yield ontology-claim or decision epistemes whose claims or practical consequences cannot jointly support the same receiving claim or consequence in the same scope. Trace each result to the exact pattern or method clauses, premises, and source-use occurrences that the application actually used; a difference between texts alone is not a conflict. One material contradiction is enough; recurrent conflict is not required.

The first useful move is to name the smallest receiving ontology claim and, for each dated application, the result claim or decision, the practical consequence it would support, and the clause, premise, or source use on which it relied. If the apparent conflict disappears after recovering the applicable scopes, return a context split. Different scope labels alone do not resolve incompatible claims in their shared domain.

**Not this pattern when.** A vocabulary difference, unlike source function, or different subject with no shared practical consequence is not a premise conflict. Use `A.7.1` for one engineering ontology defect, `F.19` for wording repair with `C.2.P`/`E.10` for a remaining semantic question, direct evidence-use or formal patterns for missing warrant, and source-currentness patterns for stale editions.

The primary reader is an FPF maintainer, architecture steward, or pattern author responsible for a material cross-pattern contradiction. The procedural content describes the reconciliation Method in §4. A `U.MethodDescription` assertion requires that admitted Method as the episteme's exact EntityOfConcern and A.3.2 membership. For any precise dated reconciliation `U.Work`, use A.13 to identify the actual performer System and let A.15.1 independently admit the occurrence. If the case or receiving result must also identify the assignment under which the reconciliation Work was performed, check that relation separately through F.6 against the assignment used by A.13. A short result may omit an assignment identifier it does not use; no unused assignment or attribution is presumed. The pattern episteme, described Method, reader, performing System, any separately established assignment species and occurrence, optional attribution check, Work, source uses, and returned FPF decision remain distinct.

### A.7.2:1 - Problem frame

Neighboring FPF pattern epistemes and `U.MethodDescription` epistemes can state different premises about existence, constitution, identity, dependence, obtaining, representation, agency, or formal projection. One dated application of a system-role-assignment clause may conclude that a relation does not obtain for its exact participants and scope because the instituting act required by its applicable rule has not occurred, while another concludes that the same relation obtains from a signed organization chart alone. Both texts may be internally clear, yet these application results conflict about assignment constitution in the same scope; duty and responsibility remain separately governed claims.

The governed concern is one bounded reconciliation of exact FPF receiving claims and their practical consequences. The ordinary result can be compatibility, separation, non-composition, no-conflict stop, or unresolved escalation. Convergence is not mandatory.

### A.7.2:2 - Problem

A premise catalogue does not repair dated applications whose result claims conflict. Prestige ranking of sources can hide the receiving claim, while broad foundation rewriting can damage unrelated pattern decisions. Conversely, treating different source functions as automatically incomparable can leave a real same-claim contradiction unresolved.

Reconciliation recovers what each application actually used, what source content bore on the receiving claim, and which evidence and currentness assertions the comparison needs. Reopen an FPF decision only when that comparison establishes a conflict requiring repair.

### A.7.2:3 - Forces

| Force | Tension |
|---|---|
| Compatibility vs honest pluralism | Shared use is valuable, but some methods should remain context-separated or non-composable. |
| Small repair vs foundation drift | Reopen the decision that carries the conflict without rewriting unrelated ontology. |
| Source use vs source prestige | Sources matter through exact claim use, not status labels or total rankings. |
| Formal comparability vs domain evidence | Typed consequences can expose contradiction, but formal shape cannot settle the world by itself. |
| Current decision vs reopenability | The current published FPF decisions supply an internal basis, while grounded counterexamples and contradictions can require reconsideration. |

### A.7.2:4 - Solution

#### A.7.2:4.1 - Recover the exact conflict

1. Name the smallest disputed receiving ontology claim and its current edition.
2. For each dated application, name its resulting ontology-claim or decision episteme, the practical consequence the receiving use would take from it, and the exact method clause, premise, or source-use occurrence on which the work relied.
3. Recover the FPF claim epistemes, dated application Work, direct kinds and relations, and source-use occurrences needed for this comparison. Include A.7.CP reasoning-basis occurrences only for claims actually used; recover scope and currentness where they affect the result.
4. Test whether the result claims support incompatible answers to the same receiving claim or practical consequence in the same scope. If not, return `noConflictStop` or `contextSplit`.
5. Compare exact source content through direct evidence, formal-semantics, domain, scope, and currentness patterns. Do not rank source labels.
6. Translate candidate distinctions into FPF objects and constructive consequences. Test them against subject evidence and only the `A7CP-*` claims used by the reconciliation work.
7. Reopen the smallest FPF decision set, preserve unaffected subject-pattern decisions, and repair the method clause or subject-pattern decision that caused the dated applications to yield incompatible results. Run enough of the affected application again to obtain a checked result; do not stop at rewriting a premise list.
8. Return one declared result with affected use, stop, and reopen condition.

#### A.7.2:4.2 - Use one closed reconciliation result set

The result episteme uses exactly one local disposition:

- `reconciledCompatibility` — repaired clauses and checked application results now support compatible use for the named claim and scope;
- `contextSplit` — the apparent incompatibility disappears under the recovered contexts or scopes; each claim retains its separate subject-matter warrant;
- `doNotCompose` — both may remain current, but their outputs must not be combined for the named use;
- `unresolvedEscalation` — evidence or decision authority is insufficient, with the exact blocked use and receiving subject pattern named;
- `noConflictStop` — the apparent conflict disappears after claim, consequence, or scope recovery.

These are reconciliation-result dispositions, not new U-kinds. Compatible co-use is demonstrated only when warranted. A current conflict does not have to end in one winner.

#### A.7.2:4.3 - Record claim-relative source use

`OntologyClaimSourceUseRelation@Context` relates one source episteme, one receiving ontology claim, and the dated ontology-decision or reconciliation work occurrence that actually consumes that source for that claim. It is local to this use and does not create a universal source-authority relation.

```text
OntologySourceUseFunctionValue ::=
  formulateReceivingClaim
  | constrainReceivingClaim
  | testOrStressReceivingClaim
  | interpretFormalOrImplementationSemantics
  | compareReceivingAlternatives
  | traceLineage

OntologySourceUseDispositionValue ::=
  adopt | adapt | reject | comparatorOnly | lineageOnly | unresolved

ReceivingClaimChangeDispositionValue ::=
  changed | unchanged | undeterminedPendingResolution

OntologyClaimSourceUseRelation@Context <: U.Relation

RelationSignature:
  SourceEpistemeSlot:
    SlotKind: SourceEpistemeSlot
    ValueKind: U.Episteme
    refMode: U.EpistemeRef
  ReceivingOntologyClaimSlot:
    SlotKind: ReceivingOntologyClaimSlot
    ValueKind: U.Episteme
    refMode: U.EpistemeRef
  OntologyDecisionWorkSlot:
    SlotKind: OntologyDecisionWorkSlot
    ValueKind: U.Work
    refMode: WorkRef

semanticDirection: SourceEpistemeSlot -> ReceivingOntologyClaimSlot
  through the named OntologyDecisionWorkSlot

RelationOccurrenceQualifiers:
  sourceUseScope: U.ClaimScope
  useFunction: OntologySourceUseFunctionValue
  sourceContentSliceRef?: U.EpistemeRef
  sourceContentKindRef?: U.KindRef
  modelUseStructureRef?: U.StructureRef
  sourceCurrentnessResultRef?: U.EpistemeRef
  receivingClaimCurrentnessResultRef?: U.EpistemeRef
  landedFPFDecisionRef?: U.EpistemeRef
  evidenceUseRelationRefs[]?: U.EntityRef
  disposition?: OntologySourceUseDispositionValue
  blockedOverreadRef?: U.EpistemeRef
  receivingClaimChangeDisposition?: ReceivingClaimChangeDispositionValue

OccurrenceIdentity:
  <exact source-episteme edition,
   exact receiving-claim edition,
   exact ontology-decision work occurrence,
   useFunction,
   sourceUseScope,
   maximalContinuousUseInterval>
```
The source participant is the source episteme and edition consumed. The receiving participant is the ontology-claim episteme and edition being formulated, constrained, tested, interpreted, compared, or traced. For the Work participant, use A.13 to identify the actual performer and A.15.1 to admit the dated ontology-decision `U.Work` independently. If the case must also identify the assignment under which that Work was performed, F.6 checks the assignment used by A.13 and compares its holder with the already identified performer. The assignment relates the independently identified System to its assigned-kind value; that System performs the Work.

The minimal occurrence needs only those three exact participants, `useFunction`, `sourceUseScope`, and the maximal continuous interval during which the named Work actually consumes content from that source episteme for that receiving claim. Citation, access, bibliography membership, prestige, publication status, or co-location alone is insufficient. If the Work consumes a separately identified claim or content episteme within the source, `sourceContentSliceRef` names that slice. A different consumed source or receiving-claim edition, Work occurrence, function, scope, or maximal continuous use episode identifies another occurrence. Correcting knowledge of the same actual episode changes the assertion, not that occurrence. A changed optional qualifier identifies another occurrence only when it changes the direct use predicate; a later review record alone does not.

Add `modelUseStructureRef` only when one independently selected `BoundedModelUseStructure` changes interpretation of this use. Add source-content kind, currentness-result, published-decision, evidence-use, disposition or receiving-claim-change references only when the reconciliation actually asserts or consumes that item under its subject rule. A `blockedOverreadRef` additionally requires F.19's independent local ground, plausible intended-reader error and effect on truth, understanding or use; state only the smallest needed correction. A recorded `unresolved` disposition needs no fabricated blocked-overread episteme. Record `unchanged` only when the Work reaches that result; an absent change disposition makes no claim.

#### A.7.2:4.4 - Identify source-use conflict without ranking traditions

`OntologySourceUseConflictFinding@Context <: U.Episteme` cites two or more exact source-use occurrences and states a conflict only when their content bears on the same receiving claim or same practical consequence in the same scope and their conclusions cannot jointly hold.

Different use functions are neither automatically comparable nor automatically insulated. Compare their exact content through direct evidence, formal-semantics, domain, scope, and currentness patterns. A finding can support adoption, adaptation, rejection, context split, non-composition, or unresolved return only with the exact counterexample, contradiction, proof consequence, or evidence relation that warrants it. “Stronger source” without claim-specific grounds is not a resolution.

#### A.7.2:4.5 - Stop and reopen

Stop with `noConflictStop` when the shared claim or consequence disappears after recovery. Stop with `contextSplit` or `doNotCompose` when that boundary truthfully protects the use. Stop unresolved only with the exact missing evidence basis or decision predicate and source and blocked use.

Reconsider affected uses when a source or receiving-claim edition changes, needed currentness changes, new domain or formal evidence bears on the same claim, a grounded blocked-overread issue becomes relevant, the consumed FPF decision changes, or later applications of repaired clauses yield incompatible same-scope consequences. Reopen only dependent source-use, application-result and receiving decisions; preserve results whose grounds remain unchanged.

### A.7.2:5 - Archetypal Grounding

**Compatible repair.** The receiving claim asks whether a `MaintenanceCoordinatorAssignment` obtains for holder `MaintenanceSystem-4` and assigned kind `MaintenanceCoordinatorKind` in scope `S`. Its independently admitted local rule requires a policy-valid assignment act and treats the signed organization chart as evidence only. The chart is present, but current facts establish that the required act did not occur. One dated application of the local rule concludes that the relation does not obtain; another application of a chart-sufficiency clause concludes that it obtains for the same participants and scope. Reconciliation Work recovers both result claims, their method clauses, source uses, and reasoning-basis uses of `A7CP-01`, `A7CP-03`, `A7CP-05`, and `A7CP-06`. It repairs the assignment clause to apply the local obtaining rule and use the chart as evidence for an assertion. Replaying both applications now yields the supported non-obtaining conclusion, without inventing an assignment occurrence. The result is `reconciledCompatibility` for that claim and scope.

If the evidence does not establish whether the required act occurred, reliance on the obtaining claim remains unresolved. Under a different independently admitted rule, authorized signing may itself be the required act; establish that actual act instead of applying this case's evidential-only rule. A separate policy-valid act may create `MaintenanceCommitment-17`, borne by `MaintenanceSystem-4`; neither this commitment nor the assignment claim by itself establishes responsibility. Test any responsibility claim separately against its admitted maintenance-responsibility predicate, actual participants, applicability, and identity; if that governor is missing, return the exact missing governor.

**Context split.** One dated application uses a pattern's `ComponentOf` clause for a pump assembly; another applies a maintenance-set pattern's belongs-to rule to a candidate item. Both result claims say “part”, but their subjects, receiving claims, constructions, and consequences differ. The result is `contextSplit`; neither source clause nor application result defeats the other.

**Non-convergence.** Two dated method applications yield incompatible same-scope dependence claims, but available evidence and formal consequences warrant neither correction. If the receiving question is whether the outputs may be combined for an assurance use requiring compatibility, return `doNotCompose` for that use. If the receiving decision instead needs the unresolved premise settled, return `unresolvedEscalation` with the result claims, missing evidence basis or decision rule, its source and the reopen condition. Familiarity or institutional status settles neither question.

### A.7.2:6 - Bias-Annotation


The dominant biases are prestige hierarchy, forced convergence, and formal-shape authority. The mitigations are claim-relative source-use occurrences, same-claim/same-consequence tests, direct evidence/currentness patterns, a smallest-decision repair, and truthful context-split/non-composition outcomes.

### A.7.2:7 - Conformance Checklist

| ID | Check |
|---|---|
| `CC-A7.2-1` | The conflict names exact receiving claims, practical consequences, contexts, scopes, and current editions. |
| `CC-A7.2-2` | Vocabulary difference or unlike source function alone does not trigger reconciliation. |
| `CC-A7.2-3` | Keep the reader, pattern episteme, described Method and result distinct. Any MethodDescription claim satisfies A.3.2. For an asserted dated reconciliation Work, retain the independent A.13/A.15.1 basis in §0, including the separately admitted assignment species and obtaining occurrence used by A.13; add F.6 only for the precise attribution consumed. A short result may omit unused identifiers without presuming their facts. |
| `CC-A7.2-4` | Every load-bearing common claim is cited from `A.7.CP` through an actual reasoning-basis occurrence. |
| `CC-A7.2-5` | Every source-use occurrence has the three participants, source and receiving-claim editions, function, claim scope and maximal continuous actual-use interval. Corrected knowledge of that interval does not itself change occurrence identity. Include only qualifiers used or asserted in this reconciliation, with blocked-overread references satisfying §4.3's F.19 conditions. |
| `CC-A7.2-6` | Evidence, publication, formal semantics, and currentness remain with subject patterns. |
| `CC-A7.2-7` | The repair reopens the smallest decision set and preserves unrelated FPF decisions. |
| `CC-A7.2-8` | The result is one of the five declared dispositions with affected use and stop/reopen condition. |
| `CC-A7.2-9` | Compatibility is demonstrated rather than assumed; context split and non-composition remain valid outcomes. |

### A.7.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Rank sources or traditions before naming the receiving claim. | Recover exact source content, use function, scope, currentness, and consequence. |
| Rewrite a premise list while dated applications keep yielding conflicting results. | Repair the smallest method clause or subject-pattern decision that causes the incompatible result, then check the affected application result. |
| Force one ontology because shared terminology looks desirable. | Permit `contextSplit` or `doNotCompose` when constructions or uses differ. |
| Treat citation, publication, or a completed review dossier as an obtaining source-use relation. | Require actual consumption by dated decision work for one receiving claim; keep optional content-slice, model-use, currentness, evidence, and disposition records only when this reconciliation uses them. |
| Let a pattern, source, reader label, system-role kind, or assignment perform reconciliation. | Use A.13 to identify the actual performer and A.15.1 to admit the dated reconciliation Work independently. Retain the separately declared assignment species and obtaining occurrence used by A.13; add F.6 only if the result must also identify the assignment under which that Work was performed. Neither the kind nor the assignment acts. |
| Copy the common compact into this method. | Cite exact `A7CP-*` claims; keep `A.7.CP` as the authoritative source for the claim content and relation definition. |

### A.7.2:9 - Consequences

The Method can establish compatible co-use, retain scoped alternatives, block composition for a named use, or return an unresolved decision with its reopen condition. Its cost is recovering the source, receiving claim and actual application facts, including currentness where it affects the comparison. That work is justified by a material conflict and stops at the sufficient scoped result.

### A.7.2:10 - Rationale

The receiving claim supplies the adjudication question. This keeps source kind, currentness, evidence use, local use function, disposition, and claim change orthogonal. Repairing the smallest method decision preserves corpus stability, while non-convergence outcomes prevent a neat vocabulary from overruling absent evidence.

**Repair the smallest foundation conflict; do not manufacture one foundation.**

### A.7.2:11 - SoTA-Echoing

| Practice question | Source contribution | FPF alignment | Disposition |
|---|---|---|---|
| Do unlike formal modalities or calculi share one world semantics? | Typed proof traditions preserve exact operator and inference behavior (Rijke, Shulman & Spitters 2020; Acclavio, Catta & Straßburger 2021). | Formal source use is one local function; representation or notation cannot settle the receiving ontology claim by form. The non-convergence case retains direct formal patterns. | **Adopt as formal comparator.** FPF does not import either calculus as universal ontology. |
| Do different ontology questions warrant different comparisons? | Keet & Khan 2024 distinguish competency-question purposes and products. | Reconciliation starts from one receiving claim and practical consequence instead of comparing whole source traditions. | **Adapt.** No mandatory question taxonomy or artifact is imported. |
| Can modal expression, object, scope, and satisfier be collapsed? | Moltmann 2024 separates modal expression, object, scope, weak/strong permission, and action satisfiers. | The method compares exact claim contents and constructive consequences instead of vocabulary labels; direct permission patterns retain their semantics. | **Adapt as a consequence-sensitive source use.** No modal-object or truthmaker U-kind is imported. |
| Do capability claims require more than possibility wording? | Toyoshima et al. 2022 retain bearer and realization conditions in applied-ontology capability accounts. | A source can test one receiving capability claim while `A.2.2` remains the FPF subject pattern. | **Comparator only.** The external hierarchy is not imported. |

A source contributes through its content and the receiving claim. A newer publication alone does not reopen unrelated FPF decisions.

### A.7.2:12 - Relations

- **Coordinates with:** `A.7.1`. `A.7.2` is neither its parent nor child; it handles material cross-pattern premise conflict and can return repaired subject-pattern decisions to it.
- **Consumes:** exact claim contents from `A.7.CP` through actual `ClaimUsedAsReasoningBasisRelation@Context` occurrences; it does not copy or own the compact. Pattern epistemes and `U.MethodDescription` epistemes supply clauses or declared premises; their described Methods remain distinct, while dated application Work and its separately governed result claims supply the reconciliation inputs.
- **Defines:** `OntologyClaimSourceUseRelation@Context` and `OntologySourceUseConflictFinding@Context` for bounded ontology-decision and reconciliation source use only.
- **Coordinates with:** `A.10` for evidence use, `G.11` for currentness, `C.29` and direct formal patterns for formal semantics, `C.2.1` for source epistemes, `E.24.PUB` for publication-occurrence, form, and carrier questions, `E.17` for multi-view publication, and subject patterns for the receiving ontology claim.
- **Preserves:** current published FPF decisions as an internal basis, with grounded, claim-specific reconsideration. Use `E.9.DA` review or DRR discharge when that separately governed question is current.
- **Does not define:** a universal source-authority kind, source role, prestige ranking, evidence relation, publication relation, or source-currentness relation.

### A.7.2:End
