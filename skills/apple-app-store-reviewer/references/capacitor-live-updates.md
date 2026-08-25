# Capacitor live-update branch

Load only when Appflow, Capgo, Capawesome, another OTA package, a remote web-bundle manifest, asset-path replacement, archive extraction, web-root switching, or custom update bootstrap is detected.

Live updates are not automatically rejected, and vendor statements that they are “App Store compliant” are not Apple authority. Make the following mandatory:

- provider/package versions, channel, environment, rollout, audit log, and kill switch;
- final bundled baseline asset manifest and every downloaded bundle hash;
- cryptographic signature or integrity validation, trusted-key rotation, TLS, and rejection of tampering;
- bundled fallback, startup-timeout recovery, rollback, revoked/corrupt/unavailable/incompatible update tests;
- native-version compatibility constraints and proof that updates cannot add plugins, native code, entitlements, or new privileged bridge APIs;
- exact description of which reviewed functionality and content may change remotely;
- current Guideline 2.5.2 analysis and Guideline 4.7 analysis only where the actual remote-software model fits;
- reviewer notes that candidly describe the mechanism.

Test with the update service unavailable and prove the submitted bundle remains useful. Record shipped/downloaded hashes, integrity verdict, selected channel, failure behavior, rollback target, and runtime screenshots/logs. A remote update cannot repair an incomplete or misleading submitted binary.

Missing policy, integrity, or rollback evidence prevents `READY FOR SUBMISSION` through `capacitor.live-update-policy`, `capacitor.live-update-integrity`, and `capacitor.live-update-rollback`.
