# LifeOS Startup HQ Master Context

LifeOS Startup HQ is a startup project focused on helping people build healthier relationships with technology, improve daily routines, and create meaningful personal operating systems.

## Core Themes

- Digital detox and intentional technology use
- Habit formation and behavior change
- Meaningful daily routines
- Productivity and self-improvement
- AI coaching and personal operating systems
- Content media, books, apps, and community
- B2B wellness and productivity services

## System Architecture

- ChatGPT supports strategy, planning, research, synthesis, and task creation.
- Notion is the central knowledge database and source of truth.
- GitHub stores execution artifacts, synced datasets, documentation, automation, and code.
- Codex implements repository tasks, documentation, scripts, and structured data organization.
- GitHub Actions syncs Notion data sources into GitHub.
- Future Custom GPT Actions or Vercel APIs may write GPT conversation summaries into Notion.

## Existing Notion Workspace

The Notion parent page and six Notion data sources already exist. Do not recreate them.

- Parent page: `38e7fcdc632080e0a6dbe668bdaaad24`
- Conversations: `9b79420c-8ac7-42d2-b310-588c3abafe48`
- Decisions: `902997fe-f362-429f-98a2-60e8337f4ff7`
- Codex tasks: `fea41f9f-2807-4bd1-a49f-d6d861096910`
- Research: `71e49791-e357-4fc5-94f8-5f8859f64298`
- Competitors: `10376d2e-2e71-4cb0-aefb-25842fc13822`
- Sync log: `0bd270a8-089b-4491-bde6-6a285219213d`

## Codex Rules

Codex must read this file first before making substantial changes.

Codex should use Notion-synced CSV data as source-of-truth context when available. Work should focus on tasks marked `Ready for Codex`. If a task or decision is ambiguous, Codex should mark it as `Needs Review` rather than inventing strategic direction.

Secrets must never be hardcoded. Substantial work should happen on branches. Do not push directly to `main` unless explicitly approved.

## Current App Planning State

The LifeOS mobile app planning track is still pre-implementation.

- `LifeOS` is a team/company placeholder.
- `하루조각 / Daymark` are app name placeholders.
- The brand name is not finalized.
- React Native vs Flutter is not finalized.
- Korean app-facing copy should use 존댓말.
- The product direction is attention, time, and life-quality protection, not a generic blocker or habit tracker.
- The UI direction should remain modern, soft, rounded, airy, beautiful, and 2026-ready.
- iOS and Android app-intervention permission risks must remain explicit.

`LIFEOS-CODEX-008` creates the AI Development Handoff Pack v0.1 before implementation. `LIFEOS-CODEX-007` is paused until this handoff pack is reviewed and the user explicitly resumes PoC work.
