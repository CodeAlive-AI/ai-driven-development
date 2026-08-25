# Specialized app and storefront branches

Apply every branch that matches. These checks supplement the core review and often require current legal, licensing, entitlement, or regional evidence. Do not declare legal compliance from code inspection alone.

## Kids Category and child-facing apps

- Confirm category choice, age range, immutable post-approval implications, parental gates, links/purchases, and advertising/analytics restrictions.
- Map all minor data, persistent identifiers, chat/UGC, photos/video/drawings, AI prompts/outputs, location, and provider sharing.
- Require applicable parental consent and child-privacy evidence.
- Test age-gate bypass and useful experience across ages.
- Metadata outside Kids Category must not misleadingly use “for kids/children” or equivalent child-primary presentation.

## Health, medical, wellness, and research

- Classify wellness information versus diagnosis/treatment/medical device/research.
- Require methodology and substantiation for measurements/accuracy claims.
- Prevent false sensor-based measurements and unsafe emergency reliance.
- Provide clinician consultation context and escalation where appropriate.
- Verify HealthKit data restrictions, iCloud handling, research consent, ethics approval, and legal entity/regulatory fields.
- Apply regional medical-device status and safety/contact requirements where current agreements/App Store Connect require them.
- Apply high-impact AI controls.

## Finance, investing, insurance, lending, and crypto

- Require submission by the relevant institution/legal entity when the rule applies, licenses, countries, disclosures, custody, KYC/AML, and support.
- Test price/market freshness, transaction confirmation, account security, and no guaranteed-return claims.
- Apply high-impact AI controls for recommendations/eligibility.
- Crypto: no on-device mining; review exchange/wallet/NFT functions, purchase treatment, region, and licensed entity.

## Gambling, betting, lotteries, contests, and sweepstakes

- Separate real-money gambling, simulated gambling, loot boxes, contests, sweepstakes, raffles, fantasy sports, and prediction markets.
- Verify license, legal entity, free-app requirement, geofencing, age rating, responsible-gaming disclosures, official rules, and Apple non-sponsorship.
- Do not use IAP to buy credit/currency for real-money gaming.
- For Brazil fixed-odds betting, require current SPA license details/supporting documents and correct App Review Information for the submitted version.
- Review Australia, Brazil, Korea, Vietnam, and other region-specific ratings.

## VPN

- Organization-account submission and required Network Extension APIs/entitlements.
- Clear data collection/use disclosure before purchase/use.
- No sale/use/disclosure of VPN traffic data contrary to current rule.
- Local licensing and unavailable-country handling.
- Test connection, disconnect, kill-switch claims, DNS/leak claims, subscription, and failure recovery.

## MDM/device management

- Organization account, Apple-granted entitlement, legitimate device-management purpose, and current terms.
- Privacy policy commitment not to sell/use/disclose user/device/app data for unrelated purposes.
- Restrict analytics to permitted performance data where applicable.
- Test enrollment/removal, consent, managed/unmanaged boundaries, and destructive commands.

## Browsers and web content

- Distinguish ordinary WebView content, reader content, browser engine entitlement, and 4.7 software.
- Review minimum functionality for website wrappers and link/content aggregators.
- Verify safe browsing, downloads, permissions, parental/age controls, external purchase behavior, and default-app/engine entitlement terms where applicable.
- Third-party sites/services require authorization and privacy/UGC review.

## Remote desktop and cloud gaming

- Apply the exact remote-desktop restrictions, host ownership/network, execution location, account creation/management, UI/store limitations, and thin-client prohibition.
- Cloud/streamed games and game subscriptions require current 4.7, IAP, catalog/index, age, controller, and content rules.
- Test latency/failure, host unavailable, input methods, and purchase boundary.

## Mini apps, HTML5 games, plug-ins, chatbots, and software catalogs

Apply current Guideline 4.7:

- Software/content safety and UGC controls.
- Compliance with payments for digital value.
- No unauthorized exposure/extension of native platform APIs.
- Index/metadata and universal links for offered software where required.
- Per-software permission/data-sharing controls.
- Identification and age restriction for content exceeding the host rating.
- Reviewability of the catalog and dynamic changes.

AI chatbot catalogs and agent marketplaces can trigger both 4.7 and AI/privacy branches.

## UGC, social networking, dating, and creator content

- Filtering, report, block, published contact, timely response, terms/community standards, moderator tooling, and repeat-offender controls.
- Random/anonymous chat, bullying, threats, objectification, pornographic use, and dating/hookup risk.
- Creator monetization and purchase labels.
- Age identification/restriction for content above app rating.
- Social-media age-question answers; under-13 disabling behavior where declared.
- AI-generated public content follows the same controls.

## News, books, media, music, and third-party content

- Rights/licenses, API/service terms, streaming/download authorization, attribution, takedown process, and regional availability.
- Reader-app/multiplatform purchase exception only when qualified.
- Minimum functionality for feeds, guides, link collections, or a single book/song/movie.
- AI summaries/translations do not erase source rights or accuracy duties.

## Education, employment, housing, and insurance

- Organization/consumer account classification and purchase treatment.
- Child/student privacy and institutional authorization.
- High-impact AI: bias/proxy testing, human review, appeal/correction, source/uncertainty, no automatic consequential decision without appropriate safeguards.
- Credential/certification and outcome claims need substantiation.

## Government, identity, and citizen services

- Authorized legal entity/agency or documented permission.
- Sensitive identity/biometric/security review.
- Government-backed login exception facts.
- No misleading official endorsement or imitation.
- Accessibility, offline/failure, and support for consequential tasks.

## Location, navigation, aviation, automotive, drones, and IoT

- Direct relevance and informed location permission.
- Do not represent location as suitable for emergency services where prohibited.
- Autonomous control, vehicle, aircraft, and safety features receive physical-harm/legal review.
- Hardware ownership, connectivity loss, firmware mismatch, background use, and reviewer hardware instructions.
- Aviation/automotive apps may need legal entity, data accuracy, and specialist evidence.

## macOS

- Sandbox and correct file-access APIs; no third-party installer in Mac App Store build.
- Self-contained app; no unauthorized shared-location installation or downloaded code.
- Consent for login items/background processes; clean quit/uninstall behavior.
- Remove `com.apple.quarantine` recursively before upload.
- Signatures, hardened runtime/entitlements, helper tools, updates, and receipt validation.

## tvOS

- Core use with Siri Remote unless controller requirement is clearly disclosed.
- Focus engine, overscan/readability, login, purchase, media rights, and controller behavior.

## watchOS

- Current architecture/SDK, paired versus independent behavior, account/purchase boundary, HealthKit, complications, background tasks, and phone-unavailable states.

## visionOS

- Spatial comfort, locomotion/safety, permissions, immersion transitions, input alternatives, unsupported Kids Category behavior, and accurate screenshots/previews.

## Extensions, widgets, keyboards, Safari extensions, and App Clips

- Host app provides appropriate value and clearly explains extension.
- Least-privilege data/container sharing and revoked-access behavior.
- Keyboard full-access justification/privacy; no secret collection.
- Safari extension website scope is minimal and current Safari compatible.
- Widget/notification does not expose sensitive data.
- App Clip size/function/payment/login/location constraints and transition to full app.

## Enterprise, B2B, custom apps, and unlisted distribution

- Confirm correct distribution channel rather than public App Store by default.
- Account access, organization contracts, employee/student audience, and consumer availability determine payment/login exceptions.
- Public metadata must not claim access unavailable to ordinary users without explanation.

## Regional/storefront checklist

For every selected storefront inspect:

- Legal availability and licenses.
- Age ratings and descriptors.
- External purchase/link entitlement and wording.
- Trader/developer identity fields.
- Price, tax, currency, subscription/product availability.
- Privacy/consent localization and data region.
- Export/sanctions/content limitations.

Never copy a storefront conclusion to all regions without checking current terms.
