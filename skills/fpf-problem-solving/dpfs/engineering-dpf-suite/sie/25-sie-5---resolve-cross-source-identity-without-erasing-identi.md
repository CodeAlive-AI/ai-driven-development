## SIE.5 - Resolve Cross-Source Identity without Erasing Identifier Authority

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `CrossSourceIdentityDisposition@Use` that states, for each load-bearing endpoint pair or set, the required entity grain and interval, identity-related disposition, the source entries, the rules and contexts or assignments and issuers that resolve them, evidence, authority boundary, unresolved cases, and the exact mappings, claim compositions, interfaces, and tests that may consume it.

### SIE.5:1 - Problem Frame

**Use this when** an integration needs to decide whether records or identifiers from different sources concern the same entity, a part, a version, a variant, an alternate description, a family, or different or unresolved entities. The recognizable failure is a join, merged key, or `sameAs` assertion that makes identifiers appear unified while erasing their issuers, grains, intervals, and authority.

For one bounded cross-source identity question, state the entity grain and time or effectivity interval at which sameness matters for the named use. The first result is a disposition that downstream work can inspect and challenge without replacing source identifiers or master-data authority.

The payoff is that the integration can join only warranted cases, identify which branches remain unresolved, and preserve source trace. Do not use SIE.5 to create identifiers, choose enterprise master identity or survivorship, decide authoritative values, or prove a source claim true. Those decisions remain with identifier owners, MDM, or the direct domain authority.

### SIE.5:2 - Problem

The same real-world item can carry manufacturer, supplier, enterprise, lot, serial, package, event, and temporary process identifiers. Conversely, the same character string can be reused by different issuers or at different times. Version, configuration, part-whole, and alternate-description relations can be mistaken for identity because they support some joins.

If an integration collapses those distinctions, the merged record no longer shows which source made each claim, the identifier it used, or the time and issuer rules that qualify that use. Contradictory events appear to concern one thing without evidence, and a master key silently becomes a domain decision.

### SIE.5:3 - Forces

| Force | Tension |
| --- | --- |
| Joinability | A common key makes computation easy, while premature merging can create false identity and irreversible provenance loss. |
| Grain | Receivers want one “item”, while wafer, die, device, package, lot, feature, version, and event answer different questions. |
| Time and effectivity | Identity may be stable across one interval, while reuse, replacement, split, merge, and revision change the warranted claim. |
| Authority | Identifier issuers and master-data stewards govern different schemes and decisions; crosswalk custody transfers neither authority. |
| Incomplete evidence | A bounded decision is needed, while some pairs must remain unresolved without blocking independent rows. |
| Reuse | A disposition can help several mappings, while its grain, interval, and use boundary prevent blanket equivalence. |

### SIE.5:4 - Solution

Frame identity as a source-qualified, grain- and interval-specific disposition for one receiving use. Preserve every source identifier and the applicable context or assignment, including its issuer when it was issued. Compare the entity criteria, relation evidence, version/effectivity, and authoritative decisions that matter. Return same, different, part, version, variant, alternate-description, family, or unresolved only at the precision supported; do not force every useful relation into identity.

#### SIE.5:4.1 - Pattern-Use Unfolding

1. **Name the receiving identity question.** State which mapping, claim composition, query, or decision needs an identity premise and what a wrong merge or split would change.
2. **Fix entity grain and interval.** Name the relevant individual or occurrence kind, part-whole level, version/configuration, lifecycle state, jurisdiction or organization, and time/effectivity interval.
3. **Resolve each source entry.** Use SIE.2 to establish what each entry can designate. Recover its assignment and issuing authority when it was issued, or the rule and context used to interpret it. Retain the applicable syntax, restrictions, source edition and provenance. If the evidence leaves several candidates or fails to identify one, record that outcome.
4. **Separate candidate relation kinds.** Consider same individual at the stated grain, different individuals, part/whole, earlier/later version or specialization, variant, alternate description, an individual satisfying a type criterion, or membership in a declared product family. When several readings still fit, check which trace or decision differs between them. Return an answer common to every admissible reading at the requested grain. Preserve any finer relation still in doubt.
5. **Collect discriminating evidence.** Use issuer records, source assertions, configuration/effectivity, provenance, physical or domain characteristics, event histories, and counterexamples. A shared string or co-occurrence is only candidate evidence.
6. **Recover authority.** Identify who may bind a source identifier, govern the master identity, decide authoritative values or establish the domain relation. SIE records the disposition for its stated use under those authorities.
7. **Assign the narrowest warranted disposition.** State conditions, confidence or uncertainty where meaningful, rejected alternatives, and unresolved evidence. Preserve source IDs even for accepted same-entity rows.
8. **Link consumers to the identity disposition.** Reference the disposition from every mapping, claim composition, interface row, and identity test that relies on it. Never copy only the merged key.
9. **Test difficult cases and reopen.** Select the alternatives that could change this use, such as identifier reuse, another part or assembly, or a split in the event history. When different admissible identities still entail the same required conclusion, return that conclusion and the limit on exact attribution. State the source or observation change that reopens the row.

#### SIE.5:4.2 - Record the Result

| Identity position | Required content |
| --- | --- |
| identity question and use | receiver, dependent action, wrong-merge/wrong-split consequence |
| entity boundary | kind and grain, part-whole level, version/configuration, interval/effectivity, relevant context |
| source identifiers | each source entry, the supported referent, remaining candidates or unresolved designation, the relevant rules and context or the assignment and its issuer, restrictions, edition and provenance |
| candidate relations | same, different, part, version/specialization, variant, alternate description, family, unresolved alternatives |
| warrant | evidence, counterevidence, counterexamples, uncertainty/confidence, rejected alternatives |
| authority | scheme-local, master-data, domain, and receiving-decision scopes |
| disposition | narrowest warranted relation or unresolved result, conditions, source-ID preservation rule |
| downstream and reopen | mapping/composition/interface/test references and the change or observation that reopens the disposition |

#### SIE.5:4.3 - What Changes in Practice

The integration stops minting a common key as proof of identity. Every load-bearing join points to a disposition with grain, interval, source identifiers, evidence, and authority. Unresolved identity becomes an explicit interface and validation branch instead of a row silently dropped or merged.

### SIE.5:5 - Archetypal Grounding - Semiconductor Recall Trace

A recall-triage query crosses a wafer identifier from a fabrication source, die coordinates, device serials, package identifiers, supplier lot identifiers, GS1 event identifiers, and an enterprise material master. The receiving question is whether a shipped device can be traced to an affected fabrication lot.

| Endpoint question | Constructed disposition |
| --- | --- |
| wafer `W-204` and supplier lot `L-88` | not identity; the supplier record asserts that the wafer is a member/output associated with the lot under a bounded process interval. Preserve both identifiers and relation provenance. |
| die coordinate `(x17,y9)` on wafer `W-204` and device serial `D-771` | Suppose the packaging record shows that this die was incorporated in the serialized device. Trace the die as a constituent of that device for the recorded interval. A serial assigned to the singulated die itself can instead identify the same die as the wafer coordinate when the designation rule or identifiable context establishes that referent. In either case retain both source identifiers, their applicable intervals and the assignment, issuer or context that establishes each designation. |
| device serial `D-771` and package code `P-55` | unresolved because the package identifier is reused after rework and the event history lacks effectivity. Keep the exact package history open. Test whether this uncertainty changes the lot-level answer. |
| enterprise material master `M-12` and device serial `D-771` | The master record describes a product class and carries the enterprise attributes it governs. To classify the particular device, establish that it meets the class criterion. Membership in a catalogue family would require the catalogue's own grouping rule. The master and the device each retain their identity. |
| GS1 event `E-901` and device `D-771` | event and object are different entities; the event may concern the device. Never merge their identifiers. |

Tests cover reused package identifiers, a die split/merge error, contradictory supplier events, a missing cross-enterprise link, and a later correction. If the records admit at least one package history and every such history traces the shipped device to the affected lot, the interface can return that lot finding while keeping the `P-55` history unresolved. If every admissible history excludes the affected lot, return that negative finding. If some lead to the affected lot and others exclude it, obtain the distinguishing rework or effectivity evidence or report the attribution still open. MDM or the domain steward may later decide a master identity; SIE.5 has not done so.

### SIE.5:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | The integration registry becomes the de facto master-data authority. | State the bounded disposition and retain MDM/domain decision ownership. |
| Architecture | One canonical key is required because the platform prefers it. | Carry a surrogate technical key only with source IDs and the identity disposition it indexes. |
| Ontology/Epistemology | Same individual, part, version, variant, alternate, and family relations collapse. | Fix grain and interval, then choose the narrowest warranted relation. |
| Pragmatics | Every identifier pair receives a costly adjudication. | Decide only pairs that are load-bearing for the receiving use; leave independent rows untouched. |
| Didactics | “Same” is read as timeless universal identity. | Display conditions, interval/effectivity, scheme, and forbidden reuse beside the disposition. |

### SIE.5:7 - Conformance Checklist

- [ ] The receiving action and wrong-merge/wrong-split consequence are named.
- [ ] Entity kind, grain, part-whole level, version/configuration, and interval/effectivity are explicit.
- [ ] Each entry can be traced to its source and edition. The rule and context or the assignment and its issuer, the restrictions and the available evidence support the stated result, including an unresolved result.
- [ ] Useful non-identity relations are not compressed into a boolean same/different field.
- [ ] Shared strings, co-occurrence, and crosswalk membership are treated only as candidate evidence.
- [ ] Evidence, counterevidence, counterexamples, and uncertainty are inspectable.
- [ ] Scheme-local, master-data, domain, and receiving-decision authority scopes remain separate.
- [ ] Accepted same-entity rows do not delete source identifiers.
- [ ] Every dependent mapping, composition, interface, and test references the disposition.
- [ ] Reuse, split/merge, version/configuration, part-whole, contradiction, and absent-link cases are tested where applicable.

### SIE.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Same string, same entity | Resolve each entry under its own assignment or contextual rule, then compare the entities at the required grain and interval using evidence for the claimed relation. |
| Universal `sameAs` | Use the narrowest relation and record unresolved or different cases. |
| Master key by integration fiat | Return master-identity and survivorship decisions to their authority. |
| Version equals object | State whether the use concerns one continuing entity, a version-specific configuration, or a relation among them. |
| Part joined as whole | Fix the entity grain and preserve part-whole relations explicitly. |
| Drop unresolved rows | Expose them as interface and validation branches with dependent actions. |

### SIE.5:9 - Consequences

The package can join warranted identities without losing source trace and can stop only the branches that depend on unresolved identity. Corrective source or steward decisions can be replayed against explicit consumers. The method also reveals when the useful relation is part, version, membership, or event participation rather than identity.

The cost is domain evidence and authority work. Some convenient global keys remain technical indexes rather than semantic truths, and some desired traces return incomplete.

### SIE.5:10 - Rationale

A formation rule determines whether an identifier is well formed. For each entry, recover what its source establishes under the applicable rule, context or assignment. Then ask what the evidence establishes about the relation at the required grain and interval. A record of reassignment can link two entries to the same entity before its serial number is known. Where the evidence permits several identities, preserve those alternatives. Retaining the source entries allows the engineer to reconsider the result as new evidence appears. Master-data and domain decisions remain with their responsible authorities.

### SIE.5:11 - SoTA-Echoing

The best-known line combines explicit identifier ownership and restrictions, provenance-qualified alternate/specialization relations, and domain traceability practice. The serious default is entity resolution that optimizes a match score or golden record. The problem arises when the score or merged record obscures grain, issuer, interval or decision authority. SIE.5 uses these contributions to return a bounded disposition for the work that relies on identity.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| Current FPF identity and relation law | adopt | Keeps identity and direct relations as explicit claims; generic law does not decide a domain pair. |
| [ISO 8000-115:2024](https://www.iso.org/standard/88847.html?browse=tc) | adapt | Contributes identifier owner, use restriction, semantics, and resolution inputs; excludes identifier creation, query/response syntax, and resolution method and does not decide equivalence. |
| [PROV-O](https://www.w3.org/TR/prov-o/) | adapt | Supplies specialization, alternates, derivation, attribution, revision, and invalidation relations useful to evidence; provenance relations are not blanket identity. |
| [SEMI traceability standards](https://www.semi.org/en/products-services/standards/traceability) and [GS1 EPCIS 2.0.1](https://ref.gs1.org/standards/epcis/2.0.1/) | adapt | Supply semiconductor and event-based identity/traceability probes; scheme use does not create enterprise master identity or authorize recall. |
| golden-record or score-only merging | reject as sufficient | It may support candidate generation or a steward decision. Preserve source identifiers, relation kinds and authority. |

Reopen the affected dispositions when an issuer reassigns one code, or when a change to a formation or resolution rule alters which entries a query can accept or resolve. New event or configuration evidence, a changed grain or interval, and repeated failures to express an action-changing relation can also reopen the result.

### SIE.5:12 - Relations

- `SIE.1` supplies the receiving action, identity-sensitive answer claims, loss boundary, tests, and stop.
- `SIE.2` supplies the source entries with the contexts for their rules or the issuers of their assignments, restrictions, source claims, editions, provenance and authority gaps.
- `SIE.4` may expose an identity question but does not answer it merely by accepting a semantic correspondence.
- `SIE.6` consumes identity dispositions when composing claims about the same bounded entity; it preserves contradictory claims separately.
- `SIE.7` and `SIE.9` reference dispositions rather than copying only merged keys.
- `SIE.10` tests every load-bearing identity premise. MDM and domain authorities retain master identity, authoritative values, and action.

### SIE.5:End
