## C.36.P - Cultural-Evolution Wording-Use Precision Restoration

> **Tech-name:** `CulturalEvolutionWordingUsePrecisionRestoration`
> **Plain-name:** cultural-evolution wording-use precision restoration
> **Type:** Precision-restoration companion pattern (C)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part C -> C.36 companion
> **Builds on:** `E.10`, `E.10.ARCH`, `E.10.DEV`, `E.10.ROLE`, `C.36`, `F.17`, `F.18`, `F.9`, `A.3.1`, `A.3.2`, `A.15`, `C.18`, `C.19`, `G.5`, and `G.11`.
> **Purpose:** recover the object, relation, or claim hidden by culture, style, tradition, genre, scene, practice, technique, platform, regime, attractor, or developmental-machinery wording, then return to the project question without turning the label into ontology.

### C.36.P:0 - Use This When

Use this pattern when source or project prose uses cultural-evolution wording and a current claim or action depends on what that wording means here. If the word is only ordinary or quoted language and no FPF claim relies on it, leave it alone.

When generic *development*, *evolution*, or *lineage* wording still hides the changed or represented subject, continuity or membership, posture, direction or value basis, or direct owner, use `E.10.DEV` first. Continue here only when that recovery exposes a cultural-population, discipline, style, tradition, recognition, selection, transmission, retention, or mediation question whose wording is still unclear. Use `E.10.MOVE` only for a separately relied-on trajectory or path ambiguity.

Trigger expressions include, for example, culture, cultural evolution, style, tradition, genre, scene, technique, practice, platform, platform regime, measurement regime, attractor, developmental machinery, cultural lineage, canon, and school. They are recognition cues.

#### C.36.P:0.1 - What Goes Wrong If Missed

The repair becomes a synonym swap. `Style` becomes `method`, `platform regime` becomes `context`, `practice` becomes a generic process label, or `attractor` becomes `dynamics` before the sentence says which object, relation, or claim is current. The result looks cleaner but still carries an accidental ontology.

#### C.36.P:0.2 - What This Buys

The first result is a short ordinary statement: what the expression means in this use and which pattern supplies the next needed definition or test. For example: `Here “platform” refers to the short-video recommendation System and to the visibility and recognition relations around it. The claim is that changes in those relations altered which dance variants were copied; use C.36 for the cultural-evolution case and C.18 only if archive retention is the next question.`

Use C.36 for a cultural-evolution case. For a Method, Work, discipline, bridge, archive, pool, selected-set result declaration, publication, architecture, dynamics, measurement, choice, or refresh claim, use the pattern that defines or tests that claim.

#### C.36.P:0.3 - First Useful Move

Write the short ordinary statement first. Stop when it makes the next project action clear.

When a handoff or repeated use needs durable memory, keep the same result in this optional line:

```text
CulturalEvolutionWordingRecoveryLine:
  triggerSpan:
  wordingUse:
  sourceRef?:
  claimScope?:
  modelUseBoundary?:
  recoveredObjects?:
  recoveredRelations?:
  recoveredClaim:
  applicablePatternRefs:
  retainedSourceLabelUse?:
  admissibleUse?:
  blockedUse?:
  nextUseOrStop:
```

Fill only the fields the receiving use needs. If the object, relation, claim, or applicable rule cannot yet be recovered, keep the label as quoted source wording, ordinary prose, or a blocked-use cue. Do not choose a smoother umbrella word merely to fill the line.

### C.36.P:1 - Problem Frame

Cultural-evolution sources and project documents use compact labels because ordinary language has to move quickly. A word such as style, genre, practice, platform, or technique may be a useful local sign. It may also hide one or more distinct objects, relations, or claims—for example a Method family, Work family, local system-role kind, System-classification judgment, assignment species or occurrence, direct participation relation, discipline, canon or memory episteme, recognition relation, selected set, archive, front, mediation System, architecture, measurement relation, publication label, or mathematical-lens claim. Ambiguity alone does not prove that several of these claims are present.

Use C.36 for the cultural-evolution case. This companion recovers only enough meaning to write the ordinary claim and use the pattern that defines or tests the next needed distinction.

### C.36.P:2 - Problem

Without recovering the object or relation, a local wording repair can produce four failures:

- source labels become root kinds by spelling;
- platform and regime labels become hidden Systems, scope containers, or authorities;
- style and tradition labels become genre trees or single trajectories;
- developmental-machinery and practice labels become method, work, or process labels by taste rather than by current relation.

The repair must keep useful local labels while stopping them from carrying unearned ontology.

### C.36.P:3 - Forces

| Force | Tension |
|---|---|
| Local language usefulness | Communities need familiar words such as style, tradition, scene, platform, canon, and technique. |
| FPF composability | Downstream work needs the applicable Method, Work, discipline, episteme, bridge, archive, pool, selected-set, architecture, measurement, choice, or refresh rule with its contribution to the next action clear. |
| Source fidelity | Some labels should remain visible because they are source terms or project terms. |
| Ontological economy | The same labels must not mint root U-kinds or local ontologies. |
| Precision vs readable action | The repair must preserve distinctions that change truth or action without making the reader complete an ontological form before doing the work. |
| C.36 focus | C.36 supplies the cultural-evolution case; C.36.P supplies wording recovery. |

### C.36.P:4 - Solution

Use the intended claim, not the trigger word, to select the result. Write the short ordinary statement, then open only the branch whose distinction changes the next action. The branches below name common routes; their trigger lists are examples.

Before these cultural routes, send unresolved generic development or evolution wording to `E.10.DEV`. Return here only when its repaired claim has a cultural-evolution subject and a cultural wording question remains; preserve its ordinary non-use, missing-information result, non-cultural population or lineage architecture gap, and one-pass stop otherwise.

1. **Cultural-evolution case.** Use C.36 when the claim concerns how a collective or discipline generates, transmits, recognizes, selects, retains, or deliberately changes variants. Method and Work families, system-role facts, canons or memory epistemes, mediation, style or tradition terms, variant sets, and interventions remain separately identifiable inside that case.
2. **Term and bridge work.** Use F.17 and F.18 when a durable source or project term needs a stable local meaning or name. Use F.9 only when an actual relation between distinct source-local cells is current. Keep C.36 only for the cultural-evolution case that makes the term matter.
3. **Practice, technique, and developmental-machinery wording.** Ask what the phrase names:

   - For a reusable way of doing, use A.3.1; for a description of that way, use A.3.2; for a plan, use A.15.2; and for dated doing, use A.15.1.
   - If several Methods are related or assembled, use A.3.1's method-relation route; it keeps ordinary relations, order-sensitive composition, and a selected Structure distinct.
   - If the wording is about who acts or how someone is assigned, E.10.ROLE separates direct participation, a local system-role kind or classification under A.2, an assignment under A.2.1, and a relation between system-role kinds under A.2.7.
   - Use A.1.1 only when the decision depends on bounded model use or one of its direct model-applicability, actual-use, or fixed-content-coherence relations. Use A.10, C.20, or C.23 only when the claim is about evidence use, discipline composition, or method-family maturity.
4. **Variant-set, archive, front, pool, selected-set, publication, and refresh wording.** Use C.18, C.19, G.5, E.17, E.24.PUB, G.11, or E.18.1 according to whether the next question concerns generation or retention, current-pool treatment, a selected-set result declaration, publication, refresh, or problem-to-work carry-through.
5. **Platform, regime, and mediator wording.** Do not presume a System. The phrase may identify, for example, a mediating System or architecture, recognition or selection relation, measurement or visibility relation, publication or source-currentness relation, episteme, bounded model-use structure, direct model-use relation, claim scope, or ordinary project label. Admit a System only when that System is the object. Keep any local system-role kind, classification, and assignment separate and optional. If the current governing rule needed to state or test the intended claim for the named participants and use is absent, return A.6.RCD's `missing-governor`.
6. **Meta-holon-transition (MHT), level, boundary, feedback, model-use or scope reframe, and frustration wording.** Recover whether the claim concerns a new holon or level, whole reidentification, a System boundary, a relation that crosses a holon boundary, supervisor-subholon feedback, bounded model use or claim scope, cross-scope architecture residual, mathematical-lens use, or interlevel ethical conflict. Use A.1, A.1.1, B.2.P, B.2, B.2.2, B.2.3, B.2.4, B.2.5, C.30.ILC, C.29, D.2, D.3, or D.4 according to that recovered claim. Keep C.36 only for the cultural-evolution case.
7. **Attractor and dynamics wording.** Use A.3.3, C.27, and C.29 only when the claim is about stable dynamics, a basin, state-transition law, temporal behavior, or mathematical-lens use. Otherwise keep the label as style or tradition term work.
8. **Architecture wording.** Use C.30 for an architecture question or ArchitectureClaim, C.30.ASV for a structural-view question, and C.30.AD for an architecture-description question. A selected structure, ArchitectureRelation, claim, description, view, representation, and publication remain distinct. Treat `ArchitectureOf@Context` only as a legacy retrieval phrase resolved by the current C.30 edition, not as a current record or ontology.

A C.36.P repair closes when the short ordinary statement names the needed object, relation, or claim and makes the next use or stop visible. The optional recovery line is not required for a clean local repair.

Use the direct patterns for development-loop semantics, archive or front relations, pool policy, selected-set result declarations, Method-family semantics, measurement, refresh, publication use, or architecture use. C.36.P recovers the wording needed to enter them.

#### C.36.P:4.1 - Recovery Result Table

The trigger phrases are examples. Recover the intended object, relation, or claim first; then use the pattern that defines or tests the distinction needed by the next action.

| Trigger use | Recover first | Applicable patterns after recovery |
|---|---|---|
| generic development, evolution, evolved, progress, growth, adaptation, or lineage | changed or represented subject; needed continuity or membership; posture; any direction or value basis; direct owner; cultural or non-cultural boundary | `E.10.DEV` first; then C.36 or C.36.P only for a recovered cultural-evolution case, and `E.10.MOVE` only for a remaining independent trajectory or path ambiguity |
| style, tradition, genre, scene, school, or cultural lineage | term row or actual bridge; Method or Work family; canon or memory episteme; recognition relation; selected set; publication label | F.17, F.18, F.9, C.36, A.3.1, C.20, C.18, G.5, E.17, or E.24.PUB |
| practice, technique, developmental machinery | Method or MethodDescription; relations among Methods or a selected Structure of them; WorkPlan or dated Work; direct participation; local system-role kind or classification; assignment species or occurrence; relation between system-role kinds; bounded model-use structure or one of its direct relations; discipline position; evidence-use claim; quote-only wording | A.3.1, A.3.2, A.15.1, A.15.2, E.10.ROLE, A.2, A.2.1, A.2.7, A.1.1, A.10, C.20, or C.23 |
| platform, platform regime, measurement regime | mediating System or architecture; recognition, selection, measurement, visibility, publication, source-currentness, or direct model-use relation; bounded model-use structure; claim scope; ordinary project label | A.1, A.1.1, C.30, C.16, A.19, E.17, E.24.PUB, G.11, or C.36 |
| MHT, level, boundary, feedback down, model-use or scope reframe, frustration, interlevel conflict | new holon or level; whole reidentification; System boundary; relation crossing a holon boundary; supervisor-subholon feedback; bounded model use or claim scope; cross-scope residual; mathematical-lens use; interlevel ethical conflict | A.1, A.1.1, B.2.P, B.2, B.2.2, B.2.3, B.2.4, B.2.5, C.30.ILC, C.29, D.2, D.3, or D.4 |
| attractor, basin, stable style | loose style term or an actual dynamics, temporal, or mathematical-lens claim | F.17, F.18, F.9, A.3.3, C.27, C.29, or C.36 |
| archive, front, Q-front, current pool, portfolio, retained set | archive or front relation; pool-policy result; selected-set result declaration; publication relation; refresh relation | C.18, C.19, G.5, E.17, E.24.PUB, G.11, or E.18.1 |

### C.36.P:5 - Worked Micro-Examples

#### C.36.P:5.1 - "The Platform Changed The Style"

Short ordinary statement: `Here “platform” refers to the short-video recommendation System and to the visibility, recognition, and selection relations around it. The claim is that changes in those relations altered which dance variants were copied and retained.`

That short statement may be enough. If the result must be handed on or reused, retain it as:

```text
CulturalEvolutionWordingRecoveryLine:
  triggerSpan: "platform changed the style"
  wordingUse: “platform” names the recommender and its visibility infrastructure
  claimScope: this circulation and teaching-cycle comparison
  recoveredObjects: short-video recommendation System; dance-variant set
  recoveredRelations: recommendation mediation; visibility; recognition; selection
  recoveredClaim: these relations changed which variants were copied and retained
  applicablePatternRefs: A.1, C.36, F.17, F.18
  retainedSourceLabelUse: keep "platform" as the source label for the recommender and visibility infrastructure
  admissibleUse: discuss how visibility and recognition changed retained dance variants
  blockedUse: treat platform as a root cultural kind or style as one global kind
  nextUseOrStop: use C.36 for the case; use C.18 or G.11 only if archive or refresh is next
```

#### C.36.P:5.2 - "This Tradition Is An Attractor"

If `attractor` is a loose metaphor for a stable recognizable style, use a term bridge and C.36 case. If the project claims basin structure, stable dynamics, or state-transition law, use `A.3.3`, `C.27`, and `C.29` before C.36 relies on the claim.

#### C.36.P:5.3 - "Technique As Developmental Machinery"

If technique names a way of doing work, use `A.3.1 U.Method`. If it names a training plan, use `A.15.2 U.WorkPlan`. If it names performed rehearsal or production, use dated `U.Work`. If the same term carries different source-local meanings, use F.17 and F.18; use F.9 only when an actual relation between distinct cells is current. Use C.36 only when the technique participates in a cultural-evolution case.

#### C.36.P:5.4 - "The Scene Became A New Level"

If a music or dance source says a scene, platform circulation, or canon “became a new level”, first recover the claim. Use C.36 for a changed recognition regime, C.18 for an archive relation, G.5 for a selected-set result declaration, G.11 for refresh, and F.17, F.18, or F.9 for term and actual-bridge work. A whole-reidentification or MHT claim uses B.2.P and then B.2 or its System or episteme specialization when current. A feedback-down claim uses B.2.5. A frustration or residual claim uses C.30.ILC for an architecture residual, C.29 for a mathematical lens, and D.3 or D.4 for ethical level conflict or mediation.

### C.36.P:6 - Boundaries

This pattern does not define the cultural-evolution case or intervention. Use C.36 for those questions.

Use C.36.P to recover one ordinary claim. Keep the optional recovery line only when a handoff or repeated use needs it. Once the meaning and applicable rule are clear, stop the wording repair and return to the project question.

If a source uses `CulturalEvolutionWordingRecoveryLine@Context`, read it as `CulturalEvolutionWordingRecoveryLine` qualified for local retrieval; recover any required scope or relation separately.

Cultural labels remain usable as local signs for the recovered objects, relations, and claims.

### C.36.P:7 - Relations

Builds on: `E.10`, `E.10.ARCH`, `E.10.DEV`, `E.10.ROLE`, `C.36`, `F.17`, `F.18`, `F.9`, `A.3.1`, `A.3.2`, `A.15`, `C.18`, `C.19`, `G.5`, and `G.11`.

Coordinates with: `E.10.MOVE` for a remaining independent trajectory or path ambiguity, `A.1`, `A.1.1`, `A.6.RCD`, `B.2`, `B.2.P`, `B.2.2`, `B.2.3`, `B.2.4`, `B.2.5`, `A.3.3`, `C.16`, `C.20`, `C.23`, `C.27`, `C.29`, `C.30`, `C.30.AD`, `C.30.ASV`, `C.30.ILC`, `D.2`, `D.3`, `D.4`, `E.17`, and `E.18.1`.

### C.36.P:End

