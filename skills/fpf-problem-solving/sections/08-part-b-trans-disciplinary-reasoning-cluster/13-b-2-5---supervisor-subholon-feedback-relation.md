## B.2.5 - Supervisor-Subholon Feedback Relation

> **Type:** Part B holonic construction pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### B.2.5:0 - Use This When

Use this pattern when a holon is supervised, regulated, steered, corrected, constrained, or coordinated through a two-sided feedback relation between a supervisor role and one or more supervised holons.

The first useful move is to recover the relation:

```text
Which holons are supervised?
Which acting system holds the supervisor role in this bounded context?
What observation, report, signal, publication, or source relation carries state?
What influence, constraint, objective, mode, or work change returns?
Which transformation, work, architecture, evidence, assurance, timing,
or causal claim is being made in addition to the relation?
```

**What goes wrong if missed.** A control diagram, policy note, dashboard, publication channel, or supervisor word starts carrying part-whole, agency, safety, assurance, timing, gate, or architecture claims that belong elsewhere.

**What this buys.** B.2.5 gives a small relation record: supervised holons, supervisor role, acting system, medium or publication relation, observation or report side, influence or constraint side, and direct owners for stronger claims.

**Not this pattern when.**

- If the question is a control-structure view, use `C.30.LCA`.
- If the question is architecture or selected structure, use `C.30`, `A.22`, and `C.30.ASV`.
- If the question is reusable dynamics, timing, rate, or temporal validity, use `A.3.3` and `C.27`.
- If the question is causal use, use `C.28`.
- If the question is evidence, assurance, gate, or constraint validity, use `A.10`, `G.6`, `B.3`, `A.20`, or `A.21`.
- If the question is module allocation or interface commitment, use `A.6.M`.
- If the question is whole reidentification, use `B.2`.

### B.2.5:1 - Problem Frame

Supervisor-subholon feedback is a relation among holons, roles, acting systems, observed or published state, and returned influence or constraint. It is not automatically parthood, not automatically a control-structure view, not automatically evidence, and not automatically a mathematical loop object.

B.2.5 governs the relation-level claim. It can sit inside a broader architecture description, control-structure view, MHT claim, work claim, or evidence claim, but those claims keep their direct owners.

### B.2.5:2 - Problem

Without this pattern, three different structures collapse:

1. **Part-whole structure.** Which holons are parts of which wholes.
2. **Supervisor-subholon feedback relation.** Which acting system holds the supervisor role, what it observes, and what influence or constraint returns.
3. **Description or representation structure.** Which diagram, dashboard, report, model, publication, or control-view description represents the relation.

When these are confused, a functional layer is treated as a physical part, a publication is treated as an acting system, a diagram is treated as evidence, or a supervisor label is treated as a gate or assurance result.

### B.2.5:3 - Forces

| Force | Tension |
| --- | --- |
| Recognizable feedback language vs kind precision | Engineers use feedback, control, supervision, and regulation language naturally; FPF needs the relation and neighboring claim kinds named. |
| Relation vs view | A supervisor-subholon relation may appear inside a control-structure view, but the view and relation are different objects. |
| Acting system vs episteme | A theory, model, standard, dashboard, or report may be revised or used, but it does not act by itself. |
| Closure vs stronger claims | A two-sided feedback relation can supply input to stability or assurance work, but does not certify those claims. |
| Medium visibility vs perfect communication | The relation needs observation or report and influence or constraint sides, including publication or medium limits when current. |

### B.2.5:4 - Solution

Model the current object as `SupervisorSubholonFeedbackRelation@Context`.

```text
SupervisorSubholonFeedbackRelation@Context:
  supervisedHolonRefs: FinSet(U.HolonRef)
  boundedContextRef:
  supervisorRoleRef:
  supervisingActingSystemRef:
  supervisedWorkOrTransformationRefs?
  observationOrReportRefs: FinSet(ObservationRef | ReportRef | PublicationUnitRef | SourceUseRef)
  influenceOrConstraintRefs: FinSet(InfluenceSignalRef | ConstraintRef | ObjectiveRef | ModeRef)
  sharedMediumOrPublicationRefs?
  holonBoundaryCrossingRelationRefs?
  feedbackClosureCondition:
  admissibleUse:
  nonAdmissibleUse:
  neighboringClaimOwnerRefs?
```

This relation is not a U-kind and not a mathematical loop lens. It is a relation record for the current bounded context.

#### B.2.5:4.1 - Two-Sided Feedback Relation

A one-way command, publication, or report relation is not yet a supervisor-subholon feedback relation. Name both:

- the observation, report, signal, source, or publication side; and
- the returned influence, constraint, objective, mode, or work-change side.

If only one side is current, record a one-sided relation and use the direct owner for that claim.

#### B.2.5:4.2 - Part-Whole Boundary

A supervised holon may be part of a larger holon, but supervision and parthood are different relations. An acting controller system, committee system, platform-governance system, review board, or tool-mediated group can hold the supervisor role without being a physical part of the supervised holon. A method, policy, or review practice can structure the supervision work; it does not supervise by itself.

Use `A.1`, `B.1`, `A.14`, and `C.13` for parthood. Use B.2.5 only for the supervisor-subholon feedback relation.

#### B.2.5:4.3 - Acting-System Boundary

The supervisor role is held by an acting system in a bounded context. Do not create `U.TransformerRef` or treat a publication, theory, dashboard, model, method description, or report as the acting system.

For acting-side externalization, use `A.12`. For transformation, use `A.3.4`. For work, use `A.15.1`. For role assignment, use `A.2.1`.

#### B.2.5:4.4 - Control-Structure View Boundary

When the relation is drawn as planner, controller, observer, plant, and supervisor structure, B.2.5 names the relation, while `C.30.LCA` owns the control-structure view. A diagram or view does not establish the relation by appearance; recover the in-life relation and the description relation separately.

#### B.2.5:4.5 - Neighboring Claim Boundary

B.2.5 does not certify stability, safety, assurance, evidence sufficiency, causal validity, gate passage, rate adequacy, or mathematical adequacy.

Use:

- `A.3.3` for reusable dynamics or state-evolution claims;
- `C.27` for temporal and rate adequacy;
- `C.28` for causal-use claims;
- `A.10` and `G.6` for evidence and provenance;
- `B.3` for assurance;
- `A.20` and `A.21` for constraint validity and gate decisions;
- `C.29` for mathematical-lens use.

### B.2.5:5 - Archetypal Grounding (Worked Cases)

#### B.2.5:5.1 - Robotic Swarm

A fleet controller supervises drones. B.2.5 records each drone as a supervised holon, the controller system holding the supervisor role, telemetry as observation side, and waypoint or mode commands as influence side.

Claims about convergence, delay tolerance, disturbance damping, evidence, assurance, or safety use their direct owners. The feedback relation does not certify them.

#### B.2.5:5.2 - Scientific Theory Revision

A theory is revised when labs publish findings and a research community reviews anomalies and accepted revisions.

B.2.5 may record the theory or constituent epistemes as supervised objects only when the current claim is about a feedback relation around review and revision. The acting system is the research community, standards body, lab, review board, or tool-mediated group in role. The theory does not sense, judge, plan, decide, or act.

Publication channels, journals, datasets, reports, and review records remain publication or source-use objects.

#### B.2.5:5.3 - Product Platform Policy

A product platform constrains component teams through interface rules and release gates. B.2.5 records the acting platform or governance system holding the supervisor role, component holons, report channels, and constraint returns.

Work authority uses `A.15`; gate passage uses `A.21`; interface commitments use `A.6.M`; architecture view uses `C.30.LCA` when the control structure is described.

### B.2.5:5.4 - Bias-Annotation

| Bias | How B.2.5 prevents it |
| --- | --- |
| Supervisor-as-superholon bias | The supervisor relation is not a parthood claim; parthood stays with `A.1`, `B.1`, `A.14`, and `C.13`. |
| Feedback-as-proof bias | A closed feedback relation may supply input to separate stability, safety, assurance, or timing work, but does not certify those claims. |
| Description-as-relation bias | A diagram, dashboard, report, or control-view description does not establish the in-life feedback relation by itself. |
| Episteme-agency bias | A theory, standard, model, dashboard, or publication may stand in a supervised slot or source-use slot, but the acting system in the supervisor role must still be named. |

### B.2.5:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-B2.5-1` | A conforming use names supervised holons, supervisor role, and the acting system holding that role. |
| `CC-B2.5-2` | A conforming use names observation, report, or source side and influence, constraint, or objective side. |
| `CC-B2.5-3` | `SupervisorSubholonFeedbackRelation@Context` is used instead of loop wording unless a separate math-lens owner selects a loop object. |
| `CC-B2.5-4` | No `U.TransformerRef` or `U.InteractionRef` is created. |
| `CC-B2.5-5` | Parthood, control-structure view, publication and source-use relation, and feedback relation are kept separate. |
| `CC-B2.5-6` | Stability, safety, timing, causal, evidence, assurance, gate, and mathematical-lens claims return to their governing patterns. |
| `CC-B2.5-7` | Episteme examples name the acting systems that perform review, revision, publication, or use. |

### B.2.5:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Ghost coordination | Subholons coordinate, but no supervisor role, acting system, medium, or feedback relation is named. | Fill `SupervisorSubholonFeedbackRelation@Context`. |
| Functional layer as component | A planning or control layer is modeled as a physical part of the controlled holon. | Separate parthood from feedback relation; use `C.30.LCA` for the view. |
| Perfect communication | State access is assumed instant, complete, or lossless. | Name medium or publication limits; use `C.27`, `A.3.3`, or evidence owners for timing and information claims. |
| Episteme acts | A theory, model, paper, dashboard, or standard senses, judges, plans, or adapts. | Name the acting system in role, the method or review practice structuring the work when current, the revision work, and any publication or source-use relation. |
| Relation certifies safety | The feedback relation is treated as evidence, assurance, gate, or safety result. | Keep the relation and apply the governing pattern for the stronger claim. |

### B.2.5:8 - Consequences

Positive consequences:

- Supervisor-subholon language stays useful without creating false acting objects or false part-whole claims.
- Control diagrams, publication channels, and feedback relations can be coordinated without being collapsed.
- Stability, safety, assurance, gate, timing, and evidence claims stay inspectable.

Costs:

- A feedback relation record is only the beginning of stronger analysis.
- Some control diagrams become less impressive because their unproven claims are separated.
- Episteme examples require explicit acting systems for review and revision.

### B.2.5:9 - Rationale

Supervisor-subholon feedback is a recurring relation in control, organization, architecture, and epistemic revision. It becomes precise only when separated from part-whole composition, control-structure views, publication and source-use relations, and stronger assurance claims.

The selected name is `SupervisorSubholonFeedbackRelation@Context` because the governed object is a relation. A mathematical loop, if needed, is a lens or structure selected by another pattern; it is not selected by the name of this relation.

### B.2.5:10 - SoTA-Echoing

| Source family | Lesson for B.2.5 | FPF decision |
| --- | --- | --- |
| Layered and multi-rate control practice | Supervisor, plant, controller, observer, rate, and feedback language are useful recognition cues. | B.2.5 recovers the relation; `C.30.LCA`, `A.3.3`, `C.27`, and `C.29` own view, dynamics, timing, and mathematical claims. |
| Cyber-physical systems practice | Medium limits, observation channels, actuation, delay, disturbance, and plant dynamics affect adequacy. | The relation names medium and returned influence; adequacy claims use direct owners. |
| Organizational policy and review practice | Supervision may be enacted through policies, reviews, reports, publication channels, and role assignments. | The acting system in role is named; publications and reports remain source-use or publication objects. |
| Episteme and publication discipline | Knowledge-bearing objects can be reviewed, revised, cited, and published, but they do not act. | Episteme examples use acting systems for review and keep the episteme as reviewed or revised object. |

### B.2.5:11 - Relations

- **Builds on:** `A.1`, `A.2.1`, `A.12`, `A.3.4`, `A.15.1`, `B.1`, `A.14`, and `C.13`.
- **Coordinates with:** `B.2` when feedback evidence creates a whole-reidentification question.
- **Coordinates with:** `C.30.LCA` for control-structure view, `A.3.3` for dynamics, `C.27` for temporal and rate adequacy, `C.28` for causal use, `A.10` and `G.6` for evidence, `B.3` for assurance, `A.20` and `A.21` for constraint validity and gate decisions, `A.6.M` for module-interface relation, and `C.29` for mathematical-lens use.
- **Uses:** `B.2.P` when feedback, supervision, emergence, or MHT wording hides the claim kind.

### B.2.5:End

