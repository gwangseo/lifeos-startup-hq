# Cursor Master Prompt v0.1

Use this prompt for a future Cursor AI session after this handoff pack has been reviewed.

```text
You are assisting with the lifeos-startup-hq repository.

Before coding, read these files in order:
1. MASTER_CONTEXT.md
2. data/codex_tasks.csv
3. data/conversations.csv
4. data/decision_log.csv
5. docs/dev/AI_DEVELOPMENT_HANDOFF_V0_1.md
6. docs/dev/DEVELOPMENT_GUARDRAILS_V0_1.md
7. docs/dev/IMPLEMENTATION_SEQUENCE_V0_1.md
8. docs/dev/REVIEW_CHECKLIST_V0_1.md

Then read the relevant product, design, and technical docs referenced in the handoff.

Do not finalize the brand name. LifeOS is a team/company placeholder. 하루조각 / Daymark are app name placeholders.

Do not finalize React Native vs Flutter unless explicitly assigned after the platform feasibility review.

Keep Korean app-facing copy in 존댓말.

Do not turn this into a generic blocker, habit tracker, productivity dashboard, or punitive restriction app.

The app direction is attention, time, and life-quality protection.

UI must remain modern, soft, rounded, airy, beautiful, and 2026-ready.

Platform permission risks around iOS and Android intervention must stay visible in code comments, docs, and review notes where relevant.

Clearly identify whether you are working on:
- planning documentation
- future throwaway PoC
- future production app code

Do not create production app code during planning tasks.

If LIFEOS-CODEX-007 is mentioned, confirm it has been explicitly resumed. Otherwise treat it as paused.
```
