# LifeOS Localization Draft v0.1

Status: Review draft

## Localization Principle

Plan Korean and English localization from the beginning as one app with localized in-app copy and localized store metadata, while allowing separate Korean/English marketing channels later.

This follows the synced decision:

- Proceed with the meaningful-day recovery app direction.
- Plan bilingual Korean/English localization from the beginning.
- Prefer one app with localized copy and metadata before considering separate apps.

## Naming Constraints

Do not finalize naming in this document.

- `LifeOS` is the team/company placeholder.
- `하루조각` is a Korean app-name placeholder.
- `Daymark` is an English app-name placeholder.

Final naming requires:

- Trademark checks.
- Domain checks.
- App Store and Google Play conflict checks.
- Korean/English pronunciation and meaning review.
- Localized store metadata strategy.

## Korean Tone

Korean app-facing copy must use 존댓말.

Preferred tone:

- Warm
- Natural
- Calm
- Non-shaming
- Low-burden
- Softly encouraging
- Attention/time/life-quality centered

Avoid:

- 반말
- Shame or guilt
- Harsh self-improvement commands
- Translation-like Korean
- Internal product-planning words
- Using `금지`, `통제`, or `차단` as primary emotional copy

## English Tone Draft

English copy should preserve the same emotional meaning rather than translate literally.

Preferred tone:

- Gentle
- Clear
- Human
- Non-punitive
- Agency-oriented
- Focused on protecting time and attention

Avoid:

- Overly strict blocking language
- Productivity-bro tone
- Shame around screen time
- Literal translation of Korean phrases when unnatural

## Key Concept Mapping

| Concept | Korean Direction | English Direction | Notes |
| --- | --- | --- | --- |
| Attention protection | `내 시간을 지키기`, `주의를 되찾기` | protect your time, reclaim attention | Avoid making it sound like surveillance |
| Pause before app open | `앱을 열기 전 잠깐 멈추기` | pause before opening | Core behavior |
| Protected moment | `지켜낸 시간`, `멈춘 기록` | protected moment, time reclaimed | Prefer positive recovery |
| Daily recovery | `오늘의 시간을 되찾기` | get part of your day back | Strong brand direction |
| Reflection | `가볍게 돌아보기` | quick reflection | Avoid heavy journaling |
| Check-in | `하루 흐름 체크` | daily check-in | 15:00 flow score |

## Draft String Structure

Use stable string IDs from the beginning.

Example:

```json
{
  "onboarding.title.v1": {
    "ko-KR": "당신의 하루를 조금 더 지켜드릴게요.",
    "en-US": "We’ll help you protect a little more of your day."
  },
  "intervention.primary.pause": {
    "ko-KR": "잠깐 멈출게요",
    "en-US": "I’ll pause for a moment"
  }
}
```

## Sample Localization Table

| String ID | ko-KR | en-US Draft |
| --- | --- | --- |
| `onboarding.title.v1` | `당신의 하루를 조금 더 지켜드릴게요.` | `We’ll help you protect a little more of your day.` |
| `onboarding.body.v1` | `무심코 앱을 열기 전, 잠깐 멈추고 내 시간을 선택할 수 있도록 도와드려요.` | `Before you open an app on autopilot, we help you pause and choose your time.` |
| `appSelection.title` | `잠깐 멈추고 싶은 앱을 골라주세요.` | `Choose the apps where you want a pause.` |
| `permission.title` | `앱을 열기 전 멈춤을 위해 권한이 필요해요.` | `Permission is needed to pause before opening apps.` |
| `intervention.title.v1` | `지금 이 앱을 열고 싶으신가요?` | `Do you want to open this app right now?` |
| `intervention.body.v1` | `잠깐만 멈춰도 오늘의 시간이 조금 달라질 수 있어요.` | `Even a short pause can change how your day feels.` |
| `home.empty.today` | `아직 내 시간을 지켜낸 기록이 없어요.` | `No protected-time records yet.` |
| `records.empty.intervention` | `아직 앱을 열기 전 멈춘 기록이 없어요.` | `No pauses before opening apps yet.` |
| `midday.title` | `지금 하루는 어떤 흐름인가요?` | `How is your day flowing right now?` |
| `evening.title` | `오늘 지켜낸 시간을 남겨볼까요?` | `Would you like to record the time you protected today?` |

## Localization Product Notes

- Korean may use more relational and caring phrasing.
- English should avoid becoming too sentimental or awkward.
- App store title/subtitle may differ by locale.
- The app can use one technical codebase and one product system with localized strings.
- Marketing pages can be localized separately.

## Open Questions

- Should `하루조각` remain as a Korean placeholder for testing?
- Is `Daymark` emotionally close enough to `하루조각`, or only a temporary English placeholder?
- Should English copy emphasize `attention`, `time`, `day`, or `life quality` first?
- Should Korean app store metadata use `하루조각`, `LifeOS`, or another placeholder during prototype review?
- How literal should Korean/English feature names be?
