## SIE.3 - Construct or Reuse a Semantic Model for a Named Use

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `UseFitSemanticModel@Use`: a reused, extended, or constructed semantic model qualified for the questions and distinctions that its receiving use requires.

### SIE.3:1 - Problem Frame

**Use this when** an integration needs to express a meaning or answer a question and the adequacy of its available models is unsettled. For example, a source describes an inspection requirement, while the receiving query needs to distinguish that requirement from an observation of a particular configured feature.

Start with one question the model must help answer and examples of answers that would count as different. Ask the domain participants to explain those distinctions before choosing an encoding. The first useful result can be confirmation that an existing model is sufficient, with its applicable edition and use conditions.

The object is the semantic model for that use: its concepts, relation meanings, constraints, and relevant commitments. The practical gain is a model whose distinctions can guide correspondence and mapping work. A stronger claim, such as adequacy for additional questions or valid inference in a formal language, needs evidence for those additional conditions.

If the supplied model is already qualified for the unchanged use, reuse that result. If the only open question is a correspondence between adequately understood source meanings, use SIE.4. A new integration endpoint alone does not create a model-construction requirement.

### SIE.3:2 - Problem

Available models often look adequate because their terms resemble the receiving question. A field named `inspection` may cover a plan, a requirement, an occurrence, or a result. Mapping every such field to one class can remove exactly the distinction the receiver needs.

The opposite failure is to construct a larger ontology whenever a model question arises. That incurs design and maintenance work even when an existing model can answer the question. Both failures begin before formalization: the required meaning and its useful boundary have not been established.

### SIE.3:3 - Forces

| Force | Tension |
| --- | --- |
| Reuse | Existing meanings and tools save work, while an unrecognized gap can invalidate the receiving answer. |
| Domain understanding | Participants know their practice, while familiar words can hide different concepts, grains, or temporal commitments. |
| Expressiveness | Richer formalization can support useful inference, while its cost and restrictions may exceed the use. |
| Modularity | An extension can preserve reusable content, while incompatible commitments may require a different model. |
| Maintenance | Consumers need a stable reference, while the domain and its required questions can change. |

### SIE.3:4 - Solution

Select or develop only the semantic content needed for the named use. Qualify it through discriminating cases and make its maintained edition accessible to the consumers who will rely on it.

#### SIE.3:4.1 - Pattern-Use Unfolding

1. **State the questions and answer distinctions.** Use competency questions or an equivalent plain description. Name the subject, grain, configuration or interval where relevant, expected answer, and a counterexample. Work with domain participants at a level where they can explain the distinction. Separate a useful model question from a request to choose a storage or diagramming tool.
2. **Recover the available meanings.** Use the relevant SIE.2 results or directly supplied source meanings. Inspect candidate models' definitions, relations, constraints, examples, edition, access, and maintenance conditions where those can affect the use. Source labels alone cannot settle suitability.
3. **Try sufficient reuse.** Replay the required questions and counterexamples against an available model. When its content and applicable conditions suffice, return that model and the qualification. This completes the Method. Leave an uncovered question explicit if a permitted narrower use can continue.
4. **Locate the actual gap.** Identify the missing distinction, relation, constraint, or incompatible commitment. Extend a module when the addition can preserve the existing commitments that consumers still use. Construct a different model when reuse or such an extension cannot supply the required content. Keep the reason tied to the gap.
5. **Develop the meaning before encoding it.** Define the needed concepts and relations, their domains of application, and the grain or temporal interpretation required by the question. Show examples and counterexamples to domain participants. Preserve a source disagreement that affects use; SIE.4 can establish a qualified correspondence between different meanings.
6. **Choose sufficient formalization.** A maintained vocabulary and relation description can be enough for some uses. Select a formal language or profile when exchange, constraints, or inference require its semantics. Check the properties claimed under that choice as well as the domain cases. Repair or qualify a model that passes an encoding check but answers the domain question incorrectly.
7. **Return a maintained, use-qualified model.** Identify the edition or stable content, covered questions, material limits, and the access and maintenance arrangement its consumers need. Return its meanings to correspondence or mapping work and its cases and qualifications to validation. A missing authoritative definition can leave one question unresolved while independently supported questions finish.

A small model can express these obligations in one short maintained description. Formalization adds the assurance required by the selected language and use. It does not change which domain question the model must answer.

#### SIE.3:4.2 - Record the Result

| Result position | Content needed by the receiver |
| --- | --- |
| Named use | Questions, expected answer distinctions, and applicable subject, grain, time, or configuration. |
| Selected model | Reused model or developed module, its edition, definitions, relation meanings, and required commitments. |
| Reuse or development decision | The adequacy evidence, or the gap that justified an extension or different model. |
| Qualification | Covered cases, counterexamples, limits, unresolved questions, and any selected formal checks. |
| Continued reliance | Access, maintenance responsibility, relied-on source conditions, and change conditions that can reopen the result. |

The result can refer to an existing qualified model instead of reproducing it. Record a reason only where it helps a consumer interpret or rely on the selection.

#### SIE.3:4.3 - What Changes in Practice

The integrator can explain why the model distinguishes two answers, or why an existing distinction is sufficient. A mapping author receives meanings and cases rather than an unexplained class list. Model construction becomes a response to a demonstrated gap.

### SIE.3:5 - Archetypal Grounding

#### SIE.3:5.1 - Reuse for Provider Availability

The receiving interface returns separately attributed provider quantities. Its questions are “How much is on hand now?” and “How much can this provider promise under its reservation and time-horizon rules?”

An available model already distinguishes both measures, their provider, unit, observation time, and relevant horizon. The integrator checks the following cases:

| Case | Required model interpretation |
| --- | --- |
| Provider A reports 12 on hand; provider B reports 9 available to promise. | Two qualified quantities with distinct measure meanings. |
| Both values happen to equal 12. | Numerical equality does not remove the difference between the measures. |
| The provider changes the promise horizon. | The horizon remains part of the promise meaning used by the receiver. |

The model represents these cases and has suitable access and maintenance conditions. The completed result references that edition for the two questions. It supplies no common quantity formed by adding the values; that operation would require a separately justified receiving meaning.

#### SIE.3:5.2 - Extend an Inspection Model

A constructed product-definition and inspection integration asks: “What observation concerns requirement Q for feature F in configuration R?” The source model already describes the feature and its requirement, but represents no actual observation.

| Model content | Development and case |
| --- | --- |
| Existing feature and requirement | Reuse their qualified definitions and configuration applicability. |
| Observation | Add the actual observation as distinct from its plan and the requirement being checked. |
| Observation relation | State which configured feature and applicable requirement it concerns. |
| Unit and time | Express the interpretation required for this observation and question. |
| Counterexamples | A planned inspection is not an observation; an observation of another configuration does not answer this question. |

The domain participants confirm those distinctions and identify any unresolved source-specific interpretation. The module can then supply SIE.4 and SIE.7 with the required meanings. In an AP242/QIF installation, its actual profiles, configuration relations, and inspection meanings must come from the qualified source results; the constructed model above is the working example, not a claim about a particular exchange's conformance.

### SIE.3:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | One participant's preferred vocabulary silently becomes the shared meaning. | Obtain the meanings needed by the receiving use and preserve unresolved authority or source disagreement. |
| Architecture | A platform choice determines the model's concepts. | State the questions and distinctions before selecting formalization or realization. |
| Ontology/Epistemology | Requirement, plan, observation, and result collapse because they share a label. | Use a counterexample that changes the receiving answer. |
| Pragmatics | A new ontology is built despite adequate reusable content. | Try the existing model and finish when the use is supported. |
| Didactics | A formal diagram appears sufficient without a working example. | Show how the model answers the question and excludes its counterexample. |

### SIE.3:7 - Conformance Checklist

- [ ] The receiving questions and material answer distinctions are recoverable.
- [ ] Available model content is compared with those questions before development is selected.
- [ ] Sufficient reuse can complete the result.
- [ ] Developed content answers an identified gap and preserves relied-on commitments or qualifies the affected use.
- [ ] Domain examples and counterexamples support the claimed scope.
- [ ] Formal checks match the selected encoding and claimed inference or exchange use.
- [ ] The receiver can identify and access the maintained model and its limits.

### SIE.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Model from familiar labels | Recover relation meanings and replay a discriminating question. |
| Construction as proof of progress | Return adequate existing content when the use is already supported. |
| Hidden repair in a transformation rule | Develop the missing semantic distinction and give the rule a qualified premise. |
| Language validity used as domain adequacy | Check the domain answer as well as the selected formal properties. |

### SIE.3:9 - Consequences

A qualified model makes correspondence and mapping decisions more explicit and reusable. Small integrations can finish with a small model. Extensions expose their actual commitments to later consumers.

The work costs domain conversation, example construction, and any formal checks the chosen use requires. Some questions remain unresolved until a source owner supplies a needed meaning. Larger scope creates additional content and maintenance obligations.

### SIE.3:10 - Architectural Rationale

Questions and counterexamples locate the distinctions that an integration must preserve. Reuse is therefore judged by its contribution to the question; extension is justified by a specific gap. Keeping model content, its maintained edition, its formal encoding, and its instances distinct makes both adequacy and later change easier to assess.

### SIE.3:11 - SoTA-Echoing

The practice question is how to settle an available model's adequacy for the receiving questions when that adequacy is still unknown. For the inspection question in §5.2, the selected starting line is requirements-led model qualification: recover the distinction between requirement, plan, and observation, try the available meanings, and develop only the gap that survives that trial. This adapts [LOT](https://doi.org/10.1016/j.engappai.2022.104755) and its [maintained resources](https://github.com/oeg-upm/LOT-resources).

A serious alternative for that same unsettled question is to develop the model together with a small knowledge-graph prototype, adapting the ontology-and-graph work described by [LOT4KG](https://lot.linkeddata.es/LOT4KG/). The prototype can reveal a missing relation when the receiving query is executed. Compare a bounded prototype with bounded model qualification, rather than charging it for a complete production platform:

| Answer to the same inspection-model question | Comparable work and useful evidence | Choice and accepted trade-off |
| --- | --- | --- |
| Qualify or extend the model before selecting its realization | Examine the required definitions with domain participants and replay the requirement/plan/observation, configuration, unit, and time cases. Keep the model and cases sufficient for that query. | **Adapt** LOT in §4.1.1–5 and §5.2. This settles the semantic distinction without choosing graph encoding or query machinery. It supplies no evidence that an executable mapping or query is correct; SIE.7 and SIE.10 still need that evidence for their own claims. |
| Qualify the model through a small graph and executable query | Examine the same definitions and cases, then encode representative instances and the query. This adds encoding and execution work but can expose errors that a prose-only model trial misses. | **Adapt** the LOT4KG route when execution can settle an uncertainty material to model adequacy, especially when graph realization is already selected. In §5.2, the first unresolved issue is what counts as an observation; executing a query over a class that also includes plans cannot settle that domain meaning. The model-first route is selected for that issue, accepting deferred execution evidence. |

The comparison is qualitative and scoped to the same questions and counterexamples; it is not a claim that one route is always cheaper or more effective. A prototype's additional effort earns its place when it can change the qualification. Neither route can replace domain meaning with successful execution.

The remaining contributions constrain that choice:

| Source and comparison role | Operative move and limit |
| --- | --- |
| LOT supplies the selected requirements, development, publication, and maintenance line. | **Adopt** domain questions and participant validation; **adapt** §4.1.3 and §4.1.7 so sufficient reuse can finish and the receiver can rely on a maintained model. The source does not decide local meanings or establish this model's adequacy. |
| LOT4KG supplies the coupled ontology/graph alternative. | **Adapt** its separation of ontology work and graph construction to the comparison above; **reject** treating graph construction as the only way to qualify a model. Its described activities support this alternative, not a measured superiority claim. |
| [OWL 2 Overview](https://www.w3.org/TR/owl2-overview/) supplies language and profile choices when formal semantics matter. | **Adapt** §4.1.6: check the properties actually claimed for the chosen language as well as the domain cases. Encoding validity cannot replace the model-adequacy question. |
| The public [ISO/IEC 21838-1](https://www.iso.org/standard/71954.html) scope supplies a possible top-level basis. | **Adapt** §4.1.2/6 only when that basis contributes needed coherence. It establishes neither a universal upper-ontology requirement nor local maintenance and versioning rules. |

Reopen the comparison if one required answer depends on a selected query or inference behavior that the model-only trial cannot settle, if a bounded prototype exposes a missed distinction, or if an available model can now answer the same cases with less qualification work. Return only to the affected question and §4.1.2–6. An already qualified model for an unchanged use remains the sufficient direct result in §4.1.3.

### SIE.3:12 - Relations

- SIE.1 supplies the receiving question, preserved distinctions, and permitted scope.
- SIE.2 supplies source meanings and identifies model gaps.
- SIE.4 uses model meanings to establish qualified correspondences; SIE.7 uses them in executable mappings.
- SIE.10 validates the integration's claimed receiving result using the relevant model qualification.
- SIE.11 follows a changed model premise to affected uses. SIE.12 supplies shared-module arrangements when an actual commons requires them.
- FPF terminology, kind, relation, and evidence guidance constrains the corresponding model claims; domain participants supply the problem-specific meanings.

### SIE.3:End
