# LifeOS MVP Scope v0.1

Status: planning handoff draft
Task: `LIFEOS-CODEX-008`
Implementation status: not started

## Purpose

This document defines the MVP boundary for the future LifeOS mobile app planning track. It is not an implementation spec, code task, or final brand decision.

## Naming Rules

- `LifeOS` is a team/company placeholder.
- `하루조각 / Daymark` are app name placeholders.
- Do not finalize the brand name in development, UI, copy, package names, bundle IDs, or store metadata.
- Korean app-facing copy must use 존댓말.

## Product Thesis

LifeOS is an attention, time, and life-quality protection app. It is not a generic blocker app and not a generic habit tracker.

The MVP should combine:

- one sec-style impulse interruption before distracting app use
- Forest-style visible emotional reward for protected time
- Daylio-style low-friction reflection
- Finch-style warm, non-shaming support

## P0 MVP Scope

| Area | Included in P0 | Notes |
| --- | --- | --- |
| Onboarding | Gentle product promise, placeholder naming, copy rules | No hard brand lock-in |
| Protected app setup | Select apps the user wants to pause before opening | Platform feasibility still unknown |
| Permission education | Explain required permissions and fallback modes | Permission Health must be visible; fallback is part of P0 |
| Pause/intervention experience | A short pause before opening selected distracting apps if technically feasible | Must not overpromise OS capability |
| Manual protected-time logging | Let users manually record a pause or protected moment when direct intervention is unavailable | P0 fallback path |
| Home | Today state, next gentle action, permission health | Avoid dense dashboard feel |
| 15:00 check-in | 1-5 low-friction attention/life-quality score | Skippable |
| 22:00 achievement log | 0-10 small wins or protected moments | Skippable, non-shaming |
| Records | Saved pauses, check-ins, small wins | Avoid unsupported minute claims |
| Settings | Protected apps, permissions, reminders, language-ready settings | Support fallback modes |

## P0 Fallback Modes

Fallback modes are part of P0 when platform intervention is limited, unavailable, unreliable, or not yet approved by store review.

P0 fallback must include:

- reminder-only mode
- manual protected-time logging
- manual pause or protected-moment records
- Permission Health status that explains why full intervention is limited

These fallback modes should preserve the same product thesis: protecting attention, time, and life quality without pretending the app can always intervene before another app opens.

## P1 Candidates

- Weekly/monthly intention plans
- Lightweight progress artifact or garden-like reward system
- Expanded intervention copy rotation
- Notification tuning
- Basic localization review for Korean and English

## Deferred

- AI coaching
- Social/community features
- B2B workspace wellness dashboards
- Advanced analytics
- Calendar or full planner workflows
- Production subscriptions, accounts, cloud sync, or admin tools

## Non-Goals

- Do not build a punitive blocking product.
- Do not make the product feel like an admin, MDM, parental-control, or surveillance tool.
- Do not position the core value as productivity optimization alone.
- Do not assume protected minutes can be measured reliably until platform validation proves it.
- Do not choose React Native vs Flutter in this document.

## Success Signals

Early success should be evaluated by:

- whether users understand the app as protecting attention and life quality
- whether permission setup feels trustworthy and recoverable
- whether pause moments reduce autopilot app opening
- whether check-ins and achievement logs feel light enough to repeat
- whether platform fallback modes still preserve the product thesis

## Still Undecided

- Final app/company name
- React Native vs Flutter
- Exact iOS intervention mechanism
- Exact Android intervention mechanism
- Whether the first prototype is Android-only, iOS-only, or cross-platform shell plus native PoCs
- Final metrics for protected time and life-quality progress
