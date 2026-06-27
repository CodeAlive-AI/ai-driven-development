## B.1 - Holon Aggregation and Part-Whole Construction

> **Type:** Part B holonic construction pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### B.1:0 - Use This When

Use this pattern when a project needs to say how several admitted objects are considered as a whole, or when a whole-level claim depends on parts, membership, component structure, constructional grounding, or a selected aggregation rule.

Typical moments:

- a product, plant, dataset, paper, model family, organization, fleet, batch, or research program is discussed as a whole;
- a dashboard rolls part measurements into a whole-level characteristic;
- a team says that a method, role, graph, or algebra "decomposes" something and may be smuggling part-whole claims;
- a collection needs whole-level characteristics without becoming an acting collective system;
- an aggregation claim is being used for architecture, assurance, evidence, or MHT reasoning.

**First useful move.** Recover the claim kind before choosing notation: part-whole construction, membership, collection-as-whole grounding, role relation structure, method relation structure, work occurrence holarchy, selected architecture structure, or mathematical description.

**What goes wrong if missed.** Γ, graph, algebra, decomposition, factor, component, step, phase, and collection wording become one universal composition language. Roles and methods become parts; work occurrence evidence is inferred from method structure; a graph is mistaken for the structure; a collection becomes an acting whole by label.

**What this buys.** B.1 gives one doorway into part-whole construction while keeping its neighbors clean: A.14 owns relation vocabulary, C.13 owns constructional grounding, B.3.5 owns Working-Model assurance grounding, A.15.1 owns work-occurrence holarchy, and C.29 owns mathematical-lens use.

**Not this pattern when.**

- If the question is the local relation word, use `A.14`.
- If the question is constructive part-whole grounding, use `C.13`.
- If the question is assurance grounding for a working model, use `B.3.5`.
- If the question is role or method relation structure, use the role or method owner and `C.29` when a mathematical lens is relied on for the current claim.
- If the question is performed-work occurrence parts, use `A.15.1`.
- If the question is whole reidentification or emergence-family wording, use `B.2` or `B.2.P`.

### B.1:1 - Problem Frame

B.1 is not a universal algebra pattern. It is the holonic construction doorway for part-whole and collection-as-whole claims.

The older Γ material remains useful only after the ontology-side claim has been recovered. Γ, graph, algebra, tuple, matrix, embedding, and neural representation can express or check a selected structure; they do not decide by spelling that the current object is a holon, that the relation is parthood, or that a role, method, step, or work occurrence is a part of a holon.

### B.1:2 - Problem

Without B.1:

1. **Mereology and notation collapse.** A graph or algebra is treated as the part-whole structure itself.
2. **Roles and methods become parts.** Role factors, method parameters, guards, steps, and compositions are read as holonic parts because the same word "decomposition" appears.
3. **Work occurrence is inferred from plan.** A method decomposition or schedule is treated as evidence that performed work had those parts.
4. **Collections become acting systems.** A set, list, batch, fleet, or community receives agency, responsibility, or capability without A.1 and role-method-work admission.
5. **Emergence becomes rhetoric.** A whole-level gain is explained by "synergy" or "more than the sum" without checking existing-whole explanations or B.2 whole reidentification.

### B.1:3 - Forces

| Force | Tension |
| --- | --- |
| Part-whole usefulness vs ontology explosion | FPF needs whole-level reasoning without minting a U-kind for every composed expression. |
| Constructional grounding vs math convenience | Algebra and graphs can make checks precise, but only after the ontology-side object and relation are selected. |
| Collection value vs false collective agency | Collections can have useful whole-level characteristics without becoming acting systems. |
| Method planning vs performed work | A method can guide expected decomposition; work occurrence parts require actual occurrence identity, timing, and evidence. |
| Emergence recognition vs ordinary repair | Some whole-level gains require B.2; many are explained inside the existing whole by ordinary part, method, measurement, or architecture repair. |

### B.1:4 - Solution

Use B.1 as a discriminator and construction frame.

#### B.1:4.1 - Holon Aggregation Claim Frame

When part-whole construction is current, recover:

```text
HolonAggregationClaim@Context:
  candidateWholeRef: U.Holon
  candidatePartRefs:
  boundedContextRef:
  identityOrRecognitionRule:
  partRelationRefs:
  constructionBasisRef?
  selectedStructureRef?
  wholeLevelCharacteristicRefs?
  assuranceGroundingRef?
  neighboringNonPartRelationRefs?
  mathLensOrRepresentationRef?
```

This is a claim frame, not a U-kind and not an acting record. It says what must be named before the aggregation claim is relied on.

Use:

- `A.14` for `ComponentOf`, `ConstituentOf`, `PortionOf`, `PhaseOf`, `MemberOf`, aspect, and related vocabulary;
- `C.13` for constructional grounding such as sum, set, slice, or another accepted construction;
- `B.3.5` when a working model relies on the part-whole claim for assurance or evidence;
- `C.16` when the current output is a whole-level characteristic;
- `A.1` and `A.15` when the whole is claimed to be an acting collective system.

#### B.1:4.2 - Didactic Firewall

| Source claim | Ontology-side recovery | Direct owner |
| --- | --- | --- |
| "This object is made of these parts." | Part-whole construction over admitted holons. | `A.1`, `A.14`, `C.13`, `B.3.5` when assurance is current. |
| "These members form a collection." | Membership or collection-as-whole grounding; no `ComponentOf` inference. | `A.14`, `C.13`, `C.16` for whole-level characteristic. |
| "This role is combined from role factors." | Role relation structure or role naming; not holonic parthood by default. | `A.2.7`, role patterns, `C.29` if mathematical lens is selected. |
| "This method has steps, parameters, guards, or variants." | Method relation structure, method family, method description, or work plan; not performed work by default. | `A.15`, method owners, `C.29` if mathematical lens is selected. |
| "This run contained episodes or concurrent sub-runs." | Work occurrence holarchy with timing, evidence, occurrence identity, and work-part relation. | `A.15.1`, temporal owner, evidence owner. |
| "This graph or algebraic notation represents the structure." | Mathematical or representation description of a selected structure. | `C.29`, `A.22`, architecture or description owner. |
| "The whole shows emergence." | Existing-whole explanation first; B.2 only when the whole itself must be reidentified. | `B.2`, `B.2.P`, or the direct characteristic, measurement, architecture, capability, or work owner. |

#### B.1:4.3 - Work Occurrence Holarchy

Performed work is different from structural composition.

A work occurrence can have temporal parts, episode parts, operational parts, concurrent sub-runs, retries, resource roll-ups, and effect composition. That is a work-occurrence holarchy governed by `A.15.1`, not evidence that the method or role expression is a holonic part-whole structure.

Use A.15.1 when the claim needs occurrence identity, temporal coverage, `Gamma_time`, `Gamma_work`, episode policy, overlap policy, resource aggregation, or performed-work evidence.

#### B.1:4.4 - Mathematical And Representation Apparatus

Use Γ, graph, algebra, tuple, matrix, embedding, or neural representation only after the object under concern and selected relation are named.

Acceptable uses:

- a mathematical lens for a selected structure;
- a constructional expression for a part-whole claim already admitted by A.14 and C.13;
- a representation of dependency relations;
- a checking apparatus for invariants or conservative bounds.

Blocked uses:

- graph wording as parthood admission;
- algebraic factorization as role, method, or work parthood admission;
- source notation as a new U-kind;
- one fold rule as a universal replacement for the direct owner.

#### B.1:4.5 - Existing-Whole Before MHT

Before declaring B.2 whole reidentification, ask whether the whole-level gain can be explained inside the existing whole:

- better parts;
- corrected part relation;
- improved measurement;
- role or method relation repair;
- work occurrence evidence repair;
- functional or architecture selected-structure repair;
- source, publication, or representation correction.

Use B.2 only when the whole itself must be reidentified.

### B.1:5 - Archetypal Grounding (Worked Cases)

#### B.1:5.1 - Pump Skid

A pump skid can be a `U.System` holon whose parts include pumps, valves, controller, frame, and connectors.

B.1 recovers the holon aggregation claim. A.14 names component or portion relations. C.13 gives constructional grounding. C.16 carries whole-level characteristics such as maximum flow or pressure envelope. If a graph is drawn, it represents a selected dependency or structure; the graph is not the skid.

#### B.1:5.2 - Evidence Corpus

A corpus can be a collection-as-whole under `MemberOf` and C.13 set construction. Its whole-level characteristics may include coverage, source freshness, bias exposure, or evidential diversity.

The corpus does not become an acting system. A review board, script, or research team may be an acting system in role. The corpus may be an episteme or publication-side object under direct owners.

#### B.1:5.3 - Method With Steps

A machining method has ordered steps and parameters. Those steps are method relation or method-description material. They do not prove that a performed machining run occurred, nor that the run had the same parts.

If the current claim is the method structure, use method owners and C.29 when algebra is selected. If the current claim is the actual run, use A.15.1.

### B.1:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Apparatus as ontology | Graph, algebra, tuple, matrix, embedding, or Gamma notation decides the object kind by spelling. | Recover the holon, relation, selected structure, and mathematical-lens use separately. |
| Decomposition as parthood | Role factors, method steps, phases, or work episodes are treated as holonic parts by label. | Use the direct owner for role, method, temporal, work, or part-whole claims. |
| Collection as acting whole | A set, list, batch, fleet, or community receives agency or responsibility by plural naming. | Recover collection grounding, whole-level characteristic, or acting collective system under direct owners. |
| Emergence rhetoric | "More than the sum" replaces existing-whole explanation. | Test measurement, architecture, role, method, work, and evidence explanations before B.2 whole reidentification. |

### B.1:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-B1-1` | The current claim identifies whether it is part-whole, membership, collection-as-whole, role relation, method relation, work occurrence holarchy, selected structure, or mathematical description. |
| `CC-B1-2` | Part-whole claims name admitted holons, bounded context, identity or recognition rule, part relation, and constructional owner. |
| `CC-B1-3` | A.14 and C.13 remain direct owners for relation vocabulary and constructive grounding. |
| `CC-B1-4` | Role and method relation structures are not treated as holonic parts merely because a label, graph, algebra, or naming convention composes them. |
| `CC-B1-5` | Performed work occurrence parts return to A.15.1. |
| `CC-B1-6` | Mathematical and representation apparatus is named as lens or expression, not as ontology by spelling. |
| `CC-B1-7` | B.2 is used only when the whole itself must be reidentified after existing-whole explanations fail. |
| `CC-B1-8` | No generic `U.Boundary`, `U.Interaction`, `U.Level`, `U.Emergence`, or `U.Frustration` is introduced by aggregation wording. |

### B.1:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Gamma as head ontology | Γ is treated as the thing that makes all wholes. | Recover the ontology-side claim first; use Γ only as constructional or mathematical apparatus when selected. |
| Graph as structure | A diagram or graph is treated as the part-whole structure. | Name the selected structure and relation owner; keep the graph as representation or math lens. |
| Method as work | A method decomposition is used as evidence that work occurred. | Use A.15.1 for performed-work occurrence and evidence. |
| Collection as acting whole | A list or pool decides, acts, or bears responsibility. | Recover membership, collection-as-whole, whole-level characteristic, or acting collective system under direct owners. |
| Emergence by narrative | "More than the sum" replaces existing-whole analysis. | Check existing-whole explanations before B.2. |

### B.1:8 - Consequences

Positive consequences:

- B.1 can still use useful aggregation apparatus without letting apparatus choose the ontology.
- Holonic part-whole claims become reviewable.
- Role, method, work, math-lens, and publication descriptions stop leaking into mereology.
- B.2 has a cleaner entry condition: whole reidentification, not ordinary improvement rhetoric.

Costs:

- Users must identify the claim kind before choosing a notation.
- Some Gamma-heavy examples require a direct owner before the notation is used: work occurrence evidence uses `A.15.1`, work-resource aggregation uses `B.1.6`, mathematical-lens reliance uses `C.29`, and whole reidentification first uses `B.2.P` and then `B.2` when the problem remains current.
- Work occurrence analysis requires evidence and timing, not just a method plan.

### B.1:9 - Rationale

The practical force of B.1 is conservative. Whole-level reasoning is useful, but it must be grounded in accepted part-whole relations, constructional discipline, and direct pattern ownership. This lets FPF speak across physical systems, epistemes, work occurrences, bounded contexts, disciplines, and collections without growing a new type for every composed expression.

Mathematical apparatus remains available. It becomes more useful after the governed object is known: graph for dependency representation, algebra for selected composition rules, tuple for slot relation expression, matrix or embedding for analysis, and C.29 when a mathematical lens is relied on for the current claim.

### B.1:10 - SoTA-Echoing

| Source family | Current lesson for B.1 | FPF decision |
| --- | --- | --- |
| Constructional ontology and applied ontology practice | Whole identity, dependency, and construction need explicit grounding rather than unrestricted composition. | B.1 requires A.14 relation vocabulary and C.13 constructional grounding before part-whole claims are relied on. |
| Systems engineering and digital engineering practice | Whole-level characteristics and architecture views need traceable part relations and selected structures. | B.1 separates part-whole construction from selected-structure descriptions, dashboards, and mathematical representations. |
| Method and process-modeling traditions | Plans, procedures, and performed occurrences are often conflated. | Method relation structure remains with method owners; performed-work holarchy remains with A.15.1. |
| Emergence and holonic systems practice | Genuine whole-level novelty must be distinguished from measurement, architecture, role, method, or work repair. | B.2 owns whole reidentification after existing-whole explanations are tested. |

### B.1:11 - Relations

- **Builds on:** `A.1` for holon admission, `A.14` for relation vocabulary, `C.13` for constructional grounding, and `B.3.5` for Working-Model assurance grounding.
- **Coordinates with:** `A.15` and `A.15.1` for method and work, `A.22` and `C.30` for selected structure and architecture, `C.16` for whole-level characteristics, `C.29` for mathematical lenses, and `B.2` for whole reidentification.
- **Refined by:** `B.1.1`, `B.1.2`, `B.1.4`, and `B.1.6` for selected dependency, system aggregation, contextual-temporal aggregation, and work-resource aggregation cases.

### B.1:End

