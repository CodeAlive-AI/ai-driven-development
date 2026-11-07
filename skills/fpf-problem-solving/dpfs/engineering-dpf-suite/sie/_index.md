# Semantic Integration Engineering Principles Framework

**DocID:** `SIE` within **FPF Library**.

> A domain pattern language for making separately governed meanings and representations usable together for a named receiving use.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 20 October 2026
- **Status:** Eternal alpha, open to correction as methods, sources, and applications change. The thirteen Methods support construction of a receiving-use integration, model reuse or development, semantic interfaces, affected-use revalidation, and modular semantic commons.
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) for original framework content; third-party material retains its own terms.
- **Publication:** [FPF Library repository](https://github.com/ailev/FPF)

Use the Readme to enter from a working difficulty, or the Table of Contents to open one available pattern. The Architectural Reference explains how the contributions work together and the scope of their use. For references to this version, use the [Citation](_index.md#citation).

# Table of Contents

Use the Readme to follow several methods through a receiving-use problem. Use this Table of Contents when you know the result you need. The 13 included bodies describe the Methods and their individual status.

`SIE.*` is the PatternID namespace. Numbers are stable addresses, not a Work sequence.

## Public units

| Unit | Reader use |
| :--- | :--- |
| [Semantic Integration Engineering Principles Framework Readme](_index.md#semantic-integration-engineering-principles-framework-readme) | Follow connected inspection, provider and semantic-commons uses, including changed premises and partial results. |
| [Citation](_index.md#citation) | Cite this edition or one pattern with its PatternID and date. |
| [Semantic Integration Engineering Principles Framework Architectural Reference](01-semantic-integration-engineering-principles-framework-archit.md) | Understand how the contributions connect, why their boundaries matter, and which combined results the repertoire can support. |
| [SIE.Reference:1](02-sie-reference-1---meanings-identifiers-claims-carriers-and-w.md) | Meanings, identifiers, claims, carriers, and world-side referents remain distinct |
| [SIE.Reference:2](03-sie-reference-2---source-authority-and-receiving-authority-r.md) | Source authority and receiving authority remain separate |
| [SIE.Reference:3](04-sie-reference-3---pattern-relations-do-not-prescribe-a-lifec.md) | Pattern relations do not prescribe a lifecycle |
| [SIE.Reference:4](05-sie-reference-4---the-first-whole-result.md) | The first whole result |
| [SIE.Reference:5](06-sie-reference-5---use-the-repertoire-at-the-scale-of-the-mis.md) | Use the repertoire at the scale of the missing result |
| [SIE.Reference:6](07-sie-reference-6---qualify-the-combined-arrangement.md) | Qualify the combined arrangement |
| [SIE.Reference:6.1](07-sie-reference-6---qualify-the-combined-arrangement.md#siereference61---a-shared-request-limit-changes-the-provider-result) | A shared request limit changes the provider result |
| [SIE.Reference:7](08-sie-reference-7---architectural-rationale.md) | Architectural Rationale |
| [SIE.Reference:7.1](08-sie-reference-7---architectural-rationale.md#siereference71---source-contributions-behind-the-arrangement) | Source contributions behind the arrangement |
| [SIE.Reference:8](09-sie-reference-8---costs-perspectives-and-correction.md) | Costs, perspectives, and correction |
| [SIE.Reference:9](10-sie-reference-9---before-relying-on-the-whole-result.md) | Before relying on the whole result |
| [SIE.Reference:10](11-sie-reference-10---intended-use-and-ordinary-non-use.md) | Intended use and ordinary non-use |
| [SIE.Reference:11](12-sie-reference-11---patternid-and-reader-order.md) | PatternID and reader order |
| [SIE.Reference:12](13-sie-reference-12---supplied-pattern-repertoire.md) | Supplied pattern repertoire |
| [SIE.Reference:13](14-sie-reference-13---package-anatomy-and-direct-result-relatio.md) | Package anatomy and direct result relations |
| [SIE.Reference:14](15-sie-reference-14---pattern-selection-and-first-returned-resu.md) | Pattern selection and first returned result |
| [SIE.Reference:15](16-sie-reference-15---related-modeling-and-engineering-work.md) | Related modeling and engineering work |
| [SIE.Reference:16](17-sie-reference-16---fpf-neighboring-practice-and-authority-bo.md) | FPF, neighboring practice, and authority boundaries |
| [SIE.Reference:17](18-sie-reference-17---representative-case-coverage.md) | Representative case coverage |
| [SIE.Reference:18](19-sie-reference-18---publication-boundary.md) | Publication boundary |
| [SIE.Sources:1](41-sie-sources-1---source-use-and-currentness.md) | Source use and currentness |
| [SIE.Sources:2](42-sie-sources-2---edition-return.md) | Edition return |
| [Authoritative Pattern Bodies](21-sie-1---bound-the-receiving-use-and-semantic-contract.md) | Use the thirteen SIE bodies under their own entry conditions; PatternID order is not a lifecycle. |
| [SIE.Application - Cross-Pattern Application](34-cross-pattern-application.md) | Inspect AP242/QIF, semiconductor identity, quality/provenance, high-change-provider, and semantic-commons cases. |
| [Semantic Integration Engineering Principles Framework Sources and Edition Notes](_index.md#semantic-integration-engineering-principles-framework-sources-and-edition-notes) | Check package anatomy, availability, sources, neighboring modeling work, owners, and edition limits. |

## Part I - Semantic Integration Engineering Methods

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [SIE.1 - Bound the Receiving Use and Semantic Contract](21-sie-1---bound-the-receiving-use-and-semantic-contract.md) | Stable | What exact receiving use, semantic loss boundary, authority, and validation obligation govern this integration? | FPF C.37; C.39.RQ; direct receiver and source-owner results |
| 2 | [SIE.2 - Recover and Qualify Source Semantics and Authority](22-sie-2---recover-and-qualify-source-semantics-and-authority.md) | Stable | What does each load-bearing source mean, under which edition, effectivity, authority, and access conditions? | SIE.1 or equivalent contract; FPF F.0.1, F.0.2; direct source owners |
| 3 | [SIE.3 - Construct or Reuse a Semantic Model for a Named Use](23-sie-3---construct-or-reuse-a-semantic-model-for-a-named-use.md) | Stable | Does an available model answer the receiving questions, or what semantic extension is needed? | SIE.1 or equivalent use; relevant SIE.2 source meanings; domain participants |
| 4 | [SIE.4 - Judge Cross-Source Correspondences and Their Permitted Uses](24-sie-4---judge-cross-source-correspondences-and-their-permitt.md) | Stable | Which exact endpoint relation, difference, or incompatibility is warranted and usable here? | SIE.2; supplied SIE.3 result when required; FPF F.9 |
| 5 | [SIE.5 - Resolve Cross-Source Identity without Erasing Identifier Authority](25-sie-5---resolve-cross-source-identity-without-erasing-identi.md) | Stable | Do these source endpoints concern the same entity at the required grain and interval, or another relation? | SIE.2; conditional SIE.4; direct MDM/domain authority inputs |
| 6 | [SIE.6 - Fuse Source-Qualified Claims without Erasing Conflict](26-sie-6---fuse-source-qualified-claims-without-erasing-conflic.md) | Stable | How can source claims be composed while preserving scope, authority, uncertainty, conflict, and non-comparability? | SIE.2, SIE.4; SIE.5 when identity is load-bearing; FPF C.2.1, A.10 |
| 7 | [SIE.7 - Specify Semantic Extraction and Transformation Mappings](27-sie-7---specify-semantic-extraction-and-transformation-mappi.md) | Stable | Which executable rules preserve the accepted correspondences, identities, claim branches, and losses? | SIE.2, SIE.4; conditional SIE.5 and SIE.6; FPF A.6.3.RT |
| 8 | [SIE.8 - Choose Virtual, Materialized, or Hybrid Semantic Realization](28-sie-8---choose-virtual-materialized-or-hybrid-semantic-reali.md) | Stable | Which available realization can meet the semantic, freshness, access, provenance, recovery, and combined resource conditions? | SIE.1, SIE.7; direct Data Engineering, platform, provider, and protection results |
| 9 | [SIE.9 - Connect a Receiving Use through a Semantic Interface](29-sie-9---connect-a-receiving-use-through-a-semantic-interface.md) | Stable | What smallest interface carries the required meanings, branches, provenance, and return paths into receiving Work? | SIE.1, SIE.7, SIE.8; conditional SIE.4-SIE.6 results |
| 10 | [SIE.10 - Validate a Semantic Integration Result for Its Receiving Use](30-sie-10---validate-a-semantic-integration-result-for-its-rece.md) | Stable | What does the evidence settle about the named receiving use, and which claimed premises still need validation? | SIE.1 or equivalent use; relevant SIE.2-SIE.9 results; direct domain and receiver acceptance criteria |
| 11 | [SIE.11 - Trace Semantic Change and Revalidate Affected Uses](31-sie-11---trace-semantic-change-and-revalidate-affected-uses.md) | Stable | Which receiving results depend on the changed semantic premise, and what can now continue? | Changed relied-on premise; relevant SIE.2-SIE.10 results; FPF A.10.1 when discovery is needed |
| 12 | [SIE.12 - Govern Modular Semantic Commons without Universal Authority](32-sie-12---govern-modular-semantic-commons-without-universal-a.md) | Stable | How can actual users maintain and rely on shared semantic modules and their changes? | Actual shared-module uses; SIE.3, SIE.4, and SIE.11 when their results are needed |
| 13 | [SIE.13 - Construct a Semantic Integration for a Named Receiving Use](33-sie-13---construct-a-semantic-integration-for-a-named-receiv.md) | Stable | How do we obtain and connect the required contributions, choose the next missing result, and supply an answer that works under their joint conditions? | Receiving need and available results; SIE.1–SIE.11 where their contributions are needed; SIE.12 for actual commons work |

# Semantic Integration Engineering Principles Framework Readme

## Practical entries

To construct a semantic integration from several contributions, use [SIE.13](33-sie-13---construct-a-semantic-integration-for-a-named-receiv.md): receiving need → required meanings and contributions → valid connections and joint conditions → next missing result → supplied receiving answer → affected return after change. Reuse adequate results and finish a sufficient local question directly; this connection is not a requirement to execute the full repertoire. The [worked construction](33-sie-13---construct-a-semantic-integration-for-a-named-receiv.md#sie135---archetypal-grounding) explains why these moves produce a usable whole.


Start from the query, decision, or operation that needs a cross-source answer. The constructed connections below show how meanings, identity, executable rules, and receiving use constrain one another. Reuse supplied results when their use and conditions still match; open the [Table of Contents](_index.md#table-of-contents) for another question or the [pattern-selection guide](15-sie-reference-14---pattern-selection-and-first-returned-resu.md) for a missing result.

The [Architectural Reference](01-semantic-integration-engineering-principles-framework-archit.md) explains the repertoire and its [architectural rationale](08-sie-reference-7---architectural-rationale.md). You can ask an assisting agent: “Explain this and give me your comments in the language of my work, without framework jargon.”

### SIE-INSPECTION - Connect inspection evidence to the configured product

- **Situation:** Product-definition and inspection sources are accessible, but a quality engineer cannot tell which inspection result concerns the feature in the configuration being reviewed.
- **Question:** How can the receiving query return applicable evidence and expose the branches it cannot establish?
- **First useful result or blocker:** The required answer for a named feature, configuration, and effectivity, with the permitted incomplete branches; or the missing configuration or acceptance decision that prevents bounding that answer.
- **Start with:** [SIE.1](21-sie-1---bound-the-receiving-use-and-semantic-contract.md) when the receiving question is unsettled; [SIE.10](30-sie-10---validate-a-semantic-integration-result-for-its-rece.md) when an existing result already fails that question.
- **Stop or return:** Stop a dependent branch on unresolved feature identity or configuration. Return a source-definition gap to its owner, a transformation defect to SIE.7, and the release or inspection-acceptance decision to the engineering or quality authority.

In [APP-SIE-01](35-sie-application-1---app-sie-01---ap242-and-qif-product-lifec.md), the engineer asks for the QIF plan and result concerning feature `F` in released revision/configuration `R` at effectivity `E`. SIE.1 makes those inputs and the acceptable answer branches explicit. [SIE.2](22-sie-2---recover-and-qualify-source-semantics-and-authority.md) then supplies the source editions, local definitions, identifier schemes, and authority needed to interpret them. If the available model cannot distinguish a planned inspection from an observation of that configured feature, [SIE.3](23-sie-3---construct-or-reuse-a-semantic-model-for-a-named-use.md) develops that missing distinction and tests it against those cases. An adequate existing model can be reused.

Those meanings allow [SIE.4](24-sie-4---judge-cross-source-correspondences-and-their-permitt.md) to state a directed relation: inspection characteristic `C-17` concerns product feature `F-17` under the plan and configuration. [SIE.5](25-sie-5---resolve-cross-source-identity-without-erasing-identi.md) qualifies the feature endpoint at the required grain and effectivity. The relation permits navigation between the records; it does not make a characteristic identical to a product feature. A shared label without the supporting plan and effectivity remains an unmatched candidate. [SIE.6](26-sie-6---fuse-source-qualified-claims-without-erasing-conflic.md) uses these premises to combine definition, plan, and observation claims while retaining their sources and any conflict.

[SIE.7](27-sie-7---specify-semantic-extraction-and-transformation-mappi.md) turns the accepted relations into selection and transformation rules. The rules select the supplied released configuration, preserve both source identifiers, and expose an unknown unit or unmatched feature. [SIE.8](28-sie-8---choose-virtual-materialized-or-hybrid-semantic-reali.md) uses those required behaviours when comparing ways to supply the result; [SIE.9](29-sie-9---connect-a-receiving-use-through-a-semantic-interface.md) makes their meanings, timestamps, provenance, and failure branches available in the engineer's query.

The constructed application permits a qualified row set with unresolved local-extension and unknown-unit branches shown separately. SIE.10 can support that narrower answer only with matching evidence for all premises on which it relies, including the engineer's interpretation. A different question can finish much earlier: if a conversion returns 1 millimetre from an input of 1 metre where 1000 millimetres is required, that case establishes the mapping failure and returns it to SIE.7; unrelated layers remain unexamined. When the released configuration changes, [SIE.11](31-sie-11---trace-semantic-change-and-revalidate-affected-uses.md) follows the changed applicability through the relied-on identity, mapping, and receiving tests. The query supplies evidence; the responsible authorities still decide release and acceptance.

### SIE-PROVIDERS - Compare live availability under semantic and access limits

- **Situation:** Two provider APIs both expose an availability number, but their quantities and copying permissions differ from what a purchasing comparison assumes.
- **Question:** Which qualified answer can the interface supply within the receiving and access conditions?
- **First useful result or blocker:** Separately attributed quantities with the conditions needed for comparison, or a semantic or access limit that defeats the proposed answer.
- **Start with:** [SIE.2](22-sie-2---recover-and-qualify-source-semantics-and-authority.md) and [SIE.6](26-sie-6---fuse-source-qualified-claims-without-erasing-conflic.md) for unsettled meanings and comparison; [SIE.8](28-sie-8---choose-virtual-materialized-or-hybrid-semantic-reali.md) when those premises are supplied and realization is the remaining question.
- **Stop or return:** Exclude prohibited copying. Return an infeasible complete answer for a permitted narrower result or an access-owner decision. Reopen the affected meaning and interface when a provider changes the quantity it reports.

In the constructed provider case of [APP-SIE-04](38-sie-application-4---app-sie-04---high-change-provider-availa.md) and SIE.6, Provider A reports 12 on hand and Provider B reports 9 available to promise. SIE.2 recovers the reservation and horizon rules behind the quantities. [SIE.3](23-sie-3---construct-or-reuse-a-semantic-model-for-a-named-use.md) can reuse a model that keeps both measures, providers, units, times, and horizons distinct. [SIE.4](24-sie-4---judge-cross-source-correspondences-and-their-permitt.md) supplies the qualified product-family relation. SIE.6 retains separate provider claims: the numbers do not support a common “21 available” total. For the question “Who can supply 8 now?”, A's reservation check and B's promise horizon must also support the receiving use.

Both providers prohibit replication. That prohibition is sufficient for SIE.8 to reject a copied availability store. If the question asks which remaining arrangement to use, compare query-time retrieval and any permitted hybrid with their latency, provenance, failure behaviour, and common resource demands. Develop only serious remaining alternatives. Obtain further evidence when its possible contribution to the choice justifies the burden and displaced work.

The [shared-request example](07-sie-reference-6---qualify-the-combined-arrangement.md#siereference61---a-shared-request-limit-changes-the-provider-result) assumes four calls for A, four for B, and three for the required common trace, all under one ten-call allowance. The complete answer needs eleven calls before retries. With permission for an incomplete answer, A plus the trace needs seven: [SIE.9](29-sie-9---connect-a-receiving-use-through-a-semantic-interface.md) can expose “12 on hand at T” and “B not retrieved”, retaining the source and rule trace. B has not reported zero. SIE.10 still checks the other conditions needed for that narrower use; if both providers are mandatory, the result is a stop until the allowance or call demand is changed on supported grounds.

Suppose B keeps the same JSON field but changes its promise horizon. [SIE.11](31-sie-11---trace-semantic-change-and-revalidate-affected-uses.md) compares the meanings and finds the uses that consume them. An “available now” view returns to claim composition, mapping, interface, and receiving-use validation; a future-planning view may accept the new horizon after checking its own conditions. Product descriptions whose meanings are independent of that quantity can keep their earlier qualification. An inaccessible consumer interpretation remains unresolved. Purchasing decides how to act on the qualified or incomplete answer.

### SIE-COMMONS - Govern shared semantic modules

- **Situation:** Several organizations use a shared classification, and a proposed improvement would change which objects belong to one of its classes.
- **Question:** How can the shared model evolve while each consumer can still identify the meaning its work needs?
- **First useful result or blocker:** The proposed distinction and the users whose questions depend on it, or an unresolved definition or decision right that prevents the change.
- **Start with:** [SIE.12](32-sie-12---govern-modular-semantic-commons-without-universal-a.md), with [SIE.3](23-sie-3---construct-or-reuse-a-semantic-model-for-a-named-use.md) for changed model content and [SIE.11](31-sie-11---trace-semantic-change-and-revalidate-affected-uses.md) for actual consumer reliance.
- **Stop or return:** Keep incompatible criteria in scoped modules when their users need them. A pair needing only one interface can complete that agreement; shared-module governance is useful when independently maintained modules and users create that further need.

In [APP-SIE-05](39-sie-application-5---app-sie-05---a-modular-equipment-classif.md), two manufacturers and a service partner share equipment classes. A proposal replaces “equipment with a replaceable drive” with “equipment serviced through a replaceable drive module”. Equipment X has only a separately replaceable drive; Y also supports drive-module replacement. These cases expose the changed classification: X belongs to the earlier class but not the proposed one, while Y belongs to both.

SIE.3 uses those cases to make the meanings distinguishable. Under the constructed SIE.12 agreement, the authorized maintainers keep `equip:DriveReplaceable` for the earlier meaning and introduce `equip:DriveModuleServiceable` for the new one. Both definitions and their editions remain recoverable. Source owners continue to supply the product descriptions on which membership depends.

SIE.11 follows each consumer's question. The service partner adopts the new class for module-replacement planning, so [SIE.4](24-sie-4---judge-cross-source-correspondences-and-their-permitt.md) revisits its correspondences and the query uses the revised relation. [SIE.10](30-sie-10---validate-a-semantic-integration-result-for-its-rece.md) checks the integration premises, including the result that admits Y and excludes X. Manufacturer A still needs its spare-drive query under the earlier meaning and can retain matching evidence. The release supplies the access, dependencies, migration information, and notice those uses need. These two completed outcomes leave other consumers' migration to be established where it matters.

## Citation

If you use this edition, cite:

```text
Anatoly Levenchuk, with AI-assisted development and review.
Semantic Integration Engineering Principles Framework.
20 October 2026.
GitHub repository: https://github.com/ailev/FPF
```

For a particular pattern, add its PatternID and title. Retain the edition designation and date, and include a permanent link or stored copy when exact wording matters.

---

## Files of this publication

Generated by the skill's splitter: one file per section, in reading order.


### Semantic Integration Engineering Principles Framework Architectural Reference

- [Semantic Integration Engineering Principles Framework Architectural Reference](01-semantic-integration-engineering-principles-framework-archit.md) (10 lines)
- [SIE.Reference:1 - Meanings, identifiers, claims, carriers, and world-side referents remain distinct](02-sie-reference-1---meanings-identifiers-claims-carriers-and-w.md) (12 lines)
- [SIE.Reference:2 - Source authority and receiving authority remain separate](03-sie-reference-2---source-authority-and-receiving-authority-r.md) (6 lines)
- [SIE.Reference:3 - Pattern relations do not prescribe a lifecycle](04-sie-reference-3---pattern-relations-do-not-prescribe-a-lifec.md) (6 lines)
- [SIE.Reference:4 - The first whole result](05-sie-reference-4---the-first-whole-result.md) (17 lines)
- [SIE.Reference:5 - Use the repertoire at the scale of the missing result](06-sie-reference-5---use-the-repertoire-at-the-scale-of-the-mis.md) (12 lines)
- [SIE.Reference:6 - Qualify the combined arrangement](07-sie-reference-6---qualify-the-combined-arrangement.md) (20 lines)
- [SIE.Reference:7 - Architectural Rationale](08-sie-reference-7---architectural-rationale.md) (32 lines)
- [SIE.Reference:8 - Costs, perspectives, and correction](09-sie-reference-8---costs-perspectives-and-correction.md) (8 lines)
- [SIE.Reference:9 - Before relying on the whole result](10-sie-reference-9---before-relying-on-the-whole-result.md) (13 lines)
- [SIE.Reference:10 - Intended use and ordinary non-use](11-sie-reference-10---intended-use-and-ordinary-non-use.md) (6 lines)
- [SIE.Reference:11 - PatternID and reader order](12-sie-reference-11---patternid-and-reader-order.md) (4 lines)
- [SIE.Reference:12 - Supplied pattern repertoire](13-sie-reference-12---supplied-pattern-repertoire.md) (12 lines)
- [SIE.Reference:13 - Package anatomy and direct result relations](14-sie-reference-13---package-anatomy-and-direct-result-relatio.md) (18 lines)
- [SIE.Reference:14 - Pattern selection and first returned result](15-sie-reference-14---pattern-selection-and-first-returned-resu.md) (18 lines)
- [SIE.Reference:15 - Related modeling and engineering work](16-sie-reference-15---related-modeling-and-engineering-work.md) (11 lines)
- [SIE.Reference:16 - FPF, neighboring practice, and authority boundaries](17-sie-reference-16---fpf-neighboring-practice-and-authority-bo.md) (6 lines)
- [SIE.Reference:17 - Representative case coverage](18-sie-reference-17---representative-case-coverage.md) (12 lines)
- [SIE.Reference:18 - Publication boundary](19-sie-reference-18---publication-boundary.md) (8 lines)
- [SIE.Reference:End](20-sie-reference-end.md) (3 lines)

### Part I - Semantic Integration Engineering Methods

- [SIE.1 - Bound the Receiving Use and Semantic Contract](21-sie-1---bound-the-receiving-use-and-semantic-contract.md) (151 lines)
- [SIE.2 - Recover and Qualify Source Semantics and Authority](22-sie-2---recover-and-qualify-source-semantics-and-authority.md) (147 lines)
- [SIE.3 - Construct or Reuse a Semantic Model for a Named Use](23-sie-3---construct-or-reuse-a-semantic-model-for-a-named-use.md) (170 lines)
- [SIE.4 - Judge Cross-Source Correspondences and Their Permitted Uses](24-sie-4---judge-cross-source-correspondences-and-their-permitt.md) (148 lines)
- [SIE.5 - Resolve Cross-Source Identity without Erasing Identifier Authority](25-sie-5---resolve-cross-source-identity-without-erasing-identi.md) (149 lines)
- [SIE.6 - Fuse Source-Qualified Claims without Erasing Conflict](26-sie-6---fuse-source-qualified-claims-without-erasing-conflic.md) (150 lines)
- [SIE.7 - Specify Semantic Extraction and Transformation Mappings](27-sie-7---specify-semantic-extraction-and-transformation-mappi.md) (152 lines)
- [SIE.8 - Choose Virtual, Materialized, or Hybrid Semantic Realization](28-sie-8---choose-virtual-materialized-or-hybrid-semantic-reali.md) (175 lines)
- [SIE.9 - Connect a Receiving Use through a Semantic Interface](29-sie-9---connect-a-receiving-use-through-a-semantic-interface.md) (153 lines)
- [SIE.10 - Validate a Semantic Integration Result for Its Receiving Use](30-sie-10---validate-a-semantic-integration-result-for-its-rece.md) (174 lines)
- [SIE.11 - Trace Semantic Change and Revalidate Affected Uses](31-sie-11---trace-semantic-change-and-revalidate-affected-uses.md) (170 lines)
- [SIE.12 - Govern Modular Semantic Commons without Universal Authority](32-sie-12---govern-modular-semantic-commons-without-universal-a.md) (191 lines)
- [SIE.13 - Construct a Semantic Integration for a Named Receiving Use](33-sie-13---construct-a-semantic-integration-for-a-named-receiv.md) (248 lines)

### Cross-Pattern Application

- [Cross-Pattern Application](34-cross-pattern-application.md) (6 lines)
- [SIE.Application:1 - APP-SIE-01 - AP242 and QIF product-lifecycle query](35-sie-application-1---app-sie-01---ap242-and-qif-product-lifec.md) (23 lines)
- [SIE.Application:2 - APP-SIE-02 - Semiconductor identity and traceability](36-sie-application-2---app-sie-02---semiconductor-identity-and.md) (8 lines)
- [SIE.Application:3 - APP-SIE-03 - End-to-end quality and provenance](37-sie-application-3---app-sie-03---end-to-end-quality-and-prov.md) (10 lines)
- [SIE.Application:4 - APP-SIE-04 - High-change provider availability without a materialized graph](38-sie-application-4---app-sie-04---high-change-provider-availa.md) (8 lines)
- [SIE.Application:5 - APP-SIE-05 - A Modular Equipment-Classification Commons](39-sie-application-5---app-sie-05---a-modular-equipment-classif.md) (8 lines)
- [SIE.Application:End](40-sie-application-end.md) (3 lines)

### Semantic Integration Engineering Principles Framework Sources and Edition Notes

- [SIE.Sources:1 - Source use and currentness](41-sie-sources-1---source-use-and-currentness.md) (21 lines)
- [SIE.Sources:2 - Edition return](42-sie-sources-2---edition-return.md) (6 lines)
- [SIE.Sources:End](43-sie-sources-end.md) (1 lines)
