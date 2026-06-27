## A.1.1 - U.BoundedContext Semantic Frame

> **Type:** Part A architectural ontology pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### A.1.1:0 - Use This When

Use this pattern when a term, role, rule, invariant, unit, status, or admissible inference is meaningful only inside a named semantic frame.

Typical moments:

- the same word means different things in engineering, finance, legal, scientific, or operations work;
- a role assignment needs the context that defines the role and its incompatibilities;
- an invariant is local to one standard, team, theory, regulation, product line, or edition;
- two contexts need a bridge relation rather than an assumed global equivalence;
- a "domain" label is too broad to decide local vocabulary or rules.

**First useful move.** Name the `U.BoundedContext` that governs the current meaning, then state the local vocabulary, local invariants, role taxonomy when role assignments are current, episteme-use/status relations when epistemic-use or status claims are current, and bridge relations that matter for the claim.

**What goes wrong if missed.** "Owner", "ticket", "service", "evidence", "role", "done", and "valid" become global labels. Integration work then appears to be about matching words, while the real problem is unspoken semantic frames.

**What this buys.** FPF can keep plural meanings without contradiction: each meaning is local, and cross-context use becomes an explicit bridge relation with stated fit and loss.

**Not this pattern when.**

- If the question is only naming a durable term, use `F.18`.
- If the question is role-method-work alignment after the context is known, use `A.15`.
- If the question is episteme description context, use `C.2.1` with `BoundedContextRef`.
- If the question is a broad field such as healthcare, physics, finance, or architecture, treat it as an informative domain family unless a specific bounded context is named.

### A.1.1:1 - Problem Frame

Meaning is local. The same expression can be coherent in one bounded context and misleading in another. "Service" in software, service operations, military organization, and contract law is not one global object by spelling. "Evidence" in a courtroom, a scientific review, a machine-learning benchmark, and a gate review is not one global role by spelling.

`U.BoundedContext` is the FPF ontic for this locality of meaning. It is a `U.Holon` that holds one semantic frame: local vocabulary, local invariants, local role taxonomy when role-assignment claims are current, local episteme-use/status relations when epistemic-use or status claims are current, and bridge relations to other contexts.

A bounded context is not an enclosing object for all work in a domain. It is the semantic frame in which a term, rule, role assignment, or inference is interpreted.

### A.1.1:2 - Problem

Without `U.BoundedContext`:

1. **Semantic drift hides in shared words.** Teams keep the same label while changing the object, role, rule, or allowed inference.
2. **Local rules leak globally.** A policy, status, role, or invariant valid in one context is applied in another without a bridge relation.
3. **Pluralism looks like contradiction.** Two contexts can each be coherent, but absent context they look mutually inconsistent.
4. **Role assignments lose their footing.** A `U.Role` is used as a global label rather than a value defined in a local role taxonomy.
5. **Domain labels pretend to govern.** "Healthcare", "AI", "architecture", or "physics" is used where a specific semantic frame is required.

### A.1.1:3 - Forces

| Force | Tension |
| --- | --- |
| Local coherence vs cross-context work | A context must be internally coherent; real projects still exchange meanings across contexts. |
| Pluralism vs one-truth pressure | Several valid frames may coexist; readers often want one global meaning. |
| Explicitness vs overhead | Naming contexts and bridges costs effort; hidden context costs more when integration or review fails. |
| Role locality vs organizational habit | Roles are defined by local rules; organizations often reuse titles as if they were global roles. |
| Domain convenience vs semantic precision | Domain family labels help orientation; bounded contexts decide meaning. |

### A.1.1:4 - Solution

Model `U.BoundedContext` as a semantic-frame holon.

```text
BoundedContextSlotRelation:
  contextIdentity:
  contextBoundary:
  localVocabulary:
  localInvariantSet:
  localRoleTaxonomy?:
  localEpistemeUseAndStatusRelationSet?:
  bridgeRelationSet?:
  stewardingSystemOrCommunityRef?:
  editionOrWindowRef?:
```

The context is the `EntityOfConcern` when the claim is about semantic locality itself. It may also fill `BoundedContextRef` in role assignments, episteme descriptions, characteristic spaces, architecture descriptions, and other patterns.

#### A.1.1:4.1 - Context Identity

`contextIdentity` names the semantic frame, not a territory, department, document, storage place, team, or domain family.

Good context names are specific enough to decide meaning:

- `Hospital.OR_2025`
- `BPMN_2_0`
- `Theory.SpecialRelativity.SelectedEdition`
- `FactoryLineB.MaintenanceRules.2026`
- `FPF.PatternQuality.E21`

Broad labels such as "healthcare", "physics", "software", "workflow", or "architecture" are informative domain families unless they are narrowed into a bounded context with local vocabulary, invariants, the relevant role taxonomy or episteme-use/status relation set, and bridge relations.

#### A.1.1:4.2 - Context Boundary

`contextBoundary` says where local meaning holds. It can be bounded by edition, standard, organization, product line, theory, practice, regulation, contract, operating mode, or another governed boundary.

The boundary is not a document boundary by default. A document may publish a context description. The context is the semantic frame that the document describes.

#### A.1.1:4.3 - Local Vocabulary

`localVocabulary` gives local senses for terms. It does not create global meanings.

When a word crosses contexts, do not infer sameness from spelling. Use a bridge relation with direction, relation kind, fit, loss, and scope.

Example: `ticket` in an airline context may denote a travel authorization; `ticket` in an IT service context may denote a work item. Those are different local meanings unless a bridge relation is declared for a specific use.

#### A.1.1:4.4 - Local Invariant Set

`localInvariantSet` names rules that hold inside the context.

Examples:

- in a hospital operating-room context, one person cannot fill surgeon and independent auditor roles for the same case;
- in a workflow-standard context, one work item cannot move from `InProgress` to `Done` without an accepted review transition;
- in a theory context, selected postulates constrain admissible derivations.

An invariant does not become global because it is well written. Cross-context reuse requires a bridge relation or a new local declaration.

#### A.1.1:4.5 - Local Role Taxonomy

`localRoleTaxonomy` defines `U.Role` values valid in the context when system-role assignments are current. A `U.RoleAssignment` uses one context:

```text
RoleAssignment:
  holderRef:
  roleRef:
  boundedContextRef:
  windowRef?:
```

The same holder may have different role assignments in different contexts. The same role name may denote different roles in different contexts. A "global role" is not a valid shortcut; it is either a role value defined in a selected context or a wording problem to repair.

Do not put postulate, evidence, derived-claim, publication, or status distinctions into `localRoleTaxonomy` merely because ordinary language calls them "roles". When the context governs epistemic use or status, record those distinctions in `localEpistemeUseAndStatusRelationSet` and apply the direct evidence-use, source-use, status-use, claim, publication, or gate pattern.

#### A.1.1:4.6 - Bridge Relation Set

`bridgeRelationSet` records cross-context relations. A bridge is not a hidden merge. It states how a meaning, role, rule, unit, status, or claim in one context relates to one in another context.

A bridge relation should state:

```text
BridgeRelation:
  sourceContextRef:
  targetContextRef:
  sourceValueRef:
  targetValueRef:
  relationKind:
  direction:
  fit:
  loss:
  scope:
```

If a bridge cannot be stated, the cross-context use remains unsupported for that claim.

#### A.1.1:4.7 - Non-Enclosing Boundary

Do not use bounded context as an enclosing object for everything nearby. A bounded context localizes meaning; it does not automatically contain every system, document, team, work plan, source, or architecture that mentions its vocabulary.

Objects can be governed by, described under, interpreted inside, or bridged across a context without being parts of the context holon. Use the relevant slot relation for each claim.

### A.1.1:5 - Archetypal Grounding

#### A.1.1:5.1 - Hospital Operating Room Context

`Hospital.OR_2025` is a bounded context for operating-room work in a named hospital edition.

```text
BoundedContextSlotRelation:
  contextIdentity: Hospital.OR_2025
  contextBoundary: operating-room policy and procedure edition for 2025
  localVocabulary: case, sterile field, time-out, circulating nurse, independent auditor
  localInvariantSet: time-out required before incision; surgeon and independent auditor roles incompatible for one case
  localRoleTaxonomy: SurgeonRole, ScrubNurseRole, CirculatingNurseRole, IndependentAuditorRole
  bridgeRelationSet: billing-code bridge, hospital-wide staffing bridge
```

The context does not perform surgery. Systems in roles perform work. The context defines the local meanings and constraints under which those role assignments and work claims are interpreted.

#### A.1.1:5.2 - Special Relativity Context

`Theory.SpecialRelativity.SelectedEdition` is a bounded context for a selected episteme tradition.

```text
BoundedContextSlotRelation:
  contextIdentity: Theory.SpecialRelativity.SelectedEdition
  contextBoundary: selected postulates, vocabulary, reference schemes, and admissible derivations
  localVocabulary: inertial frame, proper time, Lorentz transformation
  localInvariantSet: constant light speed postulate; covariance constraints
  localRoleTaxonomy: not current for theory claims
  localEpistemeUseAndStatusRelationSet: postulate-status relation; evidence-use relation; derived-claim status relation
  bridgeRelationSet: bridge to Newtonian mechanics under low-speed approximation; bridge to general relativity under selected assumptions
```

The context frames meaning. It does not make the theory true by itself and does not act. Systems in roles publish, teach, test, or revise epistemes that use this context.

#### A.1.1:5.3 - FPF Pattern Quality Context

`FPF.PatternQuality.E21` is a bounded context for evaluating FPF pattern quality. Terms such as "recognition text", "assurance text", "semio-bias resistance", and "first-use affordability" have local meanings. A different context may use "quality" for product reliability, manufacturing yield, safety assurance, or service satisfaction.

Cross-context reuse of a quality term requires a bridge relation. Spelling alone does not carry the meaning.

### A.1.1:6 - Bias-Annotation

Lenses tested: **Onto**, **Epist**, **Prag**, **Gov**, **Arch**, **Did**.

This pattern intentionally resists:

- **global-language bias:** one spelling is treated as one meaning everywhere;
- **domain-family bias:** a broad field label is treated as if it governed local meaning;
- **enclosing-object bias:** the context is treated as a storage place or enclosing object for all related work;
- **role-globalization bias:** a role name is used without the context that defines it;
- **bridge-erasure bias:** cross-context fit and loss are hidden behind "same", "equivalent", or "mapped" language.

### A.1.1:7 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-A1.1-1` | A bounded-context claim names the `U.BoundedContext` by value; broad domain-family labels do not govern local meaning. |
| `CC-A1.1-2` | The context has a boundary, local vocabulary, local invariant set, local role taxonomy when role-assignment claims are current, and local episteme-use/status relation set when epistemic-use/status claims are current. |
| `CC-A1.1-3` | Role assignments name exactly one bounded context for interpretation. |
| `CC-A1.1-4` | Cross-context use is expressed through bridge relations with direction, relation kind, fit, loss, and scope. |
| `CC-A1.1-5` | No context-to-context containment or inheritance is inferred without an explicit bridge or governing relation. |
| `CC-A1.1-6` | Publication forms that describe a context are not treated as the context itself. |
| `CC-A1.1-7` | Time, edition, and currentness qualifiers refine the context boundary or publication, but they do not create a new context unless local meaning changes. |
| `CC-A1.1-8` | Objects interpreted inside a context are not automatically parts of the context holon. |

### A.1.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Domain as context | "Healthcare" or "physics" is used where local meaning must be decided. | Name a specific bounded context or keep the broad label informative. |
| Same spelling as sameness | A word used in two contexts is treated as equivalent. | Write a bridge relation or keep the meanings separate. |
| Context as storage place | Everything mentioned in one context is treated as part of that context. | Use the appropriate slot relation: interpreted-in, governed-by, described-under, bridged-to, or part-of. |
| Global role | "Owner", "operator", or "reviewer" is used without a context. | Name the role value and the bounded context that defines it. |
| Time as context by reflex | Design-time and run-time become separate contexts even when meaning is unchanged. | Use temporal patterns or window patterns unless the local vocabulary or invariants actually change. |

### A.1.1:9 - Consequences

Positive consequences:

- Polysemy becomes governable: meaning is local and bridgeable rather than globally guessed.
- Role assignments become inspectable because the role taxonomy is named by context.
- Local invariants stop leaking into other contexts.
- Domain-family labels remain useful for orientation without becoming false kernel objects.

Costs:

- Authors must name a context when they use polysemous terms.
- Cross-context claims need bridge relations instead of "obvious" equivalence.
- Some old context hierarchies need repair into explicit bridges or domain-family metadata.

### A.1.1:10 - Rationale

`U.BoundedContext` is the semantic companion to `U.Holon`. A holon boundary says what counts as inside or outside the whole for a claim. A bounded-context boundary says where vocabulary, invariant, role taxonomy, episteme-use/status relation set, and inference rule are locally coherent when those claims are current.

The pattern is generalized from domain-driven design but is not software-only. Scientific theories, legal standards, hospital procedures, manufacturing cells, model cards, research programs, and FPF evaluation contexts all need local meaning. FPF makes that locality an ontic rather than leaving it as "it depends."

This also protects role and episteme ontology. A `U.Role` is not global; it is valid inside a bounded context. A `U.Episteme` is meaningful only when its EntityOfConcern, viewpoint, reference scheme, and bounded context are known. Bridges then make cross-context correspondence explicit instead of letting spelling decide.

### A.1.1:11 - SoTA-Echoing

| Source family | Current lesson for A.1.1 | FPF decision |
| --- | --- | --- |
| Domain-driven design bounded-context practice. | Large models scale when meanings are local and context crossings are explicit. | Generalize bounded context beyond software into a `U.Holon` semantic frame. |
| Team-topology and socio-technical boundary practice. | Team boundaries and cognitive limits shape which meanings can remain coherent locally. | Treat stewarding systems or communities as references for a context, but do not reduce the context to the team. |
| Data mesh and interoperability practice. | Cross-domain data products need explicit interoperability relations rather than one enterprise meaning. | Use bridge relations for cross-context fit and loss. |
| FAIR, provenance, and research-object practice. | Reuse depends on explicit metadata, provenance, and interpretation context. | Keep local vocabulary and invariants explicit; publication forms do not become the context. |

Source use and currentness: domain-driven bounded-context practice is the selected practice lineage generalized beyond software; team-topology and socio-technical boundary practice are current context for stewarding-system and cognitive-boundary caution; data-mesh and interoperability practice motivate explicit bridge relations; FAIR, provenance, and research-object practice motivate interpretation context and publication-boundary discipline. Reopen A.1.1 when current practice or accepted FPF work changes the criteria for semantic locality, cross-context bridge fit and loss, local role taxonomy, local episteme-use/status relation set, or context-publication separation; do not reopen it for a new domain label, team structure, metadata format, or data product style that leaves those criteria unchanged.

### A.1.1:12 - Relations

- **Builds on:** `A.1` for `U.Holon`, `E.24` for ontic discipline, and `A.6.5` for slot relation discipline.
- **Coordinates with:** `A.15` for role-method-work alignment, `C.2.1` for episteme slot relations, `F.9` for bridge relations, `E.10` and `E.10.ARCH` for context-word repair, and `E.24.PUB` for bounded-context description and publication boundary.
- **Used by:** role assignments, episteme descriptions, characteristic spaces, architecture descriptions, method descriptions, source interpretations, and any FPF claim whose terms depend on local meaning.

### A.1.1:13 - Footer Marker

### A.1.1:End

