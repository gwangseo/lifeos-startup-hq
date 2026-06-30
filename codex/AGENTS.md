# Codex Agents

## Required First Step

Always read `MASTER_CONTEXT.md` before making substantial repository changes.

## Source of Truth

Use Notion-synced data as the source of truth:

- Conversations: `data/conversations.csv`
- Decisions: `data/decision_log.csv`
- Codex tasks: `data/codex_tasks.csv`
- Research: `data/research_database.csv`
- Competitors: `data/competitors.csv`
- Sync log: `data/sync_log.csv`

## Task Selection

Work only on tasks marked `Ready for Codex` unless the user explicitly assigns different work.

If a task is unclear, strategically ambiguous, or missing acceptance criteria, mark it as `Needs Review` rather than guessing.

## Git Rules

- Do not hardcode secrets.
- Do not push directly to `main` unless explicitly approved.
- Use branches for substantial work.
- Keep changes scoped to the assigned task.
- Summarize changed files and verification steps when done.

## LifeOS App Planning Guardrails

Before any future app implementation or PoC work, read:

1. `MASTER_CONTEXT.md`
2. Latest Notion-synced CSV files in `data/`
3. `docs/dev/AI_DEVELOPMENT_HANDOFF_V0_1.md`
4. `docs/dev/DEVELOPMENT_GUARDRAILS_V0_1.md`
5. `docs/dev/IMPLEMENTATION_SEQUENCE_V0_1.md`

For `LIFEOS-CODEX-008`, do not create app code, Android/iOS project skeletons, or production implementation files.

`LIFEOS-CODEX-007` is paused unless the user explicitly resumes it.

Preserve these app-planning constraints:

- `LifeOS` is a team/company placeholder.
- `하루조각 / Daymark` are app name placeholders.
- Do not finalize the brand name.
- Do not finalize React Native vs Flutter.
- Keep Korean app-facing copy in 존댓말.
- Preserve the direction: attention, time, and life-quality protection, not a generic blocker or habit tracker.
- Keep UI modern, soft, rounded, airy, beautiful, and 2026-ready.
- Keep platform permission risks explicit.
