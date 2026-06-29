# Notion Schema

This repository reads from existing LifeOS Notion data sources. Do not recreate the Notion parent page or databases.

The sync scripts use the Notion data source API and export rows into `data/*.csv`.

## Environment Variables

| Variable | Purpose |
| --- | --- |
| `NOTION_TOKEN` | Secret Notion integration token. |
| `NOTION_PARENT_PAGE_ID` | Existing LifeOS parent page ID. |
| `NOTION_CONVERSATION_DATA_SOURCE_ID` | Existing conversations data source ID. |
| `NOTION_DECISION_DATA_SOURCE_ID` | Existing decision log data source ID. |
| `NOTION_CODEX_TASK_DATA_SOURCE_ID` | Existing Codex task data source ID. |
| `NOTION_RESEARCH_DATA_SOURCE_ID` | Existing research data source ID. |
| `NOTION_COMPETITOR_DATA_SOURCE_ID` | Existing competitor data source ID. |
| `NOTION_SYNC_LOG_DATA_SOURCE_ID` | Existing sync log data source ID. |

## Existing Data Sources

### Conversations

- Environment variable: `NOTION_CONVERSATION_DATA_SOURCE_ID`
- ID: `9b79420c-8ac7-42d2-b310-588c3abafe48`
- CSV export: `data/conversations.csv`
- Purpose: Store GPT and strategy conversation summaries.

Expected properties:

| Property | Suggested type | Purpose |
| --- | --- | --- |
| `Name` | Title | Conversation title or short label. |
| `Date` | Date | Conversation date. |
| `Source` | Select | ChatGPT, Codex, meeting, interview, or other source. |
| `Summary` | Rich text | Concise summary. |
| `Key Insights` | Rich text | Main insights worth preserving. |
| `Decisions Linked` | Relation | Related decision records. |
| `Tasks Linked` | Relation | Related Codex tasks. |
| `Status` | Status | Review state. |

### Decision Log

- Environment variable: `NOTION_DECISION_DATA_SOURCE_ID`
- ID: `902997fe-f362-429f-98a2-60e8337f4ff7`
- CSV export: `data/decision_log.csv`
- Purpose: Track strategic, product, technical, and operating decisions.

Expected properties:

| Property | Suggested type | Purpose |
| --- | --- | --- |
| `Decision` | Title | Decision title. |
| `Date` | Date | Date decided or proposed. |
| `Area` | Select | Product, brand, content, market, operations, engineering, or strategy. |
| `Status` | Status | Proposed, Approved, Rejected, Needs Review, or Deprecated. |
| `Context` | Rich text | Why the decision exists. |
| `Decision Rationale` | Rich text | Reasoning and tradeoffs. |
| `Owner` | People | Accountable person. |
| `Related Conversation` | Relation | Linked conversation records. |

### Codex Task Queue

- Environment variable: `NOTION_CODEX_TASK_DATA_SOURCE_ID`
- ID: `fea41f9f-2807-4bd1-a49f-d6d861096910`
- CSV export: `data/codex_tasks.csv`
- Purpose: Queue execution work for Codex.

Expected properties:

| Property | Suggested type | Purpose |
| --- | --- | --- |
| `Task` | Title | Task name. |
| `Status` | Status | Backlog, Needs Review, Ready for Codex, In Progress, Blocked, or Done. |
| `Priority` | Select | Low, Medium, High, or Critical. |
| `Area` | Select | Product, research, automation, docs, data, content, or operations. |
| `Instructions` | Rich text | Implementation notes. |
| `Acceptance Criteria` | Rich text | Definition of done. |
| `Repository Path` | Rich text | Target repo path if known. |
| `Related Decision` | Relation | Linked decision records. |

### Research Database

- Environment variable: `NOTION_RESEARCH_DATA_SOURCE_ID`
- ID: `71e49791-e357-4fc5-94f8-5f8859f64298`
- CSV export: `data/research_database.csv`
- Purpose: Store research on apps, creators, books, communities, reports, sources, and ideas.

Expected properties:

| Property | Suggested type | Purpose |
| --- | --- | --- |
| `Topic` | Title | Research item title. |
| `Category` | Select | App, creator, book, community, report, source, market, or behavior. |
| `URL` | URL | Primary source URL. |
| `Summary` | Rich text | Concise summary. |
| `Insights` | Rich text | Notable insights. |
| `Tags` | Multi-select | Searchable tags. |
| `Status` | Status | To Review, Reviewed, Useful, Archived, or Needs Follow-up. |

### Competitors

- Environment variable: `NOTION_COMPETITOR_DATA_SOURCE_ID`
- ID: `10376d2e-2e71-4cb0-aefb-25842fc13822`
- CSV export: `data/competitors.csv`
- Purpose: Track competitor products, positioning, pricing, and strategic notes.

Expected properties:

| Property | Suggested type | Purpose |
| --- | --- | --- |
| `Name` | Title | Competitor name. |
| `Website` | URL | Website or product URL. |
| `Category` | Select | App, service, community, course, book, enterprise, or media. |
| `Positioning` | Rich text | How the competitor presents itself. |
| `Pricing` | Rich text | Pricing notes. |
| `Strengths` | Rich text | Competitive advantages. |
| `Weaknesses` | Rich text | Gaps or limitations. |
| `Tags` | Multi-select | Searchable tags. |

### Sync Log

- Environment variable: `NOTION_SYNC_LOG_DATA_SOURCE_ID`
- ID: `0bd270a8-089b-4491-bde6-6a285219213d`
- CSV export: `data/sync_log.csv`
- Purpose: Track sync runs, issues, and automation health.

Expected properties:

| Property | Suggested type | Purpose |
| --- | --- | --- |
| `Run` | Title | Sync run label. |
| `Started At` | Date | Start timestamp. |
| `Completed At` | Date | Completion timestamp. |
| `Status` | Status | Success, Partial, Failed, or Needs Review. |
| `Rows Synced` | Number | Total rows synced. |
| `Details` | Rich text | Human-readable run notes. |
| `Error` | Rich text | Error details when applicable. |

## CSV Export Behavior

Each CSV includes metadata columns followed by Notion property columns:

- `notion_page_id`
- `notion_url`
- `created_time`
- `last_edited_time`
- `archived`
- `in_trash`

Notion properties are flattened into readable strings. Complex values such as relations, rollups, formulas, and files are serialized conservatively so the export remains stable and easy to inspect.

