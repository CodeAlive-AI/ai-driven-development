## SYSE.Application:6 - APP-SYSE-06 - Worked application: qualify a machining path with an external operation

This constructed desk example develops part of a supported manufacturing path and identifies the professional qualifications still needed. Its figures and trials are stipulated; the production procedure and capacity require the qualifications identified below.


### SYSE.Application:6.1 - Initial situation and the two users

A producer must deliver 120 acceptable brackets per working day in two fixture variants. The receiving assembly requires a finished bore of 20.000 ± 0.020 mm. Machining is internal; coating may be external and can alter the dimension needed by that assembly.

A shift contains 480 minutes. Two expected changeovers take 25 minutes each. A nominal three-minute machining cycle is quoted, but yield, rework, measurement uncertainty and sustained capability are not established.

For the supported-path question, a further illustrative observation is available: production planners and operators repeatedly reconstruct which drawing, material lot, fixture and NC-program edition a returned coated lot belongs to. A drawing file and a dispatch note circulate, but their relationship to the returned physical parts and final-dimensional decision is not reliably recoverable.

The platform users are the people preparing and performing production work. The bracket user's assembly task is a different use. A clearer dispatch interface may help the former without establishing that the latter can assemble conforming brackets.


### SYSE.Application:6.2 - 1. Select an improvement and retain the whole obtaining comparison

With `SYSE.25`, the producer selects one bounded improvement hypothesis: production users should be able to request, perform and recover an identified machining/coating undertaking without reconstructing its inputs and returned result from disconnected messages.

`SYSE.24` compares three whole arrangements on the same finished-part requirement and delivery horizon.

| Arrangement | What must be included in the comparison |
| --- | --- |
| Internal machining and coating | Tooling, process expertise, equipment, qualification, changeover, inspection, capacity, maintenance, support and continued provision. |
| External provision of finished brackets | Transferable design and acceptance basis, supplier capability, material and process evidence, delivery/transport, change commitments, recovery, rights and exit. |
| Internal machining with external coating | The internal obligations plus transport, the coating provider's independently controlled conditions, intermediate/final identity and the receiving acceptance decision. |

Compare transport, waiting, rejected lots and the work of maintaining the provider relation along with each arrangement's quoted price.

The following construction explores the mixed arrangement. Selecting it requires the missing professional results and a comparison of its benefits and burdens with repaired internal and fully external provision.


### SYSE.Application:6.3 - 2. Construct the supported transfer and its failure return

`SYSE.26` turns the improvement into a supported undertaking. A request identifies the design revision and finished-part requirement, material/lot identity, requested quantity and variant, applicable fixture and NC-program configuration, process conditions that the qualified procedure requires, and the receiving result.

The path distinguishes request receipt, input clarification, authorization for the next operation, actual dispatch/receipt, interrupted work and a returned result. An acknowledgement means that a request was received; it is not permission to machine or proof that the lot conforms. A planner can recover the undertaking and contact the responsible support function without sending an unrelated duplicate order.

An illustrative transfer exercise makes the construction testable. A request names drawing R7, lot L24 and fixture variant B, but carries the NC program associated only with variant A. The receiving interface returns the specific mismatch before the manufacturing step is authorized. Correcting the link to the intended B program lets interface qualification continue; it does not qualify that program's machining behavior.

`SYSE.13` keeps the design, lot, fixture, program, relevant setup and inspection-result effectivity distinguishable. Part and container identification must preserve the relationship through split or recombined lots; a folder containing the right files is not sufficient.

For a missing dispatch acknowledgement, first recover the original lot's actual location and receiving state. If that cannot be established, report the uncertainty and stop any action that could produce duplicate or incompatible physical work. “Retry the request” does not mean “coat the same parts again.”

The first result is therefore a supported transfer candidate with an exercised mismatch return and a recoverable uncertainty path. It remains usable for interface and planning work while production qualification is incomplete.


### SYSE.Application:6.4 - 3. Construct the independent-provider relation and contribution path

The external coater controls its own process, scheduling and willingness to continue supply. `SYSE.18` identifies the producer's dependent results and the actual provider decisions that can change them.

For this mixed arrangement, the proposed commitment covers the accepted incoming condition, applicable coating/process variant, lot identity, returned evidence, relevant change notification, delivery/partial-return conditions and the handling of a failed or disputed lot. The producer must discover which of these the provider actually accepts. An unanswered request is an unresolved dependency, not an agreed constraint on the provider.

Transfer and return exercises test whether both sides can recover the same lot, requirement and disposition. A proposed fallback names an alternative obtaining arrangement and the conditions under which it could actually receive the work.

Using `SYSE.27`, a changed fixture or NC program arrives as a bounded contribution: which supported variant changes, which earlier uses remain applicable, which qualification must be repeated, who can maintain the contribution, and which authorized receiver can accept it.

A compatible file format is only one interface fact. It cannot establish that the fixture locates the part correctly, the toolpath produces the required geometry or a changeover can be performed under the intended conditions.


### SYSE.Application:6.5 - 4. Place the decisive dimensional control and expose what it still lacks

The supplied requirement concerns the bore after coating, because that is what the assembly receives. `SYSE.28` places the decisive dimensional control after the last operation that can alter that property and before reliance by the receiving assembly.

A pre-coating measurement can still guide machining and detect an upstream problem. It cannot, by itself, establish the finished bore's conformity. The supported path must preserve which physical subjects each observation concerns.

In this case no qualified finished-part measurement chain, applicable uncertainty result or receiving decision rule has been supplied. The path can identify where to place the control, which parts to measure, what measurement result is needed and which dependent action must wait.

For example, a returned number of 20.010 mm without the applicable procedure, uncertainty and subject identity is not yet the required conformance decision. Use the qualified measurement and acceptance Methods for the actual operation to select any required tolerance guard band and sampling plan.

The Library already supplies parts of that construction. [PHY.9](../../foundational-thinking-dpf-suite/phy/16-phy-9---construct-a-measuring-interaction-for-a-physical-dis.md) helps construct the measuring interaction; C.16.MR/IR relate its recorded result to values compatible with the stated error constraints. The instrument, material, procedure and applicable error account must still be supplied for this bore. For statistical inference under a probability model of the records, use [MMP.13](../../foundational-thinking-dpf-suite/mmp/18-mmp-13---infer-unknowns-statistically-under-a-stated-observa.md), retaining the meaning of its uncertainty statement.

In a separate stipulated calculation, the identified finished bore reads 20.014 mm and the complete error is bounded by ±0.008 mm. Its compatible diameters are [20.006, 20.022] mm. That interval includes values inside and outside [19.980, 20.020], so this observation does not settle conformity. If an applicable procedure instead supplies a complete hard bound of ±0.004 mm for the same reading, the interval becomes [20.010, 20.018] mm and lies inside the specification. These are hard bounds, not confidence intervals. Whether obtaining a different measurement is worthwhile depends on the receiving decision and the cost of changing its answer; use C.11.DUA when that choice is unresolved.

This calculation concerns the stated part and error model. Acceptance of a lot also needs its applicable decision and sampling rules.

The immediate stop is precise: no acceptance claim for the finished lot from this incomplete evidence. Independent work on the interface, provider commitments or test preparation can continue.


### SYSE.Application:6.6 - 5. Separate nominal cycle arithmetic from qualified delivery capability

After the two expected changeovers, the nominal machining time is:

- 480 - 2 × 25 = 430 minutes;
- 430 / 3 = 143.33 nominal cycles, or at most 143 complete cycles under those assumptions;
- 120 × 3 = 360 nominal machining minutes, leaving 70 minutes before other demands on that same capacity.

This arithmetic has no allowance for yield loss, rework, interruption, loading assumptions omitted from the quoted cycle, inspection that uses the same constrained resources, or transport. It also says nothing about coating capacity, batch size, lead time or whether returned acceptable parts meet the day's delivery boundary. Extra work on independent resources need not subtract directly from the machine's 430 minutes, but it can still constrain delivery.

Use [OPS.10.1](../../management-dpf-suite/ops/41-ops-10-1---construct-and-compare-operating-capacity-models.md) to construct the capacity account from the needed acceptable output, actual processing and rework passes, opening work, resource demands and provider returns. Use [OPS.10.2](../../management-dpf-suite/ops/42-ops-10-2---construct-and-revise-a-feasible-deadline-schedule.md) to place those operations within their availability and delivery constraints. The methods are available; the missing production values and their applicable limits still have to be obtained.

A changed condition can already reject a candidate without a complete production study. Suppose the day starts with no partly completed brackets and an additional 71 minutes of machine unavailability leaves 359 minutes after changeovers. Even 120 single passes require 360 minutes. Under those assumptions, this machine cannot complete the proposed day's work. Before that change, the spare 70 minutes alone did not establish delivery through coating and return.

One conforming specimen does not establish the process distribution or its sustained behavior. The [NIST/SEMATECH process-capability Method](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm) is a bounded historical statistical source: its familiar capability indices compare a stable process with specification limits under applicable distribution and sampling conditions. Qualify the measurement chain separately. Distinguish relevant variants and operating conditions, and justify any pooling before interpreting a capability index.

The remaining production contributions can now be assigned.

| Contribution needed for this production case | What its receiver needs before the dependent claim can proceed |
| --- | --- |
| Tooling, program and changeover qualification | An operative procedure and evidence for the intended machine, material, fixture variants, program/configuration and changeover conditions, including the failed or interrupted case. |
| Finished-part measurement and acceptance | A qualified measurement chain with applicable uncertainty and an authorized decision rule for the coated bore and identified part/lot population. |
| Sustained process capability | Suitable observations from the qualified measurement process, stability and model checks, and a justified capability result for the relevant conditions. The NIST source is used only where its Method applies. |
| Acceptable-part delivery capacity | An end-to-end result including yield, rework, constrained resources, provider capacity, transport, waiting and the actual delivery horizon; not the isolated nominal cycle count. |
| Nonconforming-material and recovery disposition | An authorized way to identify and segregate affected material, determine permitted inspection/rework/replacement or acceptance, and establish the result before reuse. |

Use the available Library Methods for the stated constructions. Obtain or develop the physical procedures still missing, and obtain the case inputs and qualification results needed by the receiving decision. The common platform language connects those contributions.


### SYSE.Application:6.7 - 5.1. Compare independent preparation and a transferable setting

A shorter stop can require a different physical arrangement, not just a different timetable. Consider one of the 25-minute changeovers. The machine works until minute 20. Preparation takes 12 minutes, installation and datum establishment 10, and the stipulated qualification operation 3. Performing all three after the stop gives the next start at minute 45.

An alternative prepares the next module on an independent station during minutes 8–20, then performs installation and qualification on the machine: the next start is minute 33. [OPS.11.1](../../management-dpf-suite/ops/44-ops-11-1---construct-and-reconcile-operating-models-across-s.md) keeps the operator, station, module and machine demands in the same operating account. If the only fixture required for preparation remains occupied on the machine until minute 20, preparation cannot begin at minute 8 and this alternative returns to minute 45. A calendar change alone cannot create the missing independent means.

The [SMED distinction between internal and external setup](https://www.lean.org/lexicon-terms/single-minute-exchange-of-die/) helps find that opportunity. A possible physical construction is a separately prepared module with a setting that can be transferred to the actual production pairing. The [MIT kinematic-coupling proposal](https://pergatory.mit.edu/kinematiccouplings/html/design_process/improvement.html) uses measured parameters of the mating halves and calibration against a known counterpart. It distinguishes the repeatability of one pair from interchangeability across pairs. Treat this as a design proposal whose actual geometry, contact, load, friction and deformation conditions must be established.

[MMP.18](../../foundational-thinking-dpf-suite/mmp/25-mmp-18---couple-models-with-compatible-exchanges-and-scales.md) constructs the correspondence between the calibration and receiving descriptions; C.29.1 preserves the conditions under which the mathematical result can be used. In a translation-only illustration, a reference pairing places the module origin at 0.020 mm in the reference station's coordinates. A module fiducial reads 10.020 mm there, so its coordinate relative to the module origin is 10.000 mm. The production pairing places the module origin at 0.035 mm in the production frame. The predicted fiducial coordinate there is 10.035 mm. Reusing the reference reading 10.020 mm would differ by 0.015 mm.

Suppose the module-coordinate calibration has a complete hard error bound of ±0.003 mm, already including uncertainty from the reference pairing, and the production-origin offset has a complete bound of ±0.002 mm. Their sum permits [10.030, 10.040] mm for the production coordinate. Whether this is adequate depends on the receiving operation. The calculation assumes the stated one-dimensional correspondence; it supplies neither the physical measurements nor a model of rotation, deformation or loss of contact.

With SYSE.26 and SYSE.27, the proposed supported variant now states which prepared module and pairing it uses, which setting is returned and which conditions support that transfer. A different pairing or load that invalidates the correspondence returns the affected qualification question. The incumbent arrangement remains an alternative; a new coupling is unnecessary when a simpler arrangement already gives the required result.

The result is a candidate for reducing this stop from 25 to 13 minutes, with its resource condition, calibration correspondence and qualification needs exposed. The three-minute qualification operation is a stipulated duration, not evidence that three minutes can qualify an actual process. SYSE.24 compares the complete provision alternatives before adopting the change. The rest of the day's capacity and coating/return constraints still apply.


### SYSE.Application:6.8 - 6. Recover physical work and make exit real

In an adverse constructed return, a coated lot lacks a qualified final-dimensional result, or qualified inspection finds a nonconformity. Keep its disposition distinct from a conforming released lot. Recover which parts and configurations are affected before selecting an authorized action.

Possible responses include segregation, additional qualified inspection, permitted rework, replacement or an explicitly authorized acceptance disposition. This example chooses none without the missing professional and authority basis. Loading an older NC program does not restore material already removed, and cancelling a message does not reverse coating.

`SYSE.29` makes retirement of the current provider path depend on the actual remaining work. The receiver needs usable tooling, programs and process information with transferable rights, relevant material and evidence, support for outstanding lots, and demonstrated ability to perform the receiving work. Qualify the receiving arrangement's ability to perform the work with these transferred inputs.

An old support route can remain necessary for a disputed or infrequently ordered lot even when ordinary new orders use another provider. Ending new orders and ending responsibility for old results are different decisions.


### SYSE.Application:6.9 - Result and practical change

The application gives the producer a supported transfer with a response that identifies the wrong fixture/program pairing, a proposed independent-provider commitment, final-dimensional control placement and a bounded capacity calculation. It also gives a candidate for independent preparation with the calculation for transferring its setting. The available measurement and operating Methods support these constructions; the physical procedures, inputs and qualifications still needed for production are identified.

It stops before promising 120 acceptable brackets per day or treating the production path as qualified. `SYSE.11` may assess usability for the narrower interface or planning purpose already supported. Use `SYSE.14` for the production release decision when its required qualification and acceptance basis are available.

The team can improve the common path and obtain the separate machining, metrology and delivery results needed for production. A practitioner needing only the failed-lot disposition starts at the missing recovery Method; one facing a provider change starts at `SYSE.18` or `SYSE.29`. Neither must perform the entire example.
