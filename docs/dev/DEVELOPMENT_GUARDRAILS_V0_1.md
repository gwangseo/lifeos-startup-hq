# LifeOS Development Guardrails v0.1

Status: active guardrails draft
Task: `LIFEOS-CODEX-008`

## Must Not Change

- Do not finalize the brand name.
- Do not finalize React Native vs Flutter.
- Do not replace 존댓말 Korean copy with 반말 or casual copy.
- Do not turn the app into a generic blocker or generic habit tracker.
- Do not remove permission risks from docs, UI, or review notes.
- Do not hardcode secrets.
- Do not push directly to `main` unless explicitly approved.
- Do not create app code or skeletons during planning tasks.
- Do not execute `LIFEOS-CODEX-007` unless explicitly resumed.

## Product Guardrails

- Frame the app around attention, time, and life-quality protection.
- Keep intervention copy gentle, optional-feeling, and non-shaming.
- Preserve skippable check-ins and achievement logs.
- Avoid unsupported claims about saved minutes or app blocking.
- Keep fallback modes useful, not hidden.

## Design Guardrails

- Modern, soft, rounded, airy, beautiful, 2026-ready.
- Avoid rigid productivity dashboards.
- Avoid harsh red warning-heavy blocker UI.
- Avoid childish gamification unless intentionally reviewed.
- Make permission health visible and calm.

## Technical Guardrails

- Platform permission feasibility is the highest technical risk.
- UI libraries do not solve iOS/Android intervention permissions.
- Native modules are expected for serious intervention paths.
- Expo Go alone is unlikely to be enough if React Native is chosen.
- Flutter still needs native MethodChannel/plugin work for OS-level behavior.
- Treat PoC code as throwaway unless explicitly promoted.

## Documentation Guardrails

- Clearly label planning vs PoC vs production documents.
- Keep unresolved decisions visible.
- Cite source docs or synced Notion context when making strategic changes.
- Mark unclear strategy as `Needs Review`.
