## B.2.5 - Supervisor-Subholon Feedback Loop

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative for FPF use that claims a supervisor-subholon feedback-loop relation.
### B.2.5:1 - Problem frame

Use this pattern when a holon is described as being supervised, regulated, steered, corrected, constrained, or coordinated through a feedback loop between a supervisor role and one or more subordinate holons.

The first-minute working situation is familiar: a fleet controller supervises drones, a plant supervisor changes allowed operating modes, a policy role constrains teams, or a scientific community reviews and revises a theory. The useful first move is to recover the feedback-loop relation: who or what is the supervised holon, which `Transformer` or transformer-bearing system plays the supervisor role, what signal or publication channel carries state or observations, what influence or constraint returns, and what objective or constraint the loop is trying to maintain.

What goes wrong if B.2.5 is missed: a drawn loop, layer label, publication channel, or supervisor word is read as proof of stability, safety, causality, evidence sufficiency, gate validity, or assurance.

What B.2.5 buys in practice: the practitioner can keep useful supervisor/subholon language while naming the acting role, medium, returned influence, and exact governing pattern that carries any proof or exact claim.
Not this pattern when the live issue is only a control-structure view, a reusable dynamics law, a rate/timing claim, a causal intervention claim, an evidence claim, an assurance claim, a gate decision, or a module-interface relation. Use `C.30.LCA` for control-structure view adequacy, `A.3.3` for dynamics, `C.27` for temporal/rate adequacy, `C.28` for causal-use claims, `A.10`/`G.6` for evidence claim, `B.3` for assurance, `A.20`/`A.21` for constraint validity or gate decisions, and module/interface patterns for interface commitments.

The governed object is one supervisor-subholon feedback-loop relation. It is not proof that the loop is stable, safe, evidence-sufficient, gate-ready, causally valid, or assured.

### B.2.5:2 - Problem

Layered supervision is useful across engineered, biological, organizational, and epistemic cases, but it is easy to model incorrectly. The common error is to collapse three different structures into one drawing:

1. Structural composition: part-whole or carrier composition of a holon.
2. Supervisory relation: a `Transformer` or transformer-bearing system playing a supervisor role over one or more subordinate holons.
3. Interaction or publication network: observation, signal, command, constraint, report, review, or publication channels through which the loop is enacted or supported.

When these are confused, a functional or supervisory layer is treated as a physical part, a publication is treated as an acting agent, a diagram is treated as proof, or a controller label is treated as a gate or assurance result.

### B.2.5:3 - Forces

* Supervisory-loop language is useful and recognizable in control theory, cyber-physical systems, organizations, and science.
* Layered-control language often uses `layer`, `level`, `stack`, and `hierarchy`; those words need declared kind recovery.
* `U.Episteme` cases are especially fragile: an episteme can be reviewed, revised, cited, published, or used by acting systems, but the episteme itself does not sense, judge, plan, decide, or act.
* A supervisor-subholon loop can be a relation in an architecture description, but stability, safety, assurance, evidence, gate, causal, and timing claim kinds belong to exact governing patterns.
* The pattern needs to remain small enough to identify the loop before opening heavier control or assurance apparatus.

### B.2.5:4 - Solution

Model a supervisor-subholon feedback loop as a relation among holons, roles, transformers, media, and returned influence. A conforming loop identifies:

```text
SupervisorSubholonFeedbackLoop@Context ::= {
  supervisedHolonRefs      : FinSet(U.HolonRef),
  supervisorRoleRef        : U.RoleRef,
  supervisorTransformerRef : U.TransformerRef | TransformerBearingSystemRef,
  sharedMediumRefs         : FinSet(U.InteractionRef | PublicationChannelRef),
  observationOrReportRefs  : FinSet(ObservationRef | ReportRef | PublicationUnitRef),
  influenceOrConstraintRefs: FinSet(InfluenceSignalRef | ConstraintRef | ObjectiveRef),
  feedbackRelationRefs     : FinSet(QualifiedRelationRecordRef),
  objectiveOrConstraintRef?,
  loopClosureCondition,
  admissibleUse,
  nonAdmissibleUse,
  governingClaimPatternRefs?
}
```

**Loop reading.** The loop has an observation/report side and an influence/constraint side. A one-way command relation is not yet a closed supervisor-subholon feedback loop unless the return observation, report, or state relation is also declared.

**Structural-composition boundary.** A supervised holon may be part of a larger holon, but supervision is not the same relation as part-whole composition. A controller, committee, method, or review practice can supervise a subholon without being a physical component of that subholon.

**Control-structure view boundary.** When the loop appears in an architecture description as planner/controller/observer/plant/supervisor structure, use `C.30.LCA` to record the control-structure view. `B.2.5` supplies the supervisor-subholon relation; `C.30.LCA` records the broader control-structure view.

**Proof boundary.** A conforming `B.2.5` loop is a relation, not proof. Stability and reusable state-evolution claims use `A.3.3`; rate and timing claims use `C.27`; causal-use claims use `C.28`; evidence claims use `A.10` or `G.6`; assurance claims use `B.3`; gate and constraint-validity claims use `A.20`/`A.21`; mathematical-lens transfer uses `C.29`.

**Episteme case boundary.** In an episteme case, the acting and revising work is performed by systems or practices bearing `Transformer` roles. The `U.Episteme` is the knowledge-bearing object being reviewed, revised, stabilized, cited, or published. It does not itself sense, judge, plan, or act.

**Worked slice A - robotic swarm.** A drone fleet has individual drones, a shared communication medium, and a fleet-scope controller or distributed consensus method. `B.2.5` records each drone as supervised holon, the controller or consensus system as supervisor transformer, telemetry as observation side, and waypoint or mode commands as influence side. Claims about exponential convergence, delay tolerance, or disturbance damping use `A.3.3`, `C.27`, and evidence/assurance claim as live.

**Worked slice B - scientific theory.** A scientific theory is revised when labs publish findings and a research community reviews anomalies and accepted revisions. `B.2.5` records the theory or its constituent epistemes as supervised objects and the community/review practice as transformer-bearing supervisor. Journals, conferences, datasets, and review records are publication or interaction channels. The theory does not perform the sensing or judging; the acting systems and practices do.

**Worked slice C - product supervisor loop.** A product platform constrains component teams through published interface rules and release gates. `B.2.5` records the supervising platform policy role, component/subproduct holons, report channels, and constraint returns. Work authority uses `A.15`; gate passage uses `A.21`; interface commitments use module/interface patterns.

### B.2.5:5 - Archetypal Grounding

| Archetype | Without B.2.5 | With B.2.5 |
|---|---|---|
| System | A control diagram mixes physical parts, roles, and commands, then claims coordination is obvious. | The supervised systems, supervisor transformer, shared medium, feedback relation, and returned influence are named. |
| Episteme | A theory or model is said to sense, judge, plan, or adapt. | Acting systems and review practices carry the transformer role; the episteme is reviewed, revised, cited, or published. |

### B.2.5:6 - Bias-Annotation

* **Diagram closure bias.** A loop drawn on a diagram is read as a closed feedback loop. Repair by naming both observation/report and influence/constraint sides.
* **Layer/level bias.** Layered diagrams hide whether the label names control role, declared system level, aggregation scope, rate band, or publication grouping. Repair by recovering the declared kind.
* **Episteme-agent bias.** Knowledge-bearing objects are described as acting agents. Repair by naming the acting `Transformer`, publication or revision practice, and source/reliance relation.
* **Proof-by-loop bias.** A loop relation is read as stability, safety, or assurance proof. Repair by assigning the live claim kind to the governing exact governing pattern.

This checklist verifies the preceding guidance after the practitioner has chosen the live move; it is not a required project control form and not a substitute for the card, note, view, relation, or repair move above.

### B.2.5:7 - Conformance Checklist

| ID | Check | Why it matters |
|---|---|---|
| CC-B2.5-1 | A conforming use names supervised holon refs and the supervisor role/transformer refs. | Prevents ghost coordination. |
| CC-B2.5-2 | A conforming use names the shared medium or publication/interaction channel that carries observations, reports, signals, constraints, or influence. | Makes the loop inspectable. |
| CC-B2.5-3 | A conforming use names both observation/report and influence/constraint sides or explicitly says the loop is not closed. | Separates closed feedback loops from one-way commands. |
| CC-B2.5-4 | A conforming use keeps structural composition, supervisory relation, and interaction/publication network distinct. | Prevents layer/part category errors. |
| CC-B2.5-5 | Stability, safety, timing, causal, evidence, assurance, gate, and mathematical-lens claims are assigned to their governing exact governing patterns. | Prevents loop-as-proof overread. |
| CC-B2.5-6 | Episteme examples name the acting systems or practices that perform review, revision, publication, or use. | Prevents episteme-agent overread. |
| CC-B2.5-7 | If a control-structure view is live, the use cites or opens `C.30.LCA`. | Keeps relation-level feedback claims and view-level architecture claims aligned. |

### B.2.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Ghost coordination | Subholons coordinate, but no supervisor role, shared medium, or feedback relation is named. | Name supervisor role, acting transformer, observation/report side, and influence/constraint side. |
| Functional layer as component | A planning or control layer is modeled as a physical part of the controlled holon. | Separate structural composition from supervisory relation. |
| Perfect communication | The loop assumes instant, complete, or lossless access to subholon state. | Add interaction/publication medium limits and assign timing or information claims to `C.27`, `A.3.3`, or evidence claim. |
| Episteme acts | A theory, model, paper, or dashboard senses, judges, plans, or adapts. | Name the acting system, operator, review practice, or revision practice; keep the episteme as described or revised object. |
| Loop proves safety | The loop is treated as evidence, assurance, gate, or safety proof. | Keep the loop relation and apply the exact governing pattern for the live claim kind. |

### B.2.5:9 - Consequences

The gain is a precise loop relation that is usable for architecture, control, organizational, and epistemic examples without collapsing them. A practitioner can keep ordinary supervisor/subholon language while naming the acting role, medium, and returned influence.

The cost is that `B.2.5` no longer lets a layered-control diagram carry proof claim kinds. That cost is intentional: the loop relation is useful because it tells the practitioner what to inspect next, not because it silently certifies stability, safety, evidence, or assurance.

### B.2.5:10 - Rationale

Supervisor-subholon feedback loops are a recurring architecture form. The form is most useful when it is separated from structural mereology and from proof. That separation preserves the engineering insight from layered control architecture while keeping FPF's I/D/S and role/transformer distinctions intact.

The same separation also keeps the epistemic case precise. Scientific theories, documents, models, and other epistemes can participate in feedback loops as reviewed or revised objects and as publications or source/reliance objects, but acting systems and practices carry the transformer role. This lets the same pattern cover systems and epistemes without agentive overread.

### B.2.5:11 - SoTA-Echoing

| SoTA/practice anchor | What it informs | FPF adoption stance | Practitioner implication |
|---|---|---|---|
| Layered and multi-rate control architecture practice, with Matni/Ames/Doyle used here as lineage and practice lineage for layered multi-rate control rather than as current proof by itself. | Supervisor, plant, controller, planner, observer, feedback, and rate separation are useful relation cues for supervisor-subholon loop recovery. | Adopt and adapt: keep supervisor-subholon loop recognition, then assign stability, timing, safety, evidence, assurance, and gate claims to their governing patterns. | A loop diagram starts the relation record; dynamics, timing, and safety claims still need their own pattern. |
| Cyber-physical systems and feedback-control practice. | Shared medium limits, observation channels, actuation, delay, disturbance, and plant dynamics affect whether a loop is adequate. | Adopt: require loop closure and medium visibility; assign reusable dynamics claims to `A.3.3`. | If communication delay matters, it is not solved by the B.2.5 label. |
| Organizational policy and review practice. | Supervisory relations can be enacted through policies, review boards, reports, and publication channels. | Adapt: model the acting systems/practices and publication/source/reliance relations explicitly. | A committee or review practice may supervise; a published note does not act by itself. |
| FPF architecture-description discipline under `C.30` and `C.30.LCA`. | A supervisor loop can be one relation inside a control-structure view. | Reuse: `B.2.5` supplies relation recovery; `C.30.LCA` supplies view recovery. | Use the smallest pattern that carries the live claim kind, then open the neighbor when needed. |

### B.2.5:12 - Relations

* Builds on `B.2`, `A.1`, `A.2`, `A.3`, `A.7`, `A.12`, and `A.15`.
* Coordinates with `C.30.LCA` for control-structure view adequacy.
* Applies `A.3.3` for reusable dynamics or stability claims, `C.27` for temporal/rate adequacy, `C.28` for causal-use claims, `A.10`/`G.6` for evidence claim, `B.3` for assurance, `A.20`/`A.21` for constraint validity and gate decisions, `A.15` for work authority, and `C.29` for mathematical-lens transfer.

Does not replace: `C.30.LCA` control-structure view adequacy, `A.3.3` dynamics claim, `C.27` temporal/rate adequacy, `C.28` causal-use claim, `A.10`/`G.6` evidence claim, `B.3` assurance, `A.20`/`A.21` gate and constraint-validity records, `A.15` work authority, module/interface patterns, or `C.29` mathematical-lens adequacy.

### B.2.5:End
