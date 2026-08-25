# App Review notes — [APP NAME] [VERSION] ([BUILD])

## Review scope

- Platforms/device families: [LIST]
- Storefront or regional behavior relevant to this build: [NONE OR EXPLAIN]
- Release backend/environment: [IDENTIFIER; CONFIRM LIVE]
- Feature flags required for review: [NONE OR EXACT STATE]

## Demo access

- Account/role: [IDENTIFIER WITHOUT PASSWORD]
- Credentials: supplied in App Store Connect review fields through the approved secure mechanism.
- 2FA/email-link/device approval/captcha: [DISABLED/BYPASS DETAILS]
- Account expiry: [NON-EXPIRING]
- Preloaded data: [WHAT THE REVIEWER SHOULD SEE]

## Primary reviewer journey

1. [EXACT TAP]
2. [EXACT TAP]
3. [EXPECTED RESULT]

Material claims demonstrated by this path: [DESCRIPTION/SCREENSHOT CLAIMS]

## AI features

Delete this section only when no AI/ML feature exists.

- Feature and navigation: [EXACT PATH]
- Processing: [ON DEVICE / DEVELOPER BACKEND / THIRD-PARTY PROVIDER]
- Provider(s): [NAME]
- Data sent: [CATEGORIES]
- Purpose: [PURPOSE]
- Consent: [EXACT PATH; CONFIRM BEFORE FIRST TRANSMISSION]
- Decline behavior: [NO TRANSMISSION; FALLBACK/DISABLED STATE]
- Withdrawal path: [EXACT PATH]
- Retention/training: [PRECISE BEHAVIOR AND CONTROL]
- Public output/moderation: [NONE OR FILTER/REPORT/BLOCK DETAILS]
- Safe sample prompt: [PROMPT]
- High-impact limits/human review: [NONE OR EXPLAIN]

Attachment/evidence: [REQUEST-LEDGER RECORDING OR DATA-FLOW DIAGRAM]

## In-App Purchases and subscriptions

Delete this section only when no IAP/subscription exists.

| Product ID | Type/duration | Exact path | Review state |
|---|---|---|---|
| [ID] | [TYPE] | [TAPS] | [SUBMITTED WITH VERSION] |

- Restore purchases path: [TAPS]
- Manage subscription path: [TAPS]
- Introductory/trial/commitment behavior: [DETAILS]
- Special Sandbox setup: [NONE OR DETAILS]

## Account deletion

- Path: [EXACT TAPS]
- Reauthentication: [DETAILS]
- Scope and timing shown to user: [DETAILS]
- Active Apple subscription behavior: [DETAILS]
- Public content/provider data/legal retention: [DETAILS]

## Permissions, hardware, and special setup

- Protected permissions and exact feature trigger: [LIST]
- Required hardware/accessory: [NONE OR MODEL/SETUP]
- Location/region/account prerequisite: [NONE OR EXPLAIN]
- Extension/widget/VPN/MDM/regulated setup: [NONE OR EXPLAIN]

## Attachments

- [PHYSICAL-DEVICE SCREEN RECORDING OF PRIMARY JOURNEY]
- [TESTED DEVICE/OS MATRIX]
- [EXTERNAL SERVICES AND PURPOSES]
- [LICENSE/AUTHORIZATION]
- [DATA-FLOW OR METHODOLOGY]

## Known intentional behavior

[EXPLAIN ONLY NON-OBVIOUS BEHAVIOR. DO NOT DESCRIBE UNRESOLVED DEFECTS AS INTENTIONAL.]

## Review contact

- Name/role: [NAME]
- Contact: [CURRENT CONTACT]
- Availability/context: [OPTIONAL]
