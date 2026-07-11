## E.4.FPF - First Principles Framework Form and Publication-or-Access Carrier Assembly

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative.

### E.4.FPF:1 - Problem frame

Use this pattern when an FPF steward, framework author, reviewer, or AI agent must treat FPF itself as one framework edition rather than as only a file, a table of contents, a pile of patterns, a DPF, or a set of helper tools.

Primary `EntityOfConcern`: `FirstPrinciplesFrameworkEdition@Context`, the scoped FPF edition as a transdisciplinary first-principles framework. The first useful output is an FPF form map: first-principles scope, selected Core pattern set, cross-domain problem-situation and solution-move architecture, publication or access carriers, relation and edition records, quality route through `E.2.DA`, and blocked overreads.

Use this when the work changes or assembles README, Preface, ToC, `FPF-Spec.md`, extracted hosts, first-entry views, skill packs, MCP-backed access services, or other carriers of FPF itself. Use `E.4.DPF` instead when the framework is a domain or local framework grounded in FPF. Use `E.4` when the live question is only family placement and routing among framework members.

The practical payoff is simple: a reader can say "this is the FPF edition, these are its user-facing carriers, these are its access routes, this is how whole-FPF adequacy is evaluated, and this is why a DPF or local framework may depend on it without becoming it."

### E.4.FPF:2 - Problem

After DPF and local-framework publication forms become explicit, FPF itself can fall into the opposite omission: DPF packages get careful carrier, relation, naming, quality, and refresh rules, while FPF is treated as if its form were self-evident because it is "the main spec".

That creates several failures:

- `FPF-Spec.md`, README, Preface, ToC, host files, cards, skills, or MCP routes are mistaken for the FPF edition itself;
- FPF is described as one more DPF, losing the first-principles and transdisciplinary burden that makes DPFs possible;
- whole-FPF quality is checked by local pattern scores, landing status, or DPF package scales instead of `E.2.DA`;
- adoption carriers grow user-facing explanations that quietly become shadow authority beside governing patterns;
- skill or MCP access makes FPF look like a callable service, tool permission layer, or runtime dependency rather than a framework edition exposed through an access carrier.

The repair is not to copy `E.4.DPF` under another name. FPF needs its own form rule because its burden is different: it must keep first-principles distinctions usable across domains while allowing domain and local frameworks to grow from it.

### E.4.FPF:3 - Forces

| Force | Tension |
|---|---|
| First principles vs domain knowledge | FPF must carry transdisciplinary ontology, epistemology, evidence, architecture, decision, work, publication, and improvement distinctions without becoming a doctrine of one domain. |
| Public adoption vs governing authority | README, Preface, examples, cards, skills, and MCP access must help new users without becoming a second spec. |
| Core stability vs evolution | FPF needs stable dependability for downstream DPFs, while the framework remains open to new patterns, better terminology, and source-front movement. |
| Pattern-set quality vs whole-framework quality | Individual `E.21` results matter, but they do not equal whole-FPF Pillar adequacy. |
| Carrier plurality vs identity | The same FPF edition can be exposed as monolith, host set, split docs, cards, skill pack, MCP-backed service, or retrieval route; those carriers must not create several competing FPFs. |
| Access convenience vs architecture clarity | A callable access route can make FPF easier to use while hiding edition, currentness, source, and authority boundaries. |

### E.4.FPF:4 - Solution

Treat FPF as a `FirstPrinciplesFrameworkEdition`: a transdisciplinary framework edition whose selected Core pattern set, first-principles scope, cross-domain problem-situation and solution-move architecture, relation records, and publication or access carriers are distinct but coordinated. FPF patterns render recurring first-principles problem architectures and reusable solution moves in pattern-language form; the carriers expose that rendering without becoming the framework edition itself.

Use these local names:

| Local name | Kind and use |
|---|---|
| `FirstPrinciplesFrameworkEdition` | One scoped FPF edition carrying transdisciplinary first-principles distinctions and the Core pattern set that downstream frameworks depend on. |
| `FPFCorePatternSet` | The selected governing pattern set for the edition. It is not the same kind as README, Preface, ToC, skill pack, or MCP route. |
| `FPFPublicationCarrier` | Reader-facing carrier such as `FPF-Spec.md`, README, Preface, ToC, extracted host set, reviewable bundle, card set, or split documentation that publishes selected FPF content. |
| `FPFAccessCarrier` | User-facing or agent-facing access carrier such as a skill pack, MCP-backed access service, retrieval route, assistant integration, or search or index carrier. It exposes FPF; it is not FPF architecture, source authority, quality proof, runtime dependency, or work permission by itself. |
| `FPFFormMap` | Context record naming edition, Core set, carriers, relation records, quality route, currentness route, and blocked overreads. |
| `FPFLevelAdequacyRoute` | Whole-FPF adequacy route through `E.2.DA`; individual pattern quality still uses `E.21`, and DRR quality still uses `E.9.DA`. |

Create the FPF form map with this shape when FPF itself is being assembled, republished, exposed, or evaluated:

```text
FPFFormMap@Context:
  firstPrinciplesFrameworkEditionRef: <FPF edition named by value>
  firstPrinciplesScopeRef: <transdisciplinary scope and non-domain boundary>
  selectedCorePatternSetRefs: <governing pattern set or selected host or monolith slice>
  selectedFirstPrinciplesProblemSituationRefs: <recurring cross-domain problem situations and forces rendered by the edition>
  selectedFirstPrinciplesSolutionMoveRefs: <reusable solution moves, consequences, and repair routes rendered by the edition>
  selectedPublicationCarrierRefs: <README | Preface | ToC | FPF-Spec | hosts | cards | bundle | split docs>
  selectedAccessCarrierRefs: <skill pack | MCP route | retrieval route | assistant integration | other access carrier>
  relationAndEditionRefs: <E.4.PFR records, edition pins, dependency boundaries>
  firstEntryAndProjectionRefs: <E.11, E.17, I.2, README, Preface, and ToC projection loci>
  publicationSelfRenderingRefs: <README | Preface | ToC statements of reader, selected first-principles structures, deliberate coarsening, abstraction, omission, deferral, and return to governing patterns>
  qualityAndImprovementRefs: <E.2.DA for FPF-level adequacy; E.21, E.23, and E.9.DA as evidence or local routes>
  currentnessAndRefreshRefs: <G.11 and source and currentness owners>
  blockedOverreadRefs: <carrier-as-framework | DPF-as-FPF | access-route-as-authority | local-quality-as-whole-FPF>
```

The ordinary method is:

1. Name the scoped FPF edition by value: current monolith edition, selected host set, release candidate, or whole-FPF edition.
2. State the first-principles scope: FPF supplies transdisciplinary distinctions that can be reused across domains, not a domain doctrine and not an encyclopedia of all domains.
3. Identify the selected Core pattern set and any companion or projection loci that expose it.
4. Separate publication carriers from access carriers. A README, Preface, ToC, monolith, host set, card deck, skill pack, MCP route, retrieval route, or assistant integration is a carrier, not the framework edition itself.
5. Record relation, dependency, edition, deprecation, supersession, publication, and access relations through `E.4.PFR`.
6. Keep downstream direction clear: DPFs and local practice frameworks may depend on FPF Core; FPF Core does not depend on them except by a deliberate Core amendment decision.
7. For whole-FPF adequacy, use `E.2.DA` over the scoped FPF object and declared use. Use `E.21` for individual pattern bodies, `E.9.DA` for DRR, and `E.4.DPF.DA` only for DPF or local-framework packages.
8. For first-entry and reader-facing exposure, use `E.11` and `E.17`; keep their projection text thin enough that governing pattern authority remains in the patterns.
9. Make the FPF readme, Preface, and ToC structure-account-aware: they should state the reader and use they serve, which first-principles structures they foreground, what they deliberately coarsen, abstract, omit, or defer, and where the reader returns for governing pattern detail. This protects adoption text from becoming a second spec while still telling readers what FPF is about.
10. For source-front, currentness, and refresh claims, use `G.2` and `G.11`; do not let a publication carrier become source-currentness proof.
11. For skill packs or MCP-backed access, expose edition identity, dependency boundary, and currentness or refusal conditions. Generated candidate text goes to `C.35`; tool and work claims go to `A.15` and local tool or work owners; assurance, evidence, and decision authority go to their direct owners.
Use this quick routing test:

| Live question | Use |
|---|---|
| "What is the form of FPF itself, and how are its carriers separated from the framework edition?" | `E.4.FPF` |
| "Does this whole-FPF object realize the Pillars for a declared use?" | `E.2.DA` |
| "How do FPF, a DPF, and a local framework depend on one another?" | `E.4` and `E.4.PFR` |
| "How do we author a domain or local framework grounded in FPF?" | `E.4.DPF` |
| "Is this DPF package good enough for one declared domain or local use?" | `E.4.DPF.DA` |
| "Is this individual pattern body good enough?" | `E.21` |
| "How do new users find and read FPF?" | `E.11` and `E.17` |

### E.4.FPF:5 - Archetypal Grounding

Tell: A release pass updates README, Preface, ToC, several host files, and `FPF-Spec.md` after architecture and DPF campaigns. The FPF form map names one scoped FPF edition, lists the Core pattern set and carriers, records which entry text is only projection, and runs `E.2.DA` for whole-FPF adequacy. It does not say that README or Preface is the framework itself.

Show: A domain principle framework for any one practice depends on FPF Core and may cite architecture, representation, precision, and improvement patterns from FPF. It is a DPF publication or access carrier for one domain or practice. Its package adequacy uses `E.4.DPF.DA`; it does not define the FPF Core and does not make FPF a framework for that domain.

Show: An FPF skill pack exposes pattern lookup, first-entry guidance, and short-use prompts. The skill manifest carries access metadata. It can say which FPF edition it exposes and when to refresh, but a tool call, endpoint schema, or retrieval result is not FPF authority unless the retrieved governing pattern and edition are named.

Mini-map:

| Field | Filled slice |
|---|---|
| `firstPrinciplesFrameworkEditionRef` | `FPF@June2026SelectedHostEdition` |
| `firstPrinciplesScopeRef` | transdisciplinary ontology, epistemology, decision, evidence, architecture, work, publication, and improvement distinctions |
| `selectedCorePatternSetRefs` | selected Core hosts and monolith sections |
| `selectedFirstPrinciplesProblemSituationRefs` | cross-domain problem situations where meaning, evidence, description, architecture, work, decision, publication, or improvement claims collapse |
| `selectedFirstPrinciplesSolutionMoveRefs` | reusable pattern-language moves that separate kinds, recover source, route owners, compare options, publish views, and improve claims |
| `publicationStructureAccountRefs` | README and Preface statements of intended reader, selected first-principles route, deliberately coarsened, abstracted, omitted, or deferred structures, and return to pattern bodies |
| `selectedPublicationCarrierRefs` | README, Preface, ToC, `FPF-Spec.md`, extracted host set |
| `selectedAccessCarrierRefs` | optional FPF skill pack or MCP-backed retrieval route |
| `qualityAndImprovementRefs` | `E.2.DA` for whole-FPF adequacy, `E.21` for pattern bodies, `E.23` for improvement cycles |
| `blockedOverreadRefs` | README-as-spec, skill-as-framework, DPF-as-FPF, local-score-as-whole-FPF |

### E.4.FPF:6 - Bias annotation

This pattern biases FPF stewardship toward explicit framework form. That is useful when adoption carriers multiply, but it can become bureaucracy if every small wording fix is forced through a whole-FPF form map.

Use the pattern when FPF-level form, carriers, access, edition, or whole-FPF adequacy is live. Do not invoke it for one local sentence repair unless that repair changes how FPF itself is published, found, accessed, depended on, or evaluated.

### E.4.FPF:7 - Conformance checklist

| Check | Passing condition |
|---|---|
| CC-FPF.1 Edition named | The scoped FPF edition or selected FPF object is named by value. |
| CC-FPF.2 First-principles scope explicit | The text states that FPF is transdisciplinary first-principles material, including cross-domain problem-situation and solution-move architecture, not a domain or local framework. |
| CC-FPF.3 Core and carriers separated | Core pattern set, publication carriers, access carriers, relation records, source and currentness records, and quality records remain distinct. |
| CC-FPF.4 Dependency direction protected | DPFs and local frameworks may depend on FPF Core; reverse dependency requires a deliberate Core amendment. |
| CC-FPF.5 Quality route correct | Whole-FPF adequacy uses `E.2.DA`; individual patterns use `E.21`; DPF packages use `E.4.DPF.DA`; DRR uses `E.9.DA`. |
| CC-FPF.6 Publication thinness preserved | README, Preface, ToC, cards, and other projection carriers help entry without becoming semantic authority beside governing patterns. |
| CC-FPF.7 Access carrier bounded | Skill packs, MCP routes, retrieval, and assistant integrations expose edition identity, currentness, and refusal conditions without becoming framework authority, runtime dependency, or work permission. |
| CC-FPF.8 Refresh route visible | Source-front, edition, entry-use, currentness, and evaluation changes have receiving owners such as `G.2`, `G.11`, `E.2.DA`, `E.21`, or direct pattern owners. |
| CC-FPF.9 Carrier structure-account boundary visible | README, Preface, ToC, or equivalent FPF carrier states what first-principles route its publication expression tells, for which reader and use, what it deliberately coarsens, abstracts, omits, or defers, and where governing pattern detail resumes. |

### E.4.FPF:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
|---|---|---|
| FPF as one DPF | FPF is treated as a domain package, so its first-principles and transdisciplinary burden disappears. | Use `E.4.FPF` for FPF form and `E.4.DPF` only for domain or local dependents. |
| Carrier as FPF | README, Preface, ToC, monolith, host set, card deck, skill pack, or MCP route is treated as the framework edition itself. | Record carriers in `FPFFormMap`; route authority to Core pattern set and relation and edition owners. |
| Invisible FPF entry route | README or Preface helps adoption but never says what first-principles structures it foregrounds, what it leaves to the pattern bodies, or who it is written for. | Add a carrier structure-account statement while preserving thin publication-carrier status. |
| Whole-FPF quality by local score | Good `E.21` values or successful landing are treated as whole-FPF adequacy. | Run `E.2.DA` for the scoped FPF object and declared use; use local results only as evidence loci. |
| DPF reverse dependency | A good DPF discovery is treated as a hidden Core dependency. | Return it through a Core amendment decision and direct pattern owners before FPF depends on it. |
| Access route as authority | A skill, MCP endpoint, retrieval index, or assistant integration is read as source, decision, work, or currentness authority. | Keep it as an access carrier; route generated text, tool work, evidence, assurance, and refresh claims to their direct owners. |

### E.4.FPF:9 - Consequences

FPF adoption becomes easier to reproduce because authors can build README, Preface, ToC, monolith, host, skill, MCP, and retrieval carriers without changing what FPF is.

The cost is one extra distinction for stewards: whole-FPF form is not the same problem as DPF authoring, package adequacy, individual pattern quality, or first-entry publication. That cost is acceptable because those problems have different evidence and failure modes.

### E.4.FPF:10 - Rationale

FPF is structurally close to a principle framework, but it is not a DPF. Its domain is not hydroponics, narrativization, architecture review, or enterprise practice. Its burden is to carry first-principles distinctions that can seed and discipline many domain and local frameworks.

That makes FPF form a real architecture concern. If carriers and access routes are not separated from the framework edition, adoption work can silently create new authorities. If DPF scales are reused for FPF, the evaluation asks the wrong question. If whole-FPF adequacy is reduced to local pattern quality, the corpus can become locally polished and globally weaker.

### E.4.FPF:11 - SoTA-Echoing

| Claim | Exact source ref and status | Pattern locus changed | Adoption status |
|---|---|---|---|
| Architecture descriptions and publication forms must not be confused with the architecture or governed object. | `ISO/IEC/IEEE 42010:2022, Software, systems and enterprise - Architecture description`, official current standard ref already used by `E.4`. | `Solution` separates FPF edition, Core pattern set, publication carriers, and access carriers. | Adopt separation and correspondence discipline; adapt it to FPF framework-form stewardship. |
| Reusable core assets need variation and dependency discipline across a family. | Nazar, `Software Product Line Engineering: Adoption, Tooling and AI Era Challenges`, arXiv:2605.21353, 2026 survey already used by `E.4`. | Dependency direction from FPF Core to DPF or local dependents is made a checklist item. | Adopt reusable-core discipline; reject software-product feature-model ontology as universal FPF architecture. |
| Whole-language adequacy is not an average of local pattern quality. | `E.2.DA`, `E.21`, `E.22`, and `E.23` internal FPF evaluation lineage. | `Solution` routes whole-FPF evaluation to `E.2.DA` and pattern-body evaluation to `E.21`. | Adopt the object-under-improvement split; block all-`5` or landing-status substitutes. |
| Access carriers need currentness and authority boundaries. | `E.11`, `E.17`, `G.11`, `C.35`, and `A.15` internal FPF publication, refresh, generated-carrier, and work-role lines. | Skill and MCP access is named as access carrier, not authority or work permission. | Adopt explicit access-carrier limits; route stronger claims to direct owners. |

### E.4.FPF:12 - Relations

- **Specializes:** `E.4` for the case where the framework family member under form work is FPF itself.
- **Builds on:** `E.2` Pillars through `E.2.DA` for whole-FPF adequacy.
- **Coordinates with:** `E.4.PFR` for relation, edition, dependency, publication, access, deprecation, and supersession records.
- **Coordinates with:** `E.4.DPF` and `E.4.DPF.DA` as sibling patterns for domain and local frameworks, not as FPF-level substitutes.
- **Coordinates with:** `E.11`, `E.17`, and `I.2` for first-entry, projection, and publication carriers.
- **Coordinates with:** `G.2`, `G.11`, `C.33`, `C.34`, and `C.35` for source, currentness, structural preservation, and generated or transformed carriers.
- **Coordinates with:** `E.21`, `E.22`, `E.23`, and `E.9.DA` when individual pattern quality, evaluation framing, improvement loops, or DRR adequacy provide evidence for FPF-level changes.

### E.4.FPF:End

