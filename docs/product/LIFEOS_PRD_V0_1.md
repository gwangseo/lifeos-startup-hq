# LifeOS PRD v0.1

Status: Review draft

Source of truth:

- `MASTER_CONTEXT.md`
- `data/codex_tasks.csv` task `LIFEOS-CODEX-003`
- `data/conversations.csv` rows for MVP v0.2, UX Flow v0.1, UX Copy v0.2, Wireframe Brief v0.1, naming/localization, and brand tone
- `data/decision_log.csv` row for MVP v0.1 direction and bilingual localization principle
- `data/research_database.csv` Batch 1 findings and top 10 deep dives
- `data/competitors.csv` competitor landscape

## Naming Status

Do not treat any name in this document as final.

- `LifeOS` is the team/company placeholder.
- `하루조각` is a Korean app-name placeholder.
- `Daymark` is an English app-name placeholder.
- Final brand, app store naming, trademark, domain, and availability checks remain open.

## Product Direction

LifeOS is not a generic blocker app and not a generic habit tracker. The MVP direction is an attention, time, and life-quality protection app.

The product helps users notice unconscious digital impulses, pause before losing time, protect small pieces of the day, and reflect gently on what they recovered.

The preserved strategic blend is:

- `one sec`: intervention at the impulse moment
- `Forest`: visible emotional reward for protected attention
- `Daylio`: low-friction reflection
- `Finch`: warm, failure-tolerant, non-shaming support

## Problem

Users lose meaningful time to automatic app-opening, short-form scrolling, and low-awareness digital habits. Existing solutions often become either strict blockers, generic screen-time dashboards, or habit checklists.

The LifeOS opportunity is to protect attention and life quality without making users feel punished or managed.

## Goals

- Help users pause before opening selected distracting apps.
- Let users protect small moments of the day without high planning burden.
- Make protected time feel visible, warm, and emotionally rewarding.
- Support a 15:00 light check-in and 22:00 achievement log.
- Keep all Korean app-facing copy in 존댓말.
- Keep the experience soft, modern, rounded, airy, and 2026-ready.
- Plan bilingual Korean/English localization from the beginning.

## Non-Goals

- Do not become a full productivity suite.
- Do not become a generic habit tracker.
- Do not finalize brand or app names.
- Do not finalize React Native vs Flutter.
- Do not rely on complex AI recommendations in MVP.
- Do not launch social/community features in MVP.
- Do not build a heavy calendar or planner integration in MVP.
- Do not use shame, punishment, or harsh control language as the emotional center.

## Target Users

Initial likely users, pending review:

- People who habitually open social media or short-form video apps.
- Students and young professionals who want to protect study/work attention.
- Users who dislike strict blockers but still want a last line of defense.
- Users who want gentle reflection without long journaling.
- Users interested in daily life-quality recovery, not pure productivity optimization.

## Core MVP Loop

1. User selects apps or moments they want to protect.
2. User attempts to open a selected distracting app.
3. LifeOS presents a warm intervention screen if platform permissions allow.
4. User pauses, breathes, and chooses whether to continue or protect the moment.
5. If the user protects the moment, the app records a small time/attention win.
6. At 15:00, LifeOS offers a skippable 1-5 check-in.
7. At 22:00, LifeOS offers a skippable achievement log with 0-10 entries.
8. Records show moments where the user paused, resisted distraction, or took time back.

## MVP Feature Priority

### P0

- Onboarding with placeholder naming and gentle positioning.
- Target app selection.
- Permission education screen.
- Intervention screen copy variants.
- Home screen with today status.
- 15:00 check-in with 1-5 score.
- 22:00 achievement log with 0-10 entries.
- Records/review screen.
- Settings screen.
- Basic localization structure for Korean and English.

### P1

- Optional weekly/monthly plans.
- Lightweight progress artifact for protected time.
- More intervention copy variants.
- Basic notification timing controls.
- Manual fallback logging when app intervention is technically limited.

### P2

- AI coaching.
- Social accountability.
- Calendar integration.
- Full routine planner.
- Advanced analytics.
- B2B wellness/productivity services.

## Screen List

| Screen | Purpose | Priority |
| --- | --- | --- |
| Onboarding | Explain attention/time protection without finalizing naming | P0 |
| App Selection | Choose apps to protect against automatic opening | P0 |
| Permission Guide | Explain required OS permissions and limitations | P0 |
| Intervention Overlay/Screen | Warm pause at impulse moment | P0 |
| Home | Today overview and next gentle action | P0 |
| 15:00 Check-in | Low-burden 1-5 state check | P0 |
| 22:00 Achievement Log | Record protected time/actions without shame | P0 |
| Records | Review protected moments and check-ins | P0 |
| Settings | Manage apps, notification time, language, permissions | P0 |
| Weekly/Monthly Plans | Optional intention setting | P1 |

## UX Copy Requirements

Use UX Copy v0.2 as the latest source of truth:

- All Korean app-facing copy must use 존댓말.
- Do not use older casual/반말 copy.
- Avoid internal terms such as `금지`, `통제`, and `차단` as primary emotional copy.
- Copy should communicate attention/time sovereignty.
- Empty states must explain exactly what kind of record is missing.
- Examples of approved empty-state direction:
  - `아직 앱을 열기 전 멈춘 기록이 없어요.`
  - `아직 내 시간을 지켜낸 기록이 없어요.`
- Copy should feel natural, warm, and non-translation-like.

## Data Model Draft

### UserProfile

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | Local or server user ID |
| `locale` | string | Example: `ko-KR`, `en-US` |
| `timezone` | string | Used for 15:00 and 22:00 reminders |
| `createdAt` | datetime | Account/profile creation |
| `onboardingCompletedAt` | datetime nullable | Onboarding completion |

### ProtectedApp

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | App rule ID |
| `platformAppId` | string | Bundle/package identifier where available |
| `displayName` | string | User-facing app name |
| `isEnabled` | boolean | Whether LifeOS should intervene |
| `createdAt` | datetime | Rule creation |

### InterventionEvent

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | Event ID |
| `protectedAppId` | string nullable | Linked app if available |
| `triggeredAt` | datetime | Time of attempted app open or manual event |
| `copyVariantId` | string | Intervention copy shown |
| `userChoice` | enum | `paused`, `continued`, `protected_time`, `skipped` |
| `durationSeconds` | number nullable | Optional protected time |
| `source` | enum | `os_intervention`, `notification`, `manual` |

### MiddayCheckIn

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | Check-in ID |
| `date` | date | Local date |
| `score` | integer nullable | 1-5 |
| `note` | string nullable | Optional |
| `skipped` | boolean | Skips are allowed |

### AchievementLog

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | Log ID |
| `date` | date | Local date |
| `entries` | array | 0-10 protected moments or achievements |
| `mood` | string nullable | Optional lightweight mood |
| `createdAt` | datetime | Log timestamp |

### Plan

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | Plan ID |
| `period` | enum | `weekly`, `monthly` |
| `title` | string | Optional intention |
| `isActive` | boolean | Optional feature |
| `createdAt` | datetime | Plan creation |

## Technical Platform Notes

React Native and Flutter remain open. Do not finalize the stack in this PRD.

### React Native Candidate Notes

- Strong fit for Expo-based iteration and JavaScript/TypeScript ecosystem.
- App intervention APIs may require native modules or platform-specific work.
- Design system options can be explored later via React Native Paper, Tamagui, NativeWind, React Native Reusables, gluestack, or similar options.

### Flutter Candidate Notes

- Strong visual consistency and polished custom UI potential.
- App intervention permissions still require platform-specific native implementation.
- Design system options can be explored later via Material 3, Cupertino widgets, and Flutter UI kits.

## Technical Risks: App Intervention Permissions

This is the highest MVP risk area.

### iOS Risks

- iOS limits direct monitoring/interruption of arbitrary third-party app openings.
- Screen Time, FamilyControls, DeviceActivity, and ManagedSettings capabilities may be required.
- Some capabilities may require entitlements, user authorization, and careful App Review compliance.
- An overlay-style intervention may not be possible in the same way as Android.
- Fallback flows may be needed: shortcuts, notifications, scheduled check-ins, manual protected-time logging, or Screen Time style shields where allowed.

### Android Risks

- Android may allow more app-usage detection through Usage Access and Accessibility Service patterns.
- Accessibility Service use can trigger Play Store policy scrutiny if not justified by accessibility or permitted use cases.
- Background restrictions, OEM battery management, and OS version differences can reduce reliability.
- Overlay permissions can be sensitive and may create trust or review risks.
- Fallback flows may be needed for devices where app-open intervention is unreliable.

### Product Implication

The MVP should be designed with two layers:

- Ideal intervention: pause at selected app-open moment.
- Fallback intervention: notification/manual check-in/protected moment logging when OS-level app intervention is constrained.

## Success Metrics Draft

- Number of selected apps protected.
- Intervention events triggered.
- Percentage of interventions where the user pauses.
- Protected moments recorded.
- 15:00 check-in completion rate.
- 22:00 achievement log completion rate.
- Records viewed.
- Self-reported sense of getting time back.

## Open Questions

- Which platform should be prototyped first: iOS, Android, or both?
- What intervention method is technically feasible and App Store/Play Store compliant?
- What is the first target user segment?
- Should `하루조각` and `Daymark` remain placeholders or be replaced before prototype testing?
- What is the first visual progress metaphor?
- How strongly should the app use notifications?
- Should the MVP require login, or start local-first?
- What minimum analytics are acceptable without feeling surveillance-like?
