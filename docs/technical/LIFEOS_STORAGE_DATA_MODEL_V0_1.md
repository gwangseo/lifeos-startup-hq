# LifeOS Storage and Data Model v0.1

Status: data planning draft
Task: `LIFEOS-CODEX-008`
Implementation status: not started

## Purpose

This document defines a lightweight data model for future planning. It does not choose a database, sync provider, backend, or implementation framework.

## Storage Principles

- Local-first until account/cloud sync is intentionally designed.
- Store only what is needed for the MVP.
- Avoid sensitive app-usage overcollection.
- Keep permission state explainable to the user.
- Do not derive protected minutes unless the platform path can measure them reliably.

## Core Entities

### `UserProfile`

| Field | Notes |
| --- | --- |
| `id` | Local identifier |
| `locale` | Korean first, English-ready |
| `onboardingCompletedAt` | Nullable |
| `createdAt` | Local timestamp |

### `ProtectedApp`

| Field | Notes |
| --- | --- |
| `id` | Local identifier |
| `platformAppId` | Bundle ID/package name if available |
| `displayName` | User-facing app name |
| `iconRef` | Optional local/system icon reference |
| `isEnabled` | Whether pause is active |
| `createdAt` | Local timestamp |

### `PermissionStatus`

| Field | Notes |
| --- | --- |
| `platform` | `ios` or `android` |
| `capabilityMode` | `full`, `limited`, `reminder_only`, `manual`, `unknown` |
| `requiredAction` | Nullable setup/troubleshooting action |
| `lastCheckedAt` | Local timestamp |
| `details` | Non-sensitive status metadata |

### `InterventionEvent`

| Field | Notes |
| --- | --- |
| `id` | Local identifier |
| `protectedAppId` | Nullable if manual |
| `triggerType` | `app_open`, `shield`, `notification`, `manual` |
| `outcome` | `continued`, `stepped_away`, `dismissed`, `unknown` |
| `createdAt` | Local timestamp |
| `note` | Optional user note |

### `CheckIn`

| Field | Notes |
| --- | --- |
| `id` | Local identifier |
| `type` | `midday` |
| `score` | 1-5, nullable if skipped |
| `note` | Optional |
| `createdAt` | Local timestamp |

### `AchievementLog`

| Field | Notes |
| --- | --- |
| `id` | Local identifier |
| `date` | Local day |
| `entries` | 0-10 short text entries |
| `createdAt` | Local timestamp |
| `updatedAt` | Local timestamp |

### `Plan`

| Field | Notes |
| --- | --- |
| `id` | Local identifier |
| `type` | `weekly` or `monthly` |
| `intention` | Optional user text |
| `isActive` | Boolean |
| `createdAt` | Local timestamp |

### `AppSetting`

| Field | Notes |
| --- | --- |
| `key` | Setting key |
| `value` | Serializable value |
| `updatedAt` | Local timestamp |

## Privacy Notes

- Do not store full app-usage timelines by default.
- Do not collect unrelated app history.
- Make manual deletion/export requirements part of future production planning.
- Any analytics must be reviewed separately before implementation.

## Still Undecided

- SQLite vs platform storage vs framework-specific local database
- Cloud sync or account model
- Backup/export strategy
- Analytics provider
- Exact retention policy
