## C.36.P - Cultural-Evolution Wording-Use Precision Restoration

> **Tech-name:** `CulturalEvolutionWordingUsePrecisionRestoration`
> **Plain-name:** cultural-evolution wording-use precision restoration
> **Type:** Precision-restoration companion pattern (C)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part C -> C.36 companion
> **Builds on:** `E.10`, `E.10.ARCH`, `C.36`, `F.17`, `F.18`, `F.9`, `A.3.1`, `A.3.2`, `A.15`, `C.18`, `C.19`, `G.5`, and `G.11`.
> **Purpose:** recover the FPF object hidden by culture, style, tradition, genre, scene, practice, technique, platform, regime, attractor, or developmental-machinery wording.

### C.36.P:0 - Use This When

Use this pattern when source or project prose uses cultural-evolution wording and the FPF object under concern is still hidden.

Trigger words include culture, cultural evolution, style, tradition, genre, scene, technique, practice, platform, platform regime, measurement regime, attractor, developmental machinery, lineage, canon, school, and close local labels.

#### C.36.P:0.1 - What Goes Wrong If Missed

The repair becomes a synonym swap. `Style` becomes `method`, `platform regime` becomes `context`, `practice` becomes a generic process label, or `attractor` becomes `dynamics` before the sentence says which FPF value, relation, claim, or bridge is current. The result looks cleaner but still carries an accidental ontology.

#### C.36.P:0.2 - What This Buys

The practitioner gets one recovery line: current wording, recovered object, governing pattern, admissible use, blocked use, and next governed use. The subject work then returns to `C.36` or to the direct governing pattern for method, work, discipline, bridge, archive, pool, selected-set publication, architecture, dynamics, measurement, choice, or refresh.

#### C.36.P:0.3 - First Useful Move

Write one `CulturalEvolutionWordingRecoveryLine@Context`.

```text
CulturalEvolutionWordingRecoveryLine@Context:
  triggerSpan:
  sourceOrProjectContext:
  recoveredCurrentObject:
  recoveredRelationOrSlot:
  directGoverningPatternRef:
  retainedSourceLabelUse:
  admissibleUse:
  blockedUse:
  nextUse:
```

If `recoveredCurrentObject`, `recoveredRelationOrSlot`, or `directGoverningPatternRef` cannot be filled, keep the label as quoted source wording, ordinary prose, or a blocked-use cue. Do not repair it by choosing a smoother umbrella word.

### C.36.P:1 - Problem Frame

Cultural-evolution sources and project documents use compact labels because ordinary language has to move quickly. A word such as style, genre, practice, platform, or technique may be a useful local sign. It may also hide several values governed by named FPF patterns at once: a method family, work family, role assignment, discipline, canon or memory episteme, recognition regime, selected set, archive, front, mediation system, architecture, measurement relation, publication label, or mathematical-lens claim.

`C.36.P` does not decide the cultural-evolution subject. `C.36` does that. This companion only restores enough ontology to choose the current governing pattern.

### C.36.P:2 - Problem

Without a repeatable recovery line, each cultural-evolution phrase gets repaired locally. That creates four failures:

- source labels become root kinds by spelling;
- platform and regime labels become hidden systems, contexts, or authorities;
- style and tradition labels become genre trees or single trajectories;
- developmental-machinery and practice labels become method, work, or process labels by taste rather than by current relation.

The repair must keep useful local labels while stopping them from carrying unearned ontology.

### C.36.P:3 - Forces

| Force | Tension |
|---|---|
| Local language usefulness | Communities need familiar words such as style, tradition, scene, platform, canon, and technique. |
| FPF composability | Downstream work needs method, work, discipline, episteme, bridge, archive, pool, selected-set, architecture, measurement, choice, and refresh governing patterns named by value. |
| Source fidelity | Some labels should remain visible because they are source terms or project terms. |
| Ontological economy | The same labels must not mint root U-kinds or local ontologies. |
| Subject-pattern focus | `C.36` must remain a positive cultural-evolution pattern, not a repair table. |

### C.36.P:4 - Solution

Recover the current object first, then identify the direct governing pattern.

Use this recovery order:

1. **Cultural-evolution case.** If the claim is about collective-holon or discipline-facing evolution of method families, work families, role assignments, canons or memory epistemes, recognition or selection regimes, mediation systems, style or tradition labels, variant sets, or deliberate interventions, use `C.36`.
2. **Term and bridge work.** If the word is a durable public or local label crossing contexts, use `F.17`, `F.18`, and `F.9`; keep `C.36` only for the cultural-evolution case that makes the term matter.
3. **Method, practice, technique, or developmental-machinery wording.** Recover `U.Method`, method family, method relation structure, `U.MethodDescription`, work plan, dated work, role assignment, or discipline position through `A.3.1`, `A.3.2`, `A.15`, `C.20`, and `C.23`.
4. **Variant-set, archive, front, pool, selected-set, and refresh wording.** Use `C.18`, `C.19`, `G.5`, `G.11`, and `E.18.1` according to whether generation, retention, current pool treatment, selected-set publication, refresh, or problem-to-work carry-through is current.
5. **Platform, regime, and mediator wording.** Recover the system or holon-in-role value, system or product architecture, recognition or selection regime, measurement or visibility relation, publication relation, bounded context, source-currentness relation, or architecture relation before using the label.
6. **MHT, level, boundary, feedback, context-reframe, and frustration wording.** Recover whether the claim is a new holon or level, whole reidentification, system boundary, supervisor-subholon feedback, context reframe, cross-scope architecture residual, mathematical-lens use, or interlevel ethical conflict. Use `A.1`, `B.2.P`, `B.2`, `B.2.2`, `B.2.3`, `B.2.4`, `B.2.5`, `C.30.ILC`, `C.29`, `D.2`, `D.3`, `D.4`, or the direct governing pattern named by value. Keep `C.36` only for the cultural-evolution case that supplies the source context.
7. **Attractor and dynamics wording.** Use `A.3.3`, `C.27`, and `C.29` only when stable dynamics, basin, state-transition law, temporal claim, or mathematical-lens use is being claimed. Otherwise keep the label as style or tradition term work.
8. **Architecture-candidate wording.** Use `C.30`, `C.30.ASV`, or `C.30.AD` only when the recovered object is an `ArchitectureOf@Context`, selected structure, structural view, or architecture description.

`C.36.P` closes only when the direct governing pattern is named and the next use is visible. It does not govern development-loop semantics, archive semantics, front semantics, pool policy, selected-set publication, method-family semantics, measurement, refresh, publication use, or architecture use.

#### C.36.P:4.1 - Recovery Result Table

| Trigger use | Recover first | Governing pattern after recovery |
|---|---|---|
| style, tradition, genre, scene, school, lineage | term row, bridge, method family, work family, canon or memory episteme, recognition regime, selected set, publication label | `F.17`, `F.18`, `F.9`, `C.36`, `A.3.1`, `C.20`, `C.18`, `G.5` |
| practice, technique, developmental machinery | method, method family, method description, work plan, dated work, role assignment, discipline position | `A.3.1`, `A.3.2`, `A.15`, `A.15.1`, `A.15.2`, `C.20`, `C.23` |
| platform, platform regime, measurement regime | system or architecture, recognition regime, selection regime, measurement relation, visibility relation, publication relation, bounded context | `A.1`, `C.30`, `C.16`, `A.19`, `E.17`, `G.11`, `C.36` |
| MHT, level, boundary, feedback down, context reframe, frustration, interlevel conflict | new holon or level claim, whole reidentification, boundary-crossing relation, supervisor-subholon feedback, context reframe, cross-scope residual, mathematical-lens use, interlevel ethical conflict | `A.1`, `B.2.P`, `B.2`, `B.2.2`, `B.2.3`, `B.2.4`, `B.2.5`, `C.30.ILC`, `C.29`, `D.2`, `D.3`, `D.4`, and the direct holon, system, architecture, mathematical-lens, or ethics pattern named by value |
| attractor, basin, stable style | loose style term or dynamics claim | `F.17`, `F.18`, `F.9`, `A.3.3`, `C.27`, `C.29`, `C.36` |
| archive, front, Q-front, current pool, portfolio, retained set | archive relation, front relation, pool-policy result, selected-set publication, refresh relation | `C.18`, `C.19`, `G.5`, `G.11`, `E.18.1` |

### C.36.P:5 - Worked Micro-Examples

#### C.36.P:5.1 - "The Platform Changed The Style"

Recovery line:

```text
CulturalEvolutionWordingRecoveryLine@Context:
  triggerSpan: "platform changed the style"
  sourceOrProjectContext: short-video dance circulation
  recoveredCurrentObject: recommendation-system mediation plus visibility relation plus style term bridge
  recoveredRelationOrSlot: mediation system changes recognition and selection regime for a variant set
  directGoverningPatternRef: C.36, F.17, F.18, F.9, C.18, G.11
  retainedSourceLabelUse: keep "platform" as source label for the mediating system and visibility infrastructure
  admissibleUse: discuss how visibility and recognition relations changed retained dance variants
  blockedUse: treat platform as a root cultural kind or style as one global kind
  nextUse: write C.36 case card, then apply C.18 or G.11 if archive or refresh is current
```

#### C.36.P:5.2 - "This Tradition Is An Attractor"

If `attractor` is a loose metaphor for a stable recognizable style, use a term bridge and C.36 case. If the project claims basin structure, stable dynamics, or state-transition law, use `A.3.3`, `C.27`, and `C.29` before C.36 relies on the claim.

#### C.36.P:5.3 - "Technique As Developmental Machinery"

If technique names a semantic way of doing work, use `A.3.1 U.Method`. If it names a training plan, use `A.15.2 U.WorkPlan`. If it names performed rehearsal or production, use dated `U.Work`. If it names a term that crosses dance contexts, use `F.17`, `F.18`, and `F.9`. Use C.36 only when the technique participates in a cultural-evolution case.

#### C.36.P:5.4 - "The Scene Became A New Level"

If a music or dance source says a scene, platform circulation, or canon "became a new level", first recover the claim. A new recognition regime, archive, or term bridge remains C.36, C.18, G.5, G.11, F.17, F.18, or F.9 work. A whole-reidentification or MHT claim uses `B.2.P` and then `B.2` or its system or episteme specialization when current. A feedback-down claim uses the direct supervisor-subholon feedback pattern. A frustration or residual claim uses `C.30.ILC` when it is an architecture residual, `C.29` when a mathematical lens is being claimed, and `D.3` or `D.4` when ethical level conflict or mediation is current.

### C.36.P:6 - Boundaries

This pattern is not the cultural-evolution subject-governing pattern. Use `C.36` for the cultural-evolution case and cultural-evolution engineering intervention.

Use this pattern for one repeatable recovery line that names direct governing patterns. Once the governing pattern is named, stop the wording repair and return to the project question.

This pattern does not create `U.Culture`, `U.Style`, `U.Tradition`, `U.Practice`, `U.Genre`, `U.Scene`, `U.Technique`, `U.Platform`, `U.PlatformRegime`, `U.MeasurementRegime`, or `U.DevelopmentalMachine`.

### C.36.P:7 - Relations

Builds on: `E.10`, `E.10.ARCH`, `C.36`, `F.17`, `F.18`, `F.9`, `A.3.1`, `A.3.2`, `A.15`, `C.18`, `C.19`, `G.5`, and `G.11`.

Coordinates with: `A.1`, `B.2`, `B.2.P`, `B.2.2`, `B.2.3`, `B.2.4`, `B.2.5`, `A.3.3`, `C.16`, `C.20`, `C.23`, `C.27`, `C.29`, `C.30`, `C.30.AD`, `C.30.ASV`, `C.30.ILC`, `D.2`, `D.3`, `D.4`, `E.17`, and `E.18.1`.

### C.36.P:End

