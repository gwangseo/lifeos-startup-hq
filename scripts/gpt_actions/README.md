# GPT Actions

This folder contains scaffolding for a future Custom GPT Action or Vercel API that can save GPT conversation summaries into Notion.

The first version is intentionally a placeholder. Do not deploy `openapi.yaml` as-is without replacing the server URL and implementing the backing API.

Future implementation should:

- Validate incoming payloads.
- Authenticate requests.
- Write summaries to the existing conversations data source.
- Link related decisions, research, or Codex tasks when IDs are provided.
- Avoid exposing `NOTION_TOKEN` to the client.

