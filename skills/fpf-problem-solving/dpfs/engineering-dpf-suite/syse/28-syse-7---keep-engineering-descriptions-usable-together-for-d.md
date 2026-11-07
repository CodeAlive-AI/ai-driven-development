## SYSE.7 - Keep Engineering Descriptions Usable Together for Decisions

> **Status:** Stable

### SYSE.7:0 - Use This When

Use this pattern when an engineering decision depends on several description epistemes, but the project cannot
yet tell whether they concern the same subject, compatible configurations and intervals, mutually interpretable
claims, or the evidence needed by that decision.

The first useful move is to name one receiving decision and the claims that could change it.
For every description used by those claims, identify its subject, edition, reference scheme, intended use,
currentness, and the Work that relies on it. State a cross-description relation only when its participants and
meaning are recoverable.

The result is a **decision-bounded account of usable descriptions and their relations**: it names usable claims,
contradictions, unsupported correspondences, omitted claims, and refresh conditions. Its technical label is
`EngineeringDescriptionEnsembleAccount@Project`, a project-local `U.Episteme`. The account remains distinct
from the described engineered System, the descriptions it selects, their publication carriers, configuration
baselines, and evidence that their claims obtain.

Use a simpler description directly when one episteme already supports the decision and no material
cross-description claim is being made. Use `SYSE.10` when the problem is the credibility of an evidence source—for example, a model, experiment,
or trial—for a named engineering claim; use `SYSE.13`, `SYSE.14`, or `SYSE.19` when configuration identity,
change, release, or a changed source edition is the governing problem.

#### SYSE.7:0.1 - Terms and Distinctions

Words such as *model*, *view*, *specification*, *requirement*, *data*, *digital thread*, *digital twin*,
*traceability*, and *single source of truth* are recognition cues. Before relying on them, restore the
objects and relations that matter to the decision.

| Cue | Decision-usable interpretation in this pattern |
| --- | --- |
| description | One claim-bearing `U.Episteme` with a recoverable `EntityOfConcern`, claim content, effective reference scheme, edition, and current use. An expression or carrier—for example, a file, diagram, database row, screen, or spoken utterance—may carry it or be used in a publication occurrence; identify the episteme and publication relation separately. |
| model | A description episteme used under a stated modeling purpose, assumptions, omissions, interpretation, and validity boundary. Record these conditions independently of its executable, mathematical, visual, or tool form. |
| view | The same episteme individual qualifies as `U.View` only when a `U.Viewpoint` episteme and obtaining `EpistemeViewpointConformanceRelation` are present under `E.17.0`. Establish that membership through the conformance relation; presentation labels—for example, a page title, diagram type, dashboard face, or `viewpointRef`—remain publication cues. |
| viewpoint | A claim-bearing episteme specifying concerns and conformance rules for a view. A cue such as a stakeholder name, discipline label, screen layout, or familiar view list qualifies only when it supplies that content. |
| representation | A visible or formal expression used under an interpreted correspondence to an object, relation, claim, or mathematical structure. Diagrams, tables, queries, graphs, or executable files can serve this use when the correspondence is established. Ground performed Work through Agent–Work attribution, authority through its own relation, and depicted claims through evidence. Use `C.29` for a declared mathematical-lens use and its preserved and lost structure. |
| publication | An `E.24.PUB` publication occurrence with its form, carrier, audience, bounded use, and selected source edition when those identities matter. Ground the described world-side relation independently and use `E.17.0` when `U.View` membership matters. |
| engineering data | Claim-bearing epistemes and values used in engineering Work, together with the identities, editions, reference schemes, provenance, applicability, and relations needed by that use. Ground their world-side subjects separately. |
| trace or link | A recoverable direct relation: for example, a claim depends on a source claim; a test result assesses a named claim; an interface description concerns a selected configuration; or a change affects a configuration item. A hyperlink or same-name token is only an index until the intended relation and participants are stated. |
| digital thread | A maintained arrangement of description, source, configuration, change, publication, and use relations across named engineering Work. State its bounded use, participating relations, Agents assigned to maintenance Work, and currentness conditions instead of inferring them from one chain or repository. |
| digital twin | A selected description, model, data, automation, observation, and use arrangement concerning a named subject. Support every additional claim—for example, about System kind, fidelity, synchronization, beneficial use, or completeness—on its own grounds. |
| ensemble | The selected description epistemes and relations needed by one bounded set of decisions. This is an ordinary collective word. Identify each carrier and governing reference scheme independently. |
| consistency | A named set of claims can be jointly used under stated schemes, configurations, intervals, and tolerances. Establish it from claim content under those conditions; syntactic agreement, shared identifiers, and storage co-location are only comparison cues. |
| coherence | The selected claims and their correspondences support the receiving decision without an unresolved contradiction or missing distinction material to that use. Its scope is the named decision and material claims. |

Restore only the distinctions that can change the receiving decision.

### SYSE.7:1 - Problem Frame

Engineering decisions rarely depend on one self-sufficient description. A controller-architecture decision can
depend on a plant model and a sensor's component specification. These epistemes may concern different subjects,
scales, configurations, and intervals. They may use different reference schemes and intentionally omit
different characteristics.

The difficulty is not solved by putting every expression into one repository or by declaring one model
authoritative. Engineers need to know which claims support which decision, what each claim concerns, how a
cross-description comparison is warranted, and what world-side or evidence result would expose a mistake.
Otherwise a shared part number or generated link can be silently treated as identity and agreement.

Two symmetric failures recur.

1. **One-model overreach.** One favored description is expected to contain every useful engineering distinction.
   Its local ontology and omissions then become hidden project law.
2. **Unrelated-description accumulation.** Specialists maintain useful local epistemes but no one states their
   shared subjects, configuration applicability, interpretation, evidence, contradictions, or receiving
   decisions. The project has many artifacts and little joint decision support.

The general FPF distinctions support the applied engineering move between these failures: make descriptions
jointly usable for decisions about an engineered System and its affected Systems.

### SYSE.7:2 - Problem

A hidden gap in the description set can invalidate an engineering decision. Check whether the descriptions make
the following clear:


- the receiving decision and the claim that a description is expected to change;
- each claim's subject or intended referent, with its own identity and independently established kind;
- whether two descriptions concern the same individual, the same kind, related parts, successive
  configurations, or merely similarly named subjects;
- the reference scheme, scale, coordinate frame, units, tolerance, assumptions, omissions, and modeled interval;
- whether an alleged cross-description link is a representation correspondence, source dependency,
  configuration relation, transformation relation, evidence relation, or only a navigation aid;
- the edition and currentness of each source episteme and the Work that still relies on it;
- whether a diagram or simulation output describes a candidate, an intended configuration, an actual
  configuration, an observed occurrence, or a possible-future structure;
- which Agents produced, checked, changed, published, or use each result, through which Work and with what
  capability and authority;
- which contradiction, unsupported relation, or omitted characteristic blocks the next decision;
- what observation, configuration change, source change, or decision change requires refresh.

The result is often a false impression of precision. Every artifact may have an identifier and version while
the central engineering claim remains ambiguous. Automated trace generation can multiply this impression:
thousands of links exist, yet the project cannot say which direct relation each link records or which decision
would change if the linked claim failed.

### SYSE.7:3 - Forces

| Force | Tension to manage |
| --- | --- |
| Local specialist fitness and cross-specialist use | A local model should use the distinctions needed by its specialist Work; a receiving engineering decision still needs explicit correspondences and limits. |
| Maintenance burden and missing perspectives | Every additional description costs maintenance and collision checking; an omitted decision-changing claim can make the decision unsound. |
| Stable subject identity and changing configurations | Several epistemes may concern one enduring System while referring to different particulars—for example, parts, variants, versions, effectivities, or intervals. Recover the identity relation instead of relying on a shared name. |
| Human readability and machine-supported checking | Text and diagrams can reveal meaning to people; formal expressions and automation can expose selected contradictions. Warranted reliance still requires an explicit interpretation, completeness boundary, and world-side correspondence. |
| Executable model and physical result | Simulation and generated code can shorten feedback; they can also reproduce shared assumptions and omit physical effects. |
| Shared model and federated descriptions | One common model can reduce translation for a bounded use; independently maintained descriptions can preserve needed expertise and authority. Choose from the receiving decision and the losses of each arrangement. |
| Current decision and future reuse | General data structures can enable later use; speculative completeness can delay the present decision and preserve obsolete distinctions. |
| Publication convenience and epistemic identity | Several epistemes can share a carrier, with their publication relations identified separately; one episteme can appear through several publication forms. Carrier consolidation leaves claim content and editions distinct. |
| AI-assisted production and warranted reliance | AI Systems can produce candidate descriptions quickly. The outputs still need recoverable sources, subjects, error checks, and decision-specific acceptance. |
| Standards compatibility and present practice | Standards supply useful distinctions and exchange constraints. Treat conformance, official publication, and academic visibility as evidence of declared content; assess practical adoption, effectiveness, and current engineering Methods separately. |

### SYSE.7:4 - Solution

Maintain the current engineering description epistemes needed by the receiving decisions,
and make every material cross-description use explicit. Select descriptions from decisions and Work. Existing
document inventories, notations, process presentations, and tool repositories are candidate sources rather than
the selection rule.

Start with the project's existing descriptions and review results. Reuse results that still apply to the
receiving decision and whose subjects, editions and interpretations remain recoverable. When a material claim
lacks that basis, recover or establish the missing comparison through :4.1 and keep the usable results for
unaffected claims. This work can remain within the existing data-management arrangement.

#### SYSE.7:4.1 - Perform the Move

1. **Name the receiving decision and its decision-changing claims.** State the decision, decision subject,
   intended use, project focus, current option set, and the claims for which a changed value, contradiction, or
   evidence result could change the choice.
2. **Recover each described subject.** For every needed claim, identify its subject or intended referent and
   retain its independently established kind. A description of an engineered System concerns that System;
   a description of a selected organization of relations concerns a `U.Structure`. Distinguish an individual
   from its kind, one selected structure from another, and an actual configuration from a possible-future
   candidate.
3. **Select the description uses.** Choose the description epistemes needed for those claims,
   and state each description's use.
4. **Identify each episteme and expression.** Record claim content, `EntityOfConcern`, effective reference
   scheme, edition, source, provenance, modeled interval or effectivity, assumptions, omissions, and relying
   Work. Separately identify any material expression or publication object when its identity changes use.
5. **State interpretation and model-use conditions.** As needed by the decision, name conditions such as units,
   coordinate frames, scales, tolerances, abstractions, parameter sources, boundary conditions, solvers or
   inference procedures, and validation limits. State the project's interpretation separately from language rules
   and tool capabilities.
6. **Recover cross-description relations.** For every material link, state its participants and relation:
   same subject under different schemes; part or interface correspondence; claim dependency; source derivation;
   configuration applicability; transformation from one expression to another; test-to-claim assessment; or
   another direct relation. If the project lacks a governed relation kind or evidence for that claim, record an unsupported
   correspondence rather than inventing a generic trace edge.
7. **Check collisions at the claim level.** Compare claims only after subject, configuration, interval, scheme,
   scale, and tolerance are aligned or their differences are explicit. Classify the result as agreement for the
   bounded use, an explainable difference, an unresolved contradiction, a missing interpretation, or a missing
   world-side check.
8. **Check correspondence to realization and observation.** Identify which claims describe candidates or
   intentions and which concern actual configurations or occurrences. Connect design claims to relevant
   observations—for example, from realization, integration, trials, commissioning, operation, or affected
   Systems—through their evidence
   and configuration relations. Do not let description-to-description consistency substitute for physical
   adequacy.
9. **Choose publication forms for actual users.** Publish only the forms needed by the receiving Work and its
   users. Reuse or author a viewpoint only when `U.View` membership and conformance matter. Keep the source
   episteme, view, publication occurrence, form, carrier, and audience use separate.
10. **Arrange maintenance when continued reliance needs it.** For the affected entries, identify the Agent
    assigned to change a description, decide a contested interpretation, accept a cross-description relation,
    or stop reliance, together with the needed capability and authority. Specify the observations that call for
    refresh and the Work that will update the affected account.
11. **Return the bounded result.** Make the usable claims, contradictions, unsupported correspondences, gaps,
    reliance limits, and refresh conditions available to the named engineering decisions and dependent Work.

Description production, realization, checking, operation, and decision Work can overlap. Comparing claims still
requires recoverable claim content and subjects.

#### SYSE.7:4.2 - Record the Result

Keep a compact `EngineeringDescriptionEnsembleAccount@Project` for the receiving decision. Reuse applicable
existing results that supply the content below; add only what is missing or must change. It is a project-local episteme;
the FPF kinds of its participants remain unchanged.

| Field | Required content |
| --- | --- |
| receiving decision | Decision, decision subject, intended use, interval, and downstream Work that will use the result. |
| decision-changing claims | Claims whose value, contradiction, evidence, or absence can change the decision. |
| description entries | For each episteme: source and edition, claim content, `EntityOfConcern`, reference scheme, configuration/effectivity, modeled interval, assumptions, omissions, and relying Work. |
| expression and publication entries | Material expressions, publication occurrences, forms, and carriers whose identities change use; identify each separately from the source episteme. |
| model-use conditions | Purpose, scale, units, coordinates, tolerances, boundary conditions, parameter sources, interpretation, calculation or inference Method, and validity limits needed by this use. |
| relations | Direct same-subject, part, interface, configuration, source, transformation, evidence, or other governed relations; unsupported correspondence hypotheses are marked as such. |
| collision results | Claim-level agreements, explainable differences, unresolved contradictions, missing interpretations, and missing world-side checks. |
| realization correspondence | Actual configuration or occurrence, observation/evidence basis, and the decision claim it can confirm, weaken, or reopen. |
| maintenance assignments, when needed | For continued uses needing maintenance, the assigned Agents, their system-role assignments, authority, capability, Work, and acceptance conditions for producing, checking, changing, or retiring description uses. |
| return and refresh | Receiving Work and the Agents assigned to it, accepted reliance limits, current gaps, triggering observations, and the affected accounts or decisions to reconsider. |

The account can use existing publication forms. Its identity and sufficiency do not depend on one storage
technology.

#### SYSE.7:4.3 - What Changes in Practice

Engineers stop asking whether documentation or “the model” is complete. They ask whether the current
description ensemble can support a named decision without hiding a subject mismatch, configuration mismatch,
interpretation gap, contradiction, or unsupported world-side claim.

The Agent performing modeling Work enacts the Method; modeling tools are resources. Ground decision authority
and warranted reliance on modeling results through their own relations. Traceability becomes a collection of
testable relations rather than a link count.
A digital thread is a maintained arrangement for named engineering uses. Use
the local label *digital twin* only when its selected subject, descriptions, automation, observations, and use
are stated.

The account includes conditions for reconsideration. A change to, for example, a configuration, source edition,
environment, model assumption, trial result, or receiving decision can call for refresh. The assigned Agent then
refreshes the affected claims and relations. Unaffected descriptions remain usable under their stated conditions.

### SYSE.7:5 - Worked Case: Controller Architecture Description Ensemble

The project is preparing evidence for a controller-architecture decision: whether plant configuration `HP-2`
should use direct compressor modulation alone or modulation coordinated with thermal storage over the next three
heating seasons. The plant, use, configuration, and decision focus are the same across the selected inputs.
Outside-use, functional, and bearer descriptions already exist, but the decision-changing claims remain
distributed across several descriptions. The engineering team constructs this bounded account:

| Entry | Subject and use | Material interpretation or relation |
| --- | --- | --- |
| use and operating-scenario episteme | The intended heat-pump plant in occupied-building use; supplies temperature, noise, maintenance, power-price, and grid-response situations. | Scenarios are possible use descriptions, not performed operation or test evidence. |
| functional-organization episteme | Candidate control organization: demand estimation, compressor modulation, storage dispatch, limit protection, and fault handling. | Treat the listed elements as functions until separate bearer and realization relations assign them to controller modules or software processes. |
| bearer-and-interface account | Candidate controller hardware, plant sensors, actuator connections, storage valve, communication interfaces, and allocations. | Names candidate Systems, physical interface specifications, and many-to-many function allocations for the decision. |
| equation-based plant model | Thermal plant and storage behavior under selected boundary conditions. | [Modelica](https://modelica.org/projects/language/) equations describe one selected physical abstraction; solver output is not observed plant behavior. |
| controller state and timing description | Control states, transitions, sampling assumptions, fallback conditions, and actuator commands. | The description concerns intended controller behavior and must correspond to the hardware timing and sensor claims. |
| component and wiring records | Sensor variants, controller I/O, update rates, error bounds, cable and connector configurations. | Catalogue claims apply only to component variants and conditions. |
| bench and commissioning results | Observations from controller-in-the-loop Work and later installed-plant trials. | Engineers use `SYSE.10` to qualify which engineering claims those results support and `SYSE.13` to keep tested configurations explicit. |

A collision check finds that the plant simulation and controller description assume a two-hertz supply-water
temperature update with an error bound of plus or minus 0.1 kelvin. The currently selected procurement variant
is specified only for a half-hertz update and plus or minus 0.3 kelvin under the installed cable length and
filtering arrangement. Matching the token `SupplyTemperatureSensor` across three tools had hidden the
difference.

The engineers recover the sensor variant and interface configuration instead of merely synchronizing names.
They update the model-use assumptions, evaluate another component and estimator option, and perform a
controller-in-the-loop trial. The resulting evidence revises the architecture comparison: direct modulation
remains acceptable for one building profile, while the storage branch remains unselected until it has either the
faster sensing configuration or a different estimator and the corresponding assurance result. This evidence
informs the current decision; it does not approve a later storage increment.

The account records the usable description editions, the unresolved estimator claim, the tested
configuration, and a reconsideration condition tied to component substitution or a changed grid-response
requirement. Controller, procurement, integration, configuration, and assurance Work use different publication
forms over recoverable source epistemes while the decision-changing relations remain explicit. The result stays
bounded to this decision.

If the data-management review already distinguishes the sensor variants and relates the model assumptions to
the selected variant, the engineers reuse that result. When procurement later substitutes a variant, they
reconsider the affected timing and error claims and the dependent architecture branch. Unchanged descriptions
and qualified earlier results keep their stated applicability.

An AI System also produces a proposed cross-description summary and candidate correspondence list. Those
outputs are new epistemes produced by performed Work. They are checked against source editions and
accepted only where the relation and participants are recoverable. The generated confidence score supplies
neither an evidence relation nor authority to alter the architecture decision.

### SYSE.7:6 - Bias Annotation

This pattern resists four recurrent source and practice biases.

- **Artifact bias.** Sources such as standards, university curricula, tool vendors, and process descriptions
  often organize engineering around named documents or model kinds. The pattern preserves useful distinctions but begins from
  current decisions and Work.
- **Official-model bias.** A heavily published source—for example, a normative language, standard, ontology,
  or repository—may have limited or ceremonial use in projects. Official publication establishes scope and declared
  capability; assess practical adoption, beneficial use, shared interpretation, and current SoTA separately.
- **Software-transfer bias.** Software practices such as executable models, generated links, continuous
  integration, and automated checks can be valuable. Physical concerns—for example, realization, supply, installation, calibration, environmental
  exposure, or operating evidence—remain distinct and may require slower or destructive checks.
- **Academic-evidence bias.** A bounded study—for example, a prototype consistency checker, digital-twin
  mapping study, or one case—can sharpen a Method without establishing broad industrial effectiveness. Use the
  best available expert judgment with a stated epistemic status when comparative field evidence is unavailable;
  do not demand an unaffordable prevalence study or upgrade publicity to use evidence.

### SYSE.7:7 - Conformance Checklist

- [ ] One receiving engineering decision, its decision subject, and the decision Work are named.
- [ ] Applicable existing results are reused with recoverable interpretations and returns to the decision;
      added content answers a material gap.
- [ ] Every selected description has a source episteme and edition, claim content, `EntityOfConcern`,
      effective reference scheme, configuration or effectivity where material, modeled interval, and use.
- [ ] Each claim's subject or intended referent is identified without merging distinct subjects or kinds by name.
- [ ] Model purpose, assumptions, omissions, scale, units, tolerances, and interpretation are sufficient for the
      receiving decision.
- [ ] A `U.View` claim cites a viewpoint episteme and obtaining E.17.0 conformance; otherwise *view* stays
      ordinary source wording.
- [ ] Publication occurrence, form, carrier, rendering, and source episteme remain separate where their
      identities change reliance.
- [ ] Every material “trace” is resolved to a relation or marked as an unsupported correspondence.
- [ ] Cross-description comparison aligns or explicitly distinguishes subject, configuration, interval,
      reference scheme, scale, and tolerance.
- [ ] Claims about physical realization, benefit, safety, compliance, and acceptance use their own evidence;
      description consistency supplies only its stated comparison result.
- [ ] AI-generated, transformed, or summarized descriptions retain source provenance, subjects, check
      results, and reliance limits.
- [ ] For continued uses needing maintenance, the Agent, assignment, capability, authority, triggering
      observations, and refresh Work are stated for the affected entries.

- [ ] The returned account names contradictions, gaps, unsupported relations, accepted reliance limits, and the
      affected decisions or accounts to reconsider.

### SYSE.7:8 - Common Failures and Repairs


| Failure | Repair |
| --- | --- |
| Start from a compulsory document or view list | Start from the receiving decisions and decision-changing claims; add a description only when its use changes Work or reliance. |
| Treat one repository as one model | Recover each claim-bearing episteme, source edition, subject, scheme, and use independently of storage co-location. |
| Treat same names as same subjects | Resolve actual identity, kind, part, configuration, interval, and designation separately. |
| Count links as traceability | For each material link, name its participants, relation, relying decision, and failure consequence. |
| Call every publication face a view | Apply `E.17.0` only when `U.View` membership matters; otherwise name the publication form and bounded use plainly. |
| Let a simulation stand for the plant | State the modeled subject, assumptions, validity boundary, and evidence needed for the physical claim under `SYSE.10`. |
| Freeze one baseline as lifecycle truth | Keep configuration and effectivity under `SYSE.13`; refresh affected claims and relations when the world or source changes. |
| Demand one shared ontology | Use a shared scheme only where its benefits exceed lost specialist distinctions; otherwise maintain explicit correspondences and unresolved differences. |
| Create a digital twin by label | Name the selected subject, description/model set, automation, observations, current use, evidence, and maintenance Work; drop the label if it changes nothing. |
| Accept generated correspondence by confidence score | Treat it as a candidate episteme; inspect sources, subjects, relation, exceptions, and decision consequence. |
| Let specialists exchange files without a receiving use | Use `SYSE.9` to state the requested professional contribution, receiving decision, acceptance condition, and result to return. |
| Make the pattern or account act | Name the Agent, Method, and performed Work; epistemes describe, support, or constrain through use relations. |

### SYSE.7:9 - Consequences

**Benefits.** Decisions can use several specialist descriptions with their different boundaries intact.
Contradictions identify affected claims and decisions. Model, configuration, and evidence changes reopen bounded uses
rather than the whole project. Publication can be tailored to actual readers without changing source claims.
Automation can check more relations because the relation kinds and subjects are explicit.

**Costs.** Engineers must maintain subject identity, editions, interpretation, configuration applicability,
and selected correspondences. Some attractive links will remain unsupported. Specialists must expose enough of
their assumptions for the receiving decision, and the integration team must understand where formal checks stop.

**Risks.** The account can itself grow into a master-model bureaucracy. Require a receiving decision for each
maintained entry. Stop maintaining an entry when no current or required future use depends on that work.
Aggressive minimization can omit a slow feedback channel; ask what decision would become unsound if the
omitted claim failed.

### SYSE.7:10 - Rationale

An engineering decision can need claims from descriptions with different purposes and omissions. Preserving
their subjects and configuration applicability keeps the comparison about the intended case. Exposing conflicts and connecting
candidate and intended descriptions to evidence from actual realization and operation turns gaps into questions
for the engineering Work that can change the System or revise the decision.

The ensemble is decision-bounded because no description is complete for every use. The same plant can require
different selected structures and representations for control design and maintenance. Choose and relate
descriptions by the claims that must be jointly usable now.

### SYSE.7:11 - SoTA and Source Use

**Working question.** Once engineering descriptions are available and controlled, what further work makes
their claims usable together for one decision? The selected answer is an authored combination: retain adequate
data-management arrangements, then establish only the missing claim-level interpretation and applicability.
Keep that result available to the decision and to the changes that can defeat it.

[NASA's Technical Data Management treatment, §§6.6.1.2–6.6.1.3](https://www.nasa.gov/reference/6-6-technical-data-management/)
is a serious alternative. It selects needed data, addresses adequacy and consistent use, defines exchange
conventions and responsibilities, and weighs acquisition burden. It also permits existing contractor arrangements
when they meet project requirements. **Adopt** that selection and reuse principle. A tailored implementation may
already provide all the content review this decision needs. Retain an applicable result whose claim interpretation,
configuration basis and receiving use remain recoverable.

For a concrete comparison, give both approaches the HP-2 inputs in :5 and engineers able to interpret the sensor
specifications and control-model assumptions. Either can discover the conflict between the assumed two-hertz,
0.1-kelvin bound and the selected variant's half-hertz, 0.3-kelvin bound. Controlled exchange alone leaves that
conflict unresolved. Where the existing review already connects those claims to the selected variant and the
architecture choice, :4 and :4.2 reuse it. Where that connection is missing, :4.1 moves 4–8 recover the
interpretation, test the correspondence and return the unsupported architecture claim. The additional useful
result is a recoverable reason for limiting the storage branch and reconsidering it after sensor substitution,
as :5 demonstrates. This is a conditional benefit of the added comparison, not a claim that NASA's process
precludes such a check.

Both arrangements need the specialist interpretation. This pattern additionally asks that the material
correspondence, applicability and return remain recoverable. Accept the work of recording and maintaining them
when dependent decisions or changes would otherwise require reconstruction or risk reusing the wrong result.
For a one-off decision, a short explanation in its existing record may suffice. A maintained shared account earns
its cost through actual relying Work; stop maintaining entries under :9 when that work is no longer needed. Total effort depends on how often the
result is reused and how often its basis changes.

A shared semantic model is another serious alternative when recurring exchanges justify the conversion and
maintenance. The [landing-gear case in Wu et al. (2025)](https://doi.org/10.1016/j.aei.2025.103490) combines shared
model semantics, conflict handling, traceability and versioning. **Adapt** that joint treatment in :4.1 moves
4, 6 and 10. Use an existing common model when it retains the distinctions needed by the decision; use explicit
correspondences between specialist descriptions when conversion would lose a needed distinction or cost more
than maintaining those correspondences. For HP-2, either arrangement must preserve the sensor variant and its
timing and error bounds. **Reject** shared names or storage co-location as substitutes for that relation.
The case supplies a feasible arrangement, not evidence that one architecture wins across domains.

**Bound the reliance on each comparison.** [Riedmaier et al. (2021), §§2.5 and 7](https://doi.org/10.1007/s11831-020-09473-7)
distinguish validated conditions from the intended model application and examine uncertainty: **adopt** that
distinction in :4.1 moves 5 and 8. [Schwarzburg, Trauer and Rebentisch (2024), §§5.2–5.3](https://doi.org/10.1017/dsj.2024.14)
examine model history, competence, access and decision risk: **adapt** these as questions for a consequential
unresolved reliance under `SYSE.10`, without importing an exploratory confidence score as an acceptance threshold.
The study's small non-probability sample cannot establish comparative industrial effectiveness.
These sources limit what either data arrangement can warrant: internally consistent claims still need a
qualified basis for the physical use.

For optional AI assistance, **adapt** the task-specific allocation proposed by
[Pradas Gomez et al. (2025), §§4–5](https://www.cambridge.org/core/journals/proceedings-of-the-design-society/article/team-of-three-the-role-of-generative-ai-in-the-development-of-design-automation-systems-for-complex-products/2DB8CA17B63C63EA1C0C57F349769C7E).
In :5, the AI System proposes correspondences; the assigned engineers check their sources and implications
before accepting reliance. Tools remain resources under :4.3. The source offers a conceptual model for choosing
contributions; its survey and literature review do not demonstrate this HP-2 arrangement's effectiveness or
confer decision authority.

**Reconsider the choice** when a material relation cannot be recovered before use, a changed configuration or
source defeats its applicability, or a different arrangement supplies the same needed distinctions with less
total work. Reopen the affected claims and return them under :4.1 move 11 and :4.3. A credibility gap goes to
`SYSE.10`; a configuration-identity gap goes to `SYSE.13`; a changed description used by Work returns through
`SYSE.19`. Preserve the usable remainder. This is also the limit on :12's return to `SYSE.6`: only an account
applicable to the same architecture decision, configuration and horizon can inform it.



### SYSE.7:12 - Relations

- `C.2.1` supplies episteme identity, `EntityOfConcern`, effective reference scheme, and edition discipline.
- `C.2.P.DR` repairs declarative-representation overread; `C.29` applies only when a mathematical-lens use and
  its explicit correspondence, preserved structure, loss, and stop condition are current.
- `E.17.0` supplies the dependent `U.View` membership and viewpoint-conformance relation; `E.17` and
  `E.24.PUB` keep selected episteme, publication occurrence, form, carrier, reader, and use distinct.
- `A.6.3.RT` governs a representation-scheme transition when the same `EntityOfConcern` is deliberately
  redescribed; it does not establish world-side identity or the correctness of the receiving claims.
- `A.10`, `B.3`, and `G.11` govern evidence reliance, assurance, and source-edition currentness. `SYSE.10`
  specializes the return from research, models, and trials to engineering decisions.
- `E.15`, `C.27`, `SYSE.13`, `SYSE.14`, and `SYSE.19` govern configuration continuity, temporal claims, change,
  release, and revalidation when those are the current problems.
- A compatible `SYSE.1` result can supply the scope and intended-result frame for the same subject and decision.
  It does not prescribe Work order. If it does not fit, use a qualified direct source or record the missing
  result. Descriptions remain governed by their own subject patterns.
- `SYSE.7` supplies evidence to `SYSE.6` only when the account can change the same architecture decision at the
  same configuration and horizon. The account neither authorizes nor entails that decision. If the account
  cannot serve the use—for example, because it is unavailable, stale, outside scope, or incompatible—`SYSE.6`
  uses a qualified direct source or records that missing result.
- `SYSE.7` supplies a MethodDescription or representation input to `SYSE.19` only for the named receiving use.
  Description order or conformance does not establish Method order or effectiveness. If the account
  cannot serve the use—for example, because it is unavailable, stale, outside scope, or incompatible—`SYSE.19`
  uses a qualified direct source or records that missing result.
- When the current problem is requesting and accepting a professional contribution, apply `SYSE.9` to that
  result and receiving decision. When neighboring Work needs a description, its governing pattern uses the source
  episteme through its own subject, configuration, evidence, and use relations. The Agent performing that Work
  applies its governing Method, and the Work produces its own result for the named receiving use.
- Engineering profiles may require different description Methods when their subjects, formalisms, evidence,
  and realization relations change the working move.

### SYSE.7:End
