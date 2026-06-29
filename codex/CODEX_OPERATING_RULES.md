# Codex Operating Rules

## Context Order

1. Read `MASTER_CONTEXT.md`.
2. Review relevant synced Notion CSV files in `data/`.
3. Check `CODEX_TASK_QUEUE.md` for local notes.
4. Confirm the task is ready and scoped.

## Notion Data

Notion is the source of truth. This repository reads from existing Notion data sources and should not recreate them.

When Notion data conflicts with local notes, prefer the synced Notion export unless the user explicitly says otherwise.

## Task Readiness

Codex should work only on tasks marked `Ready for Codex`.

If strategic direction is unclear, use `Needs Review`.

If implementation is blocked by missing credentials, missing access, or unclear requirements, document the blocker and stop before making risky assumptions.

## Secrets

Never hardcode tokens, API keys, credentials, or private URLs.

Use:

- `.env` for local secrets.
- `.env.example` for non-secret variable names and safe IDs.
- GitHub Actions secrets for automation.

## Git Workflow

- Use branches for substantial work.
- Do not push directly to `main` unless explicitly approved.
- Keep commits focused and descriptive.
- Default setup commit message: `chore(setup): initialize LifeOS GitHub automation infrastructure`.

## Documentation

Keep documentation simple, accurate, and close to the work it describes. Prefer stable operating context over speculative detail.

