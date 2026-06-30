# LifeOS Platform Permission Strategy v0.1

Status: technical planning draft
Task: `LIFEOS-CODEX-008`
Implementation status: not started

## Boundary

This is a strategy document, not a PoC implementation. `LIFEOS-CODEX-007` remains paused until this handoff pack is reviewed and explicitly resumed.

## Primary Feasibility Question

Can LifeOS show a trustworthy pause/intervention experience before selected distracting apps open, while staying compliant with iOS App Review, Google Play policies, user trust, and platform reliability limits?

## Planning vs PoC vs Production

| Stage | Purpose | Output |
| --- | --- | --- |
| Planning documents | Preserve product, UX, design, and technical constraints | This handoff pack |
| Future PoC documents | Validate iOS/Android permission feasibility with throwaway code | Separate spike plan and results |
| Future production app documents | Define shippable architecture after feasibility is known | Later specs only |

## iOS Options

| Option | Potential Role | Risk |
| --- | --- | --- |
| `FamilyControls` | User authorization and app/category selection for Screen Time style features | Entitlement and App Review gating |
| `DeviceActivity` | Monitoring selected activity schedules/events | Limited flexibility and entitlement needs |
| `ManagedSettings` | Shielding or discouraging selected apps/categories | Shield UX may not support fully custom intervention |
| Screen Time style shield | Closest iOS-native intervention metaphor | May feel less branded/custom than desired |
| Notifications | Fallback reminder/pause prompt | Cannot reliably appear before app open |
| Manual logging | Lowest-risk fallback | Less automatic; product value changes |

Open iOS questions:

- Is the required entitlement available for this product category?
- Can the user-selected app flow support non-parental, self-directed digital wellness positioning?
- How much custom copy and UI is available in the shield experience?
- What will App Review accept for a consumer attention-protection app?

## Android Options

| Option | Potential Role | Risk |
| --- | --- | --- |
| `UsageStatsManager` | Detect recent/current app usage patterns | Requires `PACKAGE_USAGE_STATS`; may not be real-time enough |
| Usage Access settings | User-granted visibility into app usage | Setup friction and OEM variation |
| `AccessibilityService` | Potential app-open detection and intervention trigger | High Google Play policy and user-trust risk |
| Overlay / `SYSTEM_ALERT_WINDOW` | Pause UI over another app | Sensitive permission, policy risk, OEM reliability issues |
| Foreground/background service | Reliability support | Battery restrictions and OS policy limits |
| Notifications | Lower-risk fallback | Not guaranteed before app open |
| Manual logging | Reliable fallback | Less automatic |

Open Android questions:

- Can app-open detection be reliable enough without overusing AccessibilityService?
- Would Google Play approve the AccessibilityService use case for self-directed digital wellness?
- Does overlay create acceptable UX and policy risk?
- How do battery restrictions affect intervention reliability?

## Permission Health Model

Future app UX should expose the current capability honestly:

- `Full intervention possible`
- `Partial intervention possible`
- `Reminder-only mode`
- `Manual mode`
- `Needs setup`
- `Unknown`

The app must not hide degraded capability behind optimistic copy.

## Fallback Product Shape

If direct app-open intervention is not feasible or not review-safe:

- keep protected app selection as intention setting
- use notifications as timed or contextual reminders
- offer manual "I paused before opening" logging
- preserve 15:00 check-in and 22:00 achievement log
- present records around attention and life-quality moments, not fake blocked minutes

## Green / Yellow / Red Decision

| Decision | Meaning |
| --- | --- |
| Green | Direct intervention is feasible on target platforms with acceptable review, policy, and reliability risk. |
| Yellow | One platform or one path is feasible, but fallback UX is required for the other path or some users. |
| Red | Direct intervention is too risky or unreliable; shift MVP toward reminder/manual mode and reflection. |

## What AI Developers Must Not Do

- Do not promise direct app blocking before platform validation.
- Do not treat UI libraries as solving OS permission limits.
- Do not choose React Native vs Flutter before native capability requirements are clear.
- Do not ship code that depends on sensitive permissions without review of store policy and user trust.
