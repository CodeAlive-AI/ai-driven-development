# Source index and refresh map

`source-catalog.json` is the executable catalog. This file explains what each source controls and how to refresh it. Official URLs are primary; community URLs are observations only.

## Official policy and submission sources

| Source | URL | Controls |
|---|---|---|
| App Review Guidelines | `https://developer.apple.com/app-store/review/guidelines/` | Core safety, performance, business, design, legal rules; Last Updated date |
| Upcoming Requirements | `https://developer.apple.com/news/upcoming-requirements/` | Xcode/SDK upload minimums, age-rating deadlines, required-reason APIs, certificates, regional/account requirements |
| App Store Connect Help | `https://developer.apple.com/help/app-store-connect/` | Metadata, screenshots, products, subscriptions, App Privacy, review information, roles/statuses |
| Screenshot specifications | `https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications` | Accepted formats, alpha, counts, exact dimensions |
| Age rating values | `https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions/` | Global and regional values/descriptors |
| Set an app age rating | `https://developer.apple.com/help/app-store-connect/manage-app-information/set-an-app-age-rating/` | Questionnaire procedure and override behavior |
| Social-media age questions news | `https://developer.apple.com/news/?id=tlur8uvi` | July 2026 questionnaire addition and September 2026 enforcement |
| Third-party SDK requirements | `https://developer.apple.com/support/third-party-SDK-requirements/` | Current listed SDK manifest/signature set |
| Required-reason APIs | `https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api` | Declaration mechanics; link to current approved reasons |
| Privacy manifests overview | `https://developer.apple.com/documentation/bundleresources/privacy_manifest_files` | Manifest structure and aggregate behavior |
| Account deletion | `https://developer.apple.com/support/offering-account-deletion-in-your-app/` | In-app deletion implementation guidance |
| Generative AI HIG | `https://developer.apple.com/design/human-interface-guidelines/generative-ai` | Transparency, control, feedback, trust and interaction design |
| Foundation Models acceptable use | `https://developer.apple.com/apple-intelligence/acceptable-use-requirements-for-the-foundation-models-framework/` | Framework-specific prohibited/controlled use |
| Subscriptions | `https://developer.apple.com/app-store/subscriptions/` | Subscription product/presentation guidance |
| StoreKit testing | `https://developer.apple.com/documentation/storekit/testing-in-app-purchases-with-sandbox` | Sandbox runtime evidence |
| App privacy details | `https://developer.apple.com/app-store/app-privacy-details/` | App Privacy classification guidance |
| Human Interface Guidelines | `https://developer.apple.com/design/human-interface-guidelines/` | Platform design and interaction expectations |

For entitlements, storefront programs, browser engines, reader/external links, alternative distribution, and regulated categories, add the exact current entitlement/terms URL to the evidence package. These terms can change independently of the Guidelines.

## Capacitor framework sources

Capacitor qualification is a separate framework gate, not Apple policy. Refresh the v8 documentation root, 8.0 and 8.5 upgrade guides, workflow/configuration, iOS/SPM, privacy-manifest, security, deep-link, deployment, support-policy, and official release metadata before extending the tested range beyond `>=8.5.0 <9.0.0`. A material fingerprint change or future major produces `FRAMEWORK BASELINE UNVERIFIED`; it does not by itself make an older supported app violate Apple policy.

## Agent Skills sources

| Source | URL | Use |
|---|---|---|
| Best practices | `https://agentskills.io/skill-creation/best-practices` | Progressive disclosure, procedures, validators, reusable scripts, gotchas |
| Specification | `https://agentskills.io/specification` | Directory/frontmatter/field/validation requirements |
| Using scripts | `https://agentskills.io/skill-creation/using-scripts` | Script safety, interfaces, execution behavior |
| Evaluating skills | `https://agentskills.io/skill-creation/evaluating-skills` | Evals, assertions, iteration |

## Community and commercial sources

The exact observations and dates live in `source-catalog.json`. Current categories include:

- Apple Developer Forums: AI/photo/face data questions, privacy manifests, IAP submission, and operational review-delay reports.
- Reddit: minimum functionality, WebView/native-value, and developer rejection narratives.
- X: third-party AI consent/denial, thin-wrapper/4.3, submission completeness, 2.1 evidence requests, generative-content enforcement, storefront-specific metadata, and IAP commentary.
- Public commercial reviewer pages: Rork Reviewer, AcceptMyApp, NoReject AI, and related tools, used only to compare product capabilities.

When a post is deleted, inaccessible, unauthenticated, or available only as a search snippet, lower reliability and preserve only the minimal observation. Never quote private rejection correspondence unless the developer supplied it and permission permits its use.

## Refresh checklist

On each scheduled refresh:

1. Fetch all `required: true` official sources and compare fingerprints.
2. Parse the Guidelines Last Updated date.
3. Diff Upcoming Requirements and Apple Developer News since the prior baseline.
4. Refresh screenshot dimensions, metadata limits, age ratings, required-reason APIs, and listed SDKs.
5. Review App Store Connect help for product/status/schema changes.
6. Review AI/HIG/Foundation Models terms.
7. Sample current forum/Reddit/X reports; label date/reliability and do not infer frequency.
8. Update references, catalogs, scripts, fixtures, evals, and version.
9. Execute tests and a real release dry run.

## Source citation in findings

Every rule-based finding should include an official URL or a focused reference that resolves to one. A community URL may be added only as an explicitly anecdotal secondary source. Evidence is separate from source: the URL establishes the rule, while file/runtime evidence proves the app fact.
