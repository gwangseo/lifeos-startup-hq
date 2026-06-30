# LifeOS Technical Architecture v0.1

Status: architecture planning draft
Task: `LIFEOS-CODEX-008`
Implementation status: not started

## Purpose

This document defines a future architecture direction without starting implementation or choosing React Native vs Flutter.

## Architecture Principles

- Local-first by default until account/cloud decisions are made.
- Platform permission capability must be abstracted, observable, and testable.
- Product screens must work in full, limited, reminder-only, and manual modes.
- Native modules are expected for app intervention capabilities.
- UI and domain logic should not assume a specific intervention mechanism.

## Layered Shape

| Layer | Responsibility |
| --- | --- |
| Presentation | Screens, components, copy, navigation, animations |
| Product domain | Protected apps, pause events, check-ins, achievements, plans |
| Permission health | OS permission status, capability mode, troubleshooting state |
| Platform adapters | iOS Screen Time APIs, Android Usage/Accessibility/Overlay paths, notifications |
| Storage | Local persistence for settings and records |
| Analytics/logging | Future event instrumentation after privacy review |

## Native Capability Boundary

The following should be isolated behind platform interfaces:

- selected app list discovery or manual entry
- permission status checks
- app-open detection
- shield or pause UI trigger
- notification scheduling
- background/foreground reliability checks

## React Native vs Flutter Implications

Do not finalize the stack yet.

React Native implications:

- Expo Go is unlikely to support required native permission/intervention modules.
- Expo dev client, prebuild, or bare workflow may be required.
- Native Android/iOS modules will likely be needed.

Flutter implications:

- Custom plugins or `MethodChannel` integration will likely be needed.
- Native Android/iOS code remains required for OS-level intervention paths.
- UI performance is not the deciding factor; permission feasibility is.

## Future Production Shape

Only after feasibility spikes:

- choose stack
- define package/module boundaries
- define navigation structure
- define local database technology
- define telemetry/privacy posture
- define platform-specific native module contracts

## Architecture Risks

- iOS entitlement or App Review may reject the intended intervention shape.
- Android sensitive permissions may create Play Store policy risk.
- Background execution and OEM battery restrictions may reduce reliability.
- A cross-platform UI shell may hide native complexity if planned too early.
- Unsupported protected-time metrics may create misleading records.

## Current Recommendation

Keep architecture documents stack-neutral. Run platform feasibility before production app scaffolding. If a future PoC is approved, keep it throwaway and clearly separated from production code.
