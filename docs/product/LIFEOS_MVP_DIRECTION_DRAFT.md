# LifeOS MVP Direction Draft

Source files:

- `data/competitors.csv`
- `data/research_database.csv`
- `data/codex_tasks.csv`

Task: `LIFEOS-CODEX-001`

Status: Draft for ChatGPT/user review

## Draft Positioning

LifeOS should not start as only a blocker, habit tracker, productivity planner, or journal.

The synced Batch 1 research points toward a first product loop that helps users recover a meaningful day:

1. Notice an unconscious digital impulse.
2. Pause with a warm question.
3. Choose a small meaningful action.
4. Turn recovered attention into visible progress.
5. Reflect with 2-3 taps.

This direction combines the strongest synced lessons from `one sec`, `Forest`, `Daylio`, and `Finch`.

## Core MVP Hypothesis

If LifeOS helps users pause before distraction, choose one tiny meaningful action, and see that recovered time become emotionally visible, users may feel less shame about bad screen time and more agency over their day.

This hypothesis comes from the synced Notion finding that the whitespace is:

> reduce bad screen time, convert saved time into small meaningful actions, visualize progress emotionally, and close the day with low-friction reflection.

## Strategic Reference Blend

| Reference | Synced Lesson | MVP Translation |
| --- | --- | --- |
| `one sec` | Intervene at the impulse moment with friction UX. | A pause screen or prompt when the user is about to open a distraction. |
| `Forest` | Make digital restraint visible and emotionally rewarding. | A recovery garden, day badge, or visible progress artifact. |
| `Daylio` | Reflection should start with 2-3 taps. | Mood/activity check-ins instead of required long journaling. |
| `Finch` | Motivation should feel supportive and non-judgmental. | Warm language, repair-oriented feedback, and no shame after failed days. |

Secondary references:

- `Structured`: represent the day as a simple visual story.
- `Fabulous`: guide behavior change as a staged journey.
- `Jomo`: frame digital detox as getting life back, not deprivation.
- `Opal`: use rules/scores carefully, avoiding punitive feedback.
- `RISE`: account for user energy, starting with self-reported energy.
- `Habitify`: borrow routine structure without becoming a generic checklist.

## MVP Loop

### 1. Trigger

The user is about to enter a distraction loop, such as opening Instagram, YouTube Shorts, TikTok, Reddit, or another personally distracting app/site.

Open implementation question:

- The MVP may need to start with a manual or simulated trigger if platform-level app-opening intervention is too complex for v1.

### 2. Warm Pause

LifeOS asks a brief, non-judgmental question.

Example prompt style:

- "Is this what you wanted to do next?"
- "Want to get one small piece of your day back?"
- "Pause for a breath, then choose."

The exact copy should be reviewed later. The synced finding is about tone and timing, not final wording.

### 3. Tiny Meaningful Action

The user chooses a small action that fits their current energy.

Possible action categories from the research direction:

- Focus for a short block.
- Do a tiny routine step.
- Move away from the phone.
- Journal with taps.
- Start a recovery ritual.

Open implementation question:

- The first action set needs user review. Notion does not yet define final MVP actions.

### 4. Visible Recovery Artifact

Recovered attention becomes visible progress.

Synced examples and metaphors:

- `Forest`: growth artifact
- Batch findings: recovery garden, day badge, meaningful-day record
- `Structured`: day story/timeline

The artifact should make restraint feel like gain, not loss.

### 5. Low-Friction Reflection

At the end of the action or day, the user completes a 2-3 tap reflection.

The reflection should capture:

- Mood
- Energy
- Activity/action taken
- Whether the day felt more meaningful

Long-form writing should be optional.

## Candidate V1 Feature Set

This is a draft candidate set derived from synced findings, not a finalized product spec.

### Must Explore

- Distraction pause flow
- Warm intention prompt
- Tiny meaningful action selection
- Visible progress artifact
- 2-3 tap reflection
- Basic day summary

### Should Consider

- Self-reported energy level
- Simple focus timer
- Recovery streaks that allow repair
- Daily timeline or day story
- Gentle AI-generated encouragement

### Avoid In V1 Unless Reviewed

- Heavy productivity task management
- Strict punitive blocking as the primary identity
- Complex analytics dashboards
- Long required journaling
- Childish character design without adult positioning review
- Broad B2B wellness features before consumer loop validation

## User Experience Principles

### Warm Over Punitive

The product should not shame users for distraction. It should help them repair the day.

### Recovery Over Perfection

The product should handle failed days gracefully. The user can still recover one meaningful action.

### Taps Before Text

Daily interaction should work with taps first. Writing should be optional.

### Visible Meaning

Progress should be visible as an emotional artifact or day story, not only a number.

### Energy-Aware

LifeOS should not assume ideal willpower. Early versions can use self-reported energy instead of wearables.

## MVP Narrative

Working draft:

LifeOS helps you get your day back from unconscious screen time. When you reach for a distraction, it gives you a warm pause, helps you choose one tiny meaningful action, turns that recovered attention into visible progress, and ends the day with a quick reflection.

This narrative should be reviewed by ChatGPT/user before being treated as final positioning.

## Open Questions For ChatGPT/User Review

- What is the first target segment for the MVP?
- Which distraction context should be first: social media, short-form video, bedtime phone use, morning phone use, or work procrastination?
- What platform should come first: mobile app, browser extension, web app, or manual prototype?
- Is the progress metaphor a garden, badge, companion, day timeline, or something else?
- Should AI coaching appear in v1, or should the first MVP prove the behavioral loop without AI?
- What are the first 5-10 tiny meaningful actions?
- Should the product include hard blocking, soft friction, or both?
- How should LifeOS measure a "meaningful day" without creating shame?
- What should be written back into Notion as decisions after review?

## Suggested Next Codex Tasks After Review

- Create a one-page MVP spec from approved answers.
- Create a user journey map for the distraction-to-recovery loop.
- Draft UX copy options for the warm pause and reflection screens.
- Create a technical feasibility note for mobile/browser intervention options.
- Create a Notion decision entry template for MVP direction approval.
