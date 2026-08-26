## A.7.2 - FPF Ontology-Premise Reconciliation

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative

### A.7.2:0 - Use this when

Use this pattern when two or more dated applications of current FPF methods or patterns yield ontology-claim or decision epistemes whose claims or practical consequences cannot jointly support the same receiving claim or consequence in the same scope. Trace each result to the exact pattern or method clauses, premises, and accepted source-use occurrences that the application actually used; a difference between texts alone is not a conflict. One material contradiction is enough; recurrent conflict is not required.

The first useful move is to name the smallest receiving ontology claim and, for each dated application, the result claim or decision, the practical consequence it would support, and the exact clause, premise, or source use on which it relied. If the result claims or consequences differ by scope, stop with a context split instead of forcing agreement.

**Not this pattern when.** A vocabulary difference, unlike source function, or different subject with no shared practical consequence is not a premise conflict. Use `A.7.1` for one engineering ontology defect, `C.2.P`/`E.10` for wording use, direct evidence-use or formal patterns for missing warrant, and source-currentness patterns for stale editions.

The primary reader is an FPF maintainer, architecture steward, or pattern author responsible for a material cross-pattern contradiction. This pattern is a `U.MethodDescription` episteme that describes a `U.Method`. An admitted `U.System` performs the dated reconciliation `U.Work`. When the actual case relies on an assignment, that assignment is one obtaining occurrence of a separately declared `U.SystemRoleAssignment` species, and an obtaining F.6 attribution connects the exact Work to that exact assignment. A short receiving result may omit an assignment identifier it does not use, but the assignment and attribution remain world-side facts. The pattern episteme, described Method, reader, performing System, assignment species, assignment occurrence, attribution, Work, source uses, and returned FPF decision remain distinct.

### A.7.2:1 - Problem frame

Neighboring FPF pattern epistemes and `U.MethodDescription` epistemes can state different premises about existence, constitution, identity, dependence, obtaining, representation, agency, or formal projection. A dated application of a system-role-assignment method clause may yield a decision claim that assignment Work or a policy-valid instituting act must occur before an individual commitment obtains, while an application of a relation-method clause may yield a claim that a signed chart constitutes that same assignment. Both texts may be internally clear, yet the application results can conflict about assignment constitution, duty, or responsibility for one maintenance action.

The governed concern is one bounded reconciliation of exact FPF receiving claims and their practical consequences. The ordinary result can be compatibility, separation, non-composition, no-conflict stop, or unresolved escalation. Convergence is not mandatory.

### A.7.2:2 - Problem

A premise catalogue does not repair dated applications whose result claims conflict. Prestige ranking of sources can hide the receiving claim, while broad foundation rewriting can damage unrelated pattern decisions. Conversely, treating different source functions as automatically incomparable can leave a real same-claim contradiction unresolved.

Reconciliation must recover what each Work occurrence actually used, what source content bore on the named claim, the exact evidence and currentness predicates and assertions, and which smallest FPF decision must reopen.

### A.7.2:3 - Forces

| Force | Tension |
|---|---|
| Compatibility vs honest pluralism | Shared use is valuable, but some methods should remain context-separated or non-composable. |
| Small repair vs foundation drift | Reopen the decision that carries the conflict without rewriting unrelated ontology. |
| Source use vs source prestige | Sources matter through exact claim use, not status labels or total rankings. |
| Formal comparability vs domain evidence | Typed consequences can expose contradiction, but formal shape cannot settle the world by itself. |
| Current decision vs reopenability | Landed FPF is the default internal basis, yet grounded counterexamples and accepted contradictions can reopen it. |

### A.7.2:4 - Solution

#### A.7.2:4.1 - Recover the exact conflict

1. Name the smallest disputed receiving ontology claim and its current edition.
2. For each dated application, name its resulting ontology-claim or decision episteme, the practical consequence the receiving use would take from it, and the exact method clause, premise, or source-use occurrence on which the work relied.
3. Recover the exact FPF claim epistemes, dated application-work occurrences, direct kinds and relations, `A.7.CP` reasoning-basis occurrences, source-use occurrences, scope, and currentness.
4. Test whether the result claims support incompatible answers to the same receiving claim or practical consequence in the same scope. If not, return `noConflictStop` or `contextSplit`.
5. Compare exact source content through direct evidence, formal-semantics, domain, scope, and currentness patterns. Do not rank source labels.
6. Translate candidate distinctions into FPF objects and constructive consequences. Test them against subject evidence and only the `A7CP-*` claims used by the reconciliation work.
7. Reopen the smallest FPF decision set, preserve unaffected subject-pattern decisions, and repair the method clause or subject-pattern decision that caused the dated applications to yield incompatible results. Run enough of the affected application again to obtain a checked result; do not stop at rewriting a premise list.
8. Return one declared result with affected use, stop, and reopen condition.

#### A.7.2:4.2 - Use one closed reconciliation result set

The result episteme uses exactly one local disposition:

- `reconciledCompatibility` — repaired clauses and checked application results now support compatible use for the named claim and scope;
- `contextSplit` — the claims or constructions are valid only in different named contexts or scopes;
- `doNotCompose` — both may remain current, but their outputs must not be combined for the named use;
- `unresolvedEscalation` — evidence or decision authority is insufficient, with the exact blocked use and receiving subject pattern named;
- `noConflictStop` — the apparent conflict disappears after claim, consequence, or scope recovery.

These are reconciliation-result dispositions, not new U-kinds. Compatible co-use is demonstrated only when warranted. A current conflict does not have to end in one winner.

#### A.7.2:4.3 - Record claim-relative source use

`OntologyClaimSourceUseRelation@Context` records how one dated ontology-decision or reconciliation work occurrence actually consumes one source episteme for one receiving ontology claim. It is local to this use and does not create a universal source-authority relation.

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
The source participant is the source episteme and edition consumed. The receiving participant is the ontology-claim episteme and edition being formulated, constrained, tested, interpreted, compared, or traced. The Work participant is the dated ontology-decision `U.Work`, performed by an admitted `U.System`. If the actual case relies on an assignment, recover one obtaining assignment occurrence whose species is separately declared under `U.SystemRoleAssignment`. An obtaining F.6 attribution, not the assignment's existence or interval alone, connects that Work to the assignment; the assignment holder must be the same System. The assignment neither supplies the System nor performs the Work.

The minimal occurrence needs only those three exact participants, `useFunction`, `sourceUseScope`, and the derived maximal continuous interval during which the named work actually consumes content from that source episteme for that receiving claim. Citation, access, bibliography membership, prestige, publication status, or co-location alone is insufficient. If the work consumes only a separately identified claim or content episteme inside the source, `sourceContentSliceRef` names that slice; it does not duplicate the source participant under a bundle alias. Changing a source or receiving-claim edition, work occurrence, function, scope, or demonstrated actual-use interval identifies another occurrence. A changed optional qualifier identifies another occurrence only when it changes the content or direct use predicate; a later review record alone does not.

Add `modelUseStructureRef` only when one independently selected `BoundedModelUseStructure` changes interpretation of this use. Add source-content kind, currentness-result, landed-decision, evidence-use, disposition, blocked-overread, or receiving-claim-change references only when the reconciliation work actually asserts or consumes that item under its subject pattern. A recorded `unresolved` disposition needs no fabricated blocked-overread episteme; `unchanged` is recorded only when the work actually reaches that result, while absence of a change disposition remains no claim.

#### A.7.2:4.4 - Identify source-use conflict without ranking traditions

`OntologySourceUseConflictFinding@Context <: U.Episteme` cites two or more exact source-use occurrences and states a conflict only when their content bears on the same receiving claim or same practical consequence in the same scope and their conclusions cannot jointly hold.

Different use functions are neither automatically comparable nor automatically insulated. Compare their exact content through direct evidence, formal-semantics, domain, scope, and currentness patterns. A finding can support adoption, adaptation, rejection, context split, non-composition, or unresolved return only with the exact counterexample, contradiction, proof consequence, or evidence relation that warrants it. “Stronger source” without claim-specific grounds is not a resolution.

#### A.7.2:4.5 - Stop and reopen

Stop with `noConflictStop` when the shared claim or consequence disappears after recovery. Stop with `contextSplit` or `doNotCompose` when that boundary truthfully protects the use. Stop unresolved only with the exact missing evidence basis or decision predicate and source and blocked use.

Reopen when a source or receiving-claim edition changes, currentness changes, new domain or formal evidence bears on the same claim, a blocked overread becomes relevant, a landed decision changes, or later dated applications of repaired clauses yield incompatible same-scope consequences. Reopen only affected source-use, application-result, and receiving decisions.

### A.7.2:5 - Archetypal Grounding

**Compatible repair.** One dated method application yields a claim that a policy-valid instituting act creates `MaintenanceCommitment-17`, an exact `U.Commitment` whose actual bearer is `MaintenanceSystem-4`; it does not thereby establish responsibility. Another application yields a claim that a signed organization chart is sufficient to make `MaintenanceAssignment-17 : MaintenanceCoordinatorAssignment` obtain. Reconciliation Work recovers both result claims, their method clauses, source uses, and reasoning-basis uses of `A7CP-01`, `A7CP-03`, `A7CP-05`, and `A7CP-06`. It repairs the assignment clause so the chart is evidence for an assignment assertion rather than constitution of the assignment. If responsibility is also claimed, it is tested independently under an admitted maintenance-responsibility predicate with actual participants, applicability, and identity; otherwise the exact missing governor is returned. The result is `reconciledCompatibility`: commitment, assignment, responsibility, performing system, and Work no longer substitute for one another, while unrelated evidence and publication law stays unchanged.

**Context split.** One dated application uses a pattern's `ComponentOf` clause for a pump assembly; another applies a maintenance-set pattern's belongs-to rule to a candidate item. Both result claims say “part”, but their subjects, receiving claims, constructions, and consequences differ. The result is `contextSplit`; neither source clause nor application result defeats the other.

**Non-convergence.** Two dated method applications yield incompatible same-scope dependence claims, but available evidence and formal consequences warrant neither correction. The result is `doNotCompose` for the affected assurance use or `unresolvedEscalation` with exact result claims, missing evidence basis or decision predicate and source, and reopen condition. Familiarity or institutional status cannot manufacture convergence.

### A.7.2:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: material cross-pattern ontology-premise conflicts in FPF.

The dominant biases are prestige hierarchy, forced convergence, and formal-shape authority. The mitigations are claim-relative source-use occurrences, same-claim/same-consequence tests, direct evidence/currentness patterns, a smallest-decision repair, and truthful context-split/non-composition outcomes.

### A.7.2:7 - Conformance Checklist

| ID | Check |
|---|---|
| `CC-A7.2-1` | The conflict names exact receiving claims, practical consequences, contexts, scopes, and current editions. |
| `CC-A7.2-2` | Vocabulary difference or unlike source function alone does not trigger reconciliation. |
| `CC-A7.2-3` | The reader, `U.MethodDescription` episteme, described `U.Method`, admitted performing `U.System`, any separately declared assignment species and actual assignment occurrence used by the case, obtaining F.6 attribution, dated reconciliation `U.Work`, source uses, and returned result are distinct. A short result may omit an assignment identifier unused by its receiver without denying an otherwise established assignment or attribution. |
| `CC-A7.2-4` | Every load-bearing common claim is cited from `A.7.CP` through an actual reasoning-basis occurrence. |
| `CC-A7.2-5` | Every source-use occurrence has the three exact participants, source and receiving-claim editions, function, claim scope, and maximal continuous actual-use interval. It includes only content-slice, model-use, currentness, evidence, disposition, blocked-overread, or claim-change qualifiers actually used or asserted in this reconciliation. |
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
| Let a pattern, source, reader label, system-role kind, or assignment perform reconciliation. | Name the performing `U.System` and dated reconciliation `U.Work`. When the case establishes an assignment and relies on it, name its separately declared species and actual occurrence and connect that occurrence to the Work through an obtaining F.6 attribution. Neither the kind nor the assignment acts. |
| Copy the common compact into this method. | Cite exact `A7CP-*` claims; keep `A.7.CP` as the authoritative source for the claim content and relation definition. |

### A.7.2:9 - Consequences

FPF gains a way to repair foundation conflicts without a total source hierarchy or an omnibus ontology pattern. The method can prove compatible co-use, preserve scoped pluralism, block composition, or return unresolved with an accountable reopen. The cost is exact source/receiving/work and currentness recovery; that cost is paid only for material conflicts.

### A.7.2:10 - Rationale

The receiving claim supplies the adjudication question. This keeps source kind, currentness, evidence use, local use function, disposition, and claim change orthogonal. Repairing the smallest method decision preserves corpus stability, while non-convergence outcomes prevent a neat vocabulary from overruling absent evidence.

**Repair the smallest foundation conflict; do not manufacture one foundation.**

### A.7.2:11 - SoTA-Echoing

| Practice question | Current practice and source | FPF alignment | Disposition |
|---|---|---|---|
| Do unlike formal modalities or calculi share one world semantics? | Typed proof traditions preserve exact operator and inference behavior (Rijke, Shulman & Spitters 2020; Acclavio, Catta & Straßburger 2021). | Formal source use is one local function; representation or notation cannot settle the receiving ontology claim by form. The non-convergence case retains direct formal patterns. | **Adopt as formal comparator.** FPF does not import either calculus as universal ontology. |
| Do different ontology questions warrant different comparisons? | Keet & Khan 2024 distinguish competency-question purposes and products. | Reconciliation starts from one receiving claim and practical consequence instead of comparing whole source traditions. | **Adapt.** No mandatory question taxonomy or artifact is imported. |
| Can modal expression, object, scope, and satisfier be collapsed? | Moltmann 2024 separates modal expression, object, scope, weak/strong permission, and action satisfiers. | The method compares exact claim contents and constructive consequences instead of vocabulary labels; direct permission patterns retain their semantics. | **Adapt as a consequence-sensitive source use.** No modal-object or truthmaker U-kind is imported. |
| Do capability claims require more than possibility wording? | Toyoshima et al. 2022 retain bearer and realization conditions in applied-ontology capability accounts. | A source can test one receiving capability claim while `A.2.2` remains the FPF subject pattern. | **Comparator only.** The external hierarchy is not imported. |

Each row changes a source-use or comparison boundary in the Solution and cases. No row grants total authority to a source family, and a newer publication alone does not reopen unrelated FPF decisions.

### A.7.2:12 - Relations

- **Coordinates with:** `A.7.1`. `A.7.2` is neither its parent nor child; it handles material cross-pattern premise conflict and can return repaired subject-pattern decisions to it.
- **Consumes:** exact claim contents from `A.7.CP` through actual `ClaimUsedAsReasoningBasisRelation@Context` occurrences; it does not copy or own the compact. Pattern epistemes and `U.MethodDescription` epistemes supply clauses or declared premises; their described Methods remain distinct, while dated application Work and its separately governed result claims supply the reconciliation inputs.
- **Defines:** `OntologyClaimSourceUseRelation@Context` and `OntologySourceUseConflictFinding@Context` for bounded ontology-decision and reconciliation source use only.
- **Coordinates with:** `A.10` for evidence use, `G.11` for currentness, `C.29` and direct formal patterns for formal semantics, `C.2.1`/`E.17` for source epistemes and publications, and subject patterns for the receiving ontology claim.
- **Preserves:** current landed FPF decisions as default internal basis while allowing grounded, claim-specific reopen. It does not replace `E.9.DA` review or DRR discharge.
- **Does not define:** a universal source-authority kind, source role, prestige ranking, evidence relation, publication relation, or source-currentness relation.

### A.7.2:End

