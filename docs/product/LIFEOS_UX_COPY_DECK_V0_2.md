# LifeOS UX Copy Deck v0.2

Status: Review draft

This document turns the latest synced UX Copy v0.2 principles into a reviewable copy deck. It intentionally avoids older casual/반말 copy.

## Copy Source Rules

- All Korean app-facing copy must use 존댓말.
- Do not use older casual/반말 copy.
- Avoid `금지`, `통제`, and `차단` as primary emotional copy.
- Prefer language about protecting time, choosing attention, pausing, and recovering the day.
- Empty states must name the missing record type clearly.
- Tone: warm, natural, non-shaming, not translation-like.

## Naming Placeholders

- Company/team placeholder: `LifeOS`
- Korean app placeholder: `하루조각`
- English app placeholder: `Daymark`

Do not finalize these names.

## Global Copy Patterns

| Intent | Korean Copy | Notes |
| --- | --- | --- |
| Primary start | `시작하기` | Simple CTA |
| Save | `저장하기` | Generic save |
| Later | `나중에 할게요` | Gentle deferral |
| Skip | `건너뛰기` | Check-ins must be skippable |
| Continue anyway | `그래도 열게요` | Intervention secondary action |
| Protect moment | `잠깐 멈출게요` | Intervention primary action |
| Record | `기록하기` | For check-ins/logs |
| Manage apps | `지킬 앱 관리` | Avoid harsh control framing |

## Onboarding

### Variant A

- Title: `당신의 하루를 조금 더 지켜드릴게요.`
- Body: `무심코 앱을 열기 전, 잠깐 멈추고 내 시간을 선택할 수 있도록 도와드려요.`
- CTA: `시작하기`

### Variant B

- Title: `흘러가는 시간을 다시 알아차릴 수 있게 도와드려요.`
- Body: `하루를 바꾸는 건 거창한 계획보다, 잠깐 멈추는 작은 순간일 수 있어요.`
- CTA: `내 시간 지켜보기`

### Variant C

- Title: `앱을 덜 쓰는 것보다 중요한 건, 내 시간을 되찾는 거예요.`
- Body: `하루조각은 앱을 열기 전 한 번 더 생각하고, 지켜낸 순간을 기록할 수 있게 도와드려요.`
- CTA: `시작하기`

## App Selection

- Title: `잠깐 멈추고 싶은 앱을 골라주세요.`
- Body: `자주 무심코 열게 되는 앱을 선택해두면, 열기 전에 한 번 더 확인할 수 있어요.`
- Empty: `아직 선택한 앱이 없어요. 먼저 지키고 싶은 앱을 골라주세요.`
- CTA: `선택 완료`

## Permission Guide

- Title: `앱을 열기 전 멈춤을 위해 권한이 필요해요.`
- Body: `기기 설정에 따라 일부 기능은 다르게 동작할 수 있어요. 가능한 방식으로 시간을 지킬 수 있게 안내해드릴게요.`
- CTA: `권한 설정하기`
- Secondary: `나중에 할게요`
- Fallback note: `이 기기에서는 앱을 여는 순간을 직접 감지하기 어려울 수 있어요. 대신 알림과 수동 기록으로 시간을 지킬 수 있게 도와드릴게요.`

## Intervention Copy Variants

### Variant A

- Title: `지금 이 앱을 열고 싶으신가요?`
- Body: `잠깐만 멈춰도 오늘의 시간이 조금 달라질 수 있어요.`
- Primary: `잠깐 멈출게요`
- Secondary: `그래도 열게요`

### Variant B

- Title: `지금 필요한 건 이 앱일까요?`
- Body: `한 번 숨을 고르고, 내 시간을 어디에 쓸지 선택해보세요.`
- Primary: `숨 고르기`
- Secondary: `앱 열기`

### Variant C

- Title: `이 순간을 지켜볼까요?`
- Body: `지금 멈추면 오늘의 작은 조각 하나를 되찾을 수 있어요.`
- Primary: `시간 지키기`
- Secondary: `계속 진행하기`

### Variant D

- Title: `무심코 열고 있는 중일 수 있어요.`
- Body: `괜찮아요. 알아차린 것만으로도 이미 좋은 시작이에요.`
- Primary: `잠깐 멈추기`
- Secondary: `그래도 열게요`

## Home

- Greeting: `오늘도 내 시간을 지켜볼까요?`
- Today empty: `아직 내 시간을 지켜낸 기록이 없어요.`
- Today summary: `오늘 {count}번 잠깐 멈췄어요.`
- Protected time summary: `오늘 {minutes}분을 지켜냈어요.`
- Midday prompt: `지금 하루는 어떤 흐름인가요?`
- Evening prompt: `오늘 지켜낸 시간을 남겨볼까요?`
- CTA: `오늘의 기록 남기기`

## 15:00 Check-in

- Title: `지금 하루는 어떤 흐름인가요?`
- Body: `가볍게만 체크해도 괜찮아요.`
- Score 1: `많이 흐트러졌어요`
- Score 2: `조금 흔들렸어요`
- Score 3: `보통이에요`
- Score 4: `괜찮게 지키고 있어요`
- Score 5: `좋은 흐름이에요`
- Optional note placeholder: `지금 상태를 짧게 남겨보세요.`
- CTA: `기록하기`
- Skip: `건너뛰기`

## 22:00 Achievement Log

- Title: `오늘 지켜낸 시간을 남겨볼까요?`
- Body: `작은 순간도 괜찮아요. 오늘의 나를 위한 기록이에요.`
- Empty: `아직 오늘 지켜낸 시간이 기록되지 않았어요.`
- Add entry: `지켜낸 순간 추가하기`
- Placeholder: `예: 자기 전 10분 동안 쇼츠를 보지 않았어요.`
- CTA: `기록 저장하기`
- Skip: `오늘은 넘어갈게요`

## Records

- Title: `내 시간을 지켜낸 기록`
- Empty intervention: `아직 앱을 열기 전 멈춘 기록이 없어요.`
- Empty protected time: `아직 내 시간을 지켜낸 기록이 없어요.`
- Empty check-in: `아직 하루 흐름을 체크한 기록이 없어요.`
- Empty support: `잠깐 멈춘 순간이 생기면 여기에 차곡차곡 모아둘게요.`
- Filter today: `오늘`
- Filter week: `이번 주`
- Filter month: `이번 달`

## Weekly/Monthly Plans

- Weekly title: `이번 주에 지키고 싶은 시간을 정해볼까요?`
- Monthly title: `이번 달에 되찾고 싶은 흐름이 있나요?`
- Body: `계획은 가볍게 시작해도 충분해요.`
- Placeholder: `예: 자기 전 30분은 휴대폰을 내려놓기`
- CTA: `계획 저장하기`
- Skip: `나중에 할게요`

## Settings

- Title: `설정`
- Protected apps: `지킬 앱 관리`
- Permissions: `권한 상태`
- Notifications: `알림 시간`
- Language: `언어`
- Data: `데이터 관리`
- Privacy note: `기록은 사용자가 자신의 시간을 돌아보기 위한 용도로 다룹니다.`

## Error And Limitation Copy

- Permission denied: `권한이 꺼져 있어 앱을 열기 전 멈춤을 사용할 수 없어요.`
- Permission unavailable: `이 기기에서는 일부 기능이 제한될 수 있어요.`
- Sync unavailable: `지금은 기록을 불러오지 못했어요. 잠시 후 다시 시도해주세요.`
- Generic retry: `다시 시도하기`

## Copy QA Checklist

- No 반말.
- No shame.
- No final brand naming.
- No harsh primary language around control/blocking.
- Empty states are specific.
- Korean reads naturally and politely.
