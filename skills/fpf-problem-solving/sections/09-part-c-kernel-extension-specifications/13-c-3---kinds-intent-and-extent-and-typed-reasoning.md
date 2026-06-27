## C.3 - Kinds, Intent and Extent, and Typed Reasoning

> **Type:** Typed reasoning discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### C.3:0 - Use This When

Use this pattern when a claim needs to say what kind of thing it quantifies over, which instances belong to that kind in a context slice, how intent and extent are related, and how typed compatibility affects composition.

**What goes wrong if missed.** A source type, local category, programming class, schema shape, or public `U.*` name starts doing several jobs at once: membership, scope, construction basis, public kind admission, and cross-context sameness all blur.

**What this buys.** Typed reasoning becomes reviewable before naming or ontology growth: the user can separate local `U.Kind` values, intent, extent, claim scope, bridge loss, and durable FPF U-kind admission.

Typical moments:

- two claims may be about different kinds of entities;
- scope is being widened by abstract wording instead of supported slices;
- a local kind needs membership, extension, bridge, or subkind reasoning;
- a `U.Kind` or `U.SubkindOf` occurrence must be kept distinct from durable FPF U-kind admission.

**Primary EntityOfConcern.** The EntityOfConcern is the typed reasoning claim: kind, intent, extent, membership, and typed compatibility in a bounded context.

**First useful move.** Ask whether the current question is C.3 typed reasoning or U-kind admission. If it is U-kind admission, use `E.24.UK`. If it is claim quantification, stay in C.3.

When a source ontology, schema, standard, class hierarchy, or top-level ontology supplies type, class, category, or subtype wording, C.3 may govern the local typed-reasoning claim. Use `E.24.UK` only when the source construct is being proposed as a public durable FPF U-kind or as part of an E.24 ontic settlement.

### C.3:1 - Problem Frame

Across contexts, "type" can mean ontology class, programming type, schema shape, category, source label, or public FPF U-kind. C.3 provides a smaller discipline: `U.Kind` is a context-local value used for typed reasoning about claims. It is not automatically a durable FPF U-kind and it does not by itself admit a `U.*` structural name. A C.3 `U.Kind` may be backed by construction, recognition, membership, or extent criteria in its bounded context, but that basis remains local typed-reasoning law until `E.24.UK` admits durable FPF kindhood.

### C.3:2 - Problem

A project often needs typed reasoning before it is doing ontology governance. The same working word may label a source category, a project-local grouping, a schema class, an ordinary-language kind, or a candidate public FPF U-kind. If the user treats all of these as the same object, the text starts making unsupported membership, scope, naming, and construction claims. C.3 keeps the current claim's local kind value visible while leaving durable U-kind admission to `E.24.UK`.

### C.3:3 - Forces

| Force | Tension |
| --- | --- |
| Local typed reasoning vs public ontology growth | A project needs typed claims now, but not every useful local kind deserves a durable FPF `U.*` name. |
| Intent vs extent | A definition, recognition rule, or construction basis may be clear while current membership is disputed, stale, or context-local. |
| Scope vs kind | A claim can have a narrow scope without creating a narrower kind. |
| Same wording vs same kind | Two contexts may reuse a label while membership criteria, bridges, and loss notes differ. |
| Formal discipline vs working use | Users need enough typing to avoid category mistakes without turning every local distinction into ontology engineering. |

### C.3:4 - Core Split

Keep four objects separate:

| Object | Meaning |
| --- | --- |
| `U.Kind` | Context-local kind value naming what a claim quantifies over. |
| Intent | The kind's signature, predicates, invariants, and formality-bearing definition. |
| Extent | The instances belonging to the kind in one context slice. |
| Scope | Where a claim holds; this belongs to claims or capabilities, not to kinds. |

Typed reasoning composes with F-G-R and USM by order: first typed compatibility, then scope coverage, then assurance and freshness penalties where relevant.

### C.3:5 - Solution

Use C.3 when the current claim is about typed compatibility, membership, kind intent, kind extent, or cross-context kind bridges.

Do not use C.3 to admit durable U-kind names. That decision belongs to `E.24.UK`, with `A.8`, `A.11`, `F.8`, and `F.18` when kernel-level or public naming force is current.

Normative decisions:

1. `U.Kind` is context-local and intent-bearing.
2. `U.SubkindOf` is a partial-order relation over C.3 `U.Kind` values.
3. Kind intent and kind extent are different claims and may have different evidence.
4. Kinds do not carry scope; claim scope and work scope remain USM values.
5. Cross-context kind reuse requires bridge discipline and loss notes.
6. Public `U.*` spelling in a heading, title, filename, or ToC row does not follow from C.3 typed reasoning.

### C.3:6 - Decision Split With E.24.UK

Use this decision split:

| Current question | Governing pattern |
| --- | --- |
| What kind of thing does this claim quantify over? | `C.3`, `C.3.1`, and dependent C.3 patterns |
| Is this local kind a subkind of that local kind? | `C.3.1` |
| Does this context-local kind deserve a durable public FPF `U.*` name? | `E.24.UK`, then `F.8` and `F.5` or `F.18` |
| Is the candidate universal enough for kernel-level status? | `A.8` after `E.24.UK` |
| Can existing ontology express it without a new kind? | `A.11` after object recovery |

### C.3:7 - Archetypal Grounding

| Situation | C.3 typed-reasoning move | Boundary |
| --- | --- | --- |
| A safety standard uses a source category such as "critical component". | Treat the category as a context-local `U.Kind` value with intent and extent criteria for this claim. | Do not mint a durable FPF U-kind unless `E.24.UK` admits the ontic and public naming case. |
| A software schema has a `Customer` class. | Use C.3 to ask what claims quantify over instances matching that schema in the bounded context. | Do not assume the schema class is the same kind as a contractual customer, user role, payer, or account holder. |
| A cross-discipline term appears with the same label in two traditions. | Keep kind reuse bridge-visible and record loss notes before comparing extents. | Same label is not sameness of kind or scope. |
| A local project splits "robotic musical instrument" into several working categories. | Let local kinds support the current typed reasoning claim. | Public `U.*` spelling, FPF naming, and durable ontic admission remain outside C.3. |

### C.3:8 - Bias-Annotation

C.3 blocks two common biases. First, lexical bias: a familiar type word is treated as if it already carried intent, extent, scope, and public FPF kindhood. Second, ontology-growth bias: every useful project distinction is promoted into a durable `U.*` kind instead of remaining a local typed-reasoning value with bridge and scope discipline.

### C.3:9 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C3-1` | The text distinguishes C.3 `U.Kind` from durable FPF U-kind admission. |
| `CC-C3-2` | Intent, extent, and scope are not collapsed. |
| `CC-C3-3` | `U.SubkindOf` is used only as a partial-order relation over C.3 kinds unless another governing pattern explicitly says otherwise. |
| `CC-C3-4` | Public `U.*` spelling, structural headings, and new U-kind claim are governed by `E.24.UK` before C.3 typed-reasoning values are published as public FPF names. |
| `CC-C3-5` | Cross-context reuse uses bridge discipline rather than pretending that same wording gives sameness. |

### C.3:10 - Common Anti-Patterns and How to Avoid Them

* Treating a programming type, schema class, source ontology class, regulatory category, or everyday noun as a durable FPF U-kind without `E.24.UK`.
* Treating a narrower claim scope as a narrower kind.
* Treating same wording across contexts as same kind without bridge and loss notes.
* Treating current extent as the whole intent of the kind.
* Treating intent clarity as proof that all disputed instances already belong to the extent.

### C.3:11 - Consequences

**Benefits.** C.3 lets users make typed claims without premature ontology growth; it keeps local membership, scope, and cross-context reuse inspectable.

**Costs.** The user must state intent and extent when they matter and must not hide cross-context loss behind familiar labels.

**Risks avoided.** The main avoided risks are false sameness, accidental public `U.*` minting, and category mistakes in selector, evidence, architecture, or method claims.

### C.3:12 - Rationale

Typed reasoning in FPF keeps the meaning rule, current members, and claim scope as different objects. That separation lets a project use typed compatibility locally without turning every project grouping, source class, or imported category into FPF ontology growth.

### C.3:13 - SoTA-Echoing

Ontology engineering, model theory, schema practice, and bounded-context modeling all separate classification rules from current instances and from the scope of a particular assertion. C.3 adapts that discipline for FPF users by making `U.Kind` local and claim-facing, while `E.24.UK` governs durable public FPF U-kind admission. The practical safeguard is parsimony: typed reasoning remains available everywhere, but public kind growth requires an ontic, slot relation, naming, and admission case.

### C.3:14 - Detail Map

C.3 is the head pattern for typed reasoning. It should not replay all C.3 mechanics, but it must leave the detailed loci visible.

| Needed detail | Governing locus | Content carried there |
| --- | --- | --- |
| Intent and membership | `C.3.2` | `KindSignature`, formality, extension, membership, definedness, and the rule that kinds carry no claim scope. |
| Cross-context kind reuse | `C.3.3` | KindBridge, the two-bridge rule for kind and scope, loss notes, and target-context membership evaluation. |
| Local adaptation without cloning a kind | `C.3.4` | RoleMask, mask registration, mask adapters, and the boundary between masks and subkinds. |
| Abstraction facet | `C.3.5` | KindAT levels, use limits, and catalog expectations. |
| Typed guards and applied examples | `C.3.A` | Guard macros, regulatory categories, evidence and assurance use, method and work compatibility, and worked cross-context cases. |

Do not treat this compact head pattern as the whole C.3 discipline when a case needs membership, bridge, mask, abstraction, or applied-guard detail. Use the neighboring C.3 pattern that governs the live detail.

### C.3:15 - Relations

- **Builds on:** USM scope discipline, F-G-R, C.2.3 formality, and bridge patterns.
- **Coordinates with:** `C.3.1` through `C.3.5`, `C.3.A`, `E.24.UK`, `A.8`, `A.11`, `F.8`, and `F.5`.
- **Does not replace:** ontic settlement in `E.24`, U-kind admission in `E.24.UK`, or naming in Part F.

### C.3:End

