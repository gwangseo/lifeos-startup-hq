# LifeOS Implementation Sequence v0.1

Status: future sequence draft
Task: `LIFEOS-CODEX-008`
Implementation status: not started

## Current State

Implementation has not started. `LIFEOS-CODEX-007` is paused until this handoff pack is reviewed and explicitly resumed.

## Phase 0: Handoff Review

Goal: freeze the immediate next step.

Tasks:

- Review all files in this handoff pack.
- Confirm whether the next task is a native PoC, UI prototype, or additional planning.
- Confirm that naming and stack remain placeholders.
- Confirm permission risks are accepted for spike exploration.

Exit criteria:

- User explicitly approves next task.
- Branch and output files are clear.

## Phase 1: Platform Feasibility PoC

Goal: validate intervention feasibility before production app development.

Possible tracks:

- Android throwaway PoC for Usage Access, AccessibilityService, overlay, notification fallback.
- iOS throwaway PoC or entitlement research for Screen Time APIs.
- Cross-platform native module implication review.

Exit criteria:

- Green/Yellow/Red decision.
- Store policy risks documented.
- Fallback product shape confirmed.

## Phase 2: Stack Decision

Goal: choose React Native or Flutter only after native requirements are known.

Inputs:

- iOS feasibility result
- Android feasibility result
- native module complexity
- team/dev velocity
- UI requirements

Exit criteria:

- stack decision documented as reversible or irreversible
- production architecture updated

## Phase 3: MVP Prototype

Goal: build a narrow prototype after feasibility and stack decisions.

Candidate scope:

- onboarding
- protected app setup shell
- permission health shell
- pause/intervention shell or fallback
- home
- 15:00 check-in
- 22:00 achievement log
- records
- settings

Exit criteria:

- core flow works in agreed platform mode
- UI matches design direction
- copy remains 존댓말

## Phase 4: Production Readiness Planning

Goal: decide what is shippable.

Tasks:

- privacy/data review
- app store policy review
- accessibility review
- localization review
- analytics decision
- release scope decision

## Do Not Skip

- Do not start production code before platform feasibility is understood.
- Do not choose stack from UI libraries alone.
- Do not merge PoC code into production without deliberate review.
