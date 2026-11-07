## SIE.12 - Govern Modular Semantic Commons without Universal Authority

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `ModularSemanticCommonsAccount@Community` describing how actual users maintain and rely on shared semantic modules, their dependencies, decisions, and releases.

### SIE.12:1 - Problem Frame

**Use this when** independently governed participants depend on shared semantic modules and need an arrangement for maintaining them. A typical failure is a changed shared term whose consumers cannot determine who could approve the change, which meaning their interface uses, or how to migrate.

Start with one module and the uses that actually depend on it. Establish its scope, who can decide its content and release, and how its users can obtain an identifiable maintained edition. The first useful result is an agreement through which those participants can make and use a concrete module change.

The object is the shared maintenance and reliance arrangement for semantic modules. The gain is continued reuse with explicit local commitments, contribution rights, dependencies, and change consequences. A compatibility claim covering additional users needs support for those users' relevant reliance.

A team or a pair maintaining one interface can use its ordinary model and interface agreement when that suffices. A repeated file or shared repository alone does not establish a commons that needs this Method.

### SIE.12:2 - Problem

Reusable semantic assets acquire users outside their original project. A term, class, relation, or mapping then carries assumptions into interfaces maintained by other participants. Changes can break those assumptions even when the shared file remains available.

One response is to require every participant to adopt one centrally controlled model. Another is to allow local changes without a recoverable relation to the shared meaning. Both can defeat useful reuse: the first can suppress necessary domain distinctions, while the second makes compatibility impossible to assess.

### SIE.12:3 - Forces

| Force | Tension |
| --- | --- |
| Shared meaning | Common modules reduce repeated work, while participants retain distinct purposes and source authority. |
| Local development | Extensions can answer local questions, while consumers need to know which shared commitments still hold. |
| Decision rights | Maintainers need power to release a module, while contact or repository access alone cannot establish that remit. |
| Stability | Identifiable meanings support reliance, while mistakes and changed requirements need correction. |
| Participation | Open contribution can improve coverage, while unresolved proposals still need a usable decision path. |

### SIE.12:4 - Solution

Define the smallest shared module arrangement that serves the actual users. Make its semantic scope, decisions, dependencies, and releases usable in their integration work. Preserve local modules and disagreement where convergence is unnecessary or unsupported.

#### SIE.12:4.1 - Pattern-Use Unfolding

1. **Identify the shared use.** Name the users and questions that depend on the module. Locate the semantic content they share and the local distinctions they still need. If the actual need is only one interface agreement, complete that agreement through the relevant SIE Methods.
2. **Set module boundaries.** State the module's domain, concepts and relations, intended uses, material exclusions, and relation to local extensions. Use SIE.3 for content that needs model development and SIE.4 for qualified correspondences between different module meanings.
3. **Establish identification and dependencies.** Choose namespaces or identification practices that let consumers recover the intended term or module meaning. Identify editions and the dependencies each supported use needs. A permitted version range must have a semantic compatibility basis for its claimed use.
4. **Assign the decisions and communication.** State who may propose changes, decide module content, release an edition, resolve a disagreement under the community's rules, and communicate with users. Record the actual remit of each responsibility. A source owner retains its source meaning and issuance authority.
5. **Make contribution workable.** Give a proposer enough guidance to supply the changed meaning, rationale, examples, affected modules, and known consumer consequences. Route the proposal to the people authorized to decide it. Keep an unresolved disagreement explicit and permit a scoped local extension or alternative module when it can serve its users.
6. **Prepare the release for its consumers.** Identify material semantic changes and use SIE.11 for affected reliance. Provide the edition, access, dependency conditions, and migration or deprecation information needed by those users. Distinguish a clarification from a changed meaning; preserve a way to identify the earlier meaning when consumers still rely on it.
7. **Notify and maintain at the agreed scope.** Give affected users notice that permits the action required by their dependency and the community agreement. Maintain a responsive contact and a workable path for corrections. An urgent correction may require immediate qualified publication and notification; describe the resulting limits.
8. **Return the usable arrangement.** Show how the named participants can obtain a module, propose a change, decide and release it, and interpret the effect on their supported uses. An unresolved decision right or dependency limits the part of the commons that can be claimed as governed.

These responsibilities can fit a small agreement for a small commons. Broader participation adds work only where additional semantic dependence or decision needs arise.

#### SIE.12:4.2 - Record the Result

| Arrangement position | Content used by participants |
| --- | --- |
| Shared module and users | Semantic scope, supported uses, and the participants who depend on it. |
| Local relationship | Extensions, maintained correspondences, disagreements, and the commitments claimed across module boundaries. |
| Identification and dependencies | Namespaces or equivalent identifiers, recoverable editions, access, and dependency or compatibility conditions. |
| Decisions and communication | Proposal, content, release, dispute, and contact responsibilities at their actual remit. |
| Change and continued use | Material-change assessment, notices, correction, migration, deprecation, and maintained access needed by consumers. |

Refer to existing module definitions and working agreements when they supply this content. The account makes the arrangement recoverable; it need not reproduce every module or introduce a separate record for each responsibility.

#### SIE.12:4.3 - What Changes in Practice

A user can identify the meaning and edition its interface consumes and find the decision needed for a proposed change. Maintainers can release a scoped improvement while preserving the commitments they claim to retain. Participants can keep different local meanings through explicit module boundaries and correspondences.

### SIE.12:5 - Archetypal Grounding

#### SIE.12:5.1 - Equipment Classes Shared by Three Organizations

Two manufacturers and a service partner exchange service observations using a shared equipment-classification module. Each manufacturer also has local classes needed for its own products.

| Arrangement | Concrete use |
| --- | --- |
| Shared core | Describes the equipment categories needed to interpret the service observations. |
| Local modules | Retain product-specific distinctions and identify their relation to the shared core. |
| Correspondences | State the qualified relations between local and shared classes; different meanings remain visible. |
| Content decision | The agreed maintainers decide changes to the shared module within its stated scope. |
| Release decision | The participant authorized to release the module publishes an identified edition and its dependency conditions. |
| Contact | A reachable participant receives questions, communicates decisions, and helps route disputes. |
| Source authority | Each manufacturer retains the authority for its product descriptions and issued source claims. |

A participant proposes changing a shared class from “equipment with a replaceable drive” to “equipment serviced through a replaceable drive module.” The second definition changes the classification criterion. Existing service queries can depend on the first meaning.

For this constructed agreement, the maintainers retain the earlier class and introduce a distinct class for the new criterion. The illustrative identifier `equip:DriveReplaceable` continues to mean “equipment with a replaceable drive”; `equip:DriveModuleServiceable` means “equipment serviced through a replaceable drive module.” The second module edition contains both definitions and leaves the earlier edition accessible. It asserts no equivalence between the classes.

The manufacturers' qualified product descriptions supply these discriminating cases:

| Equipment | Earlier class | New class |
| --- | --- | --- |
| X: its drive can be replaced as a separate part; it has no replaceable drive service module. | Included: the drive is replaceable. | Excluded: module replacement is not its service arrangement. |
| Y: its drive can be replaced separately, and the supported service arrangement also provides a replaceable drive module. | Included. | Included under the module-service criterion. |

SIE.11 follows the changed classification need to the actual queries. Two consumer outcomes complete the illustrative transition:

- The service partner changes its receiving question to module-replacement planning. It adopts `equip:DriveModuleServiceable`, updates the relevant correspondence and query, and verifies that Y is included and X excluded. The receiving owner accepts that scoped result; SIE.10 validates its integration premises.
- Manufacturer A retains its spare-drive query against `equip:DriveReplaceable`. Its required meaning and the qualified X/Y results remain unchanged, so it retains matching evidence for that use. Adopting the new class is not a prerequisite for continuing this query.

The participant authorized to release the module publishes the identified edition with those definitions, dependency conditions, and migration information. Contact supplies the notice; the content decision, product-source claims, and receiving decisions keep the separate remits shown above. The two completed consumer results do not establish migration by every other user.
If the two manufacturers require incompatible local criteria, the commons can retain scoped local modules and their qualified correspondences.

#### SIE.12:5.2 - A Sufficient Interface Agreement

Two providers agree to expose separately attributed `on hand` and `available to promise` values. They have no additional users maintaining a shared module.

Their agreement identifies the meanings, source owners, interface responsibilities, and change conditions. SIE.3 and SIE.9 can supply the model and interface results. Those results complete the current need. A commons arrangement becomes useful if independently maintained shared modules and their users create a further maintenance problem.

#### SIE.12:5.3 - Urgent Semantic Correction

A shared mapping incorrectly interprets a quantity's unit, and a supported interface can return a wrong answer. The authorized maintainer corrects or withdraws the affected mapping according to the community's rules, identifies the affected edition, and notifies its consumers. The notice explains the correction and the supported continuation.

The completed action is an urgent qualified correction with notification. Earlier users' unresolved reliance remains visible for SIE.11; the action cannot establish that every consumer has already migrated.

### SIE.12:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | A listed contact is treated as the owner of every semantic decision. | State content, release, dispute, communication, and source responsibilities at their actual remits. |
| Architecture | A single large model replaces useful local modules. | Start with the shared uses and retain local distinctions through scoped dependencies and correspondences. |
| Ontology/Epistemology | A stable label conceals a changed classification criterion. | Compare meanings and examples; keep earlier and replacement meaning identifiable. |
| Pragmatics | A small interface acquires unnecessary community machinery. | Complete the local agreement when that is the actual shared need. |
| Didactics | A version number is read as a guarantee of compatibility. | State the semantic basis and receiving scope of compatibility. |

### SIE.12:7 - Conformance Checklist

- [ ] Actual users and their shared-module reliance justify the arrangement.
- [ ] The shared scope and local extensions preserve the commitments they claim to use.
- [ ] Consumers can identify the model meaning, edition, access, and applicable dependencies.
- [ ] Proposal, content, release, dispute, contact, and source responsibilities are distinguishable where they matter.
- [ ] A material change has a usable decision and affected-consumer path.
- [ ] Identification, notice, migration, and deprecation follow the chosen rules and actual use consequences.
- [ ] A local interface can finish without creating an unnecessary commons.
- [ ] Unresolved rights or reliance limit the corresponding claimed arrangement.

### SIE.12:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Shared repository treated as governance | Establish the decisions and dependency conditions actual users need. |
| Contact metadata treated as decision authority | Identify who may decide content and releases and at what scope. |
| Silent meaning replacement | Expose the changed criterion, identification treatment, and consumer consequences. |
| Mandatory convergence of incompatible meanings | Retain scoped alternatives and the correspondences that are actually supported. |
| Announcement treated as completed migration | Distinguish notification from each affected consumer's result. |

### SIE.12:9 - Consequences

Shared modules can evolve while their users retain identifiable meanings and workable returns. Local development remains possible, and a community can decide changes without claiming authority outside its remit.

The arrangement costs maintenance, communication, and change assessment. Those costs increase with real dependency and participation. Some proposals remain local or unresolved when shared convergence cannot be justified.

### SIE.12:10 - Architectural Rationale

A commons is useful through the semantic commitments its users share and the decisions they can actually make. Module boundaries preserve the scope of those commitments. Identifiable meanings and dependencies let users determine how a change affects their work; assigned rights let the relevant participants act on that result.

### SIE.12:11 - SoTA-Echoing

The practice question is how the three independently governed organizations in §5.1 can change their shared equipment classification while keeping supported service queries interpretable. The selected line is a scoped shared core with separately maintained local modules, explicit dependencies, identifiable meanings, and assigned content and release rights. It adapts the [OBO Foundry principles](https://obofoundry.org/principles/fp-000-summary.html) to these actual users.

A serious alternative for these same users is a jointly qualified release bundle: publish the relevant shared core and local profiles as one identified, compatible combination. This also preserves source authority and can retain older supported editions. It offers one combination to qualify instead of asking every consumer to select compatible module editions; it need not impose a universal ontology.

| Arrangement for the same equipment-class change | Comparable effort and gain | Selection and accepted trade-off |
| --- | --- | --- |
| Shared core with independently maintained local modules | Examine the same changed criterion, equipment counterexamples, mappings, and receiving queries. Qualify the affected module interfaces and state the editions each supported use can combine. An unchanged local module can remain on its supported basis. | **Adapt** §4.1.2–3/5–7 and §5.1. Separate module maintenance preserves the participants' local distinctions and lets a scoped change proceed without constructing another joint bundle. It requires explicit dependency and compatibility evidence; independent version numbers alone are insufficient. |
| One jointly qualified bundle of the relevant core and profiles | Use the same meanings and cases and reuse unchanged component evidence, then qualify and identify the supported combination. Coordinate its release and continued support with the three participants. | Retain this alternative when consumers need a common deployment combination or the participants can qualify it more economically than separate compatibility claims. It simplifies edition selection but adds joint-release coordination, including when only one component changes. |

For §5.1's independently owned local classifications, the modular arrangement is selected to preserve useful local change and scoped reuse. The accepted cost is maintaining compatibility and reliance evidence at the module interfaces. A joint bundle may be better when the shared receiving use actually requires it; fewer files or a central release number cannot decide the comparison. A pair needing only one interface remains the distinct sufficient-agreement case in §5.2, not the rival used to justify this commons.

The source contributions change particular responsibilities:

| Source and role | Operative move and transfer limit |
| --- | --- |
| OBO Foundry principles supply the selected commons-practice line. | **Adapt** actual users, collaboration, modular reuse, and maintained access in §4.1.1–2/5/8. OBO participation criteria keep their community scope; they do not prescribe the release arrangement of these three organizations. |
| OBO [term stability](https://obofoundry.org/principles/fp-019-term-stability.html) constrains either arrangement. | **Adapt** §4.1.3/6 and §5.1 so a materially changed criterion remains distinguishable from the earlier meaning under the chosen identification rules. **Reject** silent replacement behind a familiar label. |
| OBO [contact responsibility](https://obofoundry.org/principles/fp-011-locus-of-authority.html) supplies a communication contribution. | **Adapt** §4.1.4/7 to a reachable contact and mediation path. Assign content and release rights separately; contact alone establishes neither. |
| OBO [change notice](https://obofoundry.org/principles/fp-013-notification.html) constrains continued reliance. | **Adapt** §4.1.6–7 to actual consumer action and the community agreement. A community-specific notice interval does not settle another commons' timing, and notification does not prove migration. |
| The public [ISO/IEC 21838-1](https://www.iso.org/standard/71954.html) scope supplies a possible common top-level basis. | **Adapt** §4.1.2 only when that basis contributes needed coherence. It decides neither module maintenance nor the release and versioning arrangement compared above. |

Reopen the arrangement comparison when one supported use requires a joint edition that separate compatibility claims cannot economically supply, when a mistaken module-dependency claim breaks a receiving query, or when changed participant rights prevent the selected release path. Reconsider the affected module combination and §4.1.3–7. A new local distinction alone does not require replacing the entire commons.

### SIE.12:12 - Relations

- SIE.3 develops or qualifies module content; SIE.4 establishes correspondences between different meanings.
- SIE.5 retains identifier authority and grain when identity is actually a premise.
- SIE.9 supplies the receiving interfaces that consume shared modules.
- SIE.11 follows material semantic change to affected results and users; SIE.10 supplies their integration validation.
- Domain authorities retain source meanings and claims. A.3.1.MI contributes Method introduction or revision when the community is changing how it works.

### SIE.12:End
