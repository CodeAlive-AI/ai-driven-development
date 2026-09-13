## A.11 - Ontological Parsimony

> **Type:** Kernel parsimony and admission discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### A.11:0 - Use This When

Use this pattern when FPF work proposes a new U-kind, core relation, dependent durable value, or public structural name and the current question is whether existing ontology can express the claim without the proposed durable ontology addition.

Typical moments:

- a new U-kind seems useful after `E.24.UK` recovers the candidate object;
- a proposed root kind may actually be a dependent value, slot, relation, record, publication form, lens, local frame, or C.3 `U.Kind`;
- two candidates overlap strongly;
- a name is convenient but the ontology may already be expressible through existing patterns.

**Primary EntityOfConcern.** The EntityOfConcern is the parsimony claim for one candidate ontology addition.

**First useful move.** Recover the candidate with `E.24.UK` or the subject pattern, then find the best current FPF expression for the exact receiving claim or use.

In this pattern, an **existing governed expression** is an admitted kind or dependent value, slot, current relation, record, publication form, lens, local frame, or direct-pattern claim whose direct owner defines its use.

**What goes wrong if missed.** FPF grows duplicate kinds for claims already carried by governed expressions. Later patterns then argue over words instead of recovering the EntityOfConcern, exact relation or slot, and admissible claim.

**What this buys.** A small ontology can still express rich project situations: A.11 either identifies the existing governed expression that carries the claim or supplies a positive parsimony finding, with a boundary, for the candidate's complete admission test.

**Not this pattern when.** The current question is only a local display name, publication title, naming taste, or ordinary glossary cleanup. Use the relevant Part F naming pattern unless the name is being asked to carry durable ontology.

### A.11:1 - Problem Frame

FPF needs enough primitives to be useful, but every new primitive creates learning cost, bridge cost, and future repair cost. Ontological parsimony is not anti-growth. It tests whether composition, reuse, dependent-value settlement, and subject patterns can express the action-facing claim without material loss. A positive parsimony finding is necessary for the proposed addition; it does not complete its admission.

When source or draft wording proposes a candidate durable value in `U.*` form, treat that as a proposal requiring an admission decision. Apply A.11 after `E.24.UK` recovers the governed object and before naming patterns choose a public label.

For a relation-kind candidate, first apply `A.6.P`. If the participants are exact but no current direct relation expresses the named receiving claim, apply `A.6.RCD`. Stop when it returns an existing exact predicate, a local compound claim, or subject-bounded or reusable predicate-definition content. A derived relation-kind candidate continues only when a named use needs stable occurrence semantics and supplies its proposed direct settlement; an irreducible primitive relation-kind candidate continues only under A.6.RCD disposition 4.

### A.11:1.0 - Problem

A useful project word, slot-position label, publication form, diagram element, mathematical lens, or repeated source term can start acting like a durable FPF kind before the governed object and subject pattern are recovered. The problem is to decide whether the candidate preserves an action-facing distinction that the best existing governed expression cannot carry, or should remain that expression or a local name.

### A.11:1.1 - Forces

| Force | Tension |
| --- | --- |
| Expressive reach vs. kind inflation | FPF must name durable objects clearly, but each extra root kind increases learning, checking, and bridge cost. |
| Local usefulness vs. universal burden | A local project name may be helpful in one context, while a U-kind becomes a cross-corpus obligation. |
| Composition vs. material loss | Existing slots, relations, and patterns often express the claim, but some candidates preserve a distinction that composition would hide. |
| Reader clarity vs. ontology compactness | A plain label can help users, but a convenient label must not conceal a relation, slot position, publication form, or mathematical lens. |
| Growth vs. reopenability | FPF needs new primitives when problems demand them, but admitted values need reopen conditions when overlap or fuzziness appears. |

### A.11:2 - Solution

Use four gates to establish the parsimony finding for the proposed ontology addition. Apply every gate to the same exact candidate, receiving claim or use, and current facts. Find the best existing expression first; then state the exact loss, overlap discriminator, newly admissible claim or action, and nearest excluded case for that same use. A positive finding continues the complete admission test under E.24/E.24.UK or the candidate's direct subject-kind governor; it is not that admission result or project-side permission.

| Gate | Test question | Pass condition |
| --- | --- | --- |
| Composition | What is the best existing governed expression for this exact receiving claim or use? | Pass only when that expression loses a stated claim, boundary, or admissible use. |
| Non-redundancy | How far does the candidate overlap an existing governed value or relation, and what discriminates the remainder? | Pass only when the bounded remainder changes an admissible claim for the same use. |
| Action-facing contribution | Which exact claim or action becomes admissible because this addition exists? | Pass only when that contribution reaches the named use rather than supplying naming comfort or source prestige. |
| Sharp boundary | What is the one-sentence inclusion test, and which nearest case is excluded? | Pass only when both cases can be distinguished from stated facts without private author intent. |

The questions can be answered as an ordinary comparison. Use this compact record or view when the result must be retained or consumed. If an E.24-family decision is current, put or reference the parsimony evidence there and resolve this view back to that decision, preserving every required E.24:4.0a value. The view is not a second independently editable admission decision; a local wording or existing-expression answer need not create one.

```text
ParsimonyAdmissionRecord:
  Candidate: candidate examined by this parsimony inquiry
  RecoveredGovernedObject:
  E24FamilySettlementDecisionRef: exact E.24:4.0a shared decision when one is current
  ReceivingClaimOrUse:
  CurrentFactsRef:
  ExistingExpressionAttempt: best existing governed expression for that claim or use
  MaterialLossIfComposed: exact lost claim, boundary, or admissible use
  OverlapWithExistingValues: extent plus discriminator
  ActionFacingContribution: exact newly admissible claim or action
  BoundaryTest: inclusion test plus nearest excluded case
  Disposition: parsimony finding and continuation; cite the separate admission result when current
```

Possible continuations of the parsimony finding:

- retain as a root U-kind only with the corresponding complete admission result;
- retain as a dependent durable value only with its complete root-coupled settlement: same-individual dependence keeps the root individual's identity and adds a stable membership condition implying root-kind membership for that same individual; identity dependence identifies a distinct individual through a governed relation to a named root individual and all additional discriminators;
- retain as a local C.3 kind or typed claim under its direct rule;
- express through an existing governed expression;
- keep as source wording or a local name;
- for a relation-kind candidate, stop at the exact `A.6.RCD` existing-predicate, local-compound, subject-bounded-law, or reusable-predicate-definition result; none of these stops admits a relation kind;
- continue a derived relation-kind candidate only with the required stable occurrence semantics, named receiving use, and proposed direct settlement; or
- continue an irreducible primitive relation-kind candidate only when `A.6.RCD` disposition 4 passes: every accepted derivation loses the exact action-facing distinction, and independent receiving uses and obtaining, recurrence, applicability, and occurrence-identity laws are supplied.

These are continuation alternatives, not a single admission-result vocabulary. An actual U-kind decision uses E.24.UK:4.1–4.2: exactly `root`, `same-individual-dependent`, `identity-dependent`, `reuse`, `local-kind`, or `reject`. Only the first three are positive admissions after the complete test; the remaining three are non-admission exits.

### A.11:2.1 - Archetypal Grounding - Maintenance

| Candidate claim | Parsimony result | Why |
| --- | --- | --- |
| `CoolingPump` as a new root U-kind | First recover the project claim that distinguishes role classification, function, capability, component relation, or another governed expression. If that claim identifies an admitted `U.System` in an exact local cooling-circulator role, use the C.3 classification; otherwise return the missing discriminator. Add an assignment occurrence, capability, Method, or Work only when its own predicate is current. | The useful result follows the grounded project claim; the noun alone neither selects the role reading nor creates a universal kind. |
| `Actuator` or another transformer-like noun | Recover the governed object and predicate needed by the candidate use; keep an ordinary functional or other subject claim with its direct rule. Use A.3 for a grounded acting-side claim and A.3.4 to identify any independently claimed actual change. An asserted Work needs the complete A.13 core and independent A.15.1 admission, with F.6 only for consumed precise attribution. If the facts do not select the predicate, return the missing discriminator. A new durable value still needs the parsimony finding and complete E.24.UK admission. | Neither the noun nor an identified change supplies an acting System, assignment, or Work. Those claims need their own facts. |
| Provenance-chain wording | Use A.10 for one source-to-use account and bounded reliance. Open G.6 when the use needs path identity, slicing, citation, or local refresh through already established objects and relations. Continue a new durable-value proposal only if the direct evidence or provenance patterns cannot express the needed claim without material loss; complete admission remains separately required. | Parsimony tries subject patterns before minting a kernel addition; a chain label does not itself require an addressable path. |
| `SmallPart` or similar vague size class | Reject or keep local. | The boundary depends on private scale expectations unless a direct measurement or classification pattern supplies a crisp rule. |

A retained addition also needs a reopen condition. Reopen the parsimony finding and reconsider or lower admission under its governing rule when usage collapses, overlap with an existing value is discovered, an existing governed expression becomes adequate, the boundary becomes fuzzy, or the name starts hiding that expression. This is maintenance discipline, not a fixed calendar ritual.

### A.11:4 - Bias-Annotation

A.11 corrects kind-inflation bias. A useful word, field name, record label, or diagram element can start behaving like a universal kind because it appears often, feels important, or has prestige in a source tradition. The repair is ontological: recover the governed object and try the best existing governed expression before admitting a new durable value.

It also corrects false-parsimony bias. A compact ontology is not achieved by refusing every new value. If composition hides a reviewable distinction or blocks an action-facing claim, a positive parsimony finding supports continuing the candidate's admission test and states its boundary, overlap, and reopen condition.

### A.11:3 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-A11-1` | The candidate's governed object is recovered before parsimony is judged. |
| `CC-A11-2` | If the candidate uses `U.*` force, `E.24.UK` is applied before F.5, F.8, or F.18 naming. |
| `CC-A11-3` | The best existing governed expression is attempted by value. For a relation-kind candidate this includes the exact `A.6.P` / `A.6.RCD` disposition. A representation may supply evidence. A derived relation-kind candidate requires its justified stable occurrence semantics, receiving use, and direct settlement; only a primitive candidate requires A.6.RCD disposition 4's irreducibility test. Admission remains the complete governing result. |
| `CC-A11-4` | Material loss is stated as a lost claim, lost distinction, lost boundary, or lost admissible use, not as naming discomfort. |
| `CC-A11-5` | Strong overlap lowers or rejects the candidate unless the difference changes claims. |
| `CC-A11-6` | The parsimony finding identifies the applicable section 2 continuation and, for a relation-kind candidate, the exact `A.6.RCD` result. Any actual U-kind admission cites the complete E.24.UK result rather than treating a continuation as admission. |

### A.11:5 - Common Anti-Patterns and How to Avoid Them

* **Slot label becomes kind.** A system-role designation, transformation-participant label, source-maintenance position, carrier position, or boundary slot is renamed as if the label created a new universal kind; recover the admitted System, exact local system-role kind or direct relation, any separately obtaining assignment, and Work only when each is current.
* **Publication form becomes ontology.** The appearance of a card, record, view, dashboard, figure, or report title does not establish a new durable kind or make a depicted relation obtain. Recover what the claim selects: claim-bearing content, a publication form, a carrier, or another subject. Use C.2.1/E.24.PUB when that distinction changes the claim; a form can itself be a legitimate subject, and a view-episteme remains distinct from its carrier.
* **Mathematical lens becomes object.** A graph, tuple, algebra, metric, coordinate, or threshold does not establish a new durable kind by mathematical appearance. Recover its actual object and predicate. Use C.29 only for an actual lens-use claim, identifying the represented subject, correspondence, and preservation/loss boundary. An ordinary threshold, measurement, formal declaration, or other governed claim stays with its direct subject rule.
* **Local project name becomes kernel vocabulary.** A useful project label is promoted to durable FPF vocabulary before composition and direct-pattern expression are tried.
* **Overlap is ignored.** A candidate is admitted even though an existing pattern already carries the same claim with clearer boundaries.
* **Parsimony as refusal.** A new value is rejected because "fewer kinds is better" even though existing composition loses a distinction users need to claim, compare, repair, stop, or rely on.

### A.11:6 - Consequences

| Consequence | Benefit | Cost or boundary |
| --- | --- | --- |
| Smaller durable vocabulary | FPF stays learnable and bridgeable across domains because already governed expressions do not become accidental U-kinds. | The comparison must show the best existing expression by value; retain a record or view when that answer is reused. Hand-waving about simplicity is not enough. |
| Better U-kind admissions | Complete admission requires the parsimony evidence: material loss, non-redundancy, action-facing contribution, boundary test, and reopen condition; these do not replace the other admission conditions. | Some attractive names remain local or dependent even when they are common in source traditions. |
| Clearer neighboring-pattern use | Readers know when to use E.24.UK, A.8, C.3, Part F naming, or a direct subject pattern. | The pattern supplies the parsimony finding; the governing admission test decides admission and Part F chooses the public name. |

### A.11:7 - Rationale

Ontological parsimony preserves FPF's ability to handle many domains without turning every local distinction into a root object. The pattern follows the same discipline used by `E.24.UK`: recover the governed object first, then decide whether a new durable value is needed. Using an existing governed expression is a successful result, not a failure to mint a kind.

The practical criterion is not abstract minimalism. A candidate earns a positive parsimony finding only when users gain a claim, comparison, repair, stop condition, reliance condition, or boundary they cannot recover by composition without material loss. Admission still requires its complete governing test. That keeps parsimony tied to FPF's work-facing purpose rather than to a taste for small vocabularies.

### A.11:8 - SoTA-Echoing

Current ontology-engineering practice favors modularity, reuse, explicit competency questions, and controlled admission of new terms over unchecked class growth. A.11 adapts that practice to FPF: the admission question is not merely "can a class be defined?" but whether the candidate changes admissible claims, boundaries, or work-facing use inside the FPF pattern system.

Constructional-ontology and BORO-like source lines add a second discipline: identity, construction, dependency, and part-whole distinctions must be recovered before a convenient term becomes a kind. FPF keeps that source discipline without importing a classical top-level taxonomy as-is; U-kinds remain tied to accepted ontics, slot discipline, and action-facing pattern use.

### A.11:9 - Relations

- **Builds on:** `E.24.UK`, `A.6.P`, `A.6.RCD`, `A.8`, `C.3`, `F.8`, `F.18`, and direct subject patterns.
- **Coordinates with:** `E.24.CD` for candidate detection and `E.24.PUB` when a publication form or structural name created the admission claim.
- **Does not replace:** universal-core testing in `A.8`, typed claim quantification in `C.3`, or naming discipline in Part F.

### A.11:End
