# LifeOS Existing App Permission Flow Review and Technical Spike Execution Plan v0.1

Status: Review draft

Task: `LIFEOS-CODEX-006`

Research checked date: 2026-06-30

## Naming And Scope Constraints

- `LifeOS` is the team/company placeholder.
- `하루조각 / Daymark` are app-name placeholders.
- Do not finalize the brand name.
- Do not finalize React Native vs Flutter.
- This is not full app implementation.
- This document does not write production code.
- UI libraries do not solve app intervention permissions.

## 1. Executive Summary

LifeOS's riskiest MVP assumption is still platform-level intervention: can the app create a pause before a selected distracting app opens?

Existing screen-time and app-blocking products show that the market uses multiple permission patterns:

- iOS Screen Time / Family Controls style permission and shield flows.
- iOS Shortcuts automations as a workaround or reinforcement layer.
- Android Accessibility Service for strong app-open detection/intervention.
- Android Usage Access for app usage detection and fallback records.
- Android overlay permission for custom pause surfaces, with significant trust and policy risk.
- Notification/manual fallback flows when OS-level intervention is limited.

The main lesson from existing apps is that the product must not assume a single clean permission flow. LifeOS needs a staged permission strategy:

1. Explain why permissions are needed in human terms.
2. Validate the minimum viable iOS and Android paths separately.
3. Treat app-open intervention as the ideal path.
4. Preserve notification/manual logging fallback paths from day one.
5. Avoid choosing React Native vs Flutter until native feasibility is known.

## 2. Existing App Permission Flow Review

This review uses official product pages, app store listings, help-center pages, and platform documentation where available. Some competitors do not expose their full technical implementation publicly; where the source only implies a behavior, it is marked as an inference.

### 2.1 one sec

Official sources:

- [one sec homepage](https://one-sec.app/)
- [one sec platforms page](https://one-sec.app/platforms/)
- [one sec Getting Started help category](https://tutorials.one-sec.app/en/categories/682882)
- [one sec Android permission setup](https://tutorials.one-sec.app/en/articles/3034754)
- [one sec without Accessibility Permission](https://tutorials.one-sec.app/en/articles/3148866)
- [one sec App Store listing](https://apps.apple.com/us/app/one-sec-screen-time-focus/id1532875441)
- [one sec Google Play listing](https://play.google.com/store/apps/details?id=wtf.riedel.onesec)

Observed permission/setup patterns:

- iOS uses a Shortcuts-based setup path for app-open intervention, based on one sec's help-center category for "Initial one sec Shortcuts Setup on iOS".
- Android setup asks users to enable Accessibility Service.
- one sec documents an Android fallback path without Accessibility Service that prompts users to set up app usage permission instead.
- Product messaging emphasizes interrupting app openings and forcing/encouraging reflection while the behavior happens.
- App Store release notes mention delayed intervention mode and Safari extension setup, implying multiple intervention mechanisms.

LifeOS implications:

- Existing user education must handle multi-step setup.
- Accessibility-based Android flow is viable in the market, but still policy-sensitive.
- Usage Access fallback should be part of the spike, not an afterthought.
- iOS Shortcuts automation may be a useful fallback/prototype path, even if Screen Time shield is the desired native path.

### 2.2 Jomo

Official sources:

- [Jomo homepage](https://jomo.so/)
- [Jomo App Store listing](https://apps.apple.com/us/app/jomo-screen-time-blocker/id1609960918)
- [Jomo Help: How to block apps without Apple's Screen Time](https://help.jomo.so/en/article/how-to-block-apps-without-apples-screen-time-lv0ux6/)
- [Jomo Help: How to block iPhone Settings while in strict mode](https://help.jomo.so/en/article/how-to-block-iphone-settings-while-in-strict-mode-crydu3/)
- [Jomo Help: How to fix Screen Time issues](https://help.jomo.so/en/article/how-to-fix-screen-time-issues-jmz6ha/)
- [Jomo Help: Blocking does not seem to be working](https://help.jomo.so/en/article/blocking-doesnt-seem-to-be-working-pr6ji2/)

Observed permission/setup patterns:

- Jomo positions itself around screen-time reduction, app blocking, and positive habit recovery.
- Jomo help docs refer directly to Apple Screen Time data and troubleshooting when Screen Time data is incorrect.
- Jomo documents a Shortcuts-based workaround to block apps without Apple's Screen Time.
- Jomo documents strict-mode hardening around iPhone Settings and Screen Time permissions.
- Jomo notes possible conflicts between screen-time apps and recommends removing other screen-time apps when blocking behaves incorrectly.

LifeOS implications:

- Screen Time data and shield reliability may degrade or conflict when multiple screen-time apps are installed.
- A resilient product needs troubleshooting flows, not only happy-path onboarding.
- iOS Shortcuts can serve as a practical fallback/reinforcement layer, but it may be too complex for mainstream onboarding.
- Strict mode / Settings protection can quickly become harsh; LifeOS should preserve its warm attention-protection tone.

### 2.3 Opal

Official sources:

- [Opal homepage](https://www.opal.so/)
- [Opal Help Center](https://opalapp.com/help)
- [Opal App Store listing](https://apps.apple.com/us/app/opal-screen-time-control/id1497465230)
- [Opal Google Play listing](https://play.google.com/store/apps/details?id=com.withopal.opal)

Observed permission/setup patterns:

- Opal publicly emphasizes rules, focus sessions, app blocking, screen-time control, and usage statistics.
- Help-center topics focus on iOS, subscriptions, accounts, Live Activities, and troubleshooting.
- The App Store and Play Store listings confirm a cross-platform screen-time control product with app-blocking behavior.
- Inference: iOS app blocking likely depends on Screen Time / Family Controls style capabilities; public pages do not expose every technical step.

LifeOS implications:

- Opal demonstrates that polished consumer positioning can coexist with heavier permission-based blocking.
- LifeOS should review how Opal explains permission requirements during onboarding once a live device flow is tested.
- Public docs alone are not enough; install-and-record review is required.

### 2.4 AppBlock

Official sources:

- [AppBlock homepage](https://appblock.app/)
- [AppBlock Android settings help](https://appblock.app/help/android/settings)
- [AppBlock: Why do I have to grant so many permissions?](https://appblock.app/why-do-i-have-to-grant-so-many-permissions/)
- [AppBlock: Accessibility permission restricted](https://appblock.app/how-to-give-accessibility-permission-if-restricted/)
- [AppBlock: Accessibility keeps turning off](https://appblock.app/my-accessibility-keeps-turning-off-what-can-i-do/)
- [AppBlock: Why blocking is not working](https://appblock.app/why-can-i-still-access-apps-websites-that-should-be-blocked/)
- [AppBlock Google Play listing](https://play.google.com/store/apps/details?id=cz.mobilesoft.appblock)

Observed permission/setup patterns:

- AppBlock states that Android requires several permissions to block apps/sites reliably, apply schedules, and provide usage statistics.
- AppBlock directly documents Accessibility permission setup and troubleshooting.
- AppBlock documents cases where Accessibility turns off because of OS/background handling.
- AppBlock has user-facing troubleshooting around required permissions and blocking failures.

LifeOS implications:

- Android reliability is not just "can we detect app open?" It is also "can the service stay enabled and running?"
- Permission education must include troubleshooting and OS-specific instructions.
- Background reliability and battery optimization must be part of spike acceptance criteria.
- If LifeOS uses Accessibility, it must include prominent disclosure and a policy review path.

### 2.5 ScreenZen

Official source:

- [ScreenZen Google Play listing](https://play.google.com/store/apps/details?id=com.screenzen)

Observed permission/setup patterns:

- The Play listing explicitly mentions "Pause before opening apps or websites".
- It describes wait-time-based app opening friction.
- Public search did not reveal enough official setup documentation for a full permission-flow breakdown.

LifeOS implications:

- "Pause before opening" is an established Android user-facing pattern.
- LifeOS should install and record ScreenZen's live setup flow if possible, because public docs are insufficient.

## 3. Pattern Summary

| Pattern | Existing Apps | Likely Permissions | LifeOS Risk |
| --- | --- | --- | --- |
| iOS Screen Time / shield | Jomo, Opal, likely others | FamilyControls / ManagedSettings / DeviceActivity | Entitlement, App Review, limited UI customization |
| iOS Shortcuts automation | one sec, Jomo fallback/hardening | User-created personal automation | Setup friction, user error, not fully app-owned |
| Android Accessibility | one sec, AppBlock | AccessibilityService | Play policy, user trust, restricted settings, service reliability |
| Android Usage Access | one sec fallback, AppBlock-like usage stats | PACKAGE_USAGE_STATS / UsageStatsManager | May be delayed/coarse, manual settings permission |
| Android overlay | Common blocker pattern; platform-level option | SYSTEM_ALERT_WINDOW | Highly sensitive, Play policy/user trust risk |
| Notification/manual fallback | LifeOS fallback direction | Notifications, local app data | Less automatic, but store-safe and product-preserving |

## 4. Product Lessons For LifeOS Permission UX

### 4.1 Permission Copy Must Be Benefits-First

Do not lead with technical permission names. Explain the user value first:

- "앱을 열기 전 잠깐 멈출 수 있게 도와드리기 위해 필요해요."
- "기기 설정에 따라 일부 기능은 다르게 동작할 수 있어요."
- "권한이 어려운 경우에도 알림과 수동 기록으로 시간을 지킬 수 있어요."

### 4.2 Permission Flow Needs Multiple Levels

LifeOS should avoid an all-or-nothing setup.

Recommended levels:

1. Full intervention mode.
2. Reminder/notification mode.
3. Manual protected-time logging mode.
4. Check-in-only mode.

### 4.3 Troubleshooting Is Part Of The Product

Existing apps reveal common failure states:

- Screen Time data mismatch.
- Screen Time permission revoked.
- Multiple screen-time apps conflict.
- Accessibility permission disabled.
- Android background service killed.
- Overlay permission denied.
- User cannot find the right system settings page.

LifeOS MVP docs and prototype should include these states early.

### 4.4 Avoid Overpromising The Ideal Flow

Until the spike is complete, LifeOS should not promise:

- "Always pauses before every selected app opens."
- "Impossible to bypass."
- "Works the same on iOS and Android."

Safer positioning:

- "LifeOS helps you pause and protect your time where your device allows it."
- "If automatic pause is limited, you can still use reminders and simple records."

## 5. Technical Spike Execution Plan

This plan converts the platform feasibility brief into concrete execution work.

### 5.1 Spike Goals

1. Review live permission flows in existing apps.
2. Validate the minimum iOS app-open intervention path.
3. Validate the minimum Android app-open detection/intervention path.
4. Compare fallback product shapes.
5. Produce a Green / Yellow / Red recommendation for prototype scope.

### 5.2 Non-Goals

- Do not build the full MVP.
- Do not finalize React Native vs Flutter.
- Do not create production app architecture.
- Do not finalize brand/app names.
- Do not ship sensitive permissions to a public store build.
- Do not implement AI coaching, social features, or a full planner.

## 6. Existing App Review Execution

### 6.1 Apps To Install And Review

| App | Platform Priority | Why Review |
| --- | --- | --- |
| one sec | iOS + Android | Closest impulse-intervention benchmark. |
| Jomo | iOS | Strong Screen Time + Shortcuts fallback reference. |
| Opal | iOS + Android | Polished mainstream screen-time control reference. |
| AppBlock | Android | Permission-heavy Android blocking and troubleshooting reference. |
| ScreenZen | Android | Explicit "pause before opening apps" reference. |

### 6.2 Review Script

For each app:

1. Install from official store.
2. Start onboarding from a clean state.
3. Record every permission request screen.
4. Note exact wording and emotional framing.
5. Note how the app routes to system settings.
6. Grant required permissions if safe on test device.
7. Select 2-3 target apps.
8. Attempt to open target apps 10 times.
9. Record whether the app pauses, blocks, redirects, or logs usage.
10. Reboot device and repeat target app opening test.
11. Deny/revoke permission and record fallback UX.
12. Capture troubleshooting or error states.

### 6.3 Review Output Template

For each app, record:

| Field | Notes |
| --- | --- |
| Platform | iOS / Android |
| Version | App version and OS version |
| Permission names shown to user | Exact user-facing labels |
| System settings path | Steps required |
| Emotional tone | Friendly, strict, technical, scary, etc. |
| Number of steps to first working intervention | Count |
| Intervention type | Shield, overlay, redirect, notification, manual |
| Failure states | Permission denied, conflict, service killed |
| Bypass difficulty | Easy / Medium / Hard |
| LifeOS lesson | What to copy, avoid, or test |

## 7. iOS Spike Execution Plan

### 7.1 iOS Track A: Screen Time / Shield Path

Source references:

- [Apple Screen Time API](https://developer.apple.com/documentation/screentimeapidocumentation)
- [FamilyControls](https://developer.apple.com/documentation/familycontrols)
- [ManagedSettings](https://developer.apple.com/documentation/managedsettings)
- [DeviceActivity](https://developer.apple.com/documentation/deviceactivity)

Tasks:

1. Confirm Apple Developer account and entitlement request requirements.
2. Confirm whether Family Controls entitlement can be requested for LifeOS use case.
3. Create throwaway native Swift project.
4. Implement FamilyControls authorization request.
5. Add app/category picker.
6. Store selected tokens locally.
7. Apply ManagedSettings shield to selected apps/categories.
8. Test shield display when selected app is opened.
9. Test available shield customization.
10. Test shield action behavior.
11. Document App Review and entitlement concerns.

Acceptance evidence:

- Screenshot/video of authorization flow.
- Screenshot/video of app/category picker.
- Screenshot/video of shield.
- Notes on customization limits.
- Notes on entitlement status.

### 7.2 iOS Track B: Shortcuts Fallback Path

Source references:

- [Apple Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios)
- [Apple Shortcuts personal automation](https://support.apple.com/guide/shortcuts/intro-to-personal-automation-apd690170742/ios)
- [Apple Shortcuts run automatically setting](https://support.apple.com/guide/shortcuts/enable-or-disable-a-personal-automation-apd602971e63/ios)
- [Jomo Shortcuts fallback guide](https://help.jomo.so/en/article/how-to-block-apps-without-apples-screen-time-lv0ux6/)

Tasks:

1. Create a manual Shortcuts automation triggered by opening a selected app.
2. Route the automation to open the LifeOS spike app or a placeholder URL.
3. Test whether "Run Immediately" works without user confirmation.
4. Test setup complexity for 1 app, 3 apps, and 10 apps.
5. Test whether LifeOS can provide shortcut actions needed for a smoother flow.
6. Document whether this is acceptable as MVP fallback or only power-user workaround.

Acceptance evidence:

- Number of setup steps.
- Video of app-open automation.
- Notes on friction, reliability, and user comprehension.

## 8. Android Spike Execution Plan

### 8.1 Android Track A: Usage Access Path

Source references:

- [UsageStatsManager](https://developer.android.com/reference/android/app/usage/UsageStatsManager)
- [Manifest.permission](https://developer.android.com/reference/android/Manifest.permission)
- [Android AppUsageStatistics sample](https://android.googlesource.com/platform/developers/build/+/master/prebuilts/gradle/AppUsageStatistics/README.md)

Tasks:

1. Create throwaway native Android project.
2. Add `PACKAGE_USAGE_STATS`.
3. Build permission state screen.
4. Route user to Usage Access settings.
5. Query foreground/recent app usage.
6. Test selected package detection.
7. Measure detection latency.
8. Test after screen lock, reboot, and idle.
9. Test with battery optimization enabled/disabled.
10. Determine whether notification-only intervention is realistic from this path.

Acceptance evidence:

- Permission setup recording.
- Detection latency table.
- Device/OS reliability notes.
- Battery/background behavior notes.

### 8.2 Android Track B: AccessibilityService Path

Source references:

- [Create an accessibility service](https://developer.android.com/guide/topics/ui/accessibility/service)
- [AccessibilityService API](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService)
- [Google Play AccessibilityService policy](https://support.google.com/googleplay/android-developer/answer/10964491?hl=en)
- [one sec Android Accessibility setup](https://tutorials.one-sec.app/en/articles/3034754)
- [AppBlock Accessibility troubleshooting](https://appblock.app/how-to-give-accessibility-permission-if-restricted/)

Tasks:

1. Create minimal AccessibilityService.
2. Request/route to Accessibility settings.
3. Detect target app foreground/window change events.
4. Measure event timing.
5. Test whether a pause activity can be launched or surfaced.
6. Test service persistence after reboot and background restrictions.
7. Document Play Console disclosure requirements.
8. Assess whether LifeOS can justify this permission without misrepresenting accessibility.

Acceptance evidence:

- Permission setup recording.
- Event timing log.
- Policy risk note.
- User trust risk note.

### 8.3 Android Track C: Overlay Path

Source references:

- [SYSTEM_ALERT_WINDOW permission](https://developer.android.com/reference/android/Manifest.permission)
- [Android 11 permissions updates](https://developer.android.com/about/versions/11/privacy/permissions)

Tasks:

1. Add overlay permission request to throwaway app.
2. Route user to "Display over other apps" settings.
3. Show a minimal pause overlay after detecting selected app.
4. Test whether overlay appears above target app.
5. Test dismissal and safety behavior.
6. Test sensitive surfaces where overlay may be blocked.
7. Document whether this should be avoided in public MVP.

Acceptance evidence:

- Overlay setup recording.
- Overlay timing notes.
- Safety/policy risk notes.

## 9. Cross-Platform Stack Check

Do not finalize React Native vs Flutter. Use this only to estimate native integration burden.

### 9.1 React Native / Expo Check

Source references:

- [React Native native modules](https://reactnative.dev/docs/turbo-native-modules-introduction)
- [Expo custom native code](https://docs.expo.dev/workflow/customizing/)
- [Expo Continuous Native Generation](https://docs.expo.dev/workflow/continuous-native-generation/)
- [Expo prebuild](https://docs.expo.dev/guides/adopting-prebuild/)

Tasks:

1. Confirm Expo Go is not sufficient for required native APIs.
2. Create minimal Expo dev build or bare React Native spike.
3. Add placeholder native module for permission status.
4. Check feasibility of iOS extensions and entitlements.
5. Check feasibility of Android services/permissions through config plugins or native project edits.

Output:

- React Native native integration risk: Low / Medium / High.
- Expo managed/dev client/bare recommendation for spike only.

### 9.2 Flutter Check

Source reference:

- [Flutter platform channels](https://docs.flutter.dev/platform-integration/platform-channels)

Tasks:

1. Create minimal Flutter project.
2. Add `MethodChannel` for permission status.
3. Test native Android status response.
4. Test native iOS placeholder response.
5. Estimate plugin structure for Screen Time and Android monitoring.

Output:

- Flutter native integration risk: Low / Medium / High.
- Plugin/MethodChannel recommendation for spike only.

## 10. Spike Schedule

### Day 0: Preparation

- Confirm test devices.
- Confirm Apple Developer account access.
- Confirm Google Play policy review resources.
- Create evidence folder for screenshots/videos.
- Decide exact target apps for tests: Instagram, YouTube, TikTok, Reddit, or local equivalents.

### Day 1: Existing App Review

- Install and review one sec, Jomo, Opal, AppBlock, ScreenZen where available.
- Capture permission flow videos.
- Fill review output template.

### Day 2: Android Usage Access + Accessibility

- Build native Android throwaway project.
- Test UsageStats path.
- Test AccessibilityService path.
- Begin latency/reliability matrix.

### Day 3: Android Overlay + Background Reliability

- Test overlay path.
- Test reboot, lock, idle, battery optimization.
- Draft Android Green/Yellow/Red recommendation.

### Day 4: iOS Screen Time Path

- Build native iOS throwaway project.
- Test FamilyControls authorization and picker.
- Test ManagedSettings shield if entitlement/capability allows.
- Record blockers if entitlement is unavailable.

### Day 5: iOS Shortcuts Fallback + Cross-Stack Check

- Test Shortcuts app-open automation fallback.
- Test minimal React Native and Flutter native bridge assumptions if time allows.
- Draft final recommendation.

## 11. Decision Criteria

### Green

- iOS Screen Time/shield path works or entitlement path is clearly obtainable.
- Android can show a pause/intervention with acceptable latency.
- Permission flows are understandable and not trust-breaking.
- Store policy risk is manageable.
- At least one cross-platform stack can support the native work without extreme friction.

### Yellow

- One platform supports near-ideal intervention; the other needs fallback.
- iOS requires Screen Time shield instead of custom pause UI.
- Android requires Accessibility/overlay with meaningful policy risk.
- Setup flow is complex but explainable.
- Prototype should include both automatic and fallback modes.

### Red

- iOS entitlement path is blocked.
- Android requires permissions that are too risky for Play Store.
- Detection is too delayed or unreliable.
- Permission flow is too scary or complex for target users.
- Cross-platform native integration risk is too high for MVP timing.

## 12. Recommended Prototype Scope By Result

### If Green

Build a constrained prototype with:

- App selection.
- Permission guide.
- Automatic pause/shield/intervention.
- Manual fallback.
- Home.
- Records.
- 15:00 check-in.
- 22:00 achievement log.

### If Yellow

Build hybrid prototype with:

- One platform automatic intervention.
- Other platform fallback mode.
- Permission education.
- Manual protected-time logging.
- Records that distinguish automatic vs manual events.

### If Red

Build no-automatic-intervention prototype:

- Notification/reminder pause prompts.
- Manual "I paused" record.
- 15:00 and 22:00 check-ins.
- Records and reflection.
- Delay app-open intervention until entitlement/policy path improves.

## 13. LifeOS Permission UX Draft Requirements

Permission screens should:

- Use 존댓말 in Korean.
- Avoid harsh words such as "통제", "금지", and "차단" as emotional framing.
- Explain why the permission helps protect attention/time.
- Offer fallback if the user declines.
- Acknowledge platform limits clearly.
- Never imply the user failed if a permission is unavailable.

Draft copy direction:

- `앱을 열기 전 잠깐 멈추기 위해 기기 권한이 필요해요.`
- `기기 설정에 따라 일부 기능은 다르게 동작할 수 있어요.`
- `권한을 설정하지 않아도 알림과 수동 기록으로 내 시간을 지킬 수 있어요.`

## 14. Source Links

Existing app references:

- [one sec homepage](https://one-sec.app/)
- [one sec platforms](https://one-sec.app/platforms/)
- [one sec help: Getting Started](https://tutorials.one-sec.app/en/categories/682882)
- [one sec Android Accessibility setup](https://tutorials.one-sec.app/en/articles/3034754)
- [one sec without Accessibility Permission](https://tutorials.one-sec.app/en/articles/3148866)
- [one sec App Store listing](https://apps.apple.com/us/app/one-sec-screen-time-focus/id1532875441)
- [one sec Google Play listing](https://play.google.com/store/apps/details?id=wtf.riedel.onesec)
- [Jomo homepage](https://jomo.so/)
- [Jomo App Store listing](https://apps.apple.com/us/app/jomo-screen-time-blocker/id1609960918)
- [Jomo Shortcuts fallback](https://help.jomo.so/en/article/how-to-block-apps-without-apples-screen-time-lv0ux6/)
- [Jomo strict Settings protection](https://help.jomo.so/en/article/how-to-block-iphone-settings-while-in-strict-mode-crydu3/)
- [Jomo Screen Time troubleshooting](https://help.jomo.so/en/article/how-to-fix-screen-time-issues-jmz6ha/)
- [Jomo blocking troubleshooting](https://help.jomo.so/en/article/blocking-doesnt-seem-to-be-working-pr6ji2/)
- [Opal homepage](https://www.opal.so/)
- [Opal Help Center](https://opalapp.com/help)
- [Opal App Store listing](https://apps.apple.com/us/app/opal-screen-time-control/id1497465230)
- [Opal Google Play listing](https://play.google.com/store/apps/details?id=com.withopal.opal)
- [AppBlock homepage](https://appblock.app/)
- [AppBlock Android settings](https://appblock.app/help/android/settings)
- [AppBlock permissions explanation](https://appblock.app/why-do-i-have-to-grant-so-many-permissions/)
- [AppBlock Accessibility restricted help](https://appblock.app/how-to-give-accessibility-permission-if-restricted/)
- [AppBlock Accessibility reliability help](https://appblock.app/my-accessibility-keeps-turning-off-what-can-i-do/)
- [AppBlock blocking troubleshooting](https://appblock.app/why-can-i-still-access-apps-websites-that-should-be-blocked/)
- [AppBlock Google Play listing](https://play.google.com/store/apps/details?id=cz.mobilesoft.appblock)
- [ScreenZen Google Play listing](https://play.google.com/store/apps/details?id=com.screenzen)

Platform references:

- [Apple Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios)
- [Apple Shortcuts personal automation](https://support.apple.com/guide/shortcuts/intro-to-personal-automation-apd690170742/ios)
- [Apple Shortcuts automation run settings](https://support.apple.com/guide/shortcuts/enable-or-disable-a-personal-automation-apd602971e63/ios)
- [Apple Screen Time API](https://developer.apple.com/documentation/screentimeapidocumentation)
- [FamilyControls](https://developer.apple.com/documentation/familycontrols)
- [ManagedSettings](https://developer.apple.com/documentation/managedsettings)
- [DeviceActivity](https://developer.apple.com/documentation/deviceactivity)
- [UsageStatsManager](https://developer.android.com/reference/android/app/usage/UsageStatsManager)
- [Android Manifest permissions](https://developer.android.com/reference/android/Manifest.permission)
- [Android AppUsageStatistics sample](https://android.googlesource.com/platform/developers/build/+/master/prebuilts/gradle/AppUsageStatistics/README.md)
- [Create an Android accessibility service](https://developer.android.com/guide/topics/ui/accessibility/service)
- [Android AccessibilityService API](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService)
- [Google Play AccessibilityService policy](https://support.google.com/googleplay/android-developer/answer/10964491?hl=en)
- [Android SYSTEM_ALERT_WINDOW permission](https://developer.android.com/reference/android/Manifest.permission)
- [Android 11 permissions updates](https://developer.android.com/about/versions/11/privacy/permissions)
- [React Native native modules](https://reactnative.dev/docs/turbo-native-modules-introduction)
- [Expo custom native code](https://docs.expo.dev/workflow/customizing/)
- [Expo Continuous Native Generation](https://docs.expo.dev/workflow/continuous-native-generation/)
- [Expo prebuild](https://docs.expo.dev/guides/adopting-prebuild/)
- [Flutter platform channels](https://docs.flutter.dev/platform-integration/platform-channels)
