# App Review rule and evidence matrix

Use this matrix after scope classification. It is a routing aid, not a substitute for reading the current official text. Mark every applicable row `PASS`, `OPEN`, `NEEDS_REVIEW`, or `NOT_APPLICABLE` with evidence.

## 1 — Safety

| Area | Trigger | Required evidence/tests | Typical release finding |
|---|---|---|---|
| 1.1 objectionable content | Static, UGC, web, creator, or AI content | Content inventory; worst-case paths; moderation/output tests; age rationale | Reachable prohibited or materially under-rated content |
| 1.2 UGC/social | Posting, chat, profiles, comments, sharing, public AI output | Filtering; report; block; published contact; response SLA; ban/evasion controls; child safeguards | Any required abuse control absent or nonfunctional |
| 1.2.1 creator content | Non-developer-created experiences/content | Moderation; purchase labels; content-age mechanism; content cannot alter native core | Unbounded executable/app-like content without 4.7 compliance |
| 1.3 Kids Category | Kids category or child-directed presentation | Parental gates; no prohibited third-party analytics/ads; minor-data map; external-link/purchase gates | Child data transmitted or kids metadata used outside category |
| 1.4 physical harm | Medical, emergency, autonomous control, dangerous activity | Accuracy/methodology; regulatory evidence; professional escalation; device limits | Unsupported diagnostic/safety claim or harmful behavior |
| 1.5 developer information | Support/contact/user-facing identity | Reachable support; current legal entity/contact | Missing or false contact information |
| 1.6 data security | Accounts, personal/sensitive data, payment, credentials | Threat model; encryption; auth/session tests; secret scan; deletion; incident controls | Exposed secret, cross-account access, insecure transport |

## 2 — Performance

| Area | Trigger | Required evidence/tests | Typical release finding |
|---|---|---|---|
| 2.1 completeness | Every submission | Clean install/launch; production backend; demo access; complete metadata; IAP visible; no placeholders | Crash, broken login/backend, missing product, hidden feature |
| 2.2 beta testing | Beta labels, incomplete experiments | Remove beta/trial placeholders from production; use TestFlight for beta | App is materially unfinished or marketed as beta |
| 2.3 metadata | Every submission | Claim matrix across binary, runtime, metadata, screenshots, privacy, age, payment | Misleading capability, stale screenshot, keyword stuffing |
| 2.4 hardware/software compatibility | Device APIs, background, power, Mac sandbox | Device matrix; resource behavior; sandbox; current OS; no unrelated background work | Unsupported device path, excessive background behavior |
| 2.5 software requirements | Dynamic code, private APIs, browser engines, extensions | Linked API inspection; code-loading map; entitlement proof; 4.7 branch | Private API, impermissible downloaded code, hidden behavior |

## 3 — Business

| Area | Trigger | Required evidence/tests | Typical release finding |
|---|---|---|---|
| 3.1.1 IAP | Digital content/features/credits | Product export; submitted status; Sandbox purchase/restore; entitlement tests | External checkout or unavailable/unsubmitted IAP |
| 3.1.2 subscriptions | Auto-renewing access | Duration, price, benefit, renewal/cancel terms; EULA/privacy; restore/manage; state transitions | Unclear value/price, missing disclosures, nonfunctional restore |
| 3.1.3 exceptions | Reader, multiplatform, enterprise, person-to-person, physical | Exact exception qualification; storefront/legal-entity evidence | Exception claimed without satisfying its elements |
| 3.1.4 hardware-specific content | Hardware-tied features | Hardware ownership/use and unlock behavior | Using hardware purchase to bypass IAP for ordinary digital value |
| 3.1.5 crypto | Wallet/exchange/mining/NFT | Legal entity, licenses, region, custody/data flow, purchase treatment | Unlicensed exchange, on-device mining, prohibited purchase scheme |
| 3.2 other business issues | Ads, fundraising, regulated finance, catalogs | Entity/license, nonprofit approval, editorial value, ad behavior | Predominantly ads, unapproved fundraising, unlicensed finance |

## 4 — Design

| Area | Trigger | Required evidence/tests | Typical release finding |
|---|---|---|---|
| 4.1 copycats | Similar name/icon/UI/features | Trademark/right evidence; differentiation; competitor comparison | Impersonation, copied icon/name, deceptive metadata |
| 4.2 minimum functionality | WebView, link/content aggregator, thin AI wrapper, simple utility | Native-value dossier; native workflows; durable utility; original content/rights | Repackaged website, links/marketing, insufficient utility |
| 4.2.6 templates | Generated/white-label apps | Content-owner submission; meaningful customization; single-binary model where appropriate | Template provider submits near-identical client apps |
| 4.3 spam | Multiple similar apps or saturated categories | Portfolio comparison; unique audience/function/content | Duplicate bundle IDs, category spam, generic clone |
| 4.4 extensions | Keyboard/Safari/other extensions | Extension-specific behavior, permissions, host app value, data disclosure | Overbroad access, misleading extension, poor host app |
| 4.5 Apple sites/services | Game Center, Apple Music, Weather, emoji, review prompts | Correct APIs, attribution, branding, terms | Custom review prompt, unauthorized Apple asset/use |
| 4.7 software/mini apps/chatbots | Software not embedded in binary, HTML5 apps, plug-ins, chatbot | Index/universal links; filtering/reporting/blocking; per-instance permissions; IAP; age controls; API isolation | Unindexed software, unsafe content, native API exposure |
| 4.8 login services | Third-party/social primary account login | Equivalent privacy-preserving login or documented exception; deletion/revocation | Google/Facebook/X login without equivalent option |
| 4.9 Apple Pay | Apple Pay or recurring payment | Material purchase terms; correct branding; recurring disclosures | Missing recurring terms or misleading Apple Pay UI |
| 4.10 monetizing built-ins | Paid access to system capabilities | Product-value analysis | Charging solely for Apple-provided functionality |

## 5 — Legal

| Area | Trigger | Required evidence/tests | Typical release finding |
|---|---|---|---|
| 5.1.1 privacy | Any data/permission/account | In-app and metadata privacy policy; collection/use/retention/deletion; consent; minimization | Policy missing/incomplete, coercive access, no deletion |
| 5.1.2 use/sharing | Third parties, ads, AI, research | Recipient/data/purpose map; explicit permission where required; provider controls | Personal data shared with AI before explicit permission |
| 5.1.3 health research | HealthKit/research | Permitted use; consent; ethics approval; no prohibited advertising/data use | Health data used for ads or unsupported research |
| 5.1.4 kids | Minor data | Applicable child-privacy compliance and parental consent evidence | Personal data from minors mishandled |
| 5.1.5 location | Location | Direct relevance; consent; purpose string; fallback | Unnecessary location or emergency/autonomous misuse |
| 5.2 IP | Third-party brands/content/services/media | Licenses, API terms, authorization, takedown process | Unlicensed content, download/conversion, Apple endorsement |
| 5.3 gambling/lottery | Betting, sweepstakes, contests, simulated gambling | Licenses, geofencing, free app, rules, age rating, no IAP for real-money credits | Unlicensed/unrestricted gambling or missing rules |
| 5.4 VPN | VPN service | Organization account; NEVPNManager; data-use restrictions; local licenses | Individual submission or data monetization |
| 5.5 MDM | Device management | Organization account; entitlement; restricted data use; privacy commitment | Unauthorized MDM or third-party data use |
| 5.6 conduct | Developer identity/reviews/discovery/quality | Accurate identity; no manipulation; quality/refund monitoring | Fake reviews, discovery manipulation, misleading identity |

## Submission requirement overlays

These are not always numbered App Review Guidelines but can prevent upload or approval:

| Requirement | Evidence |
|---|---|
| Xcode 26 / platform SDK 26 minimum | Archive `DTXcode`, `DTSDKName`, SDK build, upload validation |
| Required-reason APIs | App and embedded manifests; API-to-reason mapping; reason truthfulness review |
| Listed third-party SDK privacy manifests/signatures | Embedded dependency inventory; manifests; signed origin/version evidence |
| Screenshot formats and dimensions | Exact deterministic image scan; locale/device coverage; 1–10 per display class |
| Age-rating questionnaire | Export/screenshot of answers; worst reachable content; regional rating review |
| EU DSA trader status | App Store Connect account/storefront evidence where distribution includes EU |
| macOS quarantine attribute | Recursive archive inspection for `com.apple.quarantine` |
| Game Center configuration | Entitlement plus App Store Connect configuration |
| Regional regulated fields | Current App Store Connect fields, licenses, legal entity, safety/contact data |

## Evidence strength

### Capacitor source/generated/submitted parity

For detected Capacitor apps, map stale or missing bundled assets and broken bridge/deep links to 2.1; screenshot/build drift to 2.3; remote `server.url` or downloaded runtime to 2.5.2 and only factually applicable 4.7 analysis; a product proven to be merely a repackaged website to 4.2; digital web checkout/unlock to 3.1; listed SDK/plugin manifest issues to third-party SDK requirements and 5.1; and plugin data sent to third-party AI to 5.1.1/5.1.2. The framework name itself supports none of these findings.

Evidence class `source/generated/submitted parity` requires named paths and hashes. Missing final-bundle evidence cannot pass config, asset, plugin, privacy, identity, or origin parity.

Use the strongest available evidence:

1. Hash-matched final archive/binary and App Store Connect export.
2. Reproducible clean-install runtime record with device, OS, build, steps, logs, and screenshots.
3. Source/configuration inspection tied to the release commit and dependency lockfiles.
4. Signed provider, legal, license, policy, or agreement documentation.
5. Manual or AI visual/semantic review with exact artifact hashes.
6. Developer statement without independent evidence.
7. Community anecdote.

A lower-tier item may trigger investigation but should not override contradictory higher-tier evidence without explaining the conflict.
