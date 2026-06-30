# LifeOS Test Plan v0.1

Status: test planning draft
Task: `LIFEOS-CODEX-008`
Implementation status: not started

## Purpose

This plan defines what future work must validate. It does not create tests or implementation code.

## Review Stages

| Stage | Validation |
| --- | --- |
| Documentation review | Confirm decisions, constraints, and reading order are clear |
| Permission PoC review | Confirm platform capability and policy risk |
| Prototype review | Confirm screens, data, and fallback modes work |
| Production readiness review | Confirm store policy, privacy, stability, and UX quality |

## Product Tests

- The app is understood as attention/time/life-quality protection.
- It does not read as a generic blocker or habit tracker.
- Copy remains polite Korean 존댓말.
- Skipping check-ins or logs does not create shame.
- Records do not imply unsupported measurement.

## UI Tests

- Modern, soft, rounded, airy, beautiful, 2026-ready feel.
- Korean text wraps correctly on small devices.
- Permission states are visible and understandable.
- Empty states are specific and helpful.
- Motion is gentle and can be reduced.

## Platform Permission Spike Tests

### iOS

- Can the app request and use relevant Screen Time APIs?
- Are `FamilyControls`, `DeviceActivity`, and `ManagedSettings` viable for the intended category?
- Is the shield experience acceptable for the product?
- What entitlement and App Review risks remain?
- What fallback is needed if entitlement is unavailable?

### Android

- Can Usage Access identify relevant app-open moments reliably enough?
- Is AccessibilityService required, and is the use case policy-safe?
- Is overlay permission acceptable and reliable?
- How do foreground/background restrictions affect behavior?
- What fallback is needed for OEM/device variation?

## Future Code Test Categories

- Unit tests for domain logic
- Component tests for UI states
- Permission adapter contract tests
- Storage migration tests
- Manual device tests
- Accessibility checks
- Localization checks

## Suggested Device Matrix For Future PoC

- Recent iPhone on current iOS
- Older supported iPhone if available
- Pixel or Android reference device
- Samsung device for OEM behavior
- Android version with current Play policy expectations

## Acceptance Decision

Use Green/Yellow/Red:

- Green: proceed toward production prototype.
- Yellow: proceed with scoped fallback and platform-specific constraints.
- Red: redesign MVP around reminder/manual mode before coding production app.
