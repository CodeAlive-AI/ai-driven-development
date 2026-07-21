## A.11 - Ontological Parsimony

> **Type:** Kernel parsimony and admission discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### A.11:0 - Use This When

Use this pattern when FPF work proposes a new U-kind, core relation, dependent durable value, or public structural name and the current question is whether existing ontology can express the claim without creating a new kind.

Typical moments:

- a new U-kind seems useful after `E.24.UK`;
- a proposed root kind may actually be a dependent value, slot, relation, record, publication form, lens, local frame, or C.3 `U.Kind`;
- two candidates overlap strongly;
- a name is convenient but the ontology may already be expressible through existing patterns.

**Primary EntityOfConcern.** The EntityOfConcern is the parsimony claim for one candidate ontology addition.

**First useful move.** Recover the candidate with `E.24.UK` or the direct governing pattern, then ask what current FPF values, slots, relations, and patterns can already express.

**What goes wrong if missed.** FPF grows duplicate kinds for slot positions, local names, publication forms, mathematical lenses, and records. Later patterns then argue over words instead of recovering the EntityOfConcern, relation, slot, and admissible claim.

**What this buys.** A small ontology can still express rich project situations: the pattern either admits a new durable value with a boundary, or shows exactly which existing kind, slot, relation, record, publication form, lens, or direct pattern already carries the claim.

**Not this pattern when.** Not this pattern when the current question is only a local display name, publication title, naming taste, or ordinary glossary cleanup. Use the relevant Part F naming pattern unless the name is being asked to carry durable ontology.

### A.11:1 - Problem Frame

FPF needs enough primitives to be useful, but every new primitive creates learning cost, bridge cost, and future repair cost. Ontological parsimony is not anti-growth. It is the rule that FPF adds a new kind only when composition, reuse, dependent-value settlement, and direct governing patterns cannot express the action-facing claim without material loss.

When source or draft wording proposes a candidate durable value in `U.*` form, treat that as an admission claim. A.11 is therefore applied after `E.24.UK` recovers the governed object and before naming patterns choose a public label.

### A.11:1.0 - Problem

A useful project word, slot-position label, publication form, diagram element, mathematical lens, or repeated source term can start acting like a durable FPF kind before the governed object and direct governing pattern are recovered. The problem is to decide whether the candidate preserves an action-facing distinction that composition cannot carry, or whether it should remain a local name, slot value, relation, record, publication form, or lens-use claim.

### A.11:1.1 - Forces

| Force | Tension |
| --- | --- |
| Expressive reach vs. kind inflation | FPF must name durable objects clearly, but each extra root kind increases learning, checking, and bridge cost. |
| Local usefulness vs. universal burden | A local project name may be helpful in one context, while a U-kind becomes a cross-corpus obligation. |
| Composition vs. material loss | Existing slots, relations, and patterns often express the claim, but some candidates preserve a distinction that composition would hide. |
| Reader clarity vs. ontology compactness | A plain label can help users, but a convenient label must not conceal a relation, slot position, publication form, or mathematical lens. |
| Growth vs. reopenability | FPF needs new primitives when problems demand them, but admitted values need reopen conditions when overlap or fuzziness appears. |

### A.11:2 - Solution

Use four gates before admitting the new ontology addition:

| Gate | Test question | Pass condition |
| --- | --- | --- |
| Composition | Can existing U-kinds, slots, relations, dependent values, or direct patterns express the claim? | Pass only when expression by composition loses a reviewable distinction. |
| Non-redundancy | Does the candidate overlap an existing governed value or relation? | Pass only when overlap is bounded and the remaining difference changes admissible claims. |
| Action-facing contribution | What can users claim, compare, repair, stop, rely on, or do because this addition exists? | Pass only when the contribution is not merely naming comfort or source prestige. |
| Sharp boundary | Is there a one-sentence inclusion and exclusion test? | Pass only when readers can distinguish included and excluded cases without private author intent. |

Use this compact record:

```text
ParsimonyAdmissionRecord:
  Candidate:
  RecoveredGovernedObject:
  E24UKDecisionRef:
  ExistingExpressionAttempt:
  MaterialLossIfComposed:
  OverlapWithExistingValues:
  ActionFacingContribution:
  BoundaryTest:
  Disposition:
```

Possible dispositions:

- retain as root U-kind;
- retain as dependent durable value under a root settlement;
- apply C.3 typed reasoning;
- express as slot, relation, record, publication form, lens, local frame, or direct governed value;
- keep as source wording or local name.

### A.11:2.1 - Archetypal Grounding - Maintenance

| Candidate claim | Parsimony result | Why |
| --- | --- | --- |
| `CoolingPump` as a new root U-kind | Express as a `U.System` or holon holding `CoolingCirculatorRole@Context`, with capability, method, and work claims added only when current. | The useful distinction is role, capability, method, and work around an existing system, not a new universal kind. |
| `Actuator` or another transformer-like noun | Recover the system or holon that participates as transformer in a `U.Transformation`; admit a durable value only if `E.24.UK` shows irreducible action-facing gain. | The bearer of change and the transformation relation are already governed; the noun alone does not create a kind. |
| Provenance-chain wording | Try G.6 evidence-graph and provenance addressing first; admit a new durable value only if the direct evidence or provenance patterns cannot express the needed claim without material loss. | Parsimony tries direct governing patterns before minting a kernel addition. |
| `SmallPart` or similar vague size class | Reject or keep local. | The boundary depends on private scale expectations unless a direct measurement or classification pattern supplies a crisp rule. |

A retained addition also needs a reopen condition. Reopen or lower the admission when usage collapses, overlap with an existing value is discovered, composition becomes adequate, the boundary becomes fuzzy, or the name starts hiding a slot, relation, record, publication form, lens, or local frame. This is maintenance discipline, not a fixed calendar ritual.

### A.11:4 - Bias-Annotation

A.11 corrects kind-inflation bias. A useful word, field name, record label, or diagram element can start behaving like a universal kind because it appears often, feels important, or has prestige in a source tradition. The repair is ontological: recover the governed object and try expression through existing U-kinds, slots, relations, dependent values, records, publication forms, lenses, and direct governing patterns before admitting a new durable value.

It also corrects false-parsimony bias. A compact ontology is not achieved by refusing every new value. If composition hides a reviewable distinction or blocks an action-facing claim, parsimony admits the new value and states its boundary, overlap, and reopen condition.

### A.11:3 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-A11-1` | The candidate's governed object is recovered before parsimony is judged. |
| `CC-A11-2` | If the candidate uses `U.*` force, `E.24.UK` is applied before F.5, F.8, or F.18 naming. |
| `CC-A11-3` | Existing expression by composition, slots, relations, dependent values, and direct governing patterns is attempted by value. |
| `CC-A11-4` | Material loss is stated as a lost claim, lost distinction, lost boundary, or lost admissible use, not as naming discomfort. |
| `CC-A11-5` | Strong overlap lowers or rejects the candidate unless the difference changes claims. |
| `CC-A11-6` | The final disposition is one of the allowed ontology outcomes, not a vague approval to keep the word. |

### A.11:5 - Common Anti-Patterns and How to Avoid Them

* **Slot label becomes kind.** A system in a role, transformer, source-maintenance, carrier, or boundary slot is renamed as if the slot label created a new universal kind.
* **Publication form becomes ontology.** A card, record, view, dashboard, figure, or report title is treated as the governed object instead of the episteme, relation, or carrier it publishes.
* **Mathematical lens becomes object.** A graph, tuple, algebra, metric, coordinate, or threshold is admitted as an ontology object without naming the EntityOfConcern and lens-use claim.
* **Local project name becomes kernel vocabulary.** A useful project label is promoted to durable FPF vocabulary before composition and direct-pattern expression are tried.
* **Overlap is ignored.** A candidate is admitted even though an existing pattern already carries the same claim with clearer boundaries.
* **Parsimony as refusal.** A new value is rejected because "fewer kinds is better" even though existing composition loses a distinction users need to claim, compare, repair, stop, or rely on.

### A.11:6 - Consequences

| Consequence | Benefit | Cost or boundary |
| --- | --- | --- |
| Smaller durable vocabulary | FPF stays learnable and bridgeable across domains because slot positions, relation values, records, lenses, and publication forms do not become accidental U-kinds. | The parsimony record must show the existing expression attempt by value; hand-waving about simplicity is not enough. |
| Better U-kind admissions | New durable values enter only with material loss, non-redundancy, action-facing contribution, boundary test, and reopen condition. | Some attractive names remain local or dependent even when they are common in source traditions. |
| Clearer neighboring-pattern use | Readers know when to return to E.24.UK, A.8, C.3, Part F naming, or a direct subject pattern. | The pattern does not choose the public name; it only decides whether durable ontology is warranted. |

### A.11:7 - Rationale

Ontological parsimony preserves FPF's ability to handle many domains without turning every local distinction into a root object. The pattern follows the same discipline used by `E.24.UK`: recover the governed object first, then decide whether a new durable value is needed. Slots, relations, dependent values, records, publication forms, and mathematical lenses are expressive resources; they are not failures to mint a kind.

The practical criterion is not abstract minimalism. A candidate earns admission only when users gain a claim, comparison, repair, stop condition, reliance condition, or boundary they cannot recover by composition without material loss. That keeps parsimony tied to FPF's work-facing purpose rather than to a taste for small vocabularies.

### A.11:8 - SoTA-Echoing

Current ontology-engineering practice favors modularity, reuse, explicit competency questions, and controlled admission of new terms over unchecked class growth. A.11 adapts that practice to FPF: the admission question is not merely "can a class be defined?" but whether the candidate changes admissible claims, boundaries, or work-facing use inside the FPF pattern system.

Constructional-ontology and BORO-like source lines add a second discipline: identity, construction, dependency, and part-whole distinctions must be recovered before a convenient term becomes a kind. FPF keeps that source discipline without importing a classical top-level taxonomy as-is; U-kinds remain tied to accepted ontics, slot discipline, and action-facing pattern use.

### A.11:9 - Relations

- **Builds on:** `E.24.UK`, `A.8`, `C.3`, `F.8`, `F.18`, and direct subject patterns.
- **Coordinates with:** `E.24.CD` for candidate detection and `E.24.PUB` when a publication form or structural name created the admission claim.
- **Does not replace:** universal-core testing in `A.8`, typed claim quantification in `C.3`, or naming discipline in Part F.

### A.11:End

