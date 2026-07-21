## A.7.2 - FPF Ontology-Premise Reconciliation

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative

### A.7.2:0 - Use this when

Use this pattern when two or more current FPF methods, patterns, or accepted source uses produce incompatible ontology claims or practical consequences for the same receiving claim in the same scope. One material contradiction is enough; recurrent conflict is not required.

The first useful move is to name the smallest receiving ontology claim and the practical consequence each FPF use produces. If the claims or consequences differ by scope, stop with a context split instead of forcing agreement.

**Not this pattern when.** A vocabulary difference, unlike source function, or different subject with no shared practical consequence is not a premise conflict. Use `A.7.1` for one engineering ontology defect, `C.2.P`/`E.10` for wording use, direct evidence or formal owners for missing warrant, and source-currentness owners for stale editions.

The primary reader is an FPF maintainer, architecture steward, or pattern author responsible for a material cross-pattern contradiction. This pattern is a `U.MethodDescription`; an admitted `U.System` under a current FPF author or maintainer role assignment performs dated reconciliation `U.Work`. The pattern episteme, reader, performer, work, source uses, and returned FPF decision remain distinct.

### A.7.2:1 - Problem frame

Neighboring FPF patterns can use different premises about existence, constitution, identity, dependence, obtaining, representation, agency, or formal projection. A role pattern may require assignment work before responsibility obtains while a relation pattern treats a signed chart as constituting the same assignment. Both texts may be internally clear, yet their methods select different responsible systems for one maintenance action.

The governed concern is one bounded reconciliation of exact FPF receiving claims and their practical consequences. The ordinary result can be compatibility, separation, non-composition, no-conflict stop, or unresolved escalation. Convergence is not mandatory.

### A.7.2:2 - Problem

A premise catalogue does not repair methods that produce incompatible results. Prestige ranking of sources can hide the receiving claim, while broad foundation rewriting can damage unrelated pattern decisions. Conversely, treating different source functions as automatically incomparable can leave a real same-claim contradiction unresolved.

Reconciliation must recover what each work occurrence actually used, what source content bore on the receiving claim, which direct owners decide evidence and currentness, and which smallest FPF decision must reopen.

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
2. State the material practical consequence produced by each FPF method or source use.
3. Recover the exact FPF claim epistemes, direct kinds and relations, `A.7.CP` reasoning-basis occurrences, source-use occurrences, scope, and currentness.
4. Test whether the outputs concern the same receiving claim or the same practical consequence in the same scope. If not, return `noConflictStop` or `contextSplit`.
5. Compare exact source content through direct evidence, formal-semantics, domain, scope, and currentness owners. Do not rank source labels.
6. Translate candidate distinctions into FPF objects and constructive consequences. Test them against subject evidence and only the `A7CP-*` claims used by the reconciliation work.
7. Reopen the smallest FPF decision set, preserve unaffected direct-owner decisions, and repair the methods or clauses that produce the conflict rather than merely rewriting a premise list.
8. Return one declared result with affected use, stop, and reopen condition.

#### A.7.2:4.2 - Use one closed reconciliation result set

The result episteme uses exactly one local disposition:

- `reconciledCompatibility` — repaired methods now support compatible use for the named claim and scope;
- `contextSplit` — the claims or constructions are valid only in different named contexts or scopes;
- `doNotCompose` — both may remain current, but their outputs must not be combined for the named use;
- `unresolvedEscalation` — evidence or decision authority is insufficient, with the exact blocked use and receiving owner named;
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
  sourceContentBundleRef: U.EpistemeRef
  sourceContentKindRef: U.KindRef
  boundedContextRef: U.BoundedContextRef
  sourceUseScope: U.ClaimScope
  useFunction: OntologySourceUseFunctionValue
  useInterval: QualificationWindowPolicy
  sourceCurrentnessRef: U.EntityRef
  receivingClaimCurrentnessRef: U.EntityRef
  landedFPFDecisionRef?: U.EpistemeRef
  evidenceUseRelationRefs[]?: U.EntityRef
  disposition: OntologySourceUseDispositionValue
  blockedOverreadRef: U.EpistemeRef
  receivingClaimChangeDisposition: ReceivingClaimChangeDispositionValue
```

The source participant is the exact source episteme and edition consumed. The receiving participant is the exact ontology-claim episteme and edition being formulated, constrained, tested, interpreted, compared, or traced. The work participant is the dated ontology-decision work; its `performedBy` role assignment supplies the admitted system.

The relation obtains during the maximal interval in which the named work actually consumes `sourceContentBundleRef` for the declared function, scope, context, and receiving claim. Citation, access, bibliography membership, prestige, publication status, or co-location alone is insufficient. A change of source edition/content bundle, receiving-claim edition, work occurrence, context, scope, function, or maximal use interval creates another occurrence.

`sourceCurrentnessRef` and `receivingClaimCurrentnessRef` resolve to results under `G.11` or the exact direct owner. `landedFPFDecisionRef` appears only when current work consumes a landed decision as internal basis; it is not a prestige weight. `evidenceUseRelationRefs` point to exact `A.10` occurrences only when evidential use is current. `unresolved` pairs with `undeterminedPendingResolution` unless independent evidence establishes `unchanged`; it never silently means `changed`.

#### A.7.2:4.4 - Identify source-use conflict without ranking traditions

`OntologySourceUseConflictFinding@Context <: U.Episteme` cites two or more exact source-use occurrences and states a conflict only when their content bears on the same receiving claim or same practical consequence in the same scope and their conclusions cannot jointly hold.

Different use functions are neither automatically comparable nor automatically insulated. Compare their exact content through direct evidence, formal-semantics, domain, scope, and currentness owners. A finding can support adoption, adaptation, rejection, context split, non-composition, or unresolved return only with the exact counterexample, contradiction, proof consequence, or evidence relation that warrants it. “Stronger source” without claim-specific grounds is not a resolution.

#### A.7.2:4.5 - Stop and reopen

Stop with `noConflictStop` when the shared claim or consequence disappears after recovery. Stop with `contextSplit` or `doNotCompose` when that boundary truthfully protects the use. Stop unresolved only with the exact missing evidence or decision owner and blocked use.

Reopen when a source or receiving-claim edition changes, currentness changes, new domain or formal evidence bears on the same claim, a blocked overread becomes relevant, a landed decision changes, or repaired methods again produce incompatible same-scope consequences. Reopen only affected source-use and receiving decisions.

### A.7.2:5 - Archetypal Grounding

**Compatible repair.** A role pattern says assignment work or a policy-valid instituting act constitutes a responsibility-bearing `U.RoleAssignment`. A neighboring relation pattern treats a signed organization chart as sufficient to make the same assignment occurrence obtain. Their methods select different responsible systems for one maintenance action. Reconciliation work recovers both claims, source uses, and reasoning-basis uses of `A7CP-01`, `A7CP-03`, `A7CP-05`, and `A7CP-06`. It repairs the relation clause so the chart is evidence for an assignment assertion rather than constitution of the assignment. The result is `reconciledCompatibility`; unrelated evidence and publication law stays unchanged.

**Context split.** One pattern uses `ComponentOf` for a pump assembly while another uses `MemberOf` for a maintenance-candidate set. Both sources say “part”, but their receiving claims, constructions, and consequences differ. The result is `contextSplit`; neither source defeats the other.

**Non-convergence.** Two current methods make incompatible same-scope dependence claims, but available evidence and formal consequences warrant neither correction. The result is `doNotCompose` for the affected assurance use or `unresolvedEscalation` with exact claims, missing evidence/decision owner, and reopen condition. Familiarity or institutional status cannot manufacture convergence.

### A.7.2:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: material cross-pattern ontology-premise conflicts in FPF.

The dominant biases are prestige hierarchy, forced convergence, and formal-shape authority. The mitigations are claim-relative source-use occurrences, same-claim/same-consequence tests, direct evidence/currentness owners, a smallest-decision repair, and truthful context-split/non-composition outcomes.

### A.7.2:7 - Conformance Checklist

| ID | Check |
|---|---|
| `CC-A7.2-1` | The conflict names exact receiving claims, practical consequences, contexts, scopes, and current editions. |
| `CC-A7.2-2` | Vocabulary difference or unlike source function alone does not trigger reconciliation. |
| `CC-A7.2-3` | The reader, method episteme, admitted performer assignment, dated work, source uses, and result are distinct. |
| `CC-A7.2-4` | Every load-bearing common claim is cited from `A.7.CP` through an actual reasoning-basis occurrence. |
| `CC-A7.2-5` | Every source-use occurrence supplies all declared participants, identity values, function, scope/currentness, disposition, blocked overread, and truthful claim-change result. |
| `CC-A7.2-6` | Evidence, publication, formal semantics, and currentness remain with direct owners. |
| `CC-A7.2-7` | The repair reopens the smallest decision set and preserves unrelated FPF decisions. |
| `CC-A7.2-8` | The result is one of the five declared dispositions with affected use and stop/reopen condition. |
| `CC-A7.2-9` | Compatibility is demonstrated rather than assumed; context split and non-composition remain valid outcomes. |

### A.7.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Rank sources or traditions before naming the receiving claim. | Recover exact source content, use function, scope, currentness, and consequence. |
| Rewrite a premise list while methods keep producing conflict. | Repair the smallest method clause or direct-owner decision that causes the incompatible result. |
| Force one ontology because shared terminology looks desirable. | Permit `contextSplit` or `doNotCompose` when constructions or uses differ. |
| Treat citation or publication as an obtaining source-use relation. | Require actual consumption by dated decision work for one receiving claim. |
| Let a pattern, source, or reader role perform reconciliation. | Name the admitted system, role assignment, and dated work occurrence. |
| Copy the common compact into this method. | Cite exact `A7CP-*` claims; leave claim content and relation ownership in `A.7.CP`. |

### A.7.2:9 - Consequences

FPF gains a way to repair foundation conflicts without a total source hierarchy or an omnibus ontology pattern. The method can prove compatible co-use, preserve scoped pluralism, block composition, or return unresolved with an accountable reopen. The cost is exact source/receiving/work and currentness recovery; that cost is paid only for material conflicts.

### A.7.2:10 - Rationale

The receiving claim supplies the adjudication question. This keeps source kind, currentness, evidence use, local use function, disposition, and claim change orthogonal. Repairing the smallest method decision preserves corpus stability, while non-convergence outcomes prevent a neat vocabulary from overruling absent evidence.

**Repair the smallest foundation conflict; do not manufacture one foundation.**

### A.7.2:11 - SoTA-Echoing

| Practice question | Current practice and source | FPF alignment | Disposition |
|---|---|---|---|
| Do unlike formal modalities or calculi share one world semantics? | Typed proof traditions preserve exact operator and inference behavior (Rijke, Shulman & Spitters 2020; Acclavio, Catta & Straßburger 2021). | Formal source use is one local function; representation or notation cannot settle the receiving ontology claim by form. The non-convergence case retains direct formal owners. | **Adopt as formal comparator.** FPF does not import either calculus as universal ontology. |
| Do different ontology questions warrant different comparisons? | Keet & Khan 2024 distinguish competency-question purposes and products. | Reconciliation starts from one receiving claim and practical consequence instead of comparing whole source traditions. | **Adapt.** No mandatory question taxonomy or artifact is imported. |
| Can modal expression, object, scope, and satisfier be collapsed? | Moltmann 2024 separates modal expression, object, scope, weak/strong permission, and action satisfiers. | The method compares exact claim contents and constructive consequences instead of vocabulary labels; direct permission owners retain their semantics. | **Adapt as a consequence-sensitive source use.** No modal-object or truthmaker U-kind is imported. |
| Do capability claims require more than possibility wording? | Toyoshima et al. 2022 retain bearer and realization conditions in applied-ontology capability accounts. | A source can test one receiving capability claim while `A.2.2` remains the FPF owner. | **Comparator only.** The external hierarchy is not imported. |

Each row changes a source-use or comparison boundary in the Solution and cases. No row grants total authority to a source family, and a newer publication alone does not reopen unrelated FPF decisions.

### A.7.2:12 - Relations

- **Coordinates with:** `A.7.1`. `A.7.2` is neither its parent nor child; it handles material cross-pattern premise conflict and can return repaired direct-owner decisions to it.
- **Consumes:** exact claim contents from `A.7.CP` through actual `ClaimUsedAsReasoningBasisRelation@Context` occurrences; it does not copy or own the compact.
- **Defines:** `OntologyClaimSourceUseRelation@Context` and `OntologySourceUseConflictFinding@Context` for bounded ontology-decision and reconciliation source use only.
- **Coordinates with:** `A.10` for evidence use, `G.11` for currentness, `C.29` and direct formal patterns for formal semantics, `C.2.1`/`E.17` for source epistemes and publications, and subject patterns for the receiving ontology claim.
- **Preserves:** current landed FPF decisions as default internal basis while allowing grounded, claim-specific reopen. It does not replace `E.9.DA` review or DRR discharge.
- **Does not define:** a universal source-authority kind, source role, prestige ranking, evidence relation, publication relation, or source-currentness relation.

### A.7.2:End

