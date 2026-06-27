## C.3.1 - U.Kind and U.SubkindOf Core

> **Type:** Typed reasoning core pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### C.3.1:0 - Use This When

Use this pattern when a context needs a minimal kind value and subkind order for typed claim reasoning.

**What goes wrong if missed.** A local kind order is confused with durable FPF U-kind governance: subkind links start standing in for construction, ontic admission, naming, scope, or dependency relations.

**What this buys.** The user gets a small, inspectable typed-reasoning core: `U.Kind` values stay context-local, `U.SubkindOf` remains a partial order, and durable U-kind admission stays with `E.24.UK`.

Typical moments:

- a claim needs a context-local kind value for what it quantifies over;
- a local kind order is needed for typed compatibility;
- `U.SubkindOf` is being mistaken for dependent durable U-kind relation;
- a source says "type" or "kind" and the author must decide whether the current use is C.3 typed reasoning or E.24.UK U-kind admission.

**Primary EntityOfConcern.** The EntityOfConcern is the C.3.1 core relation among context-local `U.Kind` values and the `U.SubkindOf` partial order.

### C.3.1:1 - Problem Frame

C.3.1 gives FPF a small object for typed reasoning without importing a full ontology stack. `U.Kind` names a kind of thing in one context. `U.SubkindOf` orders such kinds. This is different from durable FPF U-kind admission. A C.3 `U.Kind` can become part of a U-kind admission question, but it is not admitted merely by being a `U.Kind`.

### C.3.1:2 - Problem

A user can need the sentence "cooling pump is a pump" to be typed and checkable without claiming that FPF must add `U.CoolingPump`. If `U.SubkindOf` is allowed to stand for every stronger-looking relation, then dependency, part-whole, slot filling, construction, and public naming all collapse into one hierarchy. C.3.1 keeps the partial order narrow so other governing relations stay available.

### C.3.1:3 - Forces

| Force | Tension |
| --- | --- |
| Minimal typed reasoning vs full ontology | A claim needs kind compatibility, but not every kind needs an ontic and public U-kind name. |
| Subkind order vs dependency | A partial order over kinds is useful, but it is not a generic depends-on, part-of, slot, or construction relation. |
| Context-local use vs cross-context reuse | A kind can work inside one context while same-word reuse still needs bridge discipline. |
| Intent and membership detail vs compact core | C.3.1 keeps the core small; intent, membership, and bridges remain with neighboring C.3 patterns when live. |

### C.3.1:4 - Core Objects

| Object | Meaning |
| --- | --- |
| `U.Kind` | Context-local kind value used by claims for typed quantification. |
| `U.SubkindOf` | Partial-order relation over `U.Kind` values. |
| Kind identity | The local identity criterion that says when two kind refs in the same context name the same kind. |
| Parent and child links | Declared or computed `U.SubkindOf` links. |

### C.3.1:5 - Solution

Use `U.Kind` and `U.SubkindOf` only for local typed-reasoning compatibility unless another pattern explicitly brings the value into durable U-kind admission.

Norms:

1. `U.SubkindOf` is reflexive, transitive, and antisymmetric over `U.Kind` values.
2. A `U.Kind` carries no claim scope. Scope belongs to claims or capabilities under USM.
3. Intent and membership are governed by C.3.2, not by this core pattern.
4. Cross-context sameness or translation uses kind bridge discipline, not shared spelling.
5. `U.SubkindOf` is not the relation that makes a dependent durable U-kind under `E.24.UK`.
6. A structural `U.*` name that looks like a root FPF kind is governed by `E.24.UK`.

### C.3.1:6 - Decision Split

| Source cue | C.3.1 disposition |
| --- | --- |
| "This claim ranges over cooling pumps." | Create or cite the context-local `U.Kind` for cooling pump. |
| "Cooling pump is a subkind of pump." | Declare `U.SubkindOf(CoolingPumpKind, PumpKind)` in the context. |
| "CoolingPump should become a public FPF U-kind." | Use `E.24.UK`, `A.11`, and `A.8` as needed. |
| "`U.WorkPlan` depends on `U.Work`." | Do not encode as `U.SubkindOf` unless C.3 typed reasoning actually claims a subkind order. Use the governing work or E.24.UK settlement. |

### C.3.1:7 - Archetypal Grounding

| Situation | C.3.1 move | Boundary |
| --- | --- | --- |
| "Cooling pump is a pump." | Declare a context-local `U.SubkindOf(CoolingPumpKind, PumpKind)` relation. | Do not infer a durable `U.CoolingPump` root kind. |
| "WorkPlan depends on Work." | Use the governing work or E.24.UK relation. | Do not encode dependency as `U.SubkindOf` unless a real kind partial order is being claimed. |
| "Safety-critical function is a kind of function." | Use a local `U.Kind` and subkind order for the current claim. | Membership and intent detail go to C.3.2; public FPF naming goes to Part F after U-kind admission. |

### C.3.1:8 - Bias-Annotation

C.3.1 prevents subkind bias: using one familiar hierarchy relation as a universal relation for dependency, composition, construction, slot filling, role assignment, public naming, or ontology admission. It also prevents public-name bias: assuming a `U.*` spelling follows from a local kind value.

### C.3.1:9 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C31-1` | Every `U.Kind` use is context-local unless a bridge says otherwise. |
| `CC-C31-2` | Every `U.SubkindOf` use is a partial-order claim over `U.Kind` values. |
| `CC-C31-3` | Scope is not stored on the kind value. |
| `CC-C31-4` | Dependent durable U-kind relations are not modeled as `U.SubkindOf` by default. |
| `CC-C31-5` | U-kind admission and structural `U.*` repair are governed by `E.24.UK`; public naming demand is handled by Part F after the governed value is recovered. |

### C.3.1:10 - Common Anti-Patterns and How to Avoid Them

* Encoding dependency, part-whole, slot filling, construction, or admission as `U.SubkindOf`.
* Treating a source "type" hierarchy as a public FPF U-kind hierarchy.
* Storing claim scope on `U.Kind` instead of on the claim or capability.
* Treating `U.SubkindOf` as the relation that admits dependent durable U-kinds.
* Using public `U.*` spelling before `E.24.UK` and naming patterns admit it.

### C.3.1:11 - Consequences

**Benefits.** Typed compatibility and kind order remain available for everyday reasoning without forcing ontology growth.

**Costs.** Users must use the neighboring patterns for intent, membership, bridges, and U-kind admission when those questions become live.

**Risks avoided.** C.3.1 avoids false hierarchies, accidental U-kind minting, and dependency relations disguised as subkind relations.

### C.3.1:12 - Rationale

The core must stay small because it is used inside many other FPF claims. Once a local kind relation starts carrying construction, admission, naming, scope, or slot discipline, it becomes too heavy and starts creating false ontology. C.3.1 therefore gives only the typed partial order and leaves stronger relations to the patterns that govern those objects.

### C.3.1:13 - SoTA-Echoing

Formal type systems, ontology engineering, and bounded-context modeling all distinguish a local classification relation from the public ontology or schema governance that may later reuse it. C.3.1 follows that separation: `U.Kind` is a local typed-reasoning value and `U.SubkindOf` is a partial-order claim over those values. Durable FPF U-kind admission needs `E.24.UK` because it carries ontic identity, slot relation, naming, construction, and parsimony obligations that a local subkind order does not carry.

### C.3.1:14 - Relations

- **Builds on:** `C.3`, USM, F-G-R, and C.2.3 formality.
- **Coordinates with:** `E.24.UK`, `A.8`, `A.11`, `F.8`, and `F.5`.
- **Does not replace:** C.3.2 intent and membership, C.3.3 bridges, or E.24-family U-kind governance.

### C.3.1:End

