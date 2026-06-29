# LifeOS Platform Feasibility Spike v0.1

Status: Review draft

Task: `LIFEOS-CODEX-005`

Research checked date: 2026-06-30

## Naming And Scope Constraints

- `LifeOS` is the team/company placeholder.
- `하루조각 / Daymark` are app-name placeholders.
- Do not finalize the brand name.
- Do not finalize React Native vs Flutter.
- This is not full MVP implementation.
- UI libraries do not solve app intervention permissions.
- This document focuses on OS-level feasibility, native-module implications, store-policy risk, and fallback product shape.

## 1. Executive Summary

LifeOS's core MVP depends on whether the app can show a pause/intervention experience before selected distracting apps open.

The ideal product experience is:

1. User selects distracting apps.
2. User attempts to open one of those apps.
3. LifeOS shows a warm pause/intervention experience.
4. User chooses to pause, continue, or record a protected moment.

The highest technical risk is not UI implementation. It is whether iOS and Android allow this type of app-open intervention in a reliable, store-compliant way.

Early read:

- iOS likely requires the Screen Time API family: `FamilyControls`, `DeviceActivity`, `ManagedSettings`, and shield-related extensions. This path has entitlement, App Review, privacy, and UX constraints.
- Android has more possible detection/intervention paths, but each carries tradeoffs: `UsageStatsManager` may be delayed/coarse; `AccessibilityService` may be powerful but has Play policy risk; overlays via `SYSTEM_ALERT_WINDOW` are sensitive and user-trust-heavy; background reliability varies by OS and OEM behavior.
- React Native and Flutter can both call native APIs, but either path needs native code. React Native + Expo likely requires development builds, config plugins, custom native modules, or bare/prebuild workflow. Flutter likely requires `MethodChannel` or custom plugins.
- The product must be designed with fallback modes from the beginning: notification/reminder fallback and manual protected-time logging fallback.

Recommended next step:

- Run a platform feasibility spike before full MVP build.
- Test Android first for fastest app-open detection/intervention learning.
- Test iOS Screen Time entitlement and shield flow in parallel, because iOS is likely the gating platform for the ideal experience.
- Do not choose React Native vs Flutter until both native feasibility and cross-platform integration effort are understood.

## 2. Primary Feasibility Question

Can LifeOS reliably and store-compliantly show a user-facing pause/intervention experience before selected distracting apps open on iOS and Android?

Sub-questions:

- Can selected apps be identified by the user?
- Can the OS detect or intercept an attempt to open selected apps?
- Can LifeOS display a custom pause/shield experience at that moment?
- Can the user choose a LifeOS action instead of opening the target app?
- Can LifeOS log the event without invasive data collection?
- Can the implementation pass App Store / Google Play review?
- If the ideal flow is blocked, what fallback flow still preserves the product direction?

## 3. iOS Feasibility Options

Primary official source: Apple's Screen Time API documentation states that the Screen Time framework suite includes `FamilyControls`, `ManagedSettings`, and `DeviceActivity` for apps that help people manage device use while preserving privacy. See [Apple Screen Time API documentation](https://developer.apple.com/documentation/screentimeapidocumentation).

### 3.1 FamilyControls

Official sources:

- [Family Controls documentation](https://developer.apple.com/documentation/familycontrols)
- [Configuring Family Controls](https://developer.apple.com/documentation/xcode/configuring-family-controls)
- [Requesting the Family Controls entitlement](https://developer.apple.com/documentation/familycontrols/requesting-the-family-controls-entitlement)

What it may enable:

- Ask the user for authorization through Screen Time APIs.
- Let the user select apps/categories/web domains using privacy-preserving tokens.
- Provide selected app/category tokens to other Screen Time framework pieces.

Why it matters for LifeOS:

- The app selection flow should ideally use Apple's privacy-preserving selection model instead of building a raw app inventory.
- It may support the user's intention to protect selected distracting apps.

Risks and unknowns:

- Distribution requires the Family Controls entitlement.
- Entitlement access and extension configuration may be the real blocker, not UI code.
- The API is privacy-preserving, so raw app identifiers or display names may not be available in every context.
- Need to confirm whether LifeOS's use case is acceptable as self-control/digital wellbeing, not only parental control.

Spike questions:

- Can a developer account request and receive the required Family Controls distribution entitlement for the main app and any needed extensions?
- Can a test device select target apps/categories with `FamilyActivityPicker`?
- Can selected tokens be persisted and shared safely with extensions?
- What app/category labels can LifeOS show in the UI without violating privacy constraints?

### 3.2 DeviceActivity

Official source: [Device Activity documentation](https://developer.apple.com/documentation/deviceactivity)

What it may enable:

- Monitor app, category, and web-domain activity in a privacy-preserving way.
- Use a Device Activity Monitor extension.
- Schedule monitoring windows and thresholds.

Why it matters for LifeOS:

- Could support monitoring selected distracting apps or activity categories.
- May help detect usage windows or thresholds.

Risks and unknowns:

- It may be better suited for monitoring usage and thresholds than a custom pre-open pause.
- Exact timing for "before app opens" may not match the ideal intervention.
- Extension targets and entitlements can add build/review complexity.

Spike questions:

- Can DeviceActivity trigger at a point useful enough for LifeOS's pause UX?
- Can it distinguish selected app/category activity in a privacy-safe way?
- Can it support near-real-time intervention, or only scheduled/threshold-based flows?
- What extension targets are required?

### 3.3 ManagedSettings

Official sources:

- [Managed Settings documentation](https://developer.apple.com/documentation/managedsettings)
- [ManagedSettingsStore documentation](https://developer.apple.com/documentation/managedsettings/managedsettingsstore)
- [ApplicationSettings documentation](https://developer.apple.com/documentation/managedsettings/applicationsettings)

What it may enable:

- Restrict access to selected applications, categories, web domains, or device settings.
- Apply Screen Time-style controls using `ManagedSettingsStore`.

Why it matters for LifeOS:

- This is the likely route for shielding selected apps.
- It can create a system-level pause/block surface rather than a custom overlay.

Risks and unknowns:

- It may shield apps, but may not allow the exact soft custom pre-open intervention LifeOS wants.
- The system shield interaction model may constrain copy, layout, actions, and visual feel.
- The "pause" may behave more like blocking than a gentle LifeOS prompt unless carefully designed.

Spike questions:

- Can LifeOS apply and remove shields for selected apps/categories?
- Can shields be toggled dynamically based on user choices and schedules?
- Can the shield action open the LifeOS app or allow a custom secondary action?
- How much custom UI/copy is available inside shield configuration extensions?

### 3.4 Screen Time Style Shield

Official sources:

- [ShieldAction documentation](https://developer.apple.com/documentation/managedsettings/shieldaction)
- [ShieldActionDelegate documentation](https://developer.apple.com/documentation/managedsettings/shieldactiondelegate)
- [ShieldActionResponse.openParentalControlsApp](https://developer.apple.com/documentation/managedsettings/shieldactionresponse/openparentalcontrolsapp)

What it may enable:

- Display a system Screen Time-style shield when a restricted app/site is opened.
- Handle primary/secondary shield button actions through a shield action extension.
- Potentially send the user back to the LifeOS app.

Why it matters for LifeOS:

- This may be the closest iOS-supported version of the core intervention.
- The product may need to adapt from "custom overlay before app opens" to "Screen Time-style shield when protected app is accessed."

Risks and unknowns:

- Shield UI may not be fully custom.
- Button behavior may be constrained.
- The experience may feel more like a system restriction than a soft LifeOS pause.
- Entitlement and extension setup may be complex.

Spike questions:

- Can the shield show LifeOS-friendly copy?
- Can the user choose "pause" versus "continue" in a way that matches MVP goals?
- Can the shield open LifeOS for a reflection/protected-moment flow?
- Can LifeOS avoid framing the experience as punishment or hard blocking?

### 3.5 Entitlement And App Review Questions

Official sources:

- [Requesting the Family Controls entitlement](https://developer.apple.com/documentation/familycontrols/requesting-the-family-controls-entitlement)
- [Family Controls entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.family-controls)
- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Apple news: Providing safe app experiences for families](https://developer.apple.com/news/?id=db58g7r0)

Questions to answer before full MVP:

- Does LifeOS qualify for Family Controls distribution entitlement as a self-control / digital wellbeing / productivity app?
- Do all required targets need explicit entitlement approval: main app, Device Activity Monitor extension, Shield Configuration extension, Shield Action extension?
- Can the app pass App Review if the product is not positioned as parental control?
- What privacy disclosure is required?
- Are there limitations on displaying or exporting selected app names or usage metrics?
- Can TestFlight distribution be used for the spike with the required capabilities?

Decision risk:

- If entitlement access is unavailable or App Review risk is too high, iOS ideal intervention may be `Red`.
- The MVP may need to begin with notification/manual fallback or Android-first technical validation.

### 3.6 iOS Notification / Manual Fallback

Fallback paths:

- Scheduled 15:00 and 22:00 check-ins.
- Reminder-only pause prompts at high-risk times.
- Manual protected-time logging.
- Shortcuts-based experimental flow, if useful for personal testing.
- In-app "I paused before opening an app" manual record.

Product shape:

- Position as attention/time reflection and recovery first.
- Avoid promising automatic app-open intervention until entitlement and shield feasibility are proven.
- Preserve the emotional loop: pause, choose, record, reflect.

## 4. Android Feasibility Options

### 4.1 UsageStatsManager

Official sources:

- [UsageStatsManager API reference](https://developer.android.com/reference/android/app/usage/UsageStatsManager)
- [Android AppUsageStatistics sample](https://android.googlesource.com/platform/developers/build/+/master/prebuilts/gradle/AppUsageStatistics/README.md)
- [Manifest.permission reference](https://developer.android.com/reference/android/Manifest.permission)

What it may enable:

- Query app usage statistics and app foreground history.
- Detect recently used apps or foreground app changes after the fact.
- Build usage summaries and records.

Permission:

- Requires `android.permission.PACKAGE_USAGE_STATS`.
- The Android sample notes users must enable app usage access through system settings.

Why it matters for LifeOS:

- Useful for detecting whether selected distracting apps were used.
- Useful for records, analytics, and post-use reflection.
- May support a polling-based near-real-time pause experiment.

Risks and unknowns:

- It may not be immediate enough for true "before app opens" intervention.
- User must grant special usage access manually.
- Polling can be battery-sensitive and unreliable under background restrictions.
- Some data may be aggregated or delayed.

Spike questions:

- How quickly can an app-open event be inferred on Android 12-16?
- Can selected package names be monitored reliably while LifeOS is backgrounded?
- What polling interval is required, and what is the battery impact?
- Does Play policy allow this usage if clearly disclosed as attention-protection?

### 4.2 `PACKAGE_USAGE_STATS`

Official source: [Manifest.permission reference](https://developer.android.com/reference/android/Manifest.permission)

What to validate:

- Manifest declaration.
- User education flow to settings.
- Permission state detection.
- UX for denied/revoked permission.

Spike output:

- A matrix of Android versions/devices showing whether usage access can be granted and queried.
- A reliability note for foreground detection latency.

### 4.3 AccessibilityService

Official sources:

- [AccessibilityService API reference](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService)
- [Create an accessibility service](https://developer.android.com/guide/topics/ui/accessibility/service)
- [Google Play policy: Use of the AccessibilityService API](https://support.google.com/googleplay/android-developer/answer/10964491?hl=en)

What it may enable:

- Receive callbacks for UI state transitions.
- Potentially detect window changes or app foreground changes more directly.
- Potentially support a stronger app-open intervention path.

Why it matters for LifeOS:

- It may be the most technically powerful Android route for detecting app opens.
- It may enable faster intervention than UsageStats polling.

Policy risk:

- Android documentation says accessibility services should only be used to assist users with disabilities in using Android devices and apps.
- Google Play policy permits AccessibilityService API use broadly, but only services designed to help people with disabilities are eligible to declare themselves accessibility tools via `isAccessibilityTool`.
- A LifeOS digital wellbeing use case may need careful policy analysis and prominent disclosure.

Risks and unknowns:

- High Play Store review risk if the service is perceived as unrelated to accessibility.
- Sensitive user trust issue.
- Requires clear user disclosure and least-privilege design.
- Could be rejected or require product repositioning.

Spike questions:

- Can LifeOS detect selected app launch events with AccessibilityService on test devices?
- Is the detection fast enough to show a pause UI before the user starts scrolling?
- Can the service be justified under Google Play policy without misrepresenting accessibility?
- What prominent disclosure is needed?
- Is this acceptable for a mainstream consumer app?

### 4.4 Overlay / `SYSTEM_ALERT_WINDOW`

Official sources:

- [Manifest.permission reference for SYSTEM_ALERT_WINDOW](https://developer.android.com/reference/android/Manifest.permission)
- [Android 11 permissions updates: system alert window changes](https://developer.android.com/about/versions/11/privacy/permissions)

What it may enable:

- Draw an overlay on top of other apps using application overlay windows.
- Present a LifeOS pause UI while another app is launching or already open.

Why it matters for LifeOS:

- Could approximate the soft pause/intervention experience.
- May allow a more custom UI than iOS shields.

Risks and unknowns:

- `SYSTEM_ALERT_WINDOW` is a highly sensitive permission.
- Android documentation says very few apps should use it and that these windows are intended for system-level interaction.
- Overlay permission can harm user trust and may run into policy/review concerns.
- Android 11+ changed system alert window behavior to make grants more intentional.
- Some apps or OS versions may hide/prevent overlays in sensitive contexts.

Spike questions:

- Can an overlay be shown quickly enough after detecting selected app launch?
- Can the overlay be dismissed safely without trapping the user?
- Does Play Store policy allow this use for attention/time protection?
- What disclosure and settings UX are required?

### 4.5 Foreground / Background Reliability

Official sources:

- [Android 8.0 background execution limits](https://developer.android.com/about/versions/oreo/background)
- [Optimize for Doze and App Standby](https://developer.android.com/training/monitoring-device-state/doze-standby)

Risks:

- Background services are limited when the app is idle.
- Doze and App Standby defer background CPU/network activity.
- OEM battery optimization can reduce reliability beyond stock Android behavior.
- Foreground services may be needed for reliability, but they create persistent notifications and policy/UX tradeoffs.

Spike questions:

- Can LifeOS monitor selected app openings without a persistent foreground service?
- If a foreground service is needed, is the persistent notification acceptable?
- Which devices/OS versions kill or delay the monitoring path?
- What is the minimum reliable background architecture?

### 4.6 Android Notification / Manual Fallback

Fallback paths:

- Scheduled high-risk reminders.
- 15:00 and 22:00 check-ins.
- Manual protected-time logging.
- Post-use reflection when UsageStats detects recent distracting app usage.
- User-triggered pause timer before opening apps.

Product shape:

- If real-time intervention is unreliable or policy-risky, Android can still support a recovery-oriented product through detection-after-use, reminders, and manual logs.

## 5. React Native Vs Flutter Implications

React Native and Flutter remain open. This spike should inform the choice but not finalize it.

### 5.1 Native Modules Are Required Either Way

Official sources:

- [React Native Native Modules / Turbo Native Modules](https://reactnative.dev/docs/turbo-native-modules-introduction)
- [Flutter platform channels](https://docs.flutter.dev/platform-integration/platform-channels)

Implication:

- There is no pure JavaScript/Dart-only route for the ideal app-open intervention.
- Both stacks need native iOS and Android code.
- The stack decision should consider native module complexity, not just UI preference.

### 5.2 React Native Implications

Official sources:

- [React Native native modules](https://reactnative.dev/docs/turbo-native-modules-introduction)
- [Expo: Add custom native code](https://docs.expo.dev/workflow/customizing/)
- [Expo Continuous Native Generation](https://docs.expo.dev/workflow/continuous-native-generation/)
- [Expo: Adopt Prebuild](https://docs.expo.dev/guides/adopting-prebuild/)

Options:

- React Native CLI / bare app with native iOS and Android projects.
- Expo with development builds and custom native modules.
- Expo prebuild / CNG with config plugins for entitlements, manifests, and native setup.

Key implications:

- Expo Go is not enough for Screen Time / UsageStats / Accessibility / overlay native work.
- A development build or bare/prebuild workflow is likely required.
- iOS Family Controls and extensions may require native Xcode configuration that must be tested against Expo CNG/prebuild limits.
- Android manifest permissions and services may need config plugins or direct native project edits.

Spike questions:

- Can Expo CNG/prebuild manage required iOS entitlements and extension targets cleanly?
- Can Expo config plugins represent Android `PACKAGE_USAGE_STATS`, AccessibilityService, foreground service, and overlay configuration?
- Would a bare React Native app reduce friction for native spike work?

### 5.3 Flutter Implications

Official source: [Flutter platform channels](https://docs.flutter.dev/platform-integration/platform-channels)

Options:

- Flutter app with direct native iOS/Android code via `MethodChannel`.
- Custom Flutter plugin wrapping Screen Time / Android monitoring APIs.
- Platform-specific screens/extensions where needed.

Key implications:

- Flutter's UI layer can remain shared, but OS intervention logic must live in Swift/Kotlin.
- iOS extensions and entitlement configuration still need Xcode/native setup.
- Android services and permissions still need native manifest/service implementation.
- If native callbacks need to stream events to Flutter, `EventChannel` or plugin architecture may be needed.

Spike questions:

- Can `MethodChannel` support all required request/response flows for the PoC?
- Is a custom plugin needed earlier than expected?
- How cleanly can iOS Screen Time extensions communicate state back to Flutter?

## 6. Spike Tasks

### 6.1 Android PoC Plan

Goal:

- Determine whether Android can support a reliable, policy-acceptable app-open pause/intervention path.

Test devices:

- At least one recent Pixel or stock Android device.
- At least one Samsung device if available.
- Android 12+ minimum; include newest available Android version.

Tasks:

1. Create a minimal native Android spike app.
2. Implement target app selection by package name for 2-3 test apps.
3. Request and validate `PACKAGE_USAGE_STATS`.
4. Use `UsageStatsManager` to detect recent foreground app changes.
5. Measure detection latency after opening selected apps.
6. Test whether a notification-based pause prompt can appear quickly enough.
7. Separately test AccessibilityService detection speed.
8. Document Google Play policy risk for AccessibilityService use.
9. Separately test overlay feasibility with `SYSTEM_ALERT_WINDOW`.
10. Measure overlay timing, dismissal behavior, and user trust concerns.
11. Test behavior after screen lock, idle, Doze, and app standby.
12. Test whether a foreground service is required for reliability.
13. Document battery and persistent notification tradeoffs.

Do not build production code. Keep this as a throwaway native PoC.

Outputs:

- Detection latency table.
- Permission friction notes.
- Play policy risk notes.
- Recommended Android path: ideal, fallback, or no-go.

### 6.2 iOS PoC Plan

Goal:

- Determine whether iOS can support a Screen Time-style LifeOS intervention and whether entitlement/App Review risk is acceptable.

Test device:

- Physical iPhone. Simulator is not enough for meaningful Screen Time capability validation.

Tasks:

1. Confirm Apple Developer account requirements.
2. Request or verify Family Controls development/distribution entitlement path.
3. Create minimal native iOS Swift spike app.
4. Add `FamilyControls` authorization flow.
5. Add app/category selection via Screen Time APIs.
6. Test token persistence and display constraints.
7. Add `ManagedSettingsStore` shield for selected apps/categories.
8. Add Device Activity Monitor extension if needed.
9. Add Shield Configuration / Shield Action extension if needed.
10. Test whether opening a selected app shows a shield.
11. Test what copy/actions can be customized.
12. Test whether the shield can open the LifeOS app.
13. Document whether the experience feels like a warm pause or hard block.
14. Document entitlement, TestFlight, and App Review risk.

Do not build production code. Keep this as a throwaway native PoC.

Outputs:

- Entitlement status.
- Shield behavior screenshots/notes.
- Customization limits.
- App Review risk notes.
- Recommended iOS path: ideal, shield-adapted, fallback, or no-go.

### 6.3 Cross-Platform Stack Implication Check

Goal:

- Determine whether React Native or Flutter introduces unacceptable native integration friction.

Tasks:

1. For React Native:
   - Create a minimal native module interface for "getPermissionStatus" and "openPermissionSettings".
   - Test Expo development build / prebuild feasibility.
   - Determine whether iOS extension targets are manageable in Expo CNG or require bare workflow.
   - Determine whether Android services and permissions are manageable through config plugins.

2. For Flutter:
   - Create a minimal `MethodChannel` for "getPermissionStatus" and "openPermissionSettings".
   - Test native Android permission/status response.
   - Test native iOS entitlement/status placeholder response.
   - Determine whether a plugin structure is needed.

3. Compare:
   - Native setup complexity.
   - Build/release complexity.
   - Debugging workflow.
   - Extension/service support.
   - Long-term maintainability.

Output:

- Stack implication note, not a final stack decision.

## 7. Acceptance Criteria: Green / Yellow / Red

### Green

Green means the ideal or near-ideal intervention is feasible enough to proceed into MVP prototype.

Criteria:

- iOS can show a Screen Time-style shield or equivalent intervention for selected apps with acceptable customization.
- Android can detect selected app opens and show a pause UI with acceptable latency and policy risk.
- Required permissions can be explained to users without breaking trust.
- App Store / Play Store risk is acceptable or clearly manageable.
- React Native and/or Flutter native integration appears feasible.
- Fallback flows remain available for unsupported states.

Prototype implication:

- Proceed to cross-platform MVP prototype with native spike learnings built in.

### Yellow

Yellow means the ideal intervention is partially feasible, but the product must adapt.

Criteria:

- iOS supports only Screen Time-style shield rather than custom pre-open overlay.
- Android supports detection but requires sensitive permissions or has reliability gaps.
- Entitlement or policy review remains uncertain.
- One platform supports ideal intervention while the other needs fallback.
- React Native or Flutter needs a more native-heavy workflow than expected.

Prototype implication:

- Build a hybrid prototype:
  - Ideal intervention where feasible.
  - Notification/manual fallback elsewhere.
  - Product copy avoids promising exact app-open intervention.

### Red

Red means the core intervention is not feasible or carries unacceptable store/policy risk.

Criteria:

- iOS entitlement/App Review path is blocked or unacceptable.
- Android requires Accessibility/overlay patterns that are too risky for Play Store.
- Real-time detection is too delayed or unreliable.
- Required permissions create unacceptable user trust friction.
- Cross-platform stack cannot reasonably support required native pieces.

Prototype implication:

- Do not build the MVP around automatic pre-open intervention.
- Reframe prototype around:
  - Manual protected-time logging.
  - Scheduled check-ins.
  - Notification-based pause prompts.
  - Post-use reflection.
  - Optional platform-specific experiment outside public MVP.

## 8. Recommended Next Prototype Scope Depending On Result

### If Green

Build:

- Target app selection.
- Permission education.
- iOS shield or Android pause intervention.
- Intervention decision event.
- Home summary.
- 15:00 check-in.
- 22:00 achievement log.
- Records.

Keep scope small:

- No AI coaching.
- No social features.
- No full planner.
- No production analytics beyond spike-safe event logs.

### If Yellow

Build:

- Target app selection where supported.
- Permission education with clear platform limits.
- Platform-specific intervention on supported path.
- Notification/reminder fallback.
- Manual protected-time log.
- Records that distinguish automatic and manual events.

Product positioning:

- "LifeOS helps you pause and protect your time" rather than "LifeOS always stops apps before they open."

### If Red

Build:

- Manual and notification-based prototype only.
- 15:00 and 22:00 check-in loop.
- Records and reflection.
- Optional "before opening app, start a pause" user-triggered flow.

Delay:

- Automatic app-open intervention.
- Store submission using sensitive permissions.
- Heavy native module architecture.

## 9. Optional Spike Notes

No production code should be written for this task.

Optional pseudo-code only:

```text
onSelectedAppAttemptedOpen(appTokenOrPackage):
  if canShowSystemShield:
    showShield(copyVariant)
  else if canShowOverlayOrPrompt:
    showPausePrompt(copyVariant)
  else:
    scheduleFallbackNotification()
    allowManualProtectedMomentLog()
```

This pseudo-code describes the decision shape only. It is not implementation guidance.

## 10. Source Links

Apple:

- [Screen Time API documentation](https://developer.apple.com/documentation/screentimeapidocumentation)
- [Family Controls documentation](https://developer.apple.com/documentation/familycontrols)
- [Configuring Family Controls](https://developer.apple.com/documentation/xcode/configuring-family-controls)
- [Requesting the Family Controls entitlement](https://developer.apple.com/documentation/familycontrols/requesting-the-family-controls-entitlement)
- [Family Controls entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.family-controls)
- [Device Activity documentation](https://developer.apple.com/documentation/deviceactivity)
- [Managed Settings documentation](https://developer.apple.com/documentation/managedsettings)
- [ManagedSettingsStore documentation](https://developer.apple.com/documentation/managedsettings/managedsettingsstore)
- [ApplicationSettings documentation](https://developer.apple.com/documentation/managedsettings/applicationsettings)
- [ShieldAction documentation](https://developer.apple.com/documentation/managedsettings/shieldaction)
- [ShieldActionDelegate documentation](https://developer.apple.com/documentation/managedsettings/shieldactiondelegate)
- [ShieldActionResponse.openParentalControlsApp](https://developer.apple.com/documentation/managedsettings/shieldactionresponse/openparentalcontrolsapp)
- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)

Android / Google Play:

- [UsageStatsManager API reference](https://developer.android.com/reference/android/app/usage/UsageStatsManager)
- [Android AppUsageStatistics sample](https://android.googlesource.com/platform/developers/build/+/master/prebuilts/gradle/AppUsageStatistics/README.md)
- [Manifest.permission reference](https://developer.android.com/reference/android/Manifest.permission)
- [AccessibilityService API reference](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService)
- [Create an accessibility service](https://developer.android.com/guide/topics/ui/accessibility/service)
- [Google Play policy: Use of the AccessibilityService API](https://support.google.com/googleplay/android-developer/answer/10964491?hl=en)
- [Android 11 permissions updates](https://developer.android.com/about/versions/11/privacy/permissions)
- [Android 8.0 background execution limits](https://developer.android.com/about/versions/oreo/background)
- [Optimize for Doze and App Standby](https://developer.android.com/training/monitoring-device-state/doze-standby)

Cross-platform:

- [React Native native modules](https://reactnative.dev/docs/turbo-native-modules-introduction)
- [Expo: Add custom native code](https://docs.expo.dev/workflow/customizing/)
- [Expo Continuous Native Generation](https://docs.expo.dev/workflow/continuous-native-generation/)
- [Expo: Adopt Prebuild](https://docs.expo.dev/guides/adopting-prebuild/)
- [Flutter platform channels](https://docs.flutter.dev/platform-integration/platform-channels)
