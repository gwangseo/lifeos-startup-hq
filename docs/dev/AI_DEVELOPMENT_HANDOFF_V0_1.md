# LifeOS AI Development Handoff v0.1

Status: master handoff draft
Task: `LIFEOS-CODEX-008`
Implementation status: not started

## Purpose

This pack prepares future Codex, Cursor AI, or other AI development sessions before app implementation begins. It consolidates product, UX, UI, technical, permission, and review constraints into a single reading path.

## Current Instruction

Do not start app development from this task. Do not create app code. Do not create Android/iOS project skeletons. Do not execute `LIFEOS-CODEX-007` unless the user explicitly resumes it after reviewing this handoff pack.

## Exact Reading Order For Future AI Sessions

1. `MASTER_CONTEXT.md`
2. `data/codex_tasks.csv`
3. `data/conversations.csv`
4. `data/decision_log.csv`
5. `docs/dev/AI_DEVELOPMENT_HANDOFF_V0_1.md`
6. `docs/product/LIFEOS_MVP_SCOPE_V0_1.md`
7. `docs/product/LIFEOS_SCREEN_SPEC_V0_1.md`
8. `docs/design/LIFEOS_DESIGN_SYSTEM_V0_1.md`
9. `docs/design/LIFEOS_COMPONENT_SPEC_V0_1.md`
10. `docs/technical/LIFEOS_PLATFORM_PERMISSION_STRATEGY_V0_1.md`
11. `docs/technical/LIFEOS_TECHNICAL_ARCHITECTURE_V0_1.md`
12. `docs/technical/LIFEOS_STORAGE_DATA_MODEL_V0_1.md`
13. `docs/technical/LIFEOS_TEST_PLAN_V0_1.md`
14. `docs/dev/DEVELOPMENT_GUARDRAILS_V0_1.md`
15. `docs/dev/IMPLEMENTATION_SEQUENCE_V0_1.md`
16. `docs/dev/REVIEW_CHECKLIST_V0_1.md`
17. Agent-specific prompt: `docs/dev/CODEX_MASTER_PROMPT_V0_1.md` or `docs/dev/CURSOR_MASTER_PROMPT_V0_1.md`

If older PRD, wireframe, UX copy, UI direction, UI reference research, platform feasibility, or permission-flow planning docs are present in the branch, read them after this pack as supporting sources.

## Source Material Consolidated

- LifeOS PRD v0.1
- Wireframe brief v0.1
- UX copy deck v0.2
- Localization draft v0.1
- UI direction v0.1
- UI reference research v0.1
- Platform feasibility spike brief v0.1
- Existing app permission flow review and spike execution planning
- Latest synced Notion conversations and decisions

## Decisions To Preserve

- `LifeOS` is a placeholder for team/company.
- `하루조각 / Daymark` are app name placeholders.
- Brand name is not final.
- React Native vs Flutter is not final.
- Korean app-facing copy uses 존댓말.
- The product protects attention, time, and life quality.
- It is not a generic blocker app or generic habit tracker.
- UI should remain modern, soft, rounded, airy, beautiful, and 2026-ready.
- Platform permission risks must remain explicit.

## Still Undecided

- Final brand/app name
- Cross-platform stack
- iOS entitlement/App Review viability
- Android Play policy viability
- First implementation target after review
- Local database and sync strategy
- Production analytics/privacy model

## Start Conditions For Future Development

Future development should begin only after:

- this handoff pack is reviewed
- `LIFEOS-CODEX-007` is explicitly resumed or replaced
- platform spike scope is confirmed
- implementation branch and target are named
- expected output is clearly separated between PoC and production app
