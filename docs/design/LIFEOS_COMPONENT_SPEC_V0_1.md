# LifeOS Component Spec v0.1

Status: design planning draft
Task: `LIFEOS-CODEX-008`
Implementation status: not started

## Purpose

This document lists the component vocabulary future AI developers should preserve when implementation begins. It is stack-neutral and should work for either React Native or Flutter.

## Component Candidates

| Component | Purpose | Key States |
| --- | --- | --- |
| `SoftScreen` | Base screen layout with safe area, background, and spacing | default, scrollable |
| `LifeCard` | Soft rounded content container | default, selected, disabled |
| `PrimaryPillButton` | Main CTA | default, pressed, loading, disabled |
| `SecondaryTextButton` | Low-pressure secondary action | default, pressed, disabled |
| `ProtectedAppRow` | App row for selection/settings | selected, unselected, unavailable |
| `PermissionStatusCard` | Current Permission Health summary | granted, limited, denied, unknown |
| `PermissionStepRow` | One setup/troubleshooting step | todo, active, done, failed |
| `InterventionPrompt` | Pause screen prompt block | full, shield, notification, manual |
| `BreathingPauseIndicator` | Visual pause/countdown cue | running, paused, complete |
| `CheckInScale` | 1-5 midpoint reflection selector | empty, selected, skipped |
| `AchievementEntryCard` | One 22:00 achievement entry | draft, saved, empty |
| `RecordMomentCard` | Timeline item for pause/check-in/win | pause, check-in, achievement |
| `EmptyState` | Specific empty records or setup states | first-use, no-records, unavailable |
| `SettingsRow` | Settings navigation/toggle row | default, toggled, warning |

## Component Rules

- Components must support Korean copy wrapping.
- Permission-related components must show fallback states.
- Buttons should use concise text and clear hierarchy.
- Icons may be used, but they must support clarity rather than decoration.
- Do not bury permission issues in developer-only logs.

## Permission Health Components

Permission Health should be treated as a first-class product system.

Required statuses:

- `Full`: app-open intervention appears technically available.
- `Limited`: only some platform capabilities are available.
- `Reminder Only`: notification/manual fallback is active.
- `Needs Attention`: user action or OS setting is required.
- `Unknown`: app cannot verify state yet.

## Intervention Components

The pause experience may vary by OS capability:

- Native pause screen if allowed.
- Screen Time style shield on iOS if entitlement and review allow it.
- Android overlay/activity/accessibility-driven pause only if policy and reliability are acceptable.
- Notification or manual fallback when direct intervention is not available.

## Review Checklist For Components

- Does this component preserve a calm, non-shaming tone?
- Does it avoid unsupported technical promises?
- Does it support the fallback product shape?
- Does it look current and mobile-native rather than web-dashboard-like?
- Does it remain usable if copy expands in Korean?
