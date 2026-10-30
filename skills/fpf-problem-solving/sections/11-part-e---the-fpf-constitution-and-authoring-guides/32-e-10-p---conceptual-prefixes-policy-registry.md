## E.10.P - Conceptual Prefixes policy & registry

> **Status:** Stable

**Intent.** Provide a compact, **notation-neutral** registry and **minting policy** for *conceptual prefixes*: short labels for the Core vocabularies and constructs in use.

**Policy (normative).**
1. **Purpose.** A conceptual prefix exists **to aid reasoning**, not to name files, serialisations, or APIs. It signals the conceptual construct or vocabulary in use (for example, meta-type, calculus operator or relation family).
2. **Anchoring.** Every prefix **MUST** name the Core patterns that define its constructs, operators or vocabulary, or govern admission to its namespace. List these anchors in the registry and cite them in *Relations*. For a family with several definitions, name the supplying patterns for the relevant members.
3. **No tool lock‑in.** A prefix **MUST NOT** imply a particular notation or machine binding (see E.5.1–E.5.2).
4. **Minting rule.** New prefixes are introduced by a **DRR** (E.9) that demonstrates
    (a) cross‑pattern need,
    (b) non‑overlap with existing prefixes,
    (c) alignment with Pillars **P‑1/P‑5**.
5. **Scope.** Prefixes are **globally reserved** within the Core; domain patterns **MAY** mint local shorthands only within a named local glossary and its effective scheme and **MUST NOT** collide with this registry.

**Registered conceptual prefixes (Core).**
* `U.` — namespace for U-kinds admitted under E.24.UK, whose dispositions cover root and dependent kinds. Spelling, dependence or reuse alone does not establish U-kind admission. *Anchors:* E.10:8.3, M-P1, reserves the namespace; E.24.UK:4.1–4.3 governs admission. Each kind retains the identity or membership rule in its defining subject pattern.
* `Γ_` — **calculus-operator notation**, for example `Γ_epist`, `Γ_ctx` and `Γ_time`. *Anchors:* E.10:8.3, M-P1, reserves the prefix; B.1.3:4.2 defines the synthesis and compilation operators; B.1.4:3 defines the optional notation for contextual and temporal aggregation. Other flavours cite their own operator definitions. For a system aggregation or delimitation decision, use B.1.2:4 to recover the separately governed results and any missing basis.
* `ut:` — **Universal relation family** (e.g., `PartOf` sub‑relations). *Anchor:* A.14 (Mereology) — informative alias vocabulary.
* `tv:` — **Trace & Validation vocabulary** (CT2R‑LOG): `tv:AliasOf`, `tv:groundedBy`. *Anchor:* B.3.5 (CT2R-LOG).
* `ev:` — **Evidence-account vocabulary**, used for source and support labels in a descriptive account. Each support or assurance claim retains its direct governing rule. *Anchor:* A.10 / B.3.
* `mero:` — **informative trace labels** `SumTrace`, `SetTrace` and `SliceTrace` for C.13's `sum`, `set` and `slice` construction accounts. A materialized trace is a C.2.1 episteme; these labels introduce no additional kinds. *Anchor:* C.13.

**Conformance Checklist (E.10.P).**
* **CC‑LEX‑P.1** New Core text **SHALL NOT** introduce an unregistered conceptual prefix.
* **CC‑LEX‑P.2** Each occurrence of a registered prefix **SHALL** cite the applicable defining anchor on first use in a section.
* **CC‑LEX‑P.3** Incidental examples that expand a prefix into a concrete URI or machine syntax **MUST** mark the expansion *informative* and locate it in Tooling/Pedagogy. A pattern governing that concrete syntax may include necessary examples under E.5.1; the conceptual prefix alone establishes no machine binding.

**Relations.** Uses E.10:8.3 for namespace reservation, E.24.UK:4.1 for U-kind admission, B.1.3:4.2 and B.1.4:3 for the listed Γ operators, B.1.2:4 for system aggregation and delimitation decisions, and A.14, A.10, B.3, B.3.5 and C.13 for the remaining registered vocabularies. Applies E.5.1 (Lexical Firewall) and E.5.2 (Notational Independence); depends on E.9 (DRR).

### E.10.P:End
