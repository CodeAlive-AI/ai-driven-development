import XCTest

/// Template release-review suite.
///
/// Before use:
/// 1. Add stable accessibility identifiers to the app. Do not navigate by
///    localized labels when an identifier is possible.
/// 2. Replace every `REPLACE_...` identifier with the real identifier.
/// 3. Instrument a UI-testing-only request ledger for assertions that must
///    prove no third-party AI request occurred. Never ship test credentials or
///    privileged bypasses in the production build.
/// 4. Run this target against Release configuration and the exact review backend.
final class AppReviewUITests: XCTestCase {
    private var app: XCUIApplication!

    override func setUpWithError() throws {
        continueAfterFailure = false
        app = XCUIApplication()
        app.launchArguments += ["-ui-testing", "-app-review-evidence"]
        app.launchEnvironment["UITEST_DISABLE_ANIMATIONS"] = "1"
    }

    private func launchFresh(additionalArguments: [String] = []) {
        app.launchArguments += additionalArguments
        app.launch()
        XCTAssertTrue(app.wait(for: .runningForeground, timeout: 20), "App did not reach foreground")
        add(XCTAttachment(screenshot: XCUIScreen.main.screenshot()), name: "launch")
    }

    private func element(_ identifier: String, timeout: TimeInterval = 12) -> XCUIElement {
        let element = app.descendants(matching: .any)[identifier]
        XCTAssertTrue(element.waitForExistence(timeout: timeout), "Missing UI element: \(identifier)")
        return element
    }

    private func tap(_ identifier: String, timeout: TimeInterval = 12) {
        let target = element(identifier, timeout: timeout)
        XCTAssertTrue(target.isHittable, "Element is not hittable: \(identifier)")
        target.tap()
    }

    private func attach(_ name: String) {
        let attachment = XCTAttachment(screenshot: XCUIScreen.main.screenshot())
        attachment.name = name
        attachment.lifetime = .keepAlways
        add(attachment)
    }

    private func typeSecretFromEnvironment(named variable: String, into identifier: String) throws {
        guard let value = ProcessInfo.processInfo.environment[variable], !value.isEmpty else {
            throw XCTSkip("Environment variable \(variable) is not loaded")
        }
        let field = element(identifier)
        field.tap()
        field.typeText(value)
    }

    /// Mandatory: demonstrates a clean-install path from launch to the primary
    /// advertised utility. Keep this bounded and deterministic.
    func testReviewerJourney() throws {
        launchFresh(additionalArguments: ["-reset-review-state"])

        if app.descendants(matching: .any)["REPLACE_ONBOARDING_CONTINUE"].waitForExistence(timeout: 2) {
            tap("REPLACE_ONBOARDING_CONTINUE")
        }

        if app.descendants(matching: .any)["REPLACE_LOGIN_USERNAME"].waitForExistence(timeout: 2) {
            try typeSecretFromEnvironment(named: "APP_REVIEW_USERNAME", into: "REPLACE_LOGIN_USERNAME")
            try typeSecretFromEnvironment(named: "APP_REVIEW_PASSWORD", into: "REPLACE_LOGIN_PASSWORD")
            tap("REPLACE_LOGIN_SUBMIT")
        }

        XCTAssertTrue(element("REPLACE_HOME_READY").exists)
        tap("REPLACE_PRIMARY_ACTION")
        XCTAssertTrue(element("REPLACE_PRIMARY_RESULT").exists)
        attach("reviewer-journey-primary-result")
    }

    /// Mandatory for third-party AI receiving personal data: declining consent
    /// must keep the covered request count at zero.
    func testAIConsentDeniedSendsNoData() throws {
        launchFresh(additionalArguments: ["-reset-ai-consent", "-reset-ai-request-ledger"])
        tap("REPLACE_AI_ENTRY")
        XCTAssertTrue(element("REPLACE_AI_CONSENT_DISCLOSURE").exists)
        tap("REPLACE_AI_CONSENT_DECLINE")

        // Attempt the feature after denial. The app should stay coherent and
        // must not transmit covered data.
        tap("REPLACE_AI_GENERATE")
        XCTAssertTrue(element("REPLACE_AI_DISABLED_OR_LOCAL_FALLBACK").exists)

        let countLabel = element("REPLACE_AI_REQUEST_LEDGER_COUNT")
        XCTAssertEqual(countLabel.label, "0", "AI provider request occurred after consent denial")
        attach("ai-consent-denied")
    }

    /// Verify that accepting consent enables only the disclosed request path.
    func testAIConsentAcceptedUsesDisclosedProvider() throws {
        launchFresh(additionalArguments: ["-reset-ai-consent", "-reset-ai-request-ledger"])
        tap("REPLACE_AI_ENTRY")
        XCTAssertTrue(element("REPLACE_AI_CONSENT_DISCLOSURE").exists)
        XCTAssertTrue(element("REPLACE_AI_PROVIDER_NAME").exists)
        XCTAssertTrue(element("REPLACE_AI_DATA_CATEGORIES").exists)
        tap("REPLACE_AI_CONSENT_ACCEPT")
        tap("REPLACE_AI_GENERATE")
        XCTAssertTrue(element("REPLACE_AI_RESULT").waitForExistence(timeout: 30))
        attach("ai-consent-accepted-result")
    }

    func testAccountDeletionEntryPoint() throws {
        launchFresh()
        tap("REPLACE_SETTINGS_ENTRY")
        tap("REPLACE_ACCOUNT_ENTRY")
        XCTAssertTrue(element("REPLACE_DELETE_ACCOUNT_ENTRY").exists)
        tap("REPLACE_DELETE_ACCOUNT_ENTRY")
        XCTAssertTrue(element("REPLACE_DELETE_SCOPE_AND_TIMING").exists)
        attach("account-deletion-confirmation")
        // Do not complete deletion in a shared account unless the fixture is
        // disposable and the backend is reset between executions.
    }

    func testPermissionDenialRecovery() throws {
        launchFresh(additionalArguments: ["-reset-permission-demo"])
        tap("REPLACE_PERMISSION_FEATURE")
        XCTAssertTrue(element("REPLACE_PERMISSION_CONTEXT").exists)
        tap("REPLACE_PERMISSION_DECLINE_OR_SIMULATED_DENIAL")
        XCTAssertTrue(element("REPLACE_PERMISSION_DENIED_RECOVERY").exists)
        attach("permission-denial-recovery")
    }

    func testPurchaseRestoreSurface() throws {
        launchFresh()
        tap("REPLACE_PAYWALL_ENTRY")
        XCTAssertTrue(element("REPLACE_PRODUCT_PRICE").exists)
        XCTAssertTrue(element("REPLACE_SUBSCRIPTION_TERMS").exists)
        XCTAssertTrue(element("REPLACE_RESTORE_PURCHASES").exists)
        XCTAssertTrue(element("REPLACE_MANAGE_SUBSCRIPTION").exists)
        attach("paywall-and-restore")
    }
}
