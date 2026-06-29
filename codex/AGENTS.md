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

