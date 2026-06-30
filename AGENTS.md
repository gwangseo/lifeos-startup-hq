# LifeOS Startup HQ Agent Rules

## Required Reading

Always read `MASTER_CONTEXT.md` first before making substantial repository changes.

Before any app-related work, also read `docs/dev/AI_DEVELOPMENT_HANDOFF_V0_1.md`.

## Development Boundary

Do not start development unless explicitly assigned.

`LIFEOS-CODEX-007` is paused unless the user explicitly resumes it.

Do not create app code, Android/iOS project skeletons, or a `poc/` directory during documentation-only tasks.

## Product Guardrails

- Do not finalize the brand name.
- Do not finalize React Native vs Flutter.
- Keep Korean app-facing copy in 존댓말.
- Keep platform permission risks explicit.
- Preserve the product direction as attention, time, and life-quality protection, not a generic blocker app or generic habit tracker.

## Source Of Truth

Use Notion-synced data in `data/` as source-of-truth context when available, especially `data/codex_tasks.csv`, `data/conversations.csv`, and `data/decision_log.csv`.

Work only on tasks marked `Ready for Codex` unless the user explicitly assigns different work.
