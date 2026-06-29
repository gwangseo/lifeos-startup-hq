# LifeOS Startup HQ

LifeOS Startup HQ is the execution repository for a startup focused on digital detox, habit formation, meaningful routines, productivity, self-improvement, content, apps, books, community, AI coaching, and B2B wellness/productivity services.

This repository is designed to work with the existing LifeOS Notion workspace. Notion remains the central knowledge database, while GitHub stores synced data, implementation tasks, documentation, automation, and source-controlled operating context.

## Operating Model

- ChatGPT is used for strategy, planning, research, and task creation.
- Notion is the source of truth for conversations, decisions, research, competitors, Codex tasks, and sync logs.
- GitHub is the execution repository.
- Codex is the implementation, documentation, automation, and data organization agent.
- GitHub Actions syncs existing Notion data sources into this repository as CSV files.
- Later, a Custom GPT Action or Vercel API can save GPT conversation summaries into Notion.

## Repository Map

- `MASTER_CONTEXT.md` - persistent project context that Codex should read first.
- `DECISION_LOG.md` - human-readable decision log scaffold.
- `CODEX_TASK_QUEUE.md` - local task queue scaffold, synced task data lives in `data/codex_tasks.csv`.
- `NOTION_SCHEMA.md` - documented Notion data source IDs and expected properties.
- `data/` - CSV exports generated from Notion.
- `docs/` - product, brand, content, market, automation, and operations documentation.
- `research/` - market, competitor, creator, app, book, community, report, and source research.
- `scripts/notion_sync/` - Notion export scripts.
- `scripts/gpt_actions/` - Custom GPT Action scaffolding.
- `codex/` - Codex-specific operating rules and templates.

## Quick Start

1. Create a Notion integration and grant it access to the existing LifeOS parent page and databases.
2. Copy `.env.example` to `.env` for local runs.
3. Set `NOTION_TOKEN` in `.env`.
4. Run:

```bash
python scripts/notion_sync/sync_notion_to_csv.py
```

GitHub Actions uses repository secrets instead of `.env`.

## GitHub Actions Setup

Add these repository secrets:

- `NOTION_TOKEN`
- `NOTION_PARENT_PAGE_ID`
- `NOTION_CONVERSATION_DATA_SOURCE_ID`
- `NOTION_DECISION_DATA_SOURCE_ID`
- `NOTION_CODEX_TASK_DATA_SOURCE_ID`
- `NOTION_RESEARCH_DATA_SOURCE_ID`
- `NOTION_COMPETITOR_DATA_SOURCE_ID`
- `NOTION_SYNC_LOG_DATA_SOURCE_ID`

The workflow in `.github/workflows/notion-sync.yml` runs every 6 hours and can also be triggered manually.

