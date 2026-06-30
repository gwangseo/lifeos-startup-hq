# LifeOS Design System v0.1

Status: design planning draft
Task: `LIFEOS-CODEX-008`
Implementation status: not started

## Design Intent

The app should feel modern, soft, rounded, airy, beautiful, and 2026-ready. It should support reflection and self-trust rather than control.

Avoid:

- old productivity app visuals
- rigid utility dashboards
- harsh blocker aesthetics
- dense admin panels
- gamification that feels childish or loud
- one-note color palettes

## Visual Principles

| Principle | Direction |
| --- | --- |
| Soft clarity | Calm hierarchy, readable surfaces, generous spacing |
| Emotional safety | No punitive red-heavy states unless truly critical |
| Gentle progress | Progress should feel earned, not forced |
| Permission honesty | Platform limitations must be visible and calmly explained |
| Cross-platform polish | Native-feeling details without locking React Native vs Flutter |

## Token Direction

These are design directions, not final code tokens.

### Color

- Base: warm off-white or soft neutral
- Text: deep neutral with high readability
- Primary: calm blue or blue-green
- Positive: soft green
- Warm accent: peach/coral used sparingly
- Warning: muted amber, not alarmist
- Error: restrained red only for true failure states

### Typography

- Korean readability comes first.
- Use comfortable line-height for Korean body text.
- Avoid negative letter spacing.
- Keep hero-sized type only for onboarding or major empty states.

### Shape

- Rounded, soft surfaces.
- Cards and controls should feel tactile but not bulky.
- Suggested radius direction: 16-28px for mobile surfaces, smaller only for dense lists.

### Spacing

- Airy vertical rhythm.
- Avoid cramming data into dashboard grids.
- Touch targets should remain comfortable on small phones.

### Motion

- Slow, gentle transitions.
- Breathing or pause animations should reduce urgency.
- Avoid distracting particle-heavy effects.

### Elevation

- Subtle shadow or blur-like layering.
- Avoid heavy drop shadows or hard borders.

## Accessibility Requirements

- Maintain color contrast for body text and key controls.
- Do not rely on color alone for permission status.
- Support Dynamic Type or equivalent text scaling in future implementation.
- Ensure Korean copy can wrap gracefully.
- Motion should be reducible or skippable.

## Design System Objects

Future production app design should define:

- color tokens
- semantic status tokens
- typography scale
- spacing scale
- radius scale
- icon usage
- button variants
- card/surface variants
- form/list rows
- permission status patterns
- record timeline patterns

## What AI Developers Must Not Change

- Do not make the UI look like a generic blocker or habit tracker.
- Do not introduce harsh "blocked" language as the primary product emotion.
- Do not finalize a brand name.
- Do not select React Native vs Flutter from design preferences alone.
- Do not remove explicit permission risk states from the visual system.
