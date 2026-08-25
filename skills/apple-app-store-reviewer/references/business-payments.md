# Business model, In-App Purchase, subscriptions, and external purchase paths

Read this reference whenever the app charges money, unlocks value, uses credits/tokens, links to purchase, sells services, or depends on an existing entitlement.

## Classify the transaction first

For every paid item record:

- What the user receives.
- Where it is consumed or used.
- Seller/legal entity.
- One-time, consumable, non-consumable, subscription, rental, gift, donation, physical good/service, person-to-person service, enterprise contract, or reader entitlement.
- Storefronts and entitlements.
- Whether purchase can be initiated, called to action, or merely accessed in app.
- Whether the same entitlement exists on other platforms.

Do not choose payment treatment based only on the processor name. A Stripe checkout can be appropriate for a physical service and inappropriate for ordinary in-app digital features.

## Digital goods and services

Ordinary digital content, features, functionality, premium access, subscriptions, and in-app currencies consumed in the app normally require In-App Purchase unless a current exception/entitlement applies.

Review for bypass patterns:

- Web checkout, QR code, deep link, support message, chatbot instruction, account-credit top-up, crypto/NFT mechanism, or remote configuration that unlocks digital value.
- Price comparison or call to action outside permitted storefront/entitlement terms.
- “Free” app whose only useful function requires an external purchase.
- Hardware/physical purchase used as a pretext for unrelated digital unlock.

Storefront rules can differ. Never generalize U.S., EEA, reader-app, music-streaming, or entitlement treatment globally without current official terms.

## IAP evidence pack

Require an App Store Connect export or screenshots for every product:

- Product ID, reference name, type, group, duration, price tier/storefront price, localization, review screenshot, status, availability, and version attachment/submission state.
- Offer codes, introductory/promotional offers, family sharing, subscription levels, grace period, billing retry, and server notifications where used.
- Matching StoreKit identifiers in source/server configuration.
- Sandbox request and entitlement logs.

The app binary, App Store Connect product, paywall, metadata, and review notes must agree exactly.

## Runtime purchase tests

Use the matrix in `references/runtime-review.md`. A release pass requires relevant cases such as:

- Products load from App Store/Sandbox, not only local StoreKit configuration.
- Purchase, cancel sheet, pending/Ask to Buy, network interruption, duplicate tap, verification failure.
- Restore after reinstall and account/device changes.
- Subscription expiration, renewal, billing retry, grace period, refund/revocation, upgrade/downgrade/crossgrade.
- Server-to-server/App Store Server Notification reconciliation.
- Manage subscription and support.
- App-account deletion while an Apple subscription remains active.

Record exact product IDs and environment without exposing receipts or credentials.

## Subscription presentation

Before purchase, clearly communicate:

- What the user receives.
- Subscription duration and billing cadence.
- Price and per-period unit where relevant.
- Free/introductory trial length and post-trial price.
- Auto-renewal and cancellation/management route.
- Any commitment, installment, or eligibility condition.
- Links to privacy policy and Terms of Use/EULA in the appropriate product-page/paywall context.

Avoid deceptive urgency, hidden close buttons, unreadable legal copy, ambiguous “continue,” default selection that obscures cost, and claims that cancellation is possible inside the app when it is not.

For monthly subscriptions with a 12-month commitment or other newer product forms, verify current storefront availability, OS support, commitment disclosures, cancellation effect, and App Store Connect configuration.

## Credits, tokens, and AI usage

Classify credits by what they purchase. For digital AI generations or features:

- Credits normally follow digital-goods payment treatment.
- Purchased credits must not expire contrary to applicable rule/terms.
- Show balance, consumption unit, failed-generation/refund behavior, and restore/server reconciliation.
- Do not silently consume credit on provider error, moderation refusal, or duplicate request.
- Public/community creator payments require both IAP and UGC/creator-content review as applicable.

A token called “compute,” “coin,” or “API balance” does not change its economic function.

## Exceptions and special categories

### Physical goods/services

Use an appropriate non-IAP payment method when payment is for a physical good or service consumed outside the app. Verify the digital app does not add an unrelated paid unlock and that refunds/support are clear.

### Person-to-person real-time services

Document that the paid service is genuinely between two individuals in real time and meets the current exception. One-to-many, recorded, automated, or AI-delivered content may not qualify.

### Enterprise services

Document that access is sold directly to organizations for employees/students and is not ordinary consumer access. Review signup and external call-to-action separately.

### Reader/multiplatform services

Document the content/service type, existing account behavior, cross-platform entitlement, allowed communication/link entitlement, and storefront coverage. Do not add an in-app signup/checkout path that exceeds the exception.

### Donations/gifts/fundraising

Separate approved nonprofit fundraising, person-to-person gifts with 100% transfer, tips tied to digital content, and charitable collection. Require current approval and exact money flow.

### Regulated finance/crypto/gambling

Apply legal-entity, licensing, geofencing, age, and product restrictions. Do not treat IAP compliance as sufficient legal compliance.

## Metadata and screenshot consistency

Check:

- “Free,” “lifetime,” discounts, trial, “cancel anytime,” and savings calculations.
- Product names and benefit tiers.
- Storefront currency/localization.
- Paywall and submitted review screenshot.
- Restore/manage/cancel claims.
- External purchase wording and entitlement/storefront.

A stale price/trial screenshot can be materially misleading even when the purchase API works.

## Reviewer notes

List exact taps to each paywall/product, product IDs, Sandbox account setup if special, restore/manage paths, and any unavailable product with a truthful reason. Confirm that all products intended for review were submitted with the version.
