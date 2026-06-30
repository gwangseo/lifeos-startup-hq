# LifeOS UI Direction v0.1

Status: Review draft

## Direction Summary

LifeOS UI should feel modern, soft, beautiful, rounded, airy, and ready for a 2026 mobile product. It should not feel old, rigid, dense, utilitarian, or like a generic productivity dashboard.

The interface should communicate:

- Calm agency
- Protected time
- Warm self-support
- Gentle recovery
- Daily life quality

## Naming And Stack Constraints

- `LifeOS` is the team/company placeholder.
- `하루조각 / Daymark` are app-name placeholders.
- Do not finalize brand naming.
- Do not finalize React Native vs Flutter.

## Visual Personality

Keywords:

- Soft
- Airy
- Rounded
- Gentle
- Calm
- Warm
- Premium but not cold
- Trend-aware but not gimmicky
- Emotional but not childish

Avoid:

- Rigid productivity grids
- Harsh blocker-app warning screens
- Old Android utility aesthetics
- Dense admin dashboards
- Shame-heavy red alerts
- Generic habit checklist UI

## Layout Principles

- One major emotional focus per screen.
- Large rounded cards with clear hierarchy.
- Comfortable whitespace.
- Bottom CTA area for mobile reachability.
- Minimal settings density.
- Records displayed as warm memory/progress cards, not audit logs.
- Check-ins should feel like small rituals, not forms.

## Shape And Components

Suggested component style:

- Large rounded cards
- Soft pill filters
- Friendly toggles
- Rounded bottom sheets
- Calm permission cards
- Large touch targets
- Gentle progress chips
- Soft dividers or no dividers
- Light motion for transitions and state changes

Corner direction:

- Cards: rounded and friendly.
- Buttons: pill or softly rounded.
- Bottom sheets: large corner radius.
- Record cards: tactile and collectible.

## Color Direction

Use a balanced palette rather than a one-note single hue.

Potential palette directions:

- Warm off-white base with soft green/blue accents.
- Morning sky blue for calm attention.
- Fresh green for recovered time.
- Soft peach or coral for warmth.
- Deep neutral text for readability.

Avoid:

- Heavy purple/blue gradient dominance.
- Beige-only wellness look.
- Harsh red blocker states.
- Dark productivity SaaS look.
- Neon gamification unless deliberately reviewed.

## Typography Direction

- Use clean, modern mobile typography.
- Korean text must remain highly readable.
- Avoid tiny dense labels.
- Use short headings and concise body copy.
- Keep buttons clear and comfortable.

Korean copy should visually support 존댓말 warmth. Do not over-compress lines.

## Motion Direction

Motion should be subtle and supportive:

- Soft screen transitions.
- Gentle card entrance.
- Small progress animation after a protected moment.
- Calm breathing cue on intervention screen.
- No frantic gamified reward burst in MVP unless reviewed.

## Screen-Level UI Direction

### Onboarding

Feel like an invitation, not a setup burden. Use full-screen soft visuals, one clear message, and a calm CTA.

### App Selection

Use friendly app rows and toggles. The screen should feel like choosing what to protect, not configuring restrictions.

### Permission Guide

Use transparent, reassuring design. Include limitation states without alarming the user.

### Intervention

This is the emotional heart of the MVP. It should feel like a soft pause layer, not a warning wall.

Preferred feel:

- Minimal
- Spacious
- Gentle
- Immediate
- Warm

### Home

The home screen should show today's protected moments as a positive state. It should not become a task dashboard.

### Check-ins

15:00 and 22:00 check-ins should feel like small daily rituals. Use tap-first controls and avoid long forms.

### Records

Records should feel like a collection of recovered moments. Avoid making the user feel audited.

### Settings

Keep settings clear and calm. Permission status should be honest but not scary.

## Technical Design Notes

React Native and Flutter can both support the intended direction, but final choice remains open.

### React Native Considerations

- Good for fast iteration with Expo if app intervention requirements allow it.
- Advanced app intervention may require native modules outside simple Expo-managed patterns.
- UI library choice should support custom rounded, soft, modern mobile design.

### Flutter Considerations

- Strong for polished custom UI and consistent rendering.
- Platform-specific app intervention still needs native permission work.
- Material 3 can be customized, but the product should not look like default Material out of the box.

## Platform Risk Impact On UI

Because app intervention permissions are uncertain, UI must handle:

- Ideal app-open pause screen.
- Permission-denied state.
- Permission-unavailable state.
- Reminder-only mode.
- Manual protected-moment recording.
- Device-specific limitations.

Risk copy should be calm and clear. It should never imply that the user failed.

## Design QA Checklist

- Does it feel like attention/time/life-quality protection?
- Does it avoid generic blocker and habit tracker patterns?
- Is the layout airy and modern?
- Are controls rounded, touch-friendly, and soft?
- Is Korean copy readable and polite?
- Are limitation states honest without feeling frightening?
- Does the UI avoid final brand and tech stack decisions?
