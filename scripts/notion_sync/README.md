# Notion Sync Scripts

These scripts read existing LifeOS Notion data sources and export them into repository files.

## Files

- `notion_client.py` - small standard-library Notion API client.
- `sync_notion_to_csv.py` - exports configured data sources into `data/*.csv`.
- `sync_notion_to_markdown.py` - scaffolding for future Markdown exports from selected CSV rows.

## Local Usage

Copy `.env.example` to `.env`, set `NOTION_TOKEN`, then run:

```bash
python scripts/notion_sync/sync_notion_to_csv.py
```

Preview Markdown export routing:

```bash
python scripts/notion_sync/sync_notion_to_markdown.py --dry-run
```

## Notes

- The scripts do not create Notion databases.
- The scripts do not write secrets to disk.
- CSV files are overwritten on each sync to keep the repository aligned with Notion.
- Markdown export routing is intentionally simple and should be expanded once the final Notion properties are stable.

