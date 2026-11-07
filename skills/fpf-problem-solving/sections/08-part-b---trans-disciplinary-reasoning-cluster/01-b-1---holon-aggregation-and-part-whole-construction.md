## B.1 - Holon Aggregation and Part-Whole Construction

> **Type:** Part B holonic construction pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### B.1:0 - Use This When

Use this pattern when a project needs to say how several admitted objects are considered as a whole, or when a whole-level claim depends on parts, collection belonging under the collection's own rule, component structure, constructional grounding, or a selected aggregation rule.

Typical moments:

- a product, research paper, or collection is discussed as a whole;
- a dashboard rolls part measurements into a whole-level characteristic;
- a team calls a role arrangement, method structure, or graph a decomposition, and its part-whole meaning is unclear;
- a collection needs whole-level characteristics without becoming an acting collective system;
- an aggregation claim is being used for architecture, assurance, evidence, or MHT reasoning.

**First useful move.** Identify whether the claim concerns part-whole construction, collection belonging under its own rule, or collection-as-whole grounding. For other meanings of composition, use the distinctions and supplying patterns in B.1:4.2. If claim-bearing source wording still says only “role,” use `E.10.ROLE` before choosing a branch.

**What goes wrong if missed.** Composition vocabulary and notation can conceal different relations. A role or Method may then be mistaken for a part, a Method structure for evidence of performed Work, a graph for the represented structure, or a collection for an acting whole.

**What this buys.** Use B.1 to identify a proposed whole and the relations and construction rule that ground a whole-level claim. Sections B.1:4.1–B.1:4.5 connect the required relations, evidence, and representations to their supplying patterns.

**Not this pattern when.**

- If the question is the local relation word, use `A.14`.
- If the question is constructive part-whole grounding, use `C.13`.
- If a publication choice or named current requirement elects the Working-Model assurance profile for the relation claim, use `B.3.5`.
- If the question is an exact relation among local system-role kinds, use `A.2.7`; if it is classification, assignment, or a direct participation relation, state that fact through its own pattern and predicate. Send unresolved claim-bearing “role” wording through `E.10.ROLE`. Use the Method patterns for method relation structure and `C.29` when a separate mathematical representation-choice, transfer or reliance question remains unresolved.
- If the question is performed-work occurrence parts, use `A.15.1`.
- If the question is whole reidentification or emergence-family wording, use `B.2` or `B.2.P`.

### B.1:1 - Problem Frame

Whole-level claims require identified objects and a grounded account of their part or collection relations. Mathematical and computational representations can express or check that account; their notation alone establishes neither holon identity nor parthood.

### B.1:2 - Problem

When these distinctions are missed:

1. **Mereology and notation collapse.** A graph or algebra is treated as the part-whole structure itself.
2. **Roles and methods become parts.** Role factors, method parameters, guards, steps, and compositions are read as holonic parts because the same word "decomposition" appears.
3. **Work occurrence is inferred from plan.** A method decomposition or schedule is treated as evidence that performed work had those parts.
4. **Collections become acting systems.** A set, list, batch, fleet, or community is treated as an admitted acting System or responsibility bearer from plural naming, a system-role kind or assignment, a Method, or Work. Admission of the acting collective remains an A.1 question; responsibility also needs the predicate, participants, and pattern or rule that defines it.
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
  candidateWholeRef: U.Entity
  candidatePartRefs:
  aggregationPolicyRef?
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  identityOrRecognitionRule:
  partRelationRefs:
  constructionBasisRef?
  selectedStructureRef?
  wholeLevelCharacteristicRefs?
  assuranceGroundingRef?
  neighboringNonPartRelationRefs?
  mathLensOrRepresentationRef?
```

This claim frame identifies the objects, relations, and qualifications needed to rely on the aggregation claim. Include optional fields when they change that claim or its use.

Use:

- `A.14` for `ComponentOf`, `ConstituentOf`, `PortionOf`, `PhaseOf`, collection belonging under the collection's own rule, aspect, and related vocabulary;
- `C.13` for constructional grounding through its sum, set or slice accounts;
- `B.3.5` when a publication choice or named current requirement elects its assurance profile for the relation claim;
- `C.16` when the current output is a whole-level characteristic;
- `A.1` and `A.15` when the whole is claimed to be an acting collective system.

#### B.1:4.2 - Didactic Firewall

| Source claim | Ontology-side recovery | Subject pattern |
| --- | --- | --- |
| "This object is made of these parts." | Identify the candidate whole and constituents and establish the part relations and construction rule. When holonhood is claimed, apply all six A.1 components and the direct kind-specific conditions. | `A.1` for holon recognition, `A.14`, `C.13`; `B.3.5` when a publication choice or named current requirement elects its assurance profile. |
| "These items belong to this collection." | The collection's own belongs-to rule or collection-as-whole grounding; no `ComponentOf` inference. | `A.14`, `C.13`, `C.16` for a collection-level or whole-level characteristic. |
| “This role is combined from role factors.” | Unresolved source wording. It may mean an exact relation among local system-role kinds, a classification or assignment, a direct participation relation, a naming question, or ordinary prose; none is holonic parthood by default. | `E.10.ROLE` first; then `A.2.7` only for the exact relation among local system-role kinds, or the direct pattern for the recovered classification, assignment, participation, or naming claim; use `C.29` when a separate mathematical representation-choice, transfer or reliance question remains unresolved. |
| "This method has steps, parameters, guards, or variants." | Method relation structure, method family, method description, or work plan; not performed work by default. | `A.15`, Method patterns, `C.29` when a separate mathematical representation-choice, transfer or reliance question remains unresolved. |
| "This run contained episodes or concurrent sub-runs." | Work occurrence holarchy with timing, evidence, occurrence identity, and work-part relation. | `A.15.1`, temporal pattern, evidence-use pattern. |
| "This graph or algebraic notation represents the structure." | Mathematical or representation description of a selected structure. | `A.22` and the applicable architecture or description pattern; `C.29` when a separate mathematical representation-choice, transfer or reliance question remains unresolved. |
| "The whole shows emergence." | Check applicable explanations within the existing whole first. Use B.2 when changed facts leave a consequential question about whether that whole remains sufficient or a new whole is required. | `B.2`, `B.2.P`, or the direct characteristic, measurement, architecture, capability, or Work pattern. |

#### B.1:4.3 - Work Occurrence Holarchy

A Method's composition and the parts of a performed Work require different grounds.

A dated Work may have independently admitted temporal or operational parts under `A.15.1`. C.27 governs temporal claims, and B.1.4 aggregates recovered order or temporal relations when that is the question. Resource roll-ups use B.1.6; composing effects needs the direct relation and composition rule for those effects. Neither kind of calculation establishes Work parthood or makes a Method or role expression a holonic part.


#### B.1:4.4 - Mathematical And Representation Apparatus

Before using Γ notation or another aggregation representation, name the object and selected relation.

Acceptable uses:

- a mathematical lens for a selected structure;
- a constructional expression for a part-whole claim already admitted by A.14 and C.13;
- a representation of dependency relations;
- a checking apparatus for invariants or conservative bounds.

Blocked uses:

- graph wording as parthood admission;
- algebraic factorization as role, method, or work parthood admission;
- source notation as a new U-kind;
- one fold rule as a universal replacement for the subject pattern.

#### B.1:4.5 - Existing-Whole Before MHT

To assess whether changed facts require a different whole for the receiving use, first consider applicable explanations within the existing whole, such as:

- better parts;
- corrected part relation;
- improved measurement;
- role or method relation repair;
- work occurrence evidence repair;
- a correction to the selected functional or architectural structure;
- source, publication, or representation correction.

If a supported explanation is sufficient for the receiving use, keep the existing whole and stop. Use B.2 when changed facts leave a consequential question about whether that whole remains sufficient or a new whole is required; retain an unresolved comparison when its deciding grounds are missing.

### B.1:5 - Archetypal Grounding (Worked Cases)

#### B.1:5.1 - Pump Skid

A pump skid can be a `U.System` holon whose parts include pumps, valves, controller, frame, and connectors.

B.1 recovers the holon aggregation claim. A.14 names component or portion relations. C.13 gives constructional grounding. C.16 carries whole-level characteristics such as maximum flow or pressure envelope. A drawn graph represents the selected dependencies or other structure of the skid.

#### B.1:5.2 - Evidence Corpus

A corpus can be a collection under its own inclusion rule and a C.13 set account. This alone does not make it a holon. Treat an integrated claim-bearing corpus as a whole only after all six A.1 matters pass, including constructive part relations, assembly, a composition-grounded whole characteristic, and possible participation in a larger assembly. Coverage, source freshness, bias exposure, or evidential diversity may be collection-level characteristics without settling that stronger question.

The corpus does not become an acting system. A review board, running review tool, or research team may instead be admitted as a System. If the current claim says only that it takes part in ordinary review or analysis, state the direct participation relation and stop there. If it says that the System performed admitted `U.Work`, recover that performer's A.13 core and independently admit the Work under A.15.1. Add F.6 afterward only when the B.1 claim also needs precise assignment-bound attribution. A short B.1 sentence may omit an unused assignment identifier only when every relation it consumes remains recoverable. A local kind and a separate System-classification judgment remain independently optional. The corpus may be an episteme or publication-side object under its subject patterns.

#### B.1:5.3 - Method With Steps

A machining method has ordered steps and parameters. Those steps are method relation or method-description material. They do not prove that a performed machining run occurred, nor that the run had the same parts.

If the current claim is the method structure, use Method patterns. Use C.29 when a separate mathematical representation-choice, transfer or reliance question remains unresolved. If the current claim is the actual run, use A.15.1.

### B.1:6 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Apparatus as ontology | A user infers the object kind from the form of a graph or other representation. | Recover the holon, relation, selected structure, and mathematical-lens use separately. |
| Decomposition as parthood | Source “role” factors, method steps, phases, or work episodes are treated as holonic parts by label. | Use `E.10.ROLE` when the role wording is unresolved, then the direct pattern for the recovered relation; use the Method, temporal, Work, or part-whole pattern for the other claims. |
| Collection as acting whole | A set, list, batch, fleet, or community receives agency or responsibility by plural naming. | Recover who or what belongs under the collection's own rule and the collection account, or admit the actual collective System under A.1. State responsibility separately by naming its predicate, participants, applicability, and occurrence identity; if no pattern or rule defines the needed claim, return that gap. |
| Emergence rhetoric | "More than the sum" replaces existing-whole explanation. | Check applicable existing-whole explanations; use B.2 only for a consequential question that remains about keeping or reidentifying that whole. |

### B.1:7 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-B1-1` | The current claim identifies whether it is part-whole, collection belonging under the collection's own rule, collection-as-whole, a relation among local system-role kinds, classification, assignment, direct participation, method relation, work occurrence holarchy, selected structure, or mathematical description; unresolved claim-bearing “role” wording is sent through `E.10.ROLE`. |
| `CC-B1-2` | Part-whole claims name the exact whole and part participants, identity or recognition rule, part relation, constructional predicate and its defining pattern, plus any aggregation policy, selected structure, ClaimScope, or qualification window that changes the claim. |
| `CC-B1-3` | A.14 defines the relation vocabulary used here; C.13 defines the construction accounts. |
| `CC-B1-4` | Relations among local system-role kinds, classifications, assignments, direct participation relations, and Method relation structures are not treated as holonic parts merely because a label, graph, algebra, or naming convention composes them. `A.2.7` is used only for the first of those branches. |
| `CC-B1-5` | Performed work occurrence parts require A.15.1. |
| `CC-B1-6` | Mathematical and representation apparatus is named as lens or expression, not as ontology by spelling. |
| `CC-B1-7` | B.2 is selected when changed facts leave a consequential existing-whole versus new-whole question. A sufficient existing-whole explanation ends that inquiry; missing deciding grounds leave the comparison unresolved. |


### B.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Gamma as head ontology | Γ is treated as the thing that makes all wholes. | Recover the ontology-side claim first; use Γ only as constructional or mathematical apparatus when selected. |
| Graph as structure | A diagram or graph is treated as the part-whole structure. | Name the selected structure and relation pattern; keep the graph as representation or math lens. |
| Method as work | A method decomposition is used as evidence that work occurred. | Use A.15.1 for performed-work occurrence and evidence. |
| Collection as acting whole | A list or pool decides, acts, or bears responsibility. | Recover who or what belongs under the collection's own rule or its collection-as-whole account, or admit the actual collective System under A.1. A system-role kind, assignment, Method, or Work does not establish responsibility; name the predicate and the pattern or rule that defines it, or state that this is missing. |
| Emergence by narrative | "More than the sum" replaces existing-whole analysis. | Check applicable existing-whole explanations; stop when sufficient for the receiving use, or use B.2 for the consequential whole-identity question that remains. |

### B.1:9 - Consequences

Positive consequences:

- Users can combine aggregation notation with an independently grounded account of the objects and relations.
- Part-whole claims expose their objects, relations, and construction grounds for review.
- Role, Method, Work, mathematical-lens, and publication descriptions remain distinguishable from part-whole claims.
- Whole reidentification has an explicit entry condition for B.2.

Costs:

- Users must identify the claim kind before choosing a notation.
- Further grounds depend on the claim: work occurrence evidence uses `A.15.1`; work-resource aggregation uses `B.1.6`; an unresolved mathematical representation-choice, transfer or reliance question uses `C.29`. Use `B.2.P` for unresolved emergence-family wording and `B.2` when changed facts leave a consequential existing-whole versus new-whole question.

### B.1:10 - Rationale

Whole-level reasoning relies on accepted part-whole relations, constructional grounding, and the applicable subject patterns. This supports reasoning across different kinds of objects while retaining their own admission and relation rules.

Mathematical apparatus remains available. Once the governed object is known, a graph can represent dependencies, an algebra can express selected composition rules, a tuple can express a slot relation, and a matrix or embedding can support analysis. Use C.29 when a separate mathematical representation-choice, transfer or reliance question remains unresolved.

### B.1:11 - SoTA-Echoing

For the question "does a collection-level calculation warrant treating the collection as a holon?", B.1 uses A.1:4.2's recognition criterion, A.14:4's distinction between belonging and parthood, and C.13:4.1's construction accounts. A collection account and a holon account support different claims; use the lighter account when it supplies the receiving result.

The corpus in B.1:5.2 makes the comparison concrete. Its coverage or diversity can be assessed under the collection's inclusion and characteristic rules while constructive part relations and assembly remain unestablished. Those same collection facts remain insufficient for a holon claim under A.1, even if the aggregate value is correct. B.1:4.1–4.2 therefore preserve the collection result and require the six constructive components and kind-specific conditions for the stronger holon claim. In the pump-skid case, independently grounded component relations and assembly supply the corresponding part-whole basis.

This conceptual comparison settles which account these FPF claims require, with the additional construction and recognition burden made explicit for a holon claim. It does not rank external ontology or engineering methods. Reopen the choice of account when the receiving claim, construction facts or applicable identity criterion changes.

### B.1:12 - Relations

- **Builds on:** `A.1` for holon recognition, `A.14` for relation vocabulary, and `C.13` for constructional grounding. Use `B.3.5` for Working-Model assurance grounding when a publication choice or named current requirement elects that profile.
- **Coordinates with:** `A.15` and `A.15.1` for method and work, `A.22` and `C.30` for selected structure and architecture, `C.16` for whole-level characteristics, `C.29` for mathematical lenses, and `B.2` for whole reidentification.
- **Refined by:** `B.1.1`, `B.1.2`, `B.1.4`, and `B.1.6` for selected dependency, system aggregation, contextual-temporal aggregation, and work-resource aggregation cases.

### B.1:End
