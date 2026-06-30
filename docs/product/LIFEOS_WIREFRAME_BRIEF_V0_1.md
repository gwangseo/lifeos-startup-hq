# LifeOS Wireframe Brief v0.1

Status: Review draft

This brief translates the latest synced planning into screen-level wireframe guidance. Names and tech stack remain placeholders.

## Required Direction

- `LifeOS` is the team/company placeholder.
- `하루조각 / Daymark` are app-name placeholders.
- The product is an attention/time/life-quality protection app.
- The product is not a generic blocker app or generic habit tracker.
- All Korean app-facing copy must use 존댓말.
- Use UX Copy v0.2 principles, not older casual/반말 copy.
- UI should be modern, soft, beautiful, rounded, airy, and 2026-ready.
- React Native vs Flutter remains open.

## Visual Wireframe Principles

- Use generous spacing and large rounded surfaces.
- Keep screens calm and low-density.
- Use one clear primary action per screen.
- Use soft cards, gentle shadows, subtle blur, and light gradients.
- Avoid rigid dashboard aesthetics.
- Avoid harsh red error/blocked states for normal behavior.
- Make protected time feel like gain, not restriction.

## Navigation Draft

Primary tabs or main destinations:

- Home
- Records
- Plans
- Settings

Interruption/permission flows may appear outside the normal tab structure.

## Screen 1: Onboarding

### Goal

Explain the product as a way to protect attention and recover pieces of the day.

### Layout

- Full-screen soft background.
- Large title area.
- Short description.
- Three benefit chips/cards.
- Primary CTA.
- Secondary skip/later action where appropriate.

### Copy Direction

Use placeholder app names only.

Example Korean copy:

- Title: `당신의 하루를 조금 더 지켜드릴게요.`
- Body: `무심코 앱을 열기 전, 잠깐 멈추고 내 시간을 선택할 수 있도록 도와드려요.`
- CTA: `시작하기`

## Screen 2: App Selection

### Goal

Let users choose apps where they want a warm pause before opening.

### Layout

- Header with gentle explanation.
- Search/input area if app list is long.
- App list with toggles.
- Bottom sticky CTA.

### States

- No apps loaded.
- Permission not granted.
- Apps selected.
- No apps selected.

### Copy Direction

- Title: `잠깐 멈추고 싶은 앱을 골라주세요.`
- Body: `자주 무심코 열게 되는 앱을 선택해두면, 열기 전에 한 번 더 확인할 수 있어요.`
- CTA: `선택 완료`

Avoid positioning this as app punishment.

## Screen 3: Permission Guide

### Goal

Explain platform permissions clearly and honestly.

### Layout

- Friendly illustration or soft system card.
- Permission checklist.
- Risk/limitation note in calm language.
- CTA to system settings.
- Secondary `나중에 할게요`.

### Copy Direction

- Title: `앱을 열기 전 멈춤을 위해 권한이 필요해요.`
- Body: `기기 설정에 따라 일부 기능은 다르게 동작할 수 있어요. 가능한 방식으로 시간을 지킬 수 있게 안내해드릴게요.`
- CTA: `권한 설정하기`
- Secondary: `나중에 할게요`

### Technical Risk Note

Wireframes must include fallback states because iOS/Android app intervention permissions may limit exact app-open interruption.

## Screen 4: Intervention Screen

### Goal

Interrupt the automatic app-opening moment with warmth, not shame.

### Layout

- Minimal full-screen or shield-like surface.
- Calm visual focus object.
- One short question.
- Primary action to protect the moment.
- Secondary action to continue.
- Optional micro-breathing prompt.

### Copy Direction

Use randomized copy variants from `LIFEOS_UX_COPY_DECK_V0_2.md`.

Example:

- Title: `지금 이 앱을 열고 싶으신가요?`
- Body: `잠깐만 멈춰도 오늘의 시간이 조금 달라질 수 있어요.`
- Primary: `잠깐 멈출게요`
- Secondary: `그래도 열게요`

## Screen 5: Home

### Goal

Show today’s protected time/moments and the next gentle action.

### Layout

- Greeting.
- Main today card.
- Protected moments summary.
- 15:00 check-in or 22:00 log prompt depending on time.
- Small record preview.

### Copy Direction

- Greeting: `오늘도 내 시간을 지켜볼까요?`
- Empty summary: `아직 내 시간을 지켜낸 기록이 없어요.`
- CTA: `오늘의 기록 남기기`

## Screen 6: 15:00 Check-in

### Goal

Low-burden midday check-in with a 1-5 score.

### Layout

- One question.
- 1-5 scale with soft labels.
- Optional note field.
- Submit and skip actions.

### Copy Direction

- Title: `지금 하루는 어떤 흐름인가요?`
- Body: `가볍게만 체크해도 괜찮아요.`
- CTA: `기록하기`
- Skip: `건너뛰기`

## Screen 7: 22:00 Achievement Log

### Goal

Let users log 0-10 protected moments or small achievements without shame.

### Layout

- Evening title.
- Add small achievement cards.
- Optional prompts.
- Empty state that accepts no-entry days.
- CTA.

### Copy Direction

- Title: `오늘 지켜낸 시간을 남겨볼까요?`
- Body: `작은 순간도 괜찮아요. 오늘의 나를 위한 기록이에요.`
- Empty state: `아직 오늘 지켜낸 시간이 기록되지 않았어요.`
- CTA: `기록 저장하기`

## Screen 8: Records

### Goal

Show moments where the user paused, resisted distraction, or took time back.

### Layout

- Filter chips: Today, Week, Month.
- Record cards.
- Gentle stats.
- Empty states with specific record type.

### Copy Direction

- Title: `내 시간을 지켜낸 기록`
- Empty state: `아직 앱을 열기 전 멈춘 기록이 없어요.`
- Secondary empty state: `잠깐 멈춘 순간이 생기면 여기에 차곡차곡 모아둘게요.`

## Screen 9: Weekly/Monthly Plans

### Goal

Optional planning that does not become a heavy planner.

### Layout

- Period selector.
- 1-3 intention cards.
- Suggested gentle goals.
- Save/skip controls.

### Copy Direction

- Title: `이번 주에 지키고 싶은 시간을 정해볼까요?`
- Body: `계획은 가볍게 시작해도 충분해요.`
- CTA: `계획 저장하기`
- Skip: `나중에 할게요`

## Screen 10: Settings

### Goal

Control apps, permissions, notifications, language, and data.

### Layout

- Profile/localization section.
- Protected apps.
- Permission status.
- Notification times.
- Language.
- Data/privacy.

### Copy Direction

- `지킬 앱 관리`
- `권한 상태`
- `알림 시간`
- `언어`
- `데이터 관리`

## Fallback Wireframes

Because app intervention permissions are uncertain, design must include fallback states:

- Permission unavailable.
- Permission denied.
- App-open detection unavailable on this device.
- Manual protected-time logging.
- Reminder-only mode.
- Notification-based pause prompt.

Example copy:

- `이 기기에서는 앱을 여는 순간을 직접 감지하기 어려울 수 있어요. 대신 알림과 수동 기록으로 시간을 지킬 수 있게 도와드릴게요.`

## Wireframe Review Checklist

- Does every Korean user-facing line use 존댓말?
- Does the screen avoid shame and punishment?
- Does the UI feel soft, modern, rounded, and airy?
- Does the flow support fallback when OS permissions are limited?
- Does the experience protect attention/time/life quality rather than simply blocking apps?
- Does the screen avoid finalizing brand or app names?
