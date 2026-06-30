# LifeOS UI Reference Research v0.1

Status: Review draft

Task: `LIFEOS-CODEX-004`

Source context:

- `MASTER_CONTEXT.md`
- `data/codex_tasks.csv`
- `data/conversations.csv`
- `data/research_database.csv`
- `data/competitors.csv`
- Prior review draft: `LIFEOS-CODEX-003`

This document summarizes practical UI reference and design system options for a modern 2026 cross-platform LifeOS mobile app. It does not choose a final stack.

Research checked date: 2026-06-30

## Product UI Direction To Preserve

LifeOS should feel like an attention, time, and life-quality protection app. It should not feel like a generic blocker app, generic habit tracker, rigid productivity dashboard, or old utility app.

The app experience should feel:

- Soft
- Modern
- Rounded
- Airy
- Beautiful
- Calm
- Trend-aware
- Emotionally warm
- Not shame-based

Core screens that need strong UI support:

- Onboarding
- Target app selection
- Permission guide
- Intervention screen or fallback pause prompt
- Home
- 15:00 check-in
- 22:00 achievement log
- Records
- Settings
- Optional weekly/monthly plans

## Important Constraint

UI libraries do not solve app intervention permissions.

The iOS/Android permission and app-open intervention risks remain separate native/platform questions. Any UI prototype should include fallback states such as permission denied, permission unavailable, reminder-only mode, and manual protected-time logging.

## Evaluation Criteria

| Criterion | Why It Matters For LifeOS |
| --- | --- |
| Soft custom visual language | LifeOS needs a warm, ownable feeling rather than default utility UI. |
| Rounded components | Core direction calls for modern rounded, airy mobile surfaces. |
| Cross-platform fit | Candidate stacks include React Native + Expo and Flutter. |
| Speed to prototype | The team needs to move quickly from PRD/wireframes to clickable screens. |
| Copy-paste friendliness | Helpful for early Codex implementation and iteration. |
| Theming/tokens | Needed for consistent color, radius, spacing, typography, and motion. |
| Native feel where useful | Permission/settings flows may need platform familiarity. |
| Korean text support | Korean 존댓말 copy must remain readable and not cramped. |
| Avoid default look | LifeOS should not look like a stock Material or admin app. |

## React Native / Expo Options

### 1. React Native Paper

Official/reference link: https://callstack.github.io/react-native-paper/

React Native Paper is a mature Material Design component library for React Native.

Good for:

- Fast baseline components.
- Forms, buttons, text inputs, dialogs, surfaces, and lists.
- Teams that want stable, documented primitives.
- Permission/settings screens that can tolerate a Material-ish structure.

Pros:

- Mature and widely used.
- Good accessibility and component coverage.
- Theming support.
- Practical for quick production-like screens.

Cons:

- Can look too default Material if not heavily customized.
- May feel a little rigid for LifeOS's soft, premium, emotional direction.
- Less copy-paste visual ownership than custom component approaches.

LifeOS fit:

- Good as a conservative baseline.
- Not ideal as the primary visual identity unless heavily themed.
- Useful for utility screens, but intervention/home/check-in screens need more custom design.

### 2. Tamagui

Official/reference link: https://tamagui.dev/

Tamagui is a cross-platform UI system for React Native and web with styled components, tokens, themes, and performance-oriented compilation.

Good for:

- A design-token-driven app.
- Shared mobile/web design language.
- Highly custom rounded, soft surfaces.
- Future expansion into web marketing/app surfaces.

Pros:

- Strong token and theme architecture.
- Good fit for custom, ownable visual systems.
- Cross-platform ambition beyond mobile.
- Can support a polished, non-default UI.

Cons:

- Higher learning curve.
- More architecture decisions upfront.
- May be heavier than needed for a first mobile-only prototype.

LifeOS fit:

- Strong candidate if the team wants a serious long-term design system.
- Good for soft cards, themed tokens, motion-friendly layouts, and custom surfaces.
- Prototype should test whether setup complexity slows iteration.

### 3. NativeWind

Official/reference link: https://www.nativewind.dev/

NativeWind brings Tailwind-style utility classes to React Native.

Note: NativeWind currently shows a prerelease v5 path in its official docs. For an MVP prototype, confirm whether to use the stable docs/version or explicitly test the prerelease before implementation.

Good for:

- Fast styling iteration.
- Tailwind-minded development.
- Lightweight custom UI without committing to a full component library.
- Pairing with copy-paste component libraries.

Pros:

- Fast to express spacing, color, radius, and layout.
- Familiar if the team likes Tailwind.
- Flexible and not visually prescriptive.
- Works well with custom LifeOS components.

Cons:

- Not a full design system by itself.
- Needs discipline around tokens and component composition.
- Can become inconsistent if utility classes are used ad hoc.

LifeOS fit:

- Strong for first visual prototypes.
- Best when paired with a small custom LifeOS component kit or React Native Reusables / NativeWindUI / gluestack.

### 4. React Native Reusables

Official/reference link: https://rnr-docs.vercel.app/

React Native Reusables provides shadcn/ui-inspired, copy-paste-friendly React Native components, commonly used with NativeWind.

Good for:

- Copy-paste iteration.
- Owning component code inside the repo.
- Building a custom visual system without adopting a closed black-box kit.
- Fast Codex-assisted screen scaffolding.

Pros:

- Copy-paste model gives ownership and editability.
- Familiar shadcn-style component philosophy.
- Good fit for modern rounded cards, buttons, inputs, sheets, and tabs.
- Flexible enough for LifeOS branding.

Cons:

- Requires the team to maintain copied components.
- Component coverage may be narrower than larger libraries.
- Needs design discipline to avoid inconsistent variants.

LifeOS fit:

- Very strong for a first React Native prototype.
- Especially useful for intervention, home, check-in, records, and settings screens where custom warmth matters.

### 5. NativeWindUI

Official/reference link: https://nativewindui.com/

NativeWindUI is a NativeWind-oriented UI component direction for React Native.

Good for:

- Tailwind-style mobile UI.
- Fast prototypes with a modern component look.
- Teams that want prebuilt UI patterns while staying close to NativeWind.

Pros:

- Modern React Native + NativeWind direction.
- Likely faster than fully custom component writing.
- Good conceptual fit for rounded mobile components.

Cons:

- Needs review for maturity, licensing, and component coverage before production use.
- May need customization to avoid looking like a generic template.

LifeOS fit:

- Good candidate to inspect during prototype setup.
- Best treated as a reference or acceleration layer, not a final visual decision.

### 6. gluestack-ui

Official/reference link: https://gluestack.io/ui/docs/

gluestack-ui provides accessible, customizable components for React and React Native, with newer directions around NativeWind-style styling.

Good for:

- More complete component coverage.
- Cross-platform React/React Native component consistency.
- Teams that want a packaged component system with customization.

Pros:

- Broad component set.
- Accessibility-oriented.
- Cross-platform ambition.
- Can support production-like apps.

Cons:

- Requires evaluation of current version fit with Expo and the team's styling preferences.
- May feel more framework-heavy than copy-paste options.
- Visual output still needs strong LifeOS-specific styling.

LifeOS fit:

- Worth shortlisting for a production-minded React Native prototype.
- Compare against React Native Reusables if the team prefers owned copy-paste components.

## Flutter Options

### 1. Flutter Material 3

Official/reference link: https://docs.flutter.dev/ui/design/material

Flutter has strong built-in Material Design support, including Material 3 theming.

Good for:

- Fast Flutter-native UI.
- Reliable component coverage.
- Themed buttons, cards, navigation, sheets, dialogs, and inputs.
- Strong Android familiarity while still working cross-platform.

Pros:

- Official, stable, and deeply integrated.
- Excellent documentation.
- Strong theming and component breadth.
- Fastest Flutter baseline.

Cons:

- Default Material can look generic if not customized.
- LifeOS should not look like a standard Android settings/productivity app.
- Needs careful visual direction to become soft, ownable, and premium.

LifeOS fit:

- Good Flutter baseline.
- Should be customized heavily: softer color scheme, larger radii, warm cards, custom illustrations/progress artifacts, and non-default typography hierarchy.

### 2. Flutter Cupertino Widgets

Official/reference link: https://docs.flutter.dev/ui/widgets/cupertino

Flutter includes Cupertino widgets that follow iOS-style interaction and visual conventions.

Good for:

- iOS-native-feeling controls where appropriate.
- Settings, pickers, switches, and platform-adaptive surfaces.
- Avoiding overly Android-looking UI on iOS.

Pros:

- Official Flutter support.
- Helpful for platform familiarity.
- Useful for permission and settings-adjacent UI.

Cons:

- Pure Cupertino can feel too iOS-specific for a cross-platform brand.
- Does not provide the full LifeOS emotional visual language alone.
- Android parity needs careful handling.

LifeOS fit:

- Useful as a platform-native ingredient.
- Best combined with custom LifeOS components rather than used as the entire UI identity.

### 3. Flutter Adaptive Design

Official/reference link: https://docs.flutter.dev/ui/adaptive-responsive

Flutter's adaptive guidance helps build interfaces that respond to platform and screen differences.

Good for:

- Handling iOS and Android conventions thoughtfully.
- Future tablet or web expansion.
- Permission and settings flows that may differ by platform.

Pros:

- Official direction.
- Helps avoid one-size-fits-all UI.
- Important for cross-platform product quality.

Cons:

- Guidance, not a component kit.
- Still requires design and implementation decisions.

LifeOS fit:

- Important if Flutter is prototyped.
- Helps design platform-specific permission/fallback states without splitting product identity.

### 4. shadcn_ui for Flutter

Reference link: https://pub.dev/packages/shadcn_ui

shadcn_ui brings a shadcn-style component approach to Flutter.

Good for:

- Modern component aesthetics.
- Teams that like shadcn-style APIs and UI composition.
- Prototyping rounded, contemporary interfaces beyond default Material.

Pros:

- Modern visual direction.
- Useful reference for component composition.
- Can help avoid plain Material defaults.

Cons:

- Community package; maturity and maintenance should be reviewed before production.
- May not map perfectly to mobile-native interaction expectations.

LifeOS fit:

- Worth exploring as a visual reference or prototype accelerator.
- Should not replace deeper Flutter theming and custom LifeOS components.

### 5. Forui

Reference link: https://pub.dev/packages/forui

Forui is a Flutter UI library inspired by modern component systems.

Good for:

- Contemporary Flutter component exploration.
- Alternate visual direction beyond default Material/Cupertino.
- Rapid UI experiments.

Pros:

- Modern component feel.
- Useful for evaluating non-Material Flutter aesthetics.
- Can inspire LifeOS cards, controls, and sheets.

Cons:

- Community package; must verify maturity, stability, licensing, and mobile polish.
- May need substantial customization.

LifeOS fit:

- Good research/prototype candidate.
- Treat as an optional visual reference until proven in a real screen spike.

### 6. flutter_animate

Reference link: https://pub.dev/packages/flutter_animate

flutter_animate is not a design system, but it is relevant for LifeOS's soft motion direction.

Good for:

- Subtle card entrances.
- Gentle check-in transitions.
- Reward moments after protected time.
- Calm breathing/pause animation.

Pros:

- Helps LifeOS feel polished and emotionally responsive.
- Supports the "soft ritual" direction.

Cons:

- Motion can be overused.
- Does not solve component styling.

LifeOS fit:

- Strong companion library if Flutter is prototyped.
- Use restraint: subtle motion, not flashy gamification.

### 7. Widgetbook

Reference link: https://docs.widgetbook.io/

Widgetbook is useful for building and reviewing Flutter component catalogs.

Good for:

- Reviewing design states.
- Documenting LifeOS UI components.
- Comparing permission, empty, loading, and error states.

Pros:

- Helpful for design system governance.
- Good for review workflows.
- Useful once components stabilize.

Cons:

- Not needed for the first throwaway prototype.
- Adds process overhead if introduced too early.

LifeOS fit:

- Consider after the first successful Flutter UI spike.
- Useful for documenting states across intervention, check-ins, records, and settings.

## Practical Shortlist

### React Native Prototype Shortlist

1. Expo + NativeWind + React Native Reusables
2. Expo + Tamagui
3. Expo + gluestack-ui
4. React Native Paper as a conservative baseline/reference

Best first React Native visual spike:

- Build 4 screens with Expo + NativeWind + React Native Reusables:
  - Onboarding
  - Intervention
  - Home
  - Records

Why:

- Fastest path to an ownable soft UI.
- Copy-paste-friendly components are easier for Codex to modify.
- NativeWind enables rapid token experimentation.
- It avoids looking too default Material.

What to test:

- Korean text readability.
- Rounded card rhythm.
- Soft CTA style.
- Permission/fallback state.
- Whether component ownership feels manageable.

### Flutter Prototype Shortlist

1. Flutter Material 3 with heavy custom theming
2. Material 3 + selected Cupertino/adaptive widgets
3. shadcn_ui or Forui as visual exploration references
4. flutter_animate for subtle emotional motion
5. Widgetbook after initial components stabilize

Best first Flutter visual spike:

- Build 4 screens with Material 3 custom theme + selected Cupertino/adaptive patterns:
  - Onboarding
  - Intervention
  - Home
  - Records

Why:

- Fastest official Flutter baseline.
- Strong rendering and theming control.
- Easy to test if Flutter can produce the soft, modern LifeOS feeling without looking like default Material.

What to test:

- How far custom theme can move away from default Material.
- iOS/Android visual adaptation.
- Animation polish.
- Korean typography and spacing.
- Component styling effort versus React Native.

## Recommended Prototype Plan

Do not choose React Native or Flutter yet.

Instead, run two small visual spikes using the same screen set and same UX copy:

| Spike | Stack | Screens | Goal |
| --- | --- | --- | --- |
| RN Spike | Expo + NativeWind + React Native Reusables | Onboarding, Intervention, Home, Records | Test copy-paste speed and soft custom UI ownership. |
| Flutter Spike | Material 3 custom theme + selected Cupertino/adaptive patterns | Onboarding, Intervention, Home, Records | Test visual polish, rendering consistency, and custom theming depth. |

Compare them on:

- Visual softness and beauty.
- Speed to implement.
- Ease of customizing components.
- Korean text quality.
- Motion polish.
- Permission/fallback UI clarity.
- Long-term maintainability.
- Native module implications for app intervention.

## LifeOS Component Seeds

Regardless of stack, prototype these components first:

- `SoftScreen`
- `LifeCard`
- `PrimaryPillButton`
- `SecondaryTextButton`
- `ProtectedAppRow`
- `PermissionStatusCard`
- `InterventionPrompt`
- `BreathingPauseIndicator`
- `CheckInScale`
- `AchievementEntryCard`
- `RecordMomentCard`
- `EmptyState`
- `SettingsRow`

## Design Token Seeds

Create tokens before building many screens:

| Token Type | Direction |
| --- | --- |
| Radius | Large, soft, friendly; avoid sharp utility feel. |
| Spacing | Airy and calm; avoid dense dashboard spacing. |
| Color | Warm neutral base, soft blue/green, light peach/coral accents. |
| Typography | Highly readable Korean; short headings; generous line-height. |
| Shadow | Subtle and soft; avoid heavy material elevation. |
| Motion | Gentle; use for pause, transition, and protected-moment feedback. |

## Options Not Recommended As Primary Identity

| Option | Reason |
| --- | --- |
| Uncustomized React Native Paper | Too likely to feel default Material/utility. |
| Uncustomized Flutter Material 3 | Strong baseline, but too generic without a custom LifeOS theme. |
| Pure Cupertino | Too platform-specific and not enough for an ownable cross-platform brand. |
| Heavy dashboard/admin templates | Conflicts with soft, emotional, attention-protection direction. |
| Strict blocker-app UI patterns | Conflicts with non-shaming LifeOS product direction. |

## Open Questions

- Should the first visual spike prioritize iOS feel, Android feel, or a brand-first cross-platform feel?
- Should the UI use a progress garden, day badge, timeline, or another emotional artifact?
- How much illustration should be used in onboarding and empty states?
- What Korean font stack should be tested for readability and warmth?
- Should the intervention screen be full-screen, sheet-like, shield-like, or notification-like in the prototype?
- How much motion is enough to feel alive without becoming distracting?
- Should the first component system live inside the app repo, or be documented separately first?

## Bottom Line

For the first UI research/prototype phase, the strongest practical paths are:

- React Native: Expo + NativeWind + React Native Reusables for fast, ownable, copy-paste-friendly soft UI.
- Flutter: Material 3 custom theme + selected Cupertino/adaptive patterns for polished rendering and official component foundations.

This is a prototype recommendation, not a final stack decision.

## References Checked

- Expo documentation: https://docs.expo.dev/
- React Native Paper: https://callstack.github.io/react-native-paper/
- Tamagui: https://tamagui.dev/
- NativeWind: https://www.nativewind.dev/
- React Native Reusables: https://rnr-docs.vercel.app/
- gluestack-ui: https://gluestack.io/ui/docs/
- Flutter Material Design: https://docs.flutter.dev/ui/design/material
- Flutter Cupertino widgets: https://docs.flutter.dev/ui/widgets/cupertino
- Flutter adaptive/responsive design: https://docs.flutter.dev/ui/adaptive-responsive
- shadcn_ui for Flutter: https://pub.dev/packages/shadcn_ui
- Forui: https://pub.dev/packages/forui
- flutter_animate: https://pub.dev/packages/flutter_animate
- Widgetbook: https://docs.widgetbook.io/
