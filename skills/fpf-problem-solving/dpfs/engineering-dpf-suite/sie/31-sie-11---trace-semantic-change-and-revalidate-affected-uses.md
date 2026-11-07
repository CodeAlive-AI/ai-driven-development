## SIE.11 - Trace Semantic Change and Revalidate Affected Uses

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** qualified results for the semantic-integration uses affected by a changed premise; an `AffectedSemanticUseRevalidationAccount@Change` assembles them when a receiving use needs a common account.

### SIE.11:1 - Problem Frame

**Use this when** a relied-on source definition, model commitment, identifier meaning, mapping premise, or interface interpretation changes and the integration's continued use needs a decision. A familiar warning sign is an unchanged API field that now answers a different question.

Start by comparing the earlier and later meaning at the receiving question. A compatible documentation move can finish with a reference repair. A changed meaning can require repair or renewed validation of the integration results that relied on it.

The object is the affected semantic reliance and its consequences for receiving uses. The gain is a justified continuation, repair, narrowed use, or scoped unresolved result. To assert that all uses remain unaffected, establish adequate coverage of the relevant uses and their reliance.

Use the applicable domain Method directly for a known operational change that does not alter a relied-on source or semantic premise. If one already identified use is the whole question, resolve it with the relevant domain Method and retain the source, currentness and result-specific grounds that the use needs. Use A.10 when the source-to-use account is still implicit or needs to be made replayable. A.10.1 is needed when affected uses must be discovered across a scope.

### SIE.11:2 - Problem

A source update can be treated as harmless because the schema still parses, or as universally disruptive because its version changed. Either response misses the actual reliance. Some consumers use a definition that changed; others use a different proposition from the same source; still others are merely mentioned in nearby records.

Indiscriminate revalidation consumes work without settling those differences. An incomplete search can create the opposite error: one repaired mapping is reported as proof that the entire integration remains valid.

### SIE.11:3 - Forces

| Force | Tension |
| --- | --- |
| Selectivity | Only affected reliance needs reopening, while hidden consumers can remain dependent on changed meaning. |
| Continuity | Matching earlier results save work, while changed assumptions can invalidate them. |
| Coverage | A local answer can finish promptly, while a wider no-impact claim needs wider support. |
| Authority | An integrator can repair its mappings and interfaces, while source and receiving decisions retain their owners. |
| Evidence effort | Additional inquiry can change a decision, while unavailable or low-value information can consume the work needed for repair. |

### SIE.11:4 - Solution

Follow the changed proposition through actual semantic dependencies to the results and receiving uses it can alter. Complete supported branches at their proper scope. Assemble a wider account only for a receiver that needs it.

#### SIE.11:4.1 - Pattern-Use Unfolding

1. **Compare the relied-on meaning.** Identify what the receiving question depended on in the earlier source or premise and what the later content says. Include changed applicability, subject grain, interval, assumptions, or limits where relevant. An inaccessible later definition leaves that comparison unresolved.
2. **Finish a compatible repair when sufficient.** If content, applicability, and access remain compatible for the use, make the needed reference repair and retain matching results. A version or URL change alone does not require every downstream Method to run again.
3. **Find affected uses when their scope is unsettled.** Apply A.10.1 to discover actual reliance within the question's scope, using source-side and receiver-side evidence or an index that adequately covers both. Distinguish a material dependency from a mention. Retain coverage gaps that limit the intended conclusion.
4. **Select the integration result that the change can alter.** Use the domain returns below. Follow a further consumer only when the changed result can alter its action or claim. The physical proximity of files is not a dependency rule.
5. **Repair or revalidate that result.** Apply its defining Method to the changed premise. Reuse earlier evidence whose actual conditions still match. Return a supported continuation, repair, permitted narrower use, or scoped gap. Source truth, master identity, product release, and application decisions go to the owners of those decisions.
6. **Return the completed branch.** Give the receiver the result it needs, with the changed premise and remaining limits where those affect reliance. A completed direct result is sufficient for its own receiving question.
7. **Combine results when a receiver needs the wider answer.** State the covered uses, their relevant results, unresolved uses or discovery gaps, and the continuation that those results support. A broader no-impact conclusion requires the corresponding coverage; completed local branches cannot supply unexamined ones.

When additional evidence is being considered, apply `C.11.DUA` to compare its attainable contribution to the receiving decision with its cost, delay, downside, and displaced work. A gap can remain a qualified gap when further inquiry cannot support a worthwhile next action; that limitation does not warrant a stronger claim.

#### SIE.11:4.2 - Domain Returns

| Changed reliance | Integration result to revisit |
| --- | --- |
| A concept, relation, or model constraint | SIE.3 model adequacy and any affected SIE.4 correspondence. |
| Identifier meaning, scheme, grain, or interval | SIE.5 identity disposition and the results that actually use it. |
| Source-claim scope or interpretation | SIE.6 composition, conflict, or non-comparability result. |
| A transformation premise | SIE.7 mapping and its affected outputs. |
| Availability, permissions, freshness, or service conditions | SIE.8 realization choice or SIE.9 receiving interface, according to the changed condition. |
| Receiving meaning or acceptance condition | SIE.9 interface contract and the corresponding SIE.10 validation. |

This table locates the defining result; the actual dependency determines which returns are needed and their useful order.

#### SIE.11:4.3 - Record the Result

For a direct repair, use the result already needed by its consumer. For a common account, retain the following content at the scope the receiver needs:

| Account position | Receiving content |
| --- | --- |
| Change and reliance | Earlier relied-on meaning, later meaning, and the affected question. |
| Covered uses | Actual dependencies and the basis for the stated discovery scope. |
| Direct results | Completed repairs, revalidation, permitted continuation, or narrowed uses under their defining Methods. |
| Unresolved reach | Unexamined or inaccessible reliance, discovery gaps, and their effect on the conclusion. |
| Continued use | What the receiver can now rely on and which changed conditions would reopen it. |

The account summarizes its constituent results.

#### SIE.11:4.4 - What Changes in Practice

The maintainer can say which interface meaning changed, which mapping or identity result was revisited, and what can continue. A corrected local reference can finish immediately. A broader claim remains bounded by the uses actually discovered and assessed.

### SIE.11:5 - Archetypal Grounding

#### SIE.11:5.1 - Compatible Reference Repair

A publisher moves a vocabulary definition to a new documentation address. The integrator can access both the relied-on content and its new location. The definition, applicability, and access needed by the mapping remain compatible.

The integrator updates the reference used by that mapping. Its existing qualification still answers the unchanged question. This is the completed result for the reference-maintenance use; no multi-use account is needed.

If the later definition cannot be inspected, the same evidence cannot support this conclusion. The result then names the inaccessible comparison and the reliance it leaves unresolved.

#### SIE.11:5.2 - Changed Promise Horizon

A provider changes `availableToPromise` from the reservation meaning used for present availability to a promise for a future horizon. The API field and its numeric type stay the same. The semantic-integration maintainer compares the two meanings and inspects the actual consumers.

| Use | Reliance and result |
| --- | --- |
| Present-availability endpoint | Its mapping treated the quantity as answering “available now”. That premise changed. Repair the mapping and interface meaning, or withhold that answer until a qualified present-time source is supplied. SIE.10 checks the supported receiving result. |
| Future planning view | It can potentially use the new quantity when it exposes the horizon and the receiving question agrees. Validate those conditions instead of assuming that every use must stop. |
| Descriptive product catalogue | Its definitions and product descriptions do not consume the changed quantity. Where that independence is established, retain its matching result. |
| A consumer with unavailable interpretation | The maintainer cannot determine how it uses the quantity. Return that scoped uncertainty; the other completed branches retain their own results. |

If the service owner needs an integration-wide continuation decision, the account combines those results and the remaining uncertainty. It does not state that all uses are unaffected. The provider controls its source definition; the integrator controls the supplied semantic interface; each application owner determines whether the qualified answer is adequate for its decision.

### SIE.11:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | The integration maintainer appears to authorize the application's decision. | Return the qualified integration result to the receiving decision owner. |
| Architecture | Every linked component is treated as an affected consumer. | Follow the changed proposition through dependencies that can alter results. |
| Ontology/Epistemology | An unchanged field name is read as unchanged meaning. | Compare the actual definition, applicability, and receiving interpretation. |
| Pragmatics | All validation restarts after every source version change. | Retain matching results and finish sufficient direct repairs. |
| Didactics | A list of completed checks looks like complete coverage. | State which uses the evidence covers and preserve unresolved reach. |

### SIE.11:7 - Conformance Checklist

- [ ] The compared change concerns a premise used by an identified receiving question.
- [ ] Compatible reference repair can complete without a wider account.
- [ ] Discovery, where needed, supports the stated scope and distinguishes dependencies from mentions.
- [ ] Each affected integration result uses its defining Method.
- [ ] Reused evidence still matches its actual conditions.
- [ ] Independently supported branches finish at their own scope.
- [ ] A common account has a receiving use and preserves unresolved coverage.
- [ ] A wider no-impact claim has support for the uses it covers.

### SIE.11:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Schema compatibility as semantic compatibility | Compare the question answered by the field, including its horizon and applicability. |
| Every reference occurrence requires revalidation | Establish whether the result relies on the changed proposition. |
| One repaired branch clears the whole integration | Bound the conclusion by discovered and assessed uses. |

### SIE.11:9 - Consequences

Supported uses can continue while affected branches receive focused repair. Dependency evidence becomes useful because it points to a changed receiving result. Local completion no longer waits for an unnecessary integration-wide account.

Finding hidden reliance and interpreting source changes can require domain and receiver participation. A wider assurance claim may remain unavailable while an actual consumer or later definition is inaccessible. The result preserves that limitation without erasing completed branches.

### SIE.11:10 - Architectural Rationale

The changed proposition, rather than the changed carrier, determines semantic impact. Direct domain Methods decide the affected result; discovery determines where those questions arise. Keeping those contributions distinct permits reuse, independent completion, and limits on wider conclusions.

### SIE.11:11 - SoTA-Echoing

The practice question is which receiving uses must change when one semantic premise has changed and the affected scope is still unsettled. In §5.2, both the present-availability endpoint and other consumers exist; knowing the changed field alone does not settle their reliance. The selected line combines A.10/A.10.1's premise comparison and scoped discovery with the integration-specific returns in §4.2.

The serious alternative is a bounded full regression: identify the same receiving scope, update the tests to the new source meaning, and revalidate every registered use in it. This can be preferable when the suite is small and inexpensive or a reliable dependency analysis would cost more. It is not merely rerunning old tests against an unchanged schema.

| Answer to the same multi-use horizon change | Work and evidence at the same scope | Selection and accepted trade-off |
| --- | --- | --- |
| Discover changed reliance and revalidate affected results | Compare the two meanings, inspect source-side and receiver-side dependencies, qualify coverage, and retest results that rely on the changed horizon. Keep applicable evidence for the independent catalogue. | **Adopt** A.10/A.10.1 in §4.1.1–3/5–7; **adapt** §4.2 and §5.2 to semantic model, mapping, interface, and validation results. This avoids repeating the catalogue's unrelated checks and lets supported branches finish. It spends effort establishing dependencies and leaves an inaccessible consumer unresolved. |
| Revalidate every identified use in the same receiving scope | Make the same meaning and coverage comparison, then execute the appropriate receiving-use checks for every member, including those ultimately found independent. | Retain this alternative when those checks are cheaper or more dependable than selective impact analysis. It may reduce reliance on a detailed dependency model, but can repeat unaffected checks and delay a common release. It still cannot clear an unknown consumer or infer meaning from schema compatibility. |

For the worked horizon case, the established catalogue independence and separable endpoint results justify selective revalidation. The accepted trade-off is the work needed to establish that independence and the explicit limit on the unknown consumer; no universal cost or completeness advantage is claimed. §4.1.7 prevents local completions from being mistaken for a wider no-impact result. For one already known use, the direct domain result remains sufficient under §1.

[LOT4KG](https://lot.linkeddata.es/LOT4KG/) supplies a current candidate line for changes that propagate between an ontology, mappings, graph content, constraints, and validation. **Adapt** those relationships in §4.1.4–5 and §4.2 when a KG realization is selected. They help locate which integration result needs work; they do not choose source truth, application action, or a universal regression policy. For other realizations, the same return question is answered from their actual semantic dependencies. **Reject** a changed version alone as evidence that every use failed, and an unchanged carrier alone as evidence that every use passed.

Reopen this comparison when one actual affected use was missed, when a dependency or coverage claim is defeated, or when the cost of qualifying selective impact exceeds the available full receiving-use regression. Reconsider only the affected discovery and checking choice in §4.1.3–5. Changed results still require their domain evidence whichever strategy is selected.

### SIE.11:12 - Relations

- A.10.1 governs affected-use discovery when the scope of reliance needs to be found.
- SIE.2 supplies the source meaning, edition, authority, and access premises used in the comparison.
- SIE.3–SIE.9 supply the domain results located in §4.2; SIE.10 supplies validation for the affected receiving claim.
- SIE.12 supplies the module dependencies and material-change arrangements of an actual commons.
- Domain source owners, MDM, SYSE, operational providers, and receiving applications retain their respective decisions.

### SIE.11:End
