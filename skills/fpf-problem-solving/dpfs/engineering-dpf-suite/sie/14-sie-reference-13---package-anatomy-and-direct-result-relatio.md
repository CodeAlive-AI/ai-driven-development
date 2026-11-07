## SIE.Reference:13 - Package anatomy and direct result relations

[SIE.13](33-sie-13---construct-a-semantic-integration-for-a-named-receiv.md) constructs the whole from the required contributions below. The table identifies results to connect or reuse, not a required new deliverable from every pattern.


| Package part | Supplying body or return | Minimum inspectable content |
| --- | --- | --- |
| use contract | `SIE.1` | receiver, use, answer claims, tolerated loss/uncertainty, freshness/latency/quality, authority, representative tests, stop and reopen |
| source manifest | `SIE.2`; SIE.3 qualification when needed | assets, schemes, editions/effectivity, meanings and identifiers used, owners/authority, provenance/access, gaps, and references to required model qualifications |
| correspondence set | `SIE.4` | endpoints, relation or incompatibility, orientation, bounded use, permitted loss, justification/evidence, source versions, counterexamples and unresolved rows |
| cross-source identity disposition | `SIE.5` | load-bearing endpoints, grain and interval, disposition kind, schemes and issuers, evidence, authority boundary, downstream references for the relied-on identity; an explanation of unused identity only when it affects interpretation or later reliance |
| source-qualified claim composition | `SIE.6` | source claims, scope, interval, authority, uncertainty, derivation, relied-on identity premises, comparable/conflicting/non-comparable/unresolved relation, qualified view or explicit conflict |
| mapping specification | `SIE.7` | schemes, accepted semantic inputs, rules, conditions, cardinalities, units/codes, defaults, errors, loss, trace, examples and tests |
| realization and interface | `SIE.8`, `SIE.9` | virtual/materialized/hybrid decision, required implementation result, receiver contract, interpretation, currentness, errors, provenance, access assumptions and return path |
| validation account | `SIE.10` | evidence sufficient for the bounded disposition; every load-bearing layer and required cases for a positive use claim; material unexamined reach, pass/narrow/unresolved/stop, and reopen condition |

`SIE.1 → SIE.2` supplies the use and source cut. `SIE.2 → SIE.3` is conditional. `SIE.2` and any supplied use-fit model feed `SIE.4`–`SIE.6`. `SIE.4` can expose an identity question for `SIE.5` and supplies semantic premises to `SIE.7`. `SIE.5` supplies load-bearing identity premises to `SIE.6`, `SIE.7`, and `SIE.10`. `SIE.6` supplies a qualified composition or explicit conflict branch to `SIE.7` and `SIE.9`. `SIE.7 → SIE.8 → SIE.9 → SIE.10` connects executable semantics to realization, receiver, and bounded validation. SIE.11 revisits only affected reliance, using these dependencies where material. SIE.12 supplies shared-module arrangements when actual users require them. These relations may iterate.
