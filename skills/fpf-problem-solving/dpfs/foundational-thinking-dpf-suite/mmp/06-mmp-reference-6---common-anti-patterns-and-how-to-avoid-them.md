## MMP.Reference:6 - Common Anti-Patterns and How to Avoid Them

The methods address consequential failures visible in their constructions. An encoding with ignored fields can give several records for one object; MMP.10 shows how that affects counting and interpretation. A probability law for the source event can omit the procedure that selected the available records; MMP.7 reconstructs that procedure's contribution. A decision rule can accidentally depend on information unavailable at the time of action; MMP.8 constructs the allowed dependence.

Recovering one best-fitting unknown can also hide a distinction the observations never resolved; MMP.12 separates recovery from the restriction that selects it. MMP.13 distinguishes the meaning of a confidence interval, a posterior probability and a prediction. MMP.14 shows why fitting an overall mean can leave the conditional prediction wrong, and why matching the data used to design a repair is not an untouched test of that repair.

Two further failures concern changing a model. Removing variables can leave a missing contribution in the retained evolution; MMP.9 derives that contribution before choosing its replacement. A flexible fitted function can violate a property known about the modeled relation; MMP.11 constructs the variation within that property and exposes any additional restriction.

Their repairs are specific. More numerical accuracy will not recover an excluded candidate object or an omitted relation. A different equation solver can help when the obtaining operation is the actual difficulty. Locate the consequential discrepancy before deciding what to change.
