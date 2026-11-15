## SYSE.32 - Promote Verified Artifacts without Rebuilding

> **Status:** Stable

> **Normativity:** Guidance within the stated software-engineering use; examples are illustrative.

### SYSE.32:1 - Problem frame

Use this pattern when a tested software package must cross an environment, storage service or provider boundary and someone needs to rely on it being the same qualified result. Start with the artifact that was exercised, the evidence needed at the destination, and the conditions under which that evidence remains applicable.

The first result is an artifact-specific basis for promotion, or an identity, evidence or trust condition that has not been met. Promotion here means making the selected artifact available for a next use without silently replacing it. Use SYSE.41 for installation and verification of the resulting runtime when that work is needed.

If an unchanged artifact is already available at the consumer with adequate identity and applicable evidence, use that result. If the missing result is a recoverable build, use SYSE.30. If it is application acceptance, obtain the relevant engineering feedback through SYSE.31. A storage transfer cannot supply either.

### SYSE.32:2 - Problem

A version label or source revision can remain unchanged while the bytes change. A later stage may resolve different dependencies, embed another configuration or receive a substituted package. Tests of the earlier package then accompany a different result.

Authenticity is a separate question. A signature can be valid while the signer, source, build procedure or artifact is not the one the consumer expects. Conversely, a package can have the expected digest while the only evidence for that expectation came through an untrusted channel.

### SYSE.32:3 - Forces

| Force | Practical tension |
| --- | --- |
| Reuse and local adaptation | Reusing tested bytes preserves their identity; qualify the destination configuration when the next use involves running the artifact there. |
| Convenience and evidence reach | Mutable names simplify selection but can hide substitution after a test or check. |
| Verification and trust | Cryptographic checks establish particular relationships; apply the trust and acceptance conditions that govern the consumer’s use. |
| Continuity and change | Old evidence can be reused for an unchanged subject, but a new artifact or material condition requires evidence applicable to that subject and its material conditions. |

### SYSE.32:4 - Solution

#### SYSE.32:4.1 - Recover the artifact and the claim being carried

Identify the exact package, image or other deliverable that the prior activity produced and exercised. Use an identity appropriate to its form, such as a digest of the specified bytes, together with a retrievable immutable object where available. State which bytes the identity covers; a directory name or a mutable image tag is not that definition.

Recover the evidence needed for the next decision. Distinguish functional tests, build-input traceability, vulnerability or policy checks, and authenticity. For each result used, identify its subject and the conditions under which it applies. A test of source code does not automatically cover a separately built binary.

When evidence is absent or attributed only to an ambiguous label, return that gap. The team may re-establish evidence for the selected artifact or select the artifact already covered. Relabeling the new output with the old version is not a repair.

#### SYSE.32:4.2 - Separate the artifact from destination configuration

Keep destination-specific values in an independently identified configuration when the software supports that separation. Define the compatible artifact/configuration combination and protect secrets through the applicable authorized mechanism; do not publish them merely to make the build look reproducible.

If a destination requires a different compiled result, treat it as a different artifact and obtain its own evidence. Do not describe a rebuild as promotion of the previously tested bytes.

Preserve access to the selected artifact for the intended interval. A digest without obtainable bytes is not a usable delivery path. Establish whether the selected bytes will remain available and whether their distribution is permitted.

#### SYSE.32:4.3 - Transfer and verify the subject at the relying boundary

Determine where substitution can occur between the earlier check and the next use. Check the actual artifact delivered at the boundary where reliance is made, or establish a controlled chain that preserves both identity and the applicability of the earlier result. SYSE.28 helps place that control.

A failed transfer, incomplete download or digest mismatch prevents reliance on the earlier artifact evidence. Preserve the expected identity and inspect the actual result; do not repair the mismatch by silently changing the expectation to match the received package.

A matching digest establishes identity relative to the expected digest and its trust basis. It does not establish that the original artifact was correct, non-malicious or fit for this target.

#### SYSE.32:4.4 - Apply the authenticity Method when that claim is required

Use [SLSA v1.2, Verifying artifacts](https://slsa.dev/spec/v1.2/verifying-artifacts) with the consumer's configured trust roots and expectations. Its operative verification includes the signature, the actual artifact's correspondence to the provenance subject, the expected provenance type, and the recognized builder's trust basis. Compare the claimed build with the expected builder, canonical source, build type and external parameters; a valid signature alone is insufficient.

Supply those expectations through the authorized trust arrangement. Unknown or unexpected parameters require the source Method's explicit disposition, not silent acceptance. Use a verifier qualified for the deployed formats and trust system.

Distinguish missing provenance, invalid verification, an unexpected but correctly signed build, and unavailable verification. Each may require a different investigation or authorized exception decision, but none establishes the missing trust claim. If an authorized holder permits a bounded use without that assurance, retain the limitation and its scope.

#### SYSE.32:4.5 - Return a usable, bounded promotion basis

Use the selected artifact where it is already available to the consumer, or make it available there. Give the consumer the artifact’s identity, its applicable evidence, any separately specified configuration it requires, and any unresolved conditions. An existing delivery mechanism or record can supply these facts.

Use applicable results for the consequential substitution and missing-evidence cases, or exercise the cases that remain unresolved for the chosen mechanism. Establish that the consumer obtains the intended bytes and can distinguish failure from a completed verification. Reuse a result while its subject, required claim and material conditions remain the same.

If the next use requires deployment, give its operator the selected artifact, its verification results and the limits of any authorized exception for use with SYSE.41. For that deployment, establish the target's effective configuration, dependencies and observed behavior. Use SYSE.14 when a separately authorized release decision is needed; artifact promotion does not widen exposure by itself.

#### SYSE.32:4.6 - Build a promotion mechanism whose evidence reaches actual use

Begin at the next consumer and work backward. Which object will it obtain, and who can change that selection between verification and use? Prefer selecting an immutable content identity for the consumption itself. Merely verifying a tag and then asking the runtime to fetch that mutable tag again leaves a substitution interval. Where direct immutable selection is unavailable, the delivery mechanism must retain and verify the selected object through the last mutable boundary; otherwise report the remaining identity gap.

Separate the package's stable identity from its changing eligibility. A package can keep identical bytes while an expiring test condition, revoked builder trust, incompatible target or newly known defect changes whether it should be used. Keep evidence discoverable by artifact identity, with the scope and time of each result. A later policy decision can withdraw use without rewriting the artifact's history. Conversely, a new policy label cannot turn an untested binary into the subject of an old passing test.

Choose where verification occurs from the substitution and trust question. Verification at publication into a registry can reject a bad producer result early. Consumer verification can additionally cover what arrives after storage or transit. A trusted controlled store may let several consumers reuse a verification result, provided the identity-preservation and trust conditions for that reuse hold. Reuse a sufficient result while its subject and material conditions remain applicable; repeat a check when it can resolve a remaining relevant question. Skipping the only check after an uncontrolled boundary loses assurance.

Multi-platform packaging makes the subject question concrete. An image index may select different platform-specific images. A test on one architecture supports the actual selected image and its conditions, not every image mentioned by the index. For a second target, establish which child artifact will run and obtain its applicable evidence. If a distribution system repackages files, determine whether the relied-on tests concern the retained payload, packaging behavior or the entire delivered bytes. Reuse only the results whose subjects and conditions survive that transformation.

Construct the failure path as part of the same mechanism. An absent artifact returns unavailable, a mismatch leaves the expected artifact identity unconfirmed, an unrecognized provenance returns an unresolved origin, and a failed required test returns an unqualified candidate. Each result should point to the contribution that can repair it. Retain the last permitted usable selection when that remains a valid option. Do not silently fall back to an older package whose permissions, compatibility or known defects have changed.

Suppose h1 passed on a supported Linux target and a release job creates a multi-platform bundle containing h1 and a newly compiled Windows package h3. The whole bundle is new even though h1's bytes remain. The Linux consumer can reuse the applicable h1 behavior evidence after verifying its selection; the Windows consumer needs h3 evidence. A policy scanner rerun on the bundle might answer a new security question, but it cannot supply h3's missing behavior check.

### SYSE.32:5 - Archetypal Grounding

In a constructed ParcelWorks example, integrated source revision r17 produces artifact h1. Here h1 and h2 denote distinct artifact digests. The address-transformation tests exercised h1 under their stated conditions. A staging job later rebuilds r17 and obtains h2 because a build input changed.

The team wants to move the tested software to a candidate runtime. Its immediate question is whether the selected artifact carries the required evidence, not whether that runtime is already usable.

| Candidate situation | What is established | Next action |
| --- | --- | --- |
| The consumer receives h1, and the required results concern h1 under applicable conditions. | Identity and those stated evidence relationships are preserved. | Return the promotion basis. To establish runtime usability, deploy and test the target separately. |
| The consumer receives h2 with h1's test result. | The source label matches, but the tested artifact does not. | Select h1 or qualify h2 as a new candidate. |
| Provenance names h1 while the consumer receives h2. | Artifact/provenance correspondence fails. | Stop the dependent authenticity claim and inspect the mismatch. |
| Provenance is correctly signed but names an unexpected builder or source. | Signature validity does not meet the consumer's expectation. | Resolve the unexpected origin through the configured trust decision. |
| The verifier is unavailable. | This attempt yields no verification result. | Use an applicable earlier result if the controlled chain covers this delivery. Otherwise restore verification or obtain an explicit bounded exception. |

For the normal branch, the consumer obtains the retained h1 bytes through the supported artifact store. The expected identity comes from the qualified build/evidence result, not merely from the same mutable label used for downloading. The consumer verifies the required identity and authenticity conditions. Destination configuration c2 remains separate and has not yet been exercised in a runtime.

The consumer has h1 with the named applicable evidence for the intended next use. To establish runtime usability, the operator uses SYSE.41 to install h1 with c2, observe the target state and perform the bounded deployment test. An application-form defect not covered by the earlier tests remains possible.

In the adverse branch, the staging system insists on rebuilding. The team can either change that delivery mechanism to consume retained h1 or explicitly qualify h2. It cannot retain the claim of unchanged-artifact promotion while taking the second route. If the old artifact is no longer retrievable, the first route is unavailable even though its digest and logs remain.

A second supplier signs a package with a valid key, but the supplied build uses an unapproved source location. Automatic acceptance based only on signature success would admit the wrong origin. The consumer rejects this build for its unapproved source despite the valid signature.

The test result concerns the artifact it exercised. Installation, target configuration, authenticity and release each need their own grounds.

### SYSE.32:6 - Bias-Annotation

Teams can mistake familiar version names, a green pipeline or a prestigious builder label for evidence. Consumer trust expectations can also be so broad that verification accepts nearly anything the supplier signs. Inspect the consequential mismatch cases and the origin of the expectation, not only the success path.

### SYSE.32:7 - Conformance Checklist

- The artifact identity covers the actual bytes or object form used by the consumer.
- Relied-on evidence concerns that artifact and remains applicable to the intended claim.
- Destination configuration is separate, or a changed artifact is openly treated as a new candidate.
- Transfer does not silently rebuild, substitute or relabel the result.
- Required authenticity uses configured trust and artifact/provenance correspondence, not signature success alone.
- Missing, invalid, unexpected and unavailable results remain distinguishable.
- The promotion basis does not claim actual runtime usability or release permission.

### SYSE.32:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Rebuild the same source in every stage and reuse the first test result. | Carry the tested artifact, or qualify each different output on its own basis. |
| Compare two mutable labels. | Compare the delivered artifact against a qualified expected identity. |
| Accept any correctly signed provenance. | Apply the consumer's expected origin, build and trust conditions as well. |
| Treat a missing verifier result as a successful control. | Expose the missing assurance and its dependent stop or authorized limitation. |

### SYSE.32:9 - Consequences

The pattern can reduce unnoticed substitution and avoid unnecessary rebuilding between environments. It requires artifact retention, evidence attribution and maintained trust expectations. It can expose that an apparently convenient delivery mechanism changes the candidate at every stage; repairing that mechanism or qualifying each output costs work.

### SYSE.32:10 - Rationale

Evidence travels through a valid subject-and-condition relationship, not through a shared label. Preserving the artifact makes that relationship easier to maintain. Separating destination configuration and actual deployment prevents a successful storage operation from standing in for an observed running System.

### SYSE.32:11 - SoTA-Echoing

For artifact origin and integrity, **adopt** the consumer procedure in [SLSA v1.2 Verifying artifacts](https://slsa.dev/spec/v1.2/verifying-artifacts), including configured trust and expectations. The procedure checks the delivered artifact against the provenance subject and the expected build, in addition to verifying the signature. Section 4.4 uses those checks for the origin claim. Application behavior requires its own evidence.

For promotion, **adopt and adapt** the same-artifact practice in [DORA Deployment automation](https://dora.dev/capabilities/deployment-automation/) and the [Continuous Delivery pipeline](https://continuousdelivery.com/implementing/patterns/). Rebuilding per target can supply legitimately different outputs, but each then needs its own applicable evidence. Section 4.6 follows verification through the last mutable selection. For a multi-platform package, identify the selected member and reuse the evidence applicable to that member or to the package as a whole.

Compare consumer verification with a qualified shared verification boundary by substitution risk, trust, freshness and cost. Reopen reliance when packaging, retention, consumer selection, trust roots or applicable conditions change. An unchanged artifact identity does not imply unchanged permission to use it.

### SYSE.32:12 - Relations

SYSE.30 supplies the build result and its inputs; SYSE.31 supplies engineering feedback. SYSE.13 identifies the artifact/configuration combination, and SYSE.28 places controls at the relying boundary. An operator can use the promotion result for deployment under SYSE.41. SYSE.4 governs evidence reliance, and SYSE.14 governs release.

### SYSE.32:End
