## D.3 - Interlevel Ethical Conflict Structure

> **Type:** D-family ethical conflict-structure pattern
> **Status:** Stable
> **Pattern role:** This compact pattern owns the structure of an interlevel ethical conflict; mediation, decision use, assurance, causal use, and architecture residuals remain with their direct owners.

**Use this when.** Use this pattern when an ethical conflict spans declared levels or scopes and the conflict structure itself must be made inspectable before mediation, decision, assurance, or architecture return.

**Not this pattern when.** If only the ethical value frame is missing, use `D.1`. If only entry recognition is needed, use `D.2`. If the conflict structure is already mapped and the current question is mediation or decision use, use `D.4`. If the question is bias, fairness, impact audit, causal-fairness audit consumption, or ethical assurance, use `D.5`.

**What goes wrong if missed.** The team debates values or decisions before it has named the levels or scopes, carriers, harms, benefits, evidence, and residuals that actually conflict.

**What this buys.** The conflict becomes an inspectable structure that `D.4`, `D.5`, assurance, causal, and architecture owners can use without guessing.

### D.3:1 - Problem Frame

Interlevel ethical conflict is not just disagreement between people. It may involve a system part and a whole, a person and an organization, one organization and a community, a project and a society, a collection and its members, an episteme family and the decisions it shapes, or an architecture move and the holon levels it affects.

The central move is structural: name what is in conflict, at which declared levels or scopes, through which methods, work, transformations, role assignments, evidence, value concerns, and consequence horizons. Do not turn the conflict into publication wording, assurance claim, or architecture residual unless that is the current governed object.

### D.3:1.0 - Problem

Interlevel ethical conflict is often debated before it is structured. The failure is to argue over values or decisions while the affected objects, declared levels or scopes, value frames, methods, work, transformations, evidence, uncertainty, thresholds, and consequence horizons remain implicit.

### D.3:1.1 - Forces

| Force | Tension |
| --- | --- |
| Conflict structure vs. decision use | The conflict must be inspectable before D.4 can mediate, refuse, or authorize a bounded decision. |
| Level and scope plurality vs. fixed ladder | The case may involve persons, teams, organizations, communities, systems, epistemes, or environments without one universal hierarchy. |
| Ethical object vs. representation | Tables, graphs, narratives, and formal predicates can describe a conflict, but are not the conflict itself. |
| Responsibility threshold vs. agency label | Agency or responsibility may depend on thresholds and evidence; a label such as organization, public, market, or AI is not enough. |
| Architecture residual vs. ethical conflict | A cross-scope structure can be architectural, ethical, or both; owner assignment must follow the current claim. |

### D.3:2 - Solution

Record an `InterlevelEthicalConflictStructure@Context`:

```text
InterlevelEthicalConflictStructure@Context:
  conflictConcernRef
  boundedContextRef
  affectedEntityOfConcernRefs
  declaredLevelOrScopeRefs
  affectedHolonRefs
  affectedEpistemeRefs?
  collectionOrMembershipRelationRefs?
  partWholeRelationRefs?
  roleAssignmentRefs
  interestOrConcernRefs
  valueFrameRefs
  agencyOrResponsibilityThresholdRefs?
  methodOrWorkRefs?
  transformationRefs?
  evidenceRefs
  uncertaintyRefs
  consequenceHorizonRefs
  conflictRelationRefs
  nonConflictOverread
  nextUseOwnerRef
```

This structure may be represented by a table, graph, formal predicate, narrative case, or another selected description form. The representation is not the conflict itself. If a mathematical lens does work in the claim, cite `C.29`; if the publication form changes admissible use, cite `E.17`.

### D.3:3 - Collection and Episteme Cases

A collection is ethically current only when whole-level characteristics, membership relations, environment-mediated effects, or aggregate consequences matter. Use `A.14` for part-whole and membership relation vocabulary and `C.13` for constructive grounding. Do not assign responsibility to a collection merely because it has a plural name.

An episteme is ethically current when its claim-bearing structure, source-use relation, publication relation, described EntityOfConcern, or model family changes affected systems or decisions. Use `C.2.1` for the episteme slot relation and `E.17` for publication claims. Do not turn every ethical conflict over a theory, standard, architecture description, or policy description into a problem about wording.

### D.3:4 - Boundaries

| Do this in D.3 | Do not do this in D.3 |
| --- | --- |
| State the declared levels or scopes that make the conflict interlevel. | Invent `U.Level`, `U.Frustration`, or `U.Emergence`. |
| Name affected holons, systems, epistemes, collections, roles, methods, work, transformations, evidence, and value concerns. | Treat a source label such as "society", "organization", "AI", "ecosystem", or "standard" as enough. |
| Keep conflict structure separate from mediation and decision use. | Choose the compromise, refusal, or override. |
| Return architecture residuals to `C.30.ILC` when architecture structure is current. | Make ethics the owner of every cross-scope architecture problem. |
| Return bias, fairness, impact audit, and ethical assurance to `D.5`. | Rebuild D.5 inside the conflict map. |

### D.3:5 - Archetypal Grounding (Worked Slices)

**Engineering advice.** A consultant improves the effectiveness of a client's harmful project. The conflict is not only "bad client, good method." `D.3` maps the client organization, affected public, consultant role assignment, method, work occurrence, responsibility threshold, evidence uncertainty, and consequence horizon. `D.4` governs refusal, conditions, escalation, or decision use.

**Collection case.** A fleet-level optimization reduces maintenance cost but increases failure risk for a small subfleet used in harsher conditions. `D.3` names the fleet, subfleet, membership relation, affected users, evidence set, value concerns, and consequence horizon. It does not infer that the fleet is a responsible super-holon unless an admitted pattern allows that claim.

**Episteme case.** A published architecture description normalizes an interface assumption that excludes an alternative implementation option. The ethical conflict may involve the episteme whole, its source-use relation, affected suppliers, and system consequences. `D.3` maps the conflict; `C.30.AD` governs architecture-description adequacy and `E.17` governs publication-use claims.

### D.3:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Debate replaces structure | The team argues about values before naming the affected objects and relations. | Fill the conflict structure before mediation. |
| Representation becomes conflict | A diagram, matrix, or narrative is treated as the ethical conflict itself. | Separate the conflict EntityOfConcern from the selected description form. |
| Collective name becomes responsibility | Organization, society, public, market, or AI is treated as responsible by label. | Name the holon, collection, role assignment, agency or responsibility threshold, and evidence. |
| Architecture absorbs ethics | Cross-scope residual wording hides value, harm, responsibility, or admissible sacrifice. | Use architecture owners for selected structures and `D.3` and `D.4` when ethical conflict is current. |

### D.3:6 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-D3-1 | The conflict names affected EntityOfConcern refs, declared levels or scopes, value frames, evidence, and consequence horizons. | Makes the conflict structure inspectable. |
| CC-D3-2 | Collection, episteme, part-whole, membership, method, work, and transformation refs use their direct owners when those claims are current. | Prevents ethical conflict from absorbing ontology. |
| CC-D3-3 | `nextUseOwnerRef` distinguishes mediation, decision use, assurance, causal use, architecture residual, and bias, fairness, or impact audit. | Keeps D.3 separate from neighboring use patterns. |
| CC-D3-4 | The representation of the conflict is not treated as the conflict itself. | Prevents semio-bias in ethical conflict maps. |

### D.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Political label as structure | The conflict is named by a slogan such as society versus innovation. | Name the affected EntityOfConcern refs, levels or scopes, value frames, and evidence. |
| Actor by plural noun | A collection is made responsible because its name is plural or institutional. | Recover membership, part-whole, role assignment, and agency or responsibility threshold relations. |
| Description-only conflict | The case becomes a problem about wording of a report, model, or standard. | Keep episteme and publication-use claims with their owners while mapping the affected systems or decisions. |
| Mediation inside map | The conflict map chooses the compromise. | Stop at structure; D.4 owns mediation or decision use. |

### D.3:7 - Consequences

This pattern gives `D.4`, `D.5`, `B.3`, `C.28`, `A.10`, `C.11`, and `C.30.ILC` a conflict structure they can use without stealing the ethical object. The cost is that conflicts cannot be waved through by a slogan. The gain is that mediation and decision work start from a typed structure rather than from a politically convenient label.

### D.3:9 - Rationale

`D.3` provides the typed structure that ethical mediation, assurance, causal, architecture, and bias-audit patterns can use. Without it, D.4 receives slogans rather than inspectable conflicts; D.5 receives fairness claims without affected scopes; architecture receives value conflict disguised as residual; and evidence patterns receive claims with no declared consequence horizon.

The pattern therefore focuses on the conflict EntityOfConcern: affected objects, declared levels or scopes, value frames, role assignments, methods, work, transformations, evidence, uncertainty, thresholds, and consequence horizons. It keeps descriptions of the conflict useful but secondary.

### D.3:10 - SoTA-Echoing

| Source line | Practical implication for this pattern |
| --- | --- |
| Multilevel ethics and systems thinking | Ethical conflict often crosses declared levels or scopes through methods, work, transformations, role assignments, evidence, value concerns, and consequence horizons; the case must show which relations actually conflict. |
| Collective agency and responsibility debates | Collection, organization, public, or community names require grounding in holon, membership, role assignment, agency or responsibility threshold, and evidence before responsibility is assigned. |
| Constructive and episteme ontology | Conflicts can involve systems, collections, work occurrences, bounded contexts, disciplines, and epistemes; description and publication forms remain owners of description and publication claims, not substitutes for affected EntityOfConcern. |
| FPF architecture-residual discipline | Cross-scope architecture residual and interlevel ethical conflict can coincide; D.3 maps ethical conflict while `C.30.ILC` owns architecture residual triage. |

### D.3:11 - Relations

- Builds on `D.1` and `D.2` for value-frame boundary and multilevel entry.
- Builds on `A.1`, `A.14`, `B.1`, and `C.13` for holons, part-whole, membership, collections, and constructive grounding.
- Coordinates with `D.4` for mediation and decision use.
- Coordinates with `D.5` for bias, fairness, impact audit, causal-fairness audit consumption, and ethical assurance.
- Coordinates with `C.2.1` and `E.17` for episteme and publication-use claims.
- Coordinates with `C.30.ILC`, `A.10`, `B.3`, `C.28`, and `C.29` when architecture residual, evidence, assurance, causal, or mathematical-lens claims are current.

### D.3:End

