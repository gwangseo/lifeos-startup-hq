# LifeOS Screen Spec v0.1

Status: planning handoff draft
Task: `LIFEOS-CODEX-008`
Implementation status: not started

## Global Screen Rules

- Keep all Korean app-facing copy in 존댓말.
- Use the latest polite Korean UX copy direction v0.2 as source of truth.
- Avoid shame, punishment, and harsh blocker language.
- Do not use `금지`, `통제`, or `차단` as the primary emotional framing.
- Every permission-dependent screen must include a graceful fallback.
- UI should feel modern, soft, rounded, airy, beautiful, and 2026-ready.

## Primary Navigation

Future app navigation should assume four high-level areas, without locking framework implementation:

- Home
- Records
- Plans
- Settings

Plans may remain P1 or hidden in early prototypes if scope needs to stay smaller.

## Screen Specs

### 1. Onboarding

Purpose: explain the product as a gentle way to protect attention, time, and life quality.

Primary elements:

- Placeholder app name
- Short value statement
- Soft visual motif for protected moments
- Primary CTA

Copy direction:

- "오늘의 시간을 조금 더 나답게 지켜볼까요?"
- "자주 열게 되는 앱 앞에서 잠깐 멈출 수 있도록 도와드릴게요."

States:

- First launch
- Returning incomplete onboarding

### 2. Protected App Selection

Purpose: let users choose apps where they want a pause/intervention.

Primary elements:

- App list
- Search
- Selected app count
- Save/continue CTA

States:

- No apps selected
- Apps selected
- App list unavailable
- Permission required before app list can load

Copy direction:

- "잠깐 멈추고 싶은 앱을 선택해주세요."
- "선택한 앱을 열기 전, 짧은 멈춤을 준비해드릴게요."

### 3. Permission Guide

Purpose: educate users about OS permissions without promising impossible behavior.

Primary elements:

- Permission Health card
- Step-by-step permission rows
- "Continue with reminder mode" fallback
- Troubleshooting entry

States:

- Not requested
- Granted
- Denied
- Limited
- Unknown/unverified

Copy direction:

- "기기 설정에 따라 사용할 수 있는 멈춤 방식이 달라질 수 있어요."
- "권한이 없어도 알림과 직접 기록으로 계속 사용할 수 있어요."

### 4. Pause / Intervention

Purpose: create a brief mindful interruption before opening a selected distracting app, if platform capability allows.

Primary elements:

- App name or category
- Short pause prompt
- Breathing/countdown visual
- Continue button
- Choose another action

States:

- Full intervention available
- Shield-style intervention available
- Notification-based prompt
- Manual pause fallback
- Detection failed

Copy direction:

- "지금 이 앱을 열기 전에 잠깐만 멈춰볼까요?"
- "이 시간이 정말 필요하신지 한 번만 확인해보세요."

### 5. Home

Purpose: show today's gentle status and the next useful action.

Primary elements:

- Today summary
- Permission Health
- Next check-in reminder
- Recent protected moments
- Soft progress artifact

States:

- New user
- Permission incomplete
- No records yet
- Has pause/check-in records

Empty copy examples:

- "아직 앱을 열기 전 멈춘 기록이 없어요."
- "오늘은 작은 멈춤부터 시작해보셔도 좋아요."

### 6. 15:00 Check-In

Purpose: capture a simple midpoint reflection with minimal burden.

Primary elements:

- 1-5 score selector
- Optional note
- Skip action

Copy direction:

- "지금까지의 하루는 어떠셨나요?"
- "짧게만 남겨도 괜찮아요."

### 7. 22:00 Achievement Log

Purpose: let users record 0-10 small wins or protected moments without pressure.

Primary elements:

- Add entry
- Entry list
- Skip/save

Copy direction:

- "오늘 지켜낸 순간을 가볍게 남겨볼까요?"
- "없어도 괜찮아요. 오늘을 돌아본 것만으로도 충분해요."

### 8. Records

Purpose: review pause moments, check-ins, and achievement logs.

Primary elements:

- Timeline
- Filter by record type
- Empty state
- Detail view

Empty copy examples:

- "아직 내 시간을 지켜낸 기록이 없어요."
- "기록이 쌓이면 어떤 순간에 주의가 흐트러지는지 함께 볼 수 있어요."

### 9. Plans

Purpose: optional weekly/monthly intentions. This is P1 unless explicitly pulled into prototype scope.

Primary elements:

- Weekly intention
- Monthly intention
- Gentle reminders

Guardrail:

- Do not turn this into a full planner or task manager.

### 10. Settings

Purpose: manage protected apps, permissions, fallback mode, reminders, language-readiness, and privacy.

Primary elements:

- Protected app list
- Permission Health status
- Reminder settings
- Fallback mode explanation
- Privacy/data controls

States:

- Full intervention mode
- Limited permission mode
- Reminder-only mode
- Manual logging mode

## Future Implementation Notes

- This screen spec is stack-neutral.
- It must be converted into framework-specific screens only after product review and platform spike decisions.
- App-facing Korean copy must remain polite and natural.
