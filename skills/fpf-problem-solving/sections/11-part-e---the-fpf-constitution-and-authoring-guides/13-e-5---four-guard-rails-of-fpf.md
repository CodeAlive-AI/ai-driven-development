## E.5 - Four Guard‑Rails of FPF

> **Status:** Stable

### E.5:1 - Problem frame
Use this pattern when authoring or revising Core concepts or their Tooling and Pedagogy forms. Four recurring risks require different checks:

1. **Implementation language** — concept prose acquires tool-specific terms.
2. **Notation lock-in** — one diagram style becomes the only way to express a concept.
3. **Reverse dependencies** — a local convenience makes Core depend on an outer layer.
4. **Disciplinary bias** — domain-specific assumptions enter rules intended for several domains.

These risks undermine Pillars **P-1 Cognitive Elegance**, **P-4 Open-Ended Kernel** and **P-5 FPF Layering**. Use E.5.1–E.5.4 for the corresponding detailed rules.

### E.5:2 - Problem
Core definitions can become tied to transient tools or one notation, acquire dependency cycles, or present domain-specific assumptions as universal. Authors need constraints that preserve reusable meanings while permitting concrete examples and different forms of expression.


### E.5:3 - Forces

| Force | Tension |
|-------|---------|
| **Abstraction vs Concrete Use** | Stable concept definitions ↔ useful real examples. |
| **Universality vs Convention** | Rules valid across domains ↔ convenience of one familiar notation. |
| **Modularity vs Integration** | Independent layers ↔ temptation to cross‑link for speed. |
| **Cross-Domain Use vs Perspective** | Claims intended across domains ↔ contributors’ disciplinary and cultural assumptions. |

### E.5:4 - Solution — the Four Guard‑Rails
Every Core, Tooling, and Pedagogy artefact must obey these **four guard-rails** at its own layer.
**Scope.** These guard-rails regulate concepts, claims and their relations. Abstract Core definitions exclude incidental tools, formats and workflows. A rule about a named publication form, protocol or grammar may retain the syntax necessary for that subject under E.5.1, with its edition/use boundary. Linting and automation remain outside Core and are optional unless a separate operational contract requires them; they preserve the governed conditions rather than define the concepts.

| # | Guard‑Rail | Protects against |
|---|------------|------------------|
| **GR‑1** | **DevOps Lexical Firewall** | Pull of implementation, governance, automation, and DevOps concerns |
| **GR‑2** | **Notational Independence** | Notation lock‑in |
| **GR‑3** | **Unidirectional Dependency** | Convenience cycles |
| **GR‑4** | **Cross‑Disciplinary Bias Audit** | Disciplinary monoculture |

Concrete rules for each rail live in patterns **E.5.1 – E.5.4**.

### E.5:5 - Archetypal Grounding (System / Episteme)

| Guard‑Rail | `U.System` example | `U.Episteme` example |
|------------|-------------------|----------------------|
| GR‑1 | Definition of `U.System` never cites file formats or build scripts. | Definition of `U.Episteme` avoids naming specific proof engines. |
| GR‑2 | A meaning-preserving mapping between text and diagram retains the pump boundary invariant. | A meaning-preserving mapping between algebraic and graph expressions retains F‑G‑R semantics. |
| GR‑3 | A sizing helper imports Core invariants; Core never imports helper tutorials. | Learning guide cites R‑score; Core does not derive its semantics from the guide. |
| GR‑4 | Bias audit removes thermo‑mechanical jargon from a “universal” pattern. | Audit replaces physics‑centric metaphors in a trust pattern. |

### E.5:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑GR.1** | Every new Core pattern **SHALL** cite, in its *Relations* section, the guard‑rail(s) it relies on or may affect. | Ensures traceability and deliberate rule interaction. |
| **CC‑GR.2** | Core, Tooling and Pedagogy respect GR-1 through GR-4 at their own layer: implementation and runnable teaching remain in their sources; necessary subject-defining syntax follows E.5.1 and interpretation/mapping follows E.5.2. | Preserves both portability and applicable concrete-subject rules. |
| **CC‑GR.3** | A revision to any guard‑rail pattern **REQUIRES** a Design‑Rationale Record that (a) states the reason, and (b) includes a Pillar‑impact analysis per E.3 precedence model. | Aligns evolution with higher‑level principles. |
| **CC‑GR.4** | The aggregate of guard‑rail rules **MUST** remain internally consistent and acyclic; no guard‑rail may override another without explicit precedence edges. | Preserves deterministic governance. |
| **CC‑GR.5** | Every Core pattern **MUST** anchor its primary EntityOfConcern or primary relation with a declared **ReferencePlane** (`world | concept | episteme`) at first mention. | Keeps Core about extensional or intensional values rather than their paperwork, and aligns with CHR:ReferencePlane. |

*All CC‑GR duties are **conceptual**. Any automated checks are **informative only** and live in Tooling/Pedagogy.*

### E.5:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Long‑term integrity** – stops slow drift of the Core toward jargon, notation lock‑in, and hidden cycles. | Authors must check the applicable guard-rails before submission. |
| **Stable yet evolvable ecosystem** – Core meanings can remain stable while Tooling and Pedagogy change independently. | Early stage contributions may feel constrained; examples in the Pedagogical Companion show compliant paths. |
| **Trust & auditability** – readers can inspect the declared meaning, dependency and bias boundaries. | Review adds effort; the four named rules make its scope explicit. |

### E.5:8 - Rationale
The four guard-rails turn abstract Pillars into constraints on wording, notation, dependency and bias. Grouping them here gives newcomers one entry to the applicable rule, identifies any needed amendment, and supplies shared requirements for optional automated checks.

They instantiate Pillars **P-1**, **P-2**, **P-4** and **P-5** and follow the precedence order defined in **E.3**.


### E.5:9 - Relations

* **Comprises:**
  * `pat:guard/devops‑firewall` (E.5.1) – GR‑1
  * `pat:guard/notational‑independence` (E.5.2) – GR‑2
  * `pat:guard/unidirectional‑dependency` (E.5.3) – GR‑3
  * `pat:guard/bias‑audit` (E.5.4) – GR‑4
* **Depends on:**
  * `pat:constitution/pillars` (E.2)
  * `pat:constitution/principle‑taxonomy` (E.3)
* **Constrains:** every Core, Tooling, and Pedagogy artefact; all DRRs.

### E.5:End
