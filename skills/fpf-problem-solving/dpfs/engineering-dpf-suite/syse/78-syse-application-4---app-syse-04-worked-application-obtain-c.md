## SYSE.Application:4 - APP-SYSE-04 — Worked application: obtain climate control for a new greenhouse configuration

This case shows the common Systems Engineering patterns in a small cyber-physical equipment company. It includes
physical equipment, control software, provider Work, an AI Agent, internal capability, and continuing support.
Greenhouse-control, electrical-safety, commercial, legal, financial, and organization-design results enter as
inputs; their Methods remain with those practices.


### SYSE.Application:4.1 - 1. Fix the System, use, and result to obtain

`SYSE.1` selects the intended greenhouse climate-control System, designated `GreenhouseClimateControl-GH2`,
as the project system-of-interest and distinguishes it from greenhouse `GH-2` and company `GreenHeat-4`.
An actual System identity may begin later. `SYSE.16` identifies the greenhouse,
electrical supply, heating, ventilation, misting, shading, sensors, operator station, weather, and manual fallback
that form the relevant operating surroundings. `SYSE.17` identifies operators, crops, maintainers, the equipment
company, and the greenhouse owner as Systems that can bear consequences.

The receiving use is control during three representative conditions: a cold night, a rapid solar rise, and a
failed humidity sensor. `SYSE.2` supplies linked use and System concepts. Acceptance requires bounded temperature
and humidity performance, no unsafe actuator command after sensor failure, identified controller and software
configuration, recoverable observations, and supported manual fallback. These are case inputs from greenhouse-
control and electrical-safety Methods. The case takes its thresholds from those specialist results.


### SYSE.Application:4.2 - 2. Construct complete obtaining arrangements

`GreenHeat-4`'s managers initially propose buying a controller or having an AI Agent write one. The engineering
team applies `SYSE.24` and rejects those two phrases as a usable option set. A purchase is one relation inside an
arrangement; an AI Agent is one possible performer of named Work. The team follows
`SYSE.24:4.2–4.3` backwards from accepted greenhouse behaviour to local protective control, supervisory demands,
identified interfaces and the evidence needed for their integration. It then varies what is supplied: a ready
controller with integration, a commissioned whole, an internally developed whole, or a ready protective
controller with an internal supervisory complement. For each division it adds the receiving Work that remains
and follows the result forward to the same acceptance conditions. The hybrid is plausible only while its
interface keeps supervisory optimization inside the controller's qualified protective envelope. This
construction yields the four arrangements below; the common questions keep their comparison recoverable.

| Arrangement | Agents, Work, Methods, and means | Evidence, integration, support, capability, and exit |
| --- | --- | --- |
| Ready controller plus integrator | The controller vendor's engineering team supplies a configured controller. The integration company's team performs sensor, actuator, network, and commissioning Work. `GreenHeat-4`'s engineering team maintains greenhouse requirements and accepts the result. | The controller supports the stated field interface and can be commissioned in nine weeks. Greenhouse-specific failed-sensor behaviour, configuration export, and the supervisory interface remain unsupported. Vendor support is offered for three years; changing the control logic requires vendor access. |
| Commissioned custom controller | The engineering provider's team designs and integrates a custom controller and supplies source, configuration, test evidence, and support. | The provider estimates sixteen weeks against a twelve-week need date. It proposes source escrow but has supplied no representative failed-sensor evidence for this hardware family. |
| Internal development with AI assistance | `GreenHeat-4`'s controls engineers lead the Work. A general AI Agent assists with code and test generation. An independent controls specialist reviews safety-relevant behaviour. | The company would retain knowledge and change access, but it has no qualified hardware-in-the-loop environment and no evidence that the team can finish assurance within twenty weeks. AI-produced code supplies no capability or acceptance result by itself. |
| Ready controller plus internal supervisory layer | The vendor controller retains local safety interlocks and manual fallback. `GreenHeat-4`'s controls team develops greenhouse-specific supervisory optimization through a documented interface. | The arrangement is estimated at eleven weeks and preserves internal change capability above the safety boundary. It still depends on configuration export, interface timing, and the vendor update policy; failure of any one defeats the arrangement. |

The Finance result compares resource and cash consequences. The Organization Change result states the proposed
human–AI–provider Work allocation and its authority gaps. The safety result states the protected failed-sensor
condition. The commercial and legal results state the proposed access, update, data, and remedy terms.
`SYSE.24` uses those results but does not recreate their Methods or decide their questions.


### SYSE.Application:4.3 - 3. Restore parity and choose the next probe

The comparison uses the same three operating conditions, commissioning date, field interfaces, configuration
evidence, assurance burden, data access, support horizon, internal capability consequence, expected change
latency, and exit condition. The provider demonstration is not compared with an unfinished internal prototype;
both are compared with the accepted `GH-2` configuration and representative conditions.

The custom provider's sixteen-week estimate exceeds the need-date limit. Timely completion of the internal-only
arrangement remains unsupported. The ready-controller and hybrid
arrangements form a tie-set because the hybrid arrangement is better for later greenhouse-specific change only
if the vendor interface preserves timing, configuration export, and supported fallback.

The ready-controller arrangement costs EUR 84,000 and eighteen internal engineering days; the hybrid costs EUR
96,000 and thirty-two internal engineering days. Both current estimates fit the need date; the remaining
realization conditions must still be established before relying on those estimates. The operating plan expects at least three
greenhouse-specific changes in the next three years, so the deciding management team will prefer the hybrid when
its added price stays within EUR 15,000 and its added internal burden stays within fifteen engineering days, but
only after the protected interface and fallback claims are supported.

The same team is authorized to spend up to EUR 7,000, forty engineering hours, two hardware-in-the-loop laboratory
days, and five elapsed working days on this decision. The safety specialist separately authorizes the failed-
sensor injection in the laboratory. `ChoiceResult-GH2-1` is **probe again**: a EUR 5,500 replay uses thirty-two
controls-engineering hours, eight integrator hours, two laboratory days, and the available five-day reserve.

The decision rule distinguishes four outcomes. Unsafe fallback or unusable configuration export rejects both
survivors. Safe fallback and export combined with failed supervisory timing or unsupported API retains only the
ready-controller arrangement. If fallback, export, API support, and timing all pass, both survive and the stated
price-and-burden rule retains the hybrid. An interrupted or inconclusive replay that exhausts its authorized
limits leaves the protected claims unresolved and returns the commissioning-plan question; it does not establish
controller failure or permit commitment through the gap. Without the replay, neither survivor has enough evidence
for a choice under the declared rule; rejecting both would discard an arrangement that the bounded replay can retain.

The performed replay returns the third outcome: the local controller enters the supported fallback without an
unsafe actuator command, the supervisory command round trip remains below the application-profile limit, and the
configuration export reidentifies the tested controller and software values. The safety specialist limits the
first observation to the tested failure and configuration. The deciding Agent applies `C.11` again and records
`ChoiceResult-GH2-2`: **choose now** for retaining the hybrid as the arrangement whose next realization
contribution is to be developed. The replay qualifies the compared interface and fallback claims. It does
not establish that internal integration and commissioning can be completed by the need date; commitment
to that delivery still depends on the contribution below. A different safety limit or withdrawn
vendor-update support would reopen the obtaining choice.


### SYSE.Application:4.4 - 4. Continue with realization, configuration, and assurance

The realization Agent applies `SYSE.3` to the retained arrangement and identifies its first unsupported realization branch: whether the
internal integration Agent can configure the supervisory layer and produce the commissioning evidence before the
need date. The vendor controller is a supplied System and the AI Agent is a possible performer in selected Work;
neither becomes the whole realization arrangement.

`SYSE.13` identifies controller, software, interface, sensor, and greenhouse configuration and effectivity.
`SYSE.10` keeps the hardware-in-the-loop replay results tied to the claims assessed by that replay. `SYSE.4` states which acceptance
claims may rely on those observations and which still need greenhouse commissioning evidence. `SYSE.14` governs
the later change and release decision. Performed integration Work, accepted configuration, payment, provider
duty, and changed internal capability remain results of their own Methods.


### SYSE.Application:4.5 - Result, stop, and reopen

The worked application returns a project-System focus, linked use and System concepts, four comparable whole
obtaining arrangements, one evidence-qualified `C.11` choice, and the first unsupported realization branch. The
decision-making Agent can now retain the hybrid and pursue the named realization question within the
existing authority. An implementation or commissioning commitment that relies on timely internal integration
remains conditional on that missing contribution. Project integration and acceptance remain open.

Stop there. Reopen `SYSE.24` when the result, use, need date, provider capability, interface, configuration
export, support, internal capability, evidence, or exit condition can reverse the choice. Reopen only the
affected realization or assurance result when the arrangement remains preferred but one branch or claim fails.
