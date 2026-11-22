## SIE.1 - Bound the Receiving Use and Semantic Contract

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `SemanticIntegrationUseContract@Use` that names the receiving use and its recipients, required answer claims, source cut, tolerated loss and uncertainty, currentness, latency, quality, authority, grounds for acceptance and any required tests, stop conditions, and reopen conditions.

### SIE.1:1 - Problem Frame

**Use this when** a request says “integrate the data”, “align the models”, “build the knowledge graph”, or “make one source of truth”, but the intended receiver and decision-changing answer are not yet explicit. Recover which results or means the requester has already prescribed and which design choices remain open. The recognizable failure is an integration whose values cannot be interpreted, trusted, or used safely by the Work that requested it.

The subject is one semantic-integration use: a specified query, decision, operation or engineering workflow and the recipients who use its answer under stated conditions. The first move is to state that use and the answer claims it needs. The first result is a bounded contract that lets later workers decide which semantic loss, source age, unresolved row, and test outcome are acceptable.

The practical gain is a testable stopping rule before source, ontology, mapping, or platform choices accumulate. Do not use this pattern to authorize the receiving decision, decide product configuration, choose master identity, operate a data pipeline, or define generic evidence law. Obtain those results from their owners. Do not reopen a current contract merely because another source exists; reopen it when the receiver, use, answer, conditions, authority, or acceptance boundary changes.

### SIE.1:2 - Problem

Without a receiving-use contract, “semantic integration” expands toward every source and every possible reuse. Similar labels are merged without a loss budget, freshness is treated as an implementation detail, and a passing schema or sample query is reported as success. The project cannot distinguish an informative unmatched row from a defect, or a harmless delay from a stale answer that changes action.

Technology then supplies the hidden contract. A graph platform encourages graph-shaped outputs, a warehouse encourages copying, and an API encourages whichever fields are easiest to expose. None says which answer claims the receiver may rely on, who owns them, or when the correct result is to stop.

### SIE.1:3 - Forces

| Force | Tension |
| --- | --- |
| Breadth | More sources may enable future reuse, while every added source creates meanings, authority, currentness, and validation obligations. |
| Speed | A quick join can demonstrate access, while early conflation makes later correction expensive and hard to trace. |
| Loss | A useful common view often coarsens detail, while silent loss can reverse a decision or erase incompatibility. |
| Freshness and latency | Query-time access can be current but slow or fragile; copied data can be fast but stale and harder to govern. |
| Authority | Source owners, integrators, and receivers contribute different decisions; having access to or custody of a source gives no additional decision rights by itself. |
| Assurance | The receiver needs grounds that cover the promised use. Observing a few successful queries can leave an allowed branch unexamined. |
| Reuse | A broad contract appears reusable, while a small contract is easier to validate and reopen. |

### SIE.1:4 - Solution

Construct a semantic contract that covers the commissioned receiving work, including the limits of an acceptable partial answer. Begin from the receiver and work backward to required answer claims, source contexts, meanings, losses, currentness, quality, authority, grounds for acceptance, and conditions for stopping. Treat the contract as an input to later SIE patterns, not as proof that any source, correspondence, identity, mapping, interface, or implementation exists.

#### SIE.1:4.1 - Pattern-Use Unfolding

1. **Name the receiver and receiving Work.** Identify the System or role that will use the result, the query, decision, operation, or workflow, the horizon, and the answer due and any separately useful intermediate result. For separate receiving decisions, establish what each recipient may see and accept by its deadline. For one joint result, identify whose contributions count under which rule and whether participants must exchange them or agree. One result can serve both uses if it meets both sets of conditions.
2. **State the answer claims.** Write the fields or propositions the receiver needs, including scope, grain, interval or effectivity, and the action each claim can change. Keep a value, its provenance, its authority, and the receiver's decision distinct.
3. **Select the source cut.** Name only the governed contexts and candidate source assets that can change the answer. Mark sources whose inclusion is uncertain rather than adding them silently.
4. **Choose which distinctions to preserve.** Hold the local value fixed and vary the object or work in which it occurs. Then hold the whole result fixed and vary its parts, timing or allocation. Which change would alter a recipient's permitted action or the grounds requested for it? Use those differences to select the entity kinds, part relations, model constraints and source claims needed at each scale. Accept a coarsening under the agreed criterion when the required conclusion or choice is still warranted throughout its scope.
5. **State currentness, latency, availability, and quality conditions.** Specify thresholds or unresolved returns where they change use. A deadline for one query, a time bound for every admitted request and a percentile over a specified workload call for different evidence.
6. **Recover authority, permission, and protection boundaries.** Name who defines source meanings, who may grant access, who decides identities or authoritative values, who accepts semantic loss, and who owns the receiving action. Identify any missing authority or permission that blocks the use.
7. **Choose evidence for the claimed use.** Identify what would discriminate an acceptable answer from a consequential error. A definition, complete plan, proven bound or previous observation can settle a requirement when it covers the subject and conditions. Design tests for behaviour that still needs observation and for any trials specifically ordered. For each selected challenge state the expected branch.
8. **State pass, narrow, unresolved, and stop outcomes.** Where the receiver accepts a bounded subset or a finding of incompatibility, state what can be delivered on those terms. Identify which required answer an unavailable meaning, edition, authority, permission or acceptance rule prevents. Return a common conclusion if it is warranted under all remaining possibilities. Keep an unresolved required answer visible when delivering a permitted subset.
9. **State reopen conditions and next result.** Identify observations that change the contract and the smallest next result, often `SourceSemanticInventory@Use` from `SIE.2`.

#### SIE.1:4.2 - Record the Result

| Contract position | Required content |
| --- | --- |
| receiver and use | named recipients, query or operation, horizon, work each must complete, and any partial result they can use |
| answer claims | propositions or fields, grain, scope, interval/effectivity, and action changed |
| source cut | governed contexts, candidate assets, inclusion reason, and known access limits |
| semantic boundary | distinctions to preserve, permitted loss, uncertainty treatment, unmatched/incompatible behavior |
| service conditions | currentness, latency, availability, recovery, and quality thresholds that change use |
| authority and protection | meaning owner, identifier or value authority, access/permission, receiver authority, and protected conditions |
| validation | evidence or tests that distinguish the required outcomes, including any required new performance |
| disposition | pass, narrow, unresolved, or stop rules; next result and observable reopen conditions |

#### SIE.1:4.3 - What Changes in Practice

The team stops treating integration scope as the set of reachable sources. Every later correspondence, identity disposition, mapping rule, realization, interface field, and validation claim must answer to a named receiving use and loss boundary. When the receiving contract allows it, an explicit unmatched or incompatible result answers the question.

### SIE.1:5 - Archetypal Grounding - AP242/QIF Configuration Query

A quality engineer asks which QIF inspection plan and result concern feature `F` in released AP242 product-definition revision/configuration `R` at effectivity `E`. The initial request is “connect PLM and quality data in a knowledge graph.” In this case the engineer confirms that the graph is a suggested means and asks for the review answer. If a graph is itself an agreed deliverable, the contract retains it alongside any required evidence return. The resulting review contract is given below.

| Position | Constructed value |
| --- | --- |
| receiver/use | quality engineer preparing an evidence return for one configuration-bound review; query by revision/configuration, feature, and effectivity |
| answer claims | AP242 feature identifier and configuration/effectivity claim; QIF plan, characteristic, and result identifiers; relation disposition; source edition; timestamp; provenance; unmatched/incompatible status |
| preserved distinctions | product feature versus inspection characteristic; definition versus performed result; revision versus configuration; applicability/effectivity; source identifier and issuer; plan versus result |
| tolerated loss | display may coarsen source-local labels after exact identifiers and relations remain available; no unmatched feature or incompatible characteristic may become a positive relation. For this constructed evidence-return review, the receiver permits the qualified row set with unresolved local-extension and unknown-unit branches shown separately |
| currentness and latency | for this constructed review at time T, the receiver requires the released AP242 configuration applicable to the review, QIF observations from T minus 24 hours through T, and a response to this review query within two seconds. |
| authority | Systems Engineering owns release, configuration, and effectivity; the quality authority owns acceptance; source owners define their models; SIE may qualify mappings but authorizes neither decision |
| tests | known match; unmatched feature; changed revision; incompatible characteristic; stale QIF result; missing provenance; source timeout |
| stop/reopen | withhold each dependent result when the remaining configuration, effectivity, edition, identity, permission or acceptance uncertainty changes its use. Reopen when a relied-on AP242/QIF edition, review use or protected condition changes. |

This result does not claim that the two source models correspond or that an interface works. It makes those later claims testable. AP242 edition 4 is recorded by `SIE.2` with its current source status; SIE.1 only requires the edition and reopen rule to be explicit.

### SIE.1:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | The integration team silently accepts loss or acts as source/value authority. | Name each decision subject and the direct authority relation; make absence a blocker. |
| Architecture | Platform boundaries define the semantic use. | Begin from the receiving result and keep realization alternatives open. |
| Ontology/Epistemology | A shared label or data field is treated as a shared meaning or true claim. | State answer claims, source contexts, preserved distinctions, and uncertainty separately. |
| Pragmatics | The contract becomes a complete requirements catalogue rather than a decision tool. | Keep only conditions that can change the receiving action or stop. |
| Didactics | Readers infer that SIE.1 must precede every other pattern. | Enter directly elsewhere when an equivalent current contract exists; verify compatibility instead of repeating it. |

### SIE.1:7 - Conformance Checklist

- [ ] The receiving Work and the recipient or recipients whose decisions it serves are explicit.
- [ ] The required answer and any useful intermediate result are expressed at the subject, grain, scope and interval the receiver needs.
- [ ] The source cut is justified by the use rather than by reachability.
- [ ] Preserved distinctions, permitted loss, uncertainty, and unmatched/incompatible behavior are explicit.
- [ ] Currentness, latency, availability, recovery, and quality are included only where action-changing.
- [ ] Meaning, identity/value, access, semantic-loss, and receiving-action authorities remain distinct.
- [ ] The proposed evidence covers the claimed distinction. Selected tests have expected outcomes, and any separately commissioned trial is specified.
- [ ] Pass, narrow, unresolved, stop, next-result, and reopen rules are stated.
- [ ] The contract claims no correspondence, implementation, validation, authorization, or outcome that has not been obtained.

### SIE.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Integrate all enterprise data.” | Name the receiving decision, those who use its result, and the smallest source cut that can change it. |
| “The knowledge graph is the deliverable.” | State the receiving answer and treat graph materialization as one later realization option. |
| “No information loss.” | Name the distinctions and tests; unlimited preservation is not an operational contract. |
| “Real time.” | State a measurable currentness and latency condition for the use. |
| “Single source of truth.” | Name source, identity, and value authorities and the claims each may establish. |
| “Every test must return a row.” | Define legitimate unmatched, incompatible, unavailable, and stop branches. |

### SIE.1:9 - Consequences

The contract limits source fan-out, makes semantic loss and authority visible, and gives implementation and validation a shared target. It can stop an integration before expensive model or platform work. It also makes conflicts and narrow usable subsets publishable outcomes.

The cost is early negotiation about the receiver, evidence, loss, and stop conditions. Some attractive future reuse remains outside the first package and must earn its own contract or compatible extension.

### SIE.1:10 - Rationale

Semantic adequacy is relative to a use. The receiving action, answer claim, source context, permitted loss and authority determine what evidence will establish a successful integration. Beginning there prevents a carrier choice from becoming an implicit ontology, authority model, and acceptance rule.

### SIE.1:11 - SoTA-Echoing

The best-known line for this question combines use-bounded representation selection, situational Method criteria, quality-for-use, and explicit source/provenance practice. The serious default alternative is technology- or source-led integration. The difficulty arises when the choice of graph, warehouse or federation defines the answer and loss boundary. SIE.1 applies these contributions by making the whole semantic contract, including authorities and legitimate unresolved branches, the first domain result.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| Current FPF `C.37` | adopt | Bounds representation selection and co-use to a named use; does not supply the SIE package or application authority. |
| Current `C.39.RQ` | adapt | Situational criteria help state receiving Work and fit conditions; SIE adds semantic endpoints, loss, source, authority, and layered tests. |
| [DQV](https://www.w3.org/TR/vocab-dqv/) and [ISO/IEC 25012:2008](https://www.iso.org/standard/35736.html) | adapt | Supply quality dimensions and vocabulary; the contract selects only dimensions that change this use. |
| [Data on the Web Best Practices](https://www.w3.org/TR/dwbp/) | adapt | Contributes provenance, version, access, and reuse questions; no Web publication form is mandatory. |
| platform-first “single source of truth” | reject as default | A carrier and custody arrangement cannot establish cross-source meaning, authority, or receiving-use adequacy. |

Reopen this pattern when representative uses cannot express action-changing loss, authority, or validation obligations through the contract positions, or when a source line supplies a materially better first result.

### SIE.1:12 - Relations

- `SIE.2` consumes the source cut, answer claims, distinctions, and currentness questions to produce `SourceSemanticInventory@Use`.
- `SIE.4`–`SIE.10` consume the compatible contract positions relevant to their results; none may silently widen the receiver or accepted loss.
- `C.37` governs generic use-bounded representation selection. `A.10` and `A.10.1` govern evidence/provenance and generic affected-use questions.
- Applications, Systems Engineering, Operations, quality, safety, legal, and other direct owners supply their acceptance and authority results.
- A changed contract reopens the package branches that rely on the changed premise. `SIE.11` supplies affected-use discovery and integration revalidation where the affected results still need to be established.

### SIE.1:End
