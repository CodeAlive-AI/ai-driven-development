## A.5 - Open-Ended FPF Kernel and Extension Layering

**Normativity:** Informative. **A.6.0 `U.Signature`** and **A.6.1 `U.Mechanism`** govern declaration boundaries; **E.5.3** constrains dependency direction and **E.10** governs terminology.

> **Status:** Stable

### A.5:1 - Problem frame

**Use this when** adding or revising domain knowledge raises a question about what belongs in the shared Kernel, which assumptions belong in an extension, or which uses depend on a changed declaration.

**First useful move.** Name the contribution, its applicability and the declarations it relies on. Reuse an adequate existing contribution. For a new domain-specific assumption, keep its applicability with the extension rather than making every Kernel use depend on it.

FPF combines shared conceptual grounds with domain Methods by keeping the common commitments stable enough for reuse while allowing extensions to supply different assumptions and laws. Competing explanations can remain available under their respective conditions.

Different domains can require different assumptions and laws. Making a domain-specific assumption an unconditional Kernel commitment would impose it on uses where it may not hold and make those uses depend on its revision. Place domain-specific knowledge in extensions by default, with its applicability stated. Use **A.8** to test a U-kind’s cross-domain contribution and **A.11** to test whether a new ontological value is needed. The declaration rules in **A.5:4** expose dependencies so that a changed declaration can be followed to the uses that rely on it.

### A.5:2 - Problem

Admitting domain-specific primitives without their applicability boundaries can create two problems:

| Problem | Practical effect |
| --- | --- |
| **Kernel bloat** | Adding unnecessary root U-kinds or local type vocabularies increases what every Kernel user must understand and maintain. |
| **Conflicting assumptions** | Incompatible axioms presented as unconditional commitments leave the reader unable to select an applicable explanation. |

### A.5:3 - Forces

| Force                            | Tension                                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Stability vs. Evolvability**   | Stable core needed for trust ↔ constant domain innovation needed for relevance.                                       |
| **Universality vs. Specificity** | Single kernel language ↔ rich disciplinary idioms.                     |
| **Parsimony vs. Coverage**       | Few primitives keep reasoning elegant ↔ framework must still model energy budgets, epistemic uncertainty, agentic goals. |

### A.5:4 - Solution

FPF pattern texts publish law-governed declarations—vocabulary, laws and applicability—that can be reused and specialized.

To keep the Kernel open‑ended, use the following boundary rules:

1. **Kernel minimality (C‑5).** Domain knowledge stays outside the Kernel by default; it enters as extension vocabularies and laws.
2. **Boundary packaging via `U.Signature` (A.6.0).** For reusable declaration bundles admitted as signatures under **A.6.0**, expose actual declaration dependencies in an explicit `SignatureManifest` (`imports`, `provides`).
3. **Dependency vs specialisation are separate relations.** `imports` forms a dependency DAG constrained by **E.5.3**; refinement/extension (`⊑`, `⊑⁺`) is expressed separately (for mechanism declarations, see **A.6.1:4.8**; use **C.29** when a mathematical morphism is claimed) and should not be conflated with `imports`.
4. **Registry references stay references.** Registry identifiers, such as Bridge ids, policy‑ids and edition‑ids in Part F, are cited or pinned where needed, not treated as exported symbols in `provides`.

For example, an extension describes a cooling Method under specified fluid and operating-range assumptions. Keep those assumptions and its heat-transfer law with the extension. If its declaration bundle is admitted as a `U.Signature`, its manifest identifies the scale declaration it imports and the declarations it provides. A changed scale declaration directs attention to the cooling claims that depend on it. A changed fluid assumption instead requires reconsidering uses that rely on that applicability condition; it does not make the assumption a Kernel law. This connects a local revision to its affected uses while preserving unrelated contributions.

### A.5:End
