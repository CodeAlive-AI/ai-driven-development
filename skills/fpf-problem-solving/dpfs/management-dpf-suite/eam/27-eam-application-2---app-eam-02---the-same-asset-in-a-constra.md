## EAM.Application:2 - APP-EAM-02 - The same asset in a constrained programme

CityWater's funding board has allocated 8 for initial capital, a separate 0.60 for initial operating expenditure and 3 for annual operation. The infrastructure committee is authorized to select the asset programme within those allocations; changing an allocation requires a decision by the funding board. The operating plan separately supplies twelve available team/outage days before the wet season. These allocations, authorities and operating conditions are constructed case premises. No later funding is assumed in this base comparison. Each station needs one of its two qualified options. Enumerate the sixteen combinations to compare the complete programmes.

Codes below follow asset order A/B/C/D. Every row satisfies the initial and recurring operating allowances and the twelve-day bound; the base funding column identifies the remaining capital constraint. The service checks still require a non-overlapping schedule for the connected outages.

| Combination | Initial capital | Days | Total present cost | Base funding eligible? |
| --- | ---: | ---: | ---: | --- |
| `FRMR` | 11.5 | 11 | 13.025446 | capital exceeds 8 |
| `FFMR` | 10.0 | 10 | 13.080344 | capital exceeds 8 |
| `RRMR` | 13.0 | 12 | 13.199533 | capital exceeds 8 |
| `RFMR` | 11.5 | 11 | 13.254431 | capital exceeds 8 |
| `FRMK` | 8.5 | 9 | 14.537386 | capital exceeds 8 |
| `FFMK` | 7.0 | 8 | 14.592284 | yes |
| `RRMK` | 10.0 | 10 | 14.711473 | capital exceeds 8 |
| `RFMK` | 8.5 | 9 | 14.766371 | capital exceeds 8 |
| `FRLR` | 8.5 | 9 | 15.295240 | capital exceeds 8 |
| `FFLR` | 7.0 | 8 | 15.350138 | yes |
| `RRLR` | 10.0 | 10 | 15.469327 | capital exceeds 8 |
| `RFLR` | 8.5 | 9 | 15.524225 | capital exceeds 8 |
| `FRLK` | 5.5 | 7 | 16.807180 | yes |
| `FFLK` | 4.0 | 6 | 16.862078 | yes |
| `RRLK` | 7.0 | 8 | 16.981268 | yes |
| `RFLK` | 5.5 | 7 | 17.036166 | yes |

`FFMK` is the minimum-cost eligible combination: refurbish A and B, modify C and retain D under its supported policy. It uses 7 of capital, 0.50 of initial operating cash, 1.85 annually and eight team/outage days. Its total present cost is 14.592284. A feasible twelve-day calendar under these premises can place A on days 1–2, B on 3–4, C on 5–7 and D on 8, with four uncommitted days. Each restored station is available before another dependent station is removed. The uncommitted allowance does not establish that all disturbances fit.

The individual D recommendation remains true under its assumptions, but replacing D while retaining both refurbishments and C modification needs 10 of capital and is infeasible at 8. `FFLR` frees C's capital through leased service and replaces D, but costs 15.350138 overall. The unused 1 of capital is not an extra benefit or an instruction to spend it.

Three separate changed-condition branches show the decision's sensitivity:

- With the funding board's capital allocation raised to 10 and the other premises unchanged, `FFMR` becomes best: both refurbishments, C modification and D replacement, present cost 13.080344 and ten days. Use the larger feasible set once the funding board has authorized the increase.
- With only seven team/outage days and the original capital limit, `FRLK` becomes best among the supplied options: refurbish A, replace B, lease C's added service and continue D. It takes seven days, 5.5 capital and costs 16.807180. A cheaper eight-day combination does not fit merely because each job fits separately. Another qualified team or extended window would be another explicit alternative with its own full cost and service implications.
- If a new engineering finding invalidates D's continued-use policy, remove every `...K` combination. At the original limits, `FFLR` is then best, at 15.350138 and eight days. If leased service is also unavailable, A and B each still require an option costing at least 2 in capital, while the available options for C and D cost 3 each. The minimum of 10 exceeds the capital limit of 8. That excludes every combination in the stated choice set even before their life-cycle costs are ranked.

The EAM team submits its programme recommendation to the infrastructure committee. The finance practitioner supplies cost estimates and an affordability assessment against the funding board's allocations; those allocations set the spending limits. The infrastructure committee selects and authorizes an asset programme that fits those limits and the water-delivery mandate. Maintenance and operating authorities subsequently determine the permissions and conditions for protected work and resumption. The team can deliver its supported recommendation before the committee decides; the team reports an authorized programme only after that decision is supplied.



### EAM.Application:2.1 - When the demand basis changes

The sixteen combinations cover the supplied North wet-season requirement of 1,100 m³/h. Suppose a later demand forecast puts a peak at 1,250. Establish when demands coincide and how the service commitment treats that peak (EAM.4). Either option for C adds 200 to North’s existing 1,000. On those premises the whole district can supply 1,200. The gap of at least 50 excludes all sixteen combinations **if service at 1,250 is required**. If 1,100 remains the obligation, the forecast identifies an exposure for the service owner to assess under the agreed risk criterion.

When the higher flow must be served, use EAM.7 to find additional supply or an authorized way of reducing coincident demand. Compare the revised options on that basis. If the existing service obligation and risk criterion are still met, the decision maker may keep the programme. A change to what users are promised requires the responsible authority. EAM.13 brings a material change in demand, risk or obligation back to the choices it affects.



### EAM.Application:2.2 - When a shared dependency changes recovery

A common dependency can require another option even when the normal-demand comparison passes. [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md)'s separate feeder example shows both units losing their contribution together, reserve exhaustion before full recovery, and an independent supply whose time to usable service changes the result. Its qualified recovery conditions become inputs when developing alternatives with [EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md) and EAM.8 and a calendar with [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md). A favourable price or available team does not restore the missing service.

To apply that construction to CityWater, obtain the relevant dependency, deliverability, usable reserve and restoration account for its actual service boundaries. Compare the resulting options in [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) and EAM.10 and retain the relied-on recovery conditions in the recommendation. The original CityWater outage bounds remain useful for the situations they describe. If an observed restoration time or dependency changes, [EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) returns to the affected capability, option and timing.



### EAM.Application:2.3 - When shared work changes the consequences

The sixteen rows above use their declared additive costs and whole-work times. They do not establish whether a different work arrangement could share a mobilization, require extra temporary service or change a later commitment. [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md)'s separate P+Q/Z case shows why that question matters: one qualified shared mobilization makes the joint solution cost 3.8 against the alternative's 3.9, while two required visits make it cost 4.0.

For a proposed CityWater arrangement, use [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md) to establish the windows and the work each would have to accommodate. Use [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) to establish the service conditions. [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md) then reconstructs that combination's consequences; [FIN.9](../fin/22-fin-9---compare-capital-investments-and-allocations.md) supplies the financial return if joint cash or dated funding must be developed. Recompute the affected rows rather than applying a discount to all sixteen. If the change also affects demand, recovery or a continuing policy, return that premise to [EAM.4](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md), [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) or EAM.8. The existing capital, time and D-qualification branches remain valid on their stated premises.



### EAM.Application:2.4 - What subsequent outcomes and practice questions would mean

The committee’s decision covers added service from C and continued supported use of D within the authorized funding. The appraisal forecasts spending. To report what the programme actually delivered or cost, compare evidence of usable service or incurred expenditure with the corresponding commitment or estimate. A single acceptance or expenditure record can settle the particular condition it certifies. EAM.13 shows how to revise a premise when the recorded result differs.

The later practice examples are separately constructed continuations. [EAM.14](23-eam-14---decide-whether-and-how-to-change-the-asset-manageme.md) compares a small responsibility/information repair with a new application. [EAM.15](24-eam-15---decide-whether-and-how-to-change-engineering-asset.md) compares a condition-priority rule with complete combination comparison and distinguishes a desk result from a trial in real decisions. [EAM.16](25-eam-16---deliberately-continue-and-change-engineering-asset.md) examines teaching, later use and selection of the reusable practice with different evidence. To establish that the appraisal method was selected for later use, look for the decision or practice concerning that method.
