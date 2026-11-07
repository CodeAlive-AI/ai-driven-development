## SYSE.13 - Establish Configuration Identity, Variants, and Effectivity

> **Status:** Stable

### SYSE.13:0 - Use This When

Use this pattern when an engineering decision depends on an actual System's identity and configuration or on a
description's applicability—for example, which physical unit has which part and installed software, or which
description edition applies to that unit—but records reuse a label such as a part number, version, baseline,
release, or status as if it answered all of those questions.

Begin with the receiving decision and the actual Systems whose differences can change it. Select only the
configuration-item boundaries needed for that decision. Restore every distinction used by the case—for example,
actual units, product-family variants, software packages and installed realizations, description editions,
reference baselines, or effectivity. Then state the supported correspondences that allow one record to be used
with another.

The first useful result is a **decision-specific configuration basis**: an episteme that tells an engineer which
actual units and descriptions can be used for one decision, where each claim applies, which collisions or gaps
remain, and what later change reopens it. The actual Systems and configurations are its subjects; descriptions
carry its claims; evidence supports them; and release decisions and performed Work remain separately identified.
Use the governing FPF pattern directly when one identity, structure, characteristic, edition, or temporal claim
already answers the question. Use `SYSE.7` when several descriptions must be made jointly usable, `SYSE.14` when a proposed or
performed change must be connected to release, and `SYSE.19` when a changed source may reopen earlier decisions.

#### SYSE.13:0.1 - Terms and Distinctions

| Name in this pattern | What it denotes |
| --- | --- |
| actual configuration | The decision-relevant actual constituents, obtaining relations, and characteristic values of one identified actual System over an interval. A configuration description carries claims about that configuration; a database value or dashboard status is not the configured System. |
| configuration item | A decision-local designation of an already identified entity whose separate identity, parthood where relevant, and change matter to the receiving decision. The entity may be, for example, a System, physical part, software-package episteme, or description episteme. The designation creates no universal kind. |
| physical or serial unit | One actual System individual. Its part number, family description, bill of material, variant name, and status record are separate descriptions or claims. |
| product family | A stated grouping of actual Systems or possible-future System referents under a classification and variation scheme. The current claim must say whether it concerns a kind, set, lineage, or description. |
| variant | A combination of design or configuration claims, normally carried by a description and possibly realized by actual units. A variant label does not prove realization. |
| software package and installed realization | In this pattern, a package or build episteme specifies software content. The content installed in a unit and its actual operation in that unit are separate world-side facts whose correspondence to the package needs evidence. |
| description edition | One episteme related to an earlier edition only under an edition-continuity relation. A changed filename, timestamp, or revision number is insufficient. |
| baseline | A selected reference episteme or claim set used for one comparison. Actual configuration, evidential support, authority, and release require their own claims or decisions. |
| effectivity | A claim that a description, change, release, or configuration claim applies to identified subjects and conditions—for example, Systems, serial units, lots, sites, intervals, operating conditions, or a stated combination. A date alone is insufficient when the subject or condition is unknown. |
| status | A claim or decision value about a subject for a use and interval. A value such as *approved*, *released*, *installed*, or *current* in one tool does not establish the corresponding world-side fact. |
| comparison labels such as *as-designed*, *as-realized*, *as-integrated*, or *as-maintained* | Source terms for local comparison roles of configurations and descriptions. Recover the role used by the decision; the label imposes no lifecycle and guarantees no correspondence. |

Record a performance account when the receiving question depends on which Work occurred, how it was performed
or who was responsible for it. Include the performer, assignment and Method only as needed to support that claim.
Keep preparation of the configuration basis distinct from the receiving decision when different Agents have
those responsibilities.

### SYSE.13:1 - Problem Frame

Continuing engineering keeps several configurations relevant at once—for example, candidate architectures,
manufactured variants, installed software realizations, experimental units, or service replacements. Engineering,
manufacturing, operating, and maintenance descriptions can also differ. Each kind of receiving Work may need
different item boundaries.

Shared identifiers and records—whether kept in a product-data system, a bill of material, linked-model
infrastructure, or a naming standard—do not remove the semantic problem. These resources can preserve identifiers
and links, while engineers still decide what each identifier denotes, which differences matter to the decision,
and what evidence connects the record to the actual System. One label can hide incompatible granularity;
different labels can denote the same unit under different schemes.

### SYSE.13:2 - Problem

A decision-specific configuration basis answers eight questions:

1. Which actual or intended subject does the decision concern—for example, a System, part, serial unit, lot,
   or site?
2. Which boundaries need independent identity for this decision, and why?
3. For each identifier, which reference scheme gives it meaning, which Agent issues or maintains it, over what
   interval, and in which record?
4. Which variant and software-package claims are candidates, and which actual units have evidence of realizing
   them?
5. Which constituents and relations obtain for each unit and interval, and which characteristic values are
   supported—for example, installed realizations or parameter values?
6. To which subjects and conditions does each description or change apply—for example, units, lots, sites,
   intervals, or operating conditions?
7. What does each cross-tool mapping preserve or lose, what evidence supports it, and is that loss acceptable for
   receiving Work such as build, integration, release, operation, service, or modernization?
8. Which Agent can settle a disputed identity or mapping, which receiving Work relies on the answer, and what
   change reopens it?

Without those answers, every local record can be internally consistent while the engineering decision is wrong.
Firmware can fit one board variant and fail another; an engineering bill of material can disagree with an
installed unit; a release can name the right part number but omit the units to which it applies.

### SYSE.13:3 - Forces

Recurring tensions include:

- A change can preserve or end an entity's identity; reusing its earlier label settles neither case.
- Design, manufacturing, integration, operation, and maintenance need different item boundaries, while receiving
  Work needs supported mappings among them.
- Family descriptions enable reuse; release, service, and failure decisions often depend on serial units and
  installed configurations.
- Extra fields and links cost maintenance, while one omitted unit, edition, condition, or correspondence can
  invalidate the choice.
- Several descriptions can agree with each other and still be wrong about the actual System.
- Automated comparison exposes differences among identifiers, bills, hashes, and editions quickly. Engineers
  still determine the intended referent, applicability, and acceptable loss.
- A selected reference basis aids comparison while experimental, installed, and service configurations can
  legitimately coexist.

### SYSE.13:4 - Solution

Develop a configuration basis sufficient for the engineering decision to distinguish actual Systems,
variants, descriptions and applicability; include the burden of maintaining it in that choice.

Use an established configuration-management arrangement directly when its records, supported mappings and
verification already answer the receiving question. A query or existing report can supply the whole basis.
When something is missing, name the claim that cannot yet be supported and construct only the needed addition.
For example, reconcile two differently organized bills for one comparison, or qualify the time over which an
inspection supports an installed-state claim.

Compare a checked manual reconciliation with maintaining a reusable mapping when either could supply that
addition. Use the same subjects, claim and period for both; include checking, correction and later maintenance
work. A one-off question can justify the manual result, while recurring use can justify maintaining the relation.
Keep the result in the existing account when it can carry the required meaning and evidence.

Use [the record-and-time explanation](38-syse-13---establish-configuration-identity-variants-and-effe.md#syse1344---use-a-record-for-one-configuration-dependent-claim) when the correspondence is unfamiliar; continue with an adequate existing basis when it is already established.

#### SYSE.13:4.1 - Perform the Move

1. **Name the decision and differences that matter.** State the deciding Agent, question, use, project
   System-of-interest or other subject, interval, and configuration differences that can change the result. Do not
   begin by inventorying everything.
2. **Identify actual and intended subjects.** Name every subject needed by the decision—for example, an actual
   unit, part, site, or possible-future referent. State needed part–whole and structure relations; a product code
   or bill-of-material row is not the bearer.
3. **Choose item boundaries for this use.** Designate only the entities that must be distinguished independently,
   such as Systems, parts, software-package epistemes, or descriptions. Different kinds of receiving Work may
   choose different boundaries; relate them instead of forcing one granularity.
4. **State identifier schemes and mappings.** For each item, name the identifier, scheme, issuing or maintaining
   Agent, interval, and supported mapping to another scheme. Shared spelling is not identity; a mapping need not
   be symmetric or lossless.
5. **Separate variants, units, packages, installations, and editions.** Name the variant description, actual units
   claimed to realize it, software package, observed installed realization, and description edition. Mark
   unsupported realization claims as gaps.
6. **State actual configuration and effectivity.** Name the actual constituents, obtaining relations, and
   characteristic values needed by the decision—for example, parts, interfaces, installed software, or parameter
   values. State the supporting evidence and interval, then name the subjects and conditions to which every
   description or change applies. Keep candidate and intended configurations modal.
7. **Choose a baseline only for comparison.** Identify the reference episteme and its decision. Keep it unchanged
   for that comparison; establish actual configuration and decision authority separately.
8. **Check collisions and return the basis.** Align bearer, boundary, scheme, edition, interval, and tolerance
   before comparing. Classify each problem by the action it requires—for example, repair an actual
   incompatibility, reconcile contradictory descriptions, qualify a lossy mapping, obtain missing evidence, or
   accept a harmless naming difference. State receiving Work, the Agent with revision authority, blockers, and
   the conditions for reconsidering the affected claims.

Identification, design, realization, integration, observation, and change Work may overlap. Receiving Work can
rely only on claims whose bearer and effectivity are known for that use.

#### SYSE.13:4.2 - Record the Result

| Field | Required content |
| --- | --- |
| receiving use | Decision, deciding Agent, actual System or intended System referent selected as the project system-of-interest, or another subject, interval, affected Work, and differences that can change the result. |
| subjects and item boundaries | Actual Systems, serial units, parts, or sites; possible-future referents where needed; selected item designations; rationale; and needed part–whole or structure claims. |
| identifiers and mappings | Schemes, issuing or maintaining Agents, intervals, directional mappings, preserved meaning, losses, evidence, and use limits. |
| variants, units, software, and descriptions | Candidate variant descriptions, actual-unit realization claims, software packages, installed realizations, description editions, and unresolved gaps. |
| configuration and effectivity | Actual constituents, obtaining relations, characteristic values, supporting evidence, and interval; subjects and conditions to which each description or change applies. |
| reference and collisions | Optional baseline and purpose; incompatible actual elements, contradictory claims, unsupported or lossy mappings, missing evidence, and harmless naming differences. |
| maintenance and return | Agents and authority for revision, receiving Work, reliance limits, blockers, and conditions for reconsidering the affected claims. |

The basis may be published in a form such as text, a table, a product-data query, a model view, or a generated
report.

#### SYSE.13:4.3 - What Changes in Practice

Engineers ask whether the current configuration basis distinguishes the units, variants, descriptions, and
conditions needed by the decision. Product-family reuse remains available,
while release and service claims become serial-unit and effectivity aware.

Tools may expose a mismatch without deciding what it means. Engineers resolve collisions that can change
the decision and leave unrelated inventory alone. When a source changes, reconsider the affected claims;
retain the reference baseline for its stated comparison.

#### SYSE.13:4.4 - Use a record for one configuration-dependent claim

Use this explanation when you can work with the records of your practice but are unsure which state, event or period a record supports. Start with the claim your present decision needs. An adequate established correspondence can be used directly.

Name the actual or intended subject of the record and the subject of the decision. Recover the description edition, identifier scheme and conditions when they can change this use. A common name or a later date does not establish the correspondence. Keep an installed state distinct from a design, plan or status entry. Different identifiers can be harmless when their supported mapping preserves the subject needed by the decision.

**Distinguish three questions about time.** When was the record made or the account entered? When did the reported state or event actually obtain? At what time, or over what interval, must the claim needed by the decision apply? The answers can coincide, but one answer does not establish the others. Recover only the distinctions needed by your claim.

An entry date helps recover the history of an account. Use evidence of installation to establish or bound when it occurred. A quotation has its own subject and conditions: it can be written before installation yet cover the subsequently installed configuration, or be written later and still cover a different configuration. Its issue date does not establish the period for which its terms apply.

Place the relevant states and events on the interval the decision concerns. Attach an observation to the supported state at its observation time. To use that observation over a longer interval, identify the grounds for that extension. Split an interval at a configuration change that affects the claim. Keep unsupported parts qualified.

When a later record supplies a supported correction of the earlier account, revise the affected correspondence and retain the earlier account as history. Entry of that correction is not another physical installation. When the sources do not settle the state or event, return the uncertainty to the receiving decision.

##### SYSE.13:4.4.1 - When the change time is uncertain

Suppose the evidence supports an earlier state, a later state and exactly one transition between them, but bounds its time τ only by `a ≤ τ ≤ b`. The case treats the transition as one boundary: from τ onward the state is the later one. Before a the earlier state is supported; from b onward the later state is supported. At times in `[a,b)`, a claim that depends on which state obtained remains conditional unless further evidence settles it. Additional transitions, reversals or gaps require a different history.

Apply the receiving calculation or decision to the admissible event times. Retain conclusions that remain supported across them. Qualify the parts that change and obtain a worthwhile observation or source answer that could settle the receiving question. A midpoint is an estimate only when there are grounds to use it; it is not a recovered event time.

Quantities calculated from the same unknown event can vary together. If one component leaves when another enters and this is the only replacement in a continuously operating window `[u,v)`, their durations are `τ−u` and `v−τ`; their sum is `v−u` for every admissible τ. For `τ∈[8,10]` in `[6,12)`, the paired durations include `(2,4)`, `(3,3)` and `(4,2)`: the total is always 6. Combining both separate maxima would describe no admissible history. Stops, different duty or another exposure measure require the receiving practice's own calculation.

**Return to your task.** Bring back the supported correspondence, its time limits and remaining uncertainty. Explain which record supports which claim and which changed fact would change the answer. Use the receiving method to decide whether a gap matters, which further result is worth obtaining and which subject-specific evidence or permission is still needed. Retain unrelated usable results.

If you came from [EAM.3's first use (EAM.3:4.1)](../../management-dpf-suite/eam/12-eam-3---establish-the-asset-information-and-configuration-ba.md#eam341---first-use-with-two-quotations), return to its quotation task and discussion. If you came from [MNT.12's first use (MNT.12:4.1)](../mnt/23-mnt-12---maintain-maintenance-information-and-configuration.md#mnt1241---first-use-with-a-replacement-history), return to its event and exposure task. Otherwise return to the decision you named at the start.

### SYSE.13:5 - Worked Case: Pump-Controller Variants and Ten Installed Units

A pump manufacturer is deciding which of ten installed controllers may receive a cold-start protection change.
The first export gives all ten the same product number and the status *current*. Inspection results and source
records show four different decision-relevant groups:

| Installed units | Observed configuration | Effect on the release decision |
| --- | --- | --- |
| S001–S004 | Input board IO-A and the older installed firmware realization. | Outside the candidate firmware package's hardware compatibility claim. |
| S005 | Input board IO-B and temperature sensor TS-2, but no current sensor calibration evidence. | Possible candidate after calibration evidence; not currently eligible. |
| S006–S008 | IO-B, TS-2, current calibration evidence, and an installed realization corresponding to the supported firmware lineage. | May enter the current release comparison, subject to installation and verification Work. |
| S009–S010 | IO-B and TS-2; the database says *installed*, but current calibration evidence is absent. | Possible candidates after the missing evidence is obtained; status alone is insufficient. |

The candidate firmware package is an episteme describing support for IO-B. It is not the software realization
currently executing in any controller. Installation and observation are needed before that correspondence can be
claimed.

A query of a competent CM arrangement could return these groups with their evidence and applicability; that
would be sufficient for this configuration question. Here the existing records supply the unit and inspection
facts, but the export does not supply the correspondence between the two bills of material. The engineer
compares checking that correspondence once with maintaining a reusable relation for later queries. For this
one-off ten-unit comparison, the team accepts the manual checking effort and keeps the checked correspondence
with its existing change account. It does not undertake continuing mapping maintenance without a use that
justifies it. Both alternatives still need the same calibration and installation evidence.

The engineering and manufacturing bills of material use different item boundaries. The checked directional
mapping relates the engineering board item to the manufacturing board-and-harness items. It loses
installation-routing detail and cannot be used in reverse without another check. A changed bill or later
reuse therefore needs its applicability checked. The engineer does not designate every fastener or database
row as a configuration item because those differences cannot change this release.

The effectivity proposal names S006–S008, the supported operating-temperature conditions, the candidate package
edition, and the required installation and verification Work. S001–S004 are excluded; S005 and S009–S010 retain
explicit evidence gaps. A selected reference configuration supports comparison but does not claim that every
installed unit realizes it.

The configuration basis can inform `SYSE.14` and bound the integration Work in `SYSE.11`. It establishes neither
installation, permission, release, nor successful operation. A changed board, sensor, package edition,
calibration source, inspection, or release question reopens only the affected unit and correspondence claims.

**When the full pattern is unnecessary.** If a laboratory engineer needs only to know whether one already
identified controller contains IO-B at the current inspection time, direct System, structure, temporal, and
evidence patterns answer the question. A product-family configuration basis adds no value.

### SYSE.13:6 - Bias Annotation

Document-control practice can make the record or baseline appear more real than the physical unit.
Software-centred records can hide installed hardware and effectivity; hardware-centred records can collapse
software packages and description editions into part numbers. Start with actual Systems and the receiving
decision.

A signal such as an official identifier, required form, vendor schema, digital-thread label, or declared
conformance status supports only the claim it actually records; actual project use and configuration
correspondence require their own evidence. Use expert judgment with an explicit
epistemic status when broad field evidence is unavailable.

### SYSE.13:7 - Conformance Checklist

- [ ] One receiving decision and the configuration differences that can change it are stated.
- [ ] Each actual System and part has its own identity; descriptions, identifiers, records, and status claims have
      their own bearers.
- [ ] Every configuration-item boundary has a decision-specific reason.
- [ ] Product-family variants, actual units, software packages, installed realizations, and description editions
      remain distinct.
- [ ] Each load-bearing effectivity claim names the units or lots, sites, intervals, and conditions required by
      the use.
- [ ] Cross-scheme mappings state direction, preserved meaning, loss, evidence, and use limits.
- [ ] Any baseline serves the stated comparison; configuration claims carry their evidence limits; a required
      release or permission is distinguished from performed installation.
- [ ] The basis records collisions, unsupported correspondences, missing evidence, receiving Work, revision
      authority, and conditions for reconsidering the affected claims.

### SYSE.13:8 - Common Failures and Repairs

These recurring failures can change the engineering decision:

| Failure | Repair |
| --- | --- |
| Treat one identifier as one bearer everywhere | Name the bearer and reference scheme for each use; state supported mappings among schemes. |
| Treat configuration item as a universal kind | Use it as a local designation of an already identified System, part, software package, or description chosen for this decision. |
| Treat a variant as an installed unit | Keep the variant description and unit separate and require realization evidence. |
| Treat latest as applicable | Name the edition and effectivity; current publication does not establish compatibility with the unit. |
| Treat a baseline or green status as reality | Keep the reference or status episteme separate from the observed actual configuration. |
| Make one product-data system the ontology | Use it as a resource and recover Systems, parts, epistemes, relations, schemes, and losses outside its schema when needed. |
| Inventory everything before deciding | Select item boundaries and claims sufficient for the receiving decision, accounting for their maintenance burden. |

### SYSE.13:9 - Consequences

Release, integration, service, and modernization decisions can identify the units and descriptions they concern.
Product-family reuse keeps serial-unit differences visible, and cross-tool automation can support comparisons
through declared identifier schemes and supported mappings.

The cost is maintaining selected identifiers, mappings, evidence, and effectivity claims. Some questions remain
unresolved until actual-unit observation or authority is available. Application profiles may still need specialized Methods for domain relations—for example,
interchangeability, software-package identity, regulated genealogy, ship configuration, or electrical
qualification.

### SYSE.13:10 - Rationale

The configuration basis is an episteme for one engineering decision. Starting from one
decision makes the boundary and maintenance burden testable. Keeping actual Systems, variant descriptions,
software packages, installed realizations, episteme editions, baselines, and status claims separate prevents the
situation in which every record is valid but no one knows which unit may be changed or released.

Effectivity is load-bearing because change rarely applies uniformly across a family. Time is only one condition;
another condition—for example, serial unit, lot, site, installed part, software realization, environment, or
operating envelope—may determine applicability.

### SYSE.13:11 - SoTA and Source Use

**Working question:** How can an engineer obtain a configuration basis for one decision while keeping the
necessary correspondence work affordable?

The selected line is tailored configuration management whose result is qualified for the receiving use.
Use a competent existing CM query or report when it already supplies the needed subjects, configuration,
evidence and applicability. An established linked-model view can likewise suffice for a description comparison
whose correspondence to the receiving subjects is already supported. Use those sufficient results directly as described in :4; another configuration account would add
maintenance without improving that decision.

When those results leave a consequential gap, the authored construction in :4.1 connects the selected item
boundaries, directional mappings and effectivity to that decision. Section :4.4 develops the record/event/use
time distinction and uncertainty treatment needed for a time-dependent claim. A shared model can supply some
of these relations; it needs additional evidence when a description comparison is being used to claim an
installed state or a historical interval. A CM arrangement that already supplies that evidence remains
sufficient.

The controller case in :5 compares a checked manual correspondence with a maintained mapping for the same
ten units and release question. It chooses the former for the one-off use, accepting checking effort to avoid
an unsupported continuing maintenance commitment. Repeated queries can reverse that choice. Preserving two
useful item structures also accepts a directional loss: the checked engineering-to-manufacturing relation
cannot answer a reverse routing question. A common model is competitive when its wider supported reuse
justifies construction and upkeep. These are conditional choices, not measured claims of universal savings.

| Source answer considered | Disposition in this Method | Scope of the comparison |
| --- | --- | --- |
| [NASA Systems Engineering Handbook §6.5](https://www.nasa.gov/reference/6-5-configuration-management/), official CM guidance on identification, change management, status accounting and verification | **Adopt** the connection between product information, controlled change and verified incorporation; **adapt** it to the decision-specific basis at :4. Use its existing implementation directly when it supplies that basis. | The maintained page was updated in 2023 and presents NASA's programme practice. Its phase baselines and organizational arrangements are not required for every use here. The guidance supplies a serious CM answer, not comparative effectiveness evidence. |
| Frank B. Watts, *Configuration Management for Senior Managers* (2015), treatments of part changes, bills of material, effectivity and field changes | **Adopt** revision/interchangeability and incorporation distinctions; **adapt** the reconciliation of engineering and operational views to :4.1 and :5. Its online processing and coordination can support a competent existing arrangement. | This historical practitioner treatment supplies substantive CM methods. Its particular numbering, departmental and approval policies require their own fit; they are not universal conditions of this configuration basis. |
| [Brovar, Sadeghzadeh and Fortin 2024](https://doi.org/10.1017/pds.2024.40), §§3–4, engineering/manufacturing relations | **Adapt** the explicit relations between differently grouped descriptions in :4.1 steps 3–4 and :5. Use an adequate existing mapping result directly. | The engine-front-mount construction follows engineering changes into manufacturing assemblies. The implemented direction does not establish reverse use or general scale; the controller case retains that directional qualification. |
| [Wu et al. 2025](https://doi.org/10.1016/j.aei.2025.103490), heterogeneous-model integration and versioning | **Adapt** shared semantics, traceability and model-version relations where they supply the required description comparison. Retain this as a competing construction for repeated model use. | The landing-gear model case does not itself qualify a physical unit or its effectivity. Such reliance needs the corresponding evidence in :4.1 steps 5–6 and, when time matters, :4.4. |

Reopen only the affected choice when a new use needs a lost mapping detail, changed evidence alters effectivity,
or recurring work makes another adequate arrangement worth its maintenance cost. A better source procedure
changes the relying step only where its subjects, conditions and result fit.

### SYSE.13:12 - Relations

- `A.1` and `A.1.SCR` distinguish actual Systems from intended referents. `A.22` governs selected structures,
  `A.19.SPR` state-like claims, and `C.27.TA` temporal aspects. None by itself produces an engineering
  configuration basis.
- `C.2.1` keeps descriptions, editions, subjects, reference schemes, carriers, and publications distinct. `A.10`
  and `B.3` govern evidence and assurance when current; neither proves the actual configuration.
- `F.10`, `A.21`, `A.2.8.PER`, `C.11`, `A.15.1`, and `A.3.4` distinguish status, gate, permission, choice, Work,
  and transformation from configuration claims.
- A compatible `SYSE.6` result can supply architecture constraints for the same System, decision, configuration,
  and horizon. It neither selects item boundaries nor proves an actual configuration.
- A decision-specific configuration basis can inform `SYSE.14` only for the same change and release question and
  can inform `SYSE.11` only for the named integration or modernization increment. It establishes neither release
  nor realization.
- `SYSE.7` coordinates several decision-usable descriptions. `SYSE.19` revalidates decisions after a relied-on
  source changes. Co-use creates no additional dependency or temporal order.
- Application profiles—such as software, electrical, mechanical, manufacturing, medical-device, ship, or
  building profiles—may specialize item identity, effectivity, interchangeability, evidence, and release when
  the kinds or uses of Systems designated as project systems-of-interest change the working move.

### SYSE.13:End
