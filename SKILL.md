---
name: higgsfield
description: >
  Use for Higgsfield prompt authoring, model and camera selection, Cinema Studio,
  Photodump, or diagnosis of a Higgsfield generation. For generic video/image
  prompt requests, use it only when Higgsfield is the selected platform. Approved
  prompt execution, job status, recovery, and downloads route to the selected
  executor without restarting prompt authoring.
user-invocable: true
metadata:
  tags: [higgsfield, video, image, prompt, cinematic, AI, filmmaking, motion, camera]
  version: 3.40.0
  updated: 2026-09-26
  author: O-Side Media
  license: MIT
---

# Higgsfield AI Prompt Skill

**Local language rule:** Default to Simplified Chinese for newly written prompts (including copyable prompt blocks), headings, reference-role descriptions, diagnoses, and QC notes unless the user explicitly requests another language. Preserve the approved language of dialogue and on-screen copy. Keep user-provided text, reference handles, asset IDs, paths, API fields, enum values, and other machine syntax exact. Never silently translate or revise an approved execution prompt. If the selected executor has a verified language requirement, explain it and keep the Chinese review text separate from a faithful execution translation; do not assume English performs better without evidence for that model and mode.

**Scope of the checks below:** Apply Higgsfield authoring checks when creating or substantively revising a Higgsfield prompt. A ready, approved prompt goes directly to its selected execution skill unchanged; a status, recovery, or download request does not restart prompt authoring. User-approved copy, assets, model, duration, and technique take precedence over optional craft heuristics. Use a risk-specific negative constraint only when the failure it addresses is relevant. Do not add emotion, cuts, retries, or batches to satisfy a generic recipe. Treat local iteration counts and batch advice as options tied to diagnosed evidence and the user's authorized scope, not mandatory steps.

---

## HARD RULES — pre-delivery checklist

These rules apply to new Higgsfield prompt authoring within the scope above. They are written as a pre-delivery checklist. The failure mode they prevent is **plausibility-over-verification** — producing a response that looks correct because the agent's training data knows the rough shape of Higgsfield work, rather than because the agent actually read the skill files and verified the platform's ground truth.

**Before delivering any Higgsfield response, confirm in this order:**

1. **Useful routing line.** When routing to a sub-skill for new authoring, name the sub-skills used in one line. Do not repeat the badge on every status/result reply or reopen creative skills for execution of an approved prompt.

2. **Routed sub-skills opened and read in this conversation.** For new Higgsfield prompt authoring, match the user's ask to the routing table below, open `skills/higgsfield-prompt/SKILL.md` and the matching specialist files with the read tool, and READ them. Grepped snippets do not satisfy this rule. Platform vocabulary, preset names, and model parameters must come from the selected platform's files or verified schema because its lineup changes between releases. An external provider's approved prompt uses that provider's writer and executor without an extra Higgsfield rewrite.

3. **Named vocabulary verified, not invented.** Camera preset names, motion preset names, model names, and MCP tool parameter names all come from the skill files or from verification. For Higgsfield model parameters, enums, and durations, consult `specs/model-specs.yaml` first — it records a dated snapshot (see `snapshot_date`); if stale (>30 days), verify through the selected Higgsfield executor's current schema. For another platform, that platform's executor owns verification. If you found yourself thinking "this preset is probably called Y" — stop. Read the file or verify it. Plausibility is not validity. Do not substitute generic video-prompt vocabulary for named Higgsfield presets; do not invent model versions, camera presets, or motion-preset names. If the user names one you don't see in the skill files, say so and ask for clarification.

4. **MCSLA structure on new short-form Higgsfield video prompts.** Model · Camera · Subject · Look · Action. Keep a selected model-specific dialect or approved prompt in its own structure; do not add these headings solely for conformity.

5. **Relevant negative constraints.** When a newly drafted prompt has a concrete artifact risk, consult `skills/shared/negative-constraints.md` and use the applicable phrase, respecting the selected model's wording. Do not append boilerplate to an approved execution prompt.

6. **Aspect ratio is an enum, not a free-form value.** For Higgsfield execution, check the model's allowed ratios against `specs/model-specs.yaml`; when the needed field is missing or disputed, verify it against the current Higgsfield schema. For another platform, its executor owns the current schema. Seedance 2.0 supports native 21:9, Kling 3.0 does not. Anamorphic / 2.35:1 / 2.39:1 are *style register* vocabulary for the Look line, not output ratios. See `vocab.md` § Aspect Ratio: output spec vs. style register. In a multi-shot Seedance sequence whose location plates carry a baked lens, whether the optics words still belong in the video prompt (Style Prefix included) is OPEN — one studio drops them, Hell Grind keeps the look in both (`skills/higgsfield-seedance/SKILL.md` § Bake it into the asset; `skills/shared/house-rulings.md` P2-6).

7. **Review length in the chosen regime.** The 200-word MCSLA guideline is a soft editing cue for new single-shot prompts, not a provider limit or a reason to truncate approved content. Block-scaffold production prompts (`skills/higgsfield-seedance/SKILL.md` § Official Prompt Architecture) use structural review instead — harvested production Seedance briefs run 218–2,059-word medians depending on register `[FIELD — 13-project community harvest, 2026-07-18]`. Enforce only the current executor's verified input limits.

**If any of items 1–7 are missing or unverified, the response is incomplete. Complete them before sending, not after.**

---

## What Is Higgsfield?

Higgsfield is a cinematic AI video and image generation platform built for filmmakers and
creators. Unlike single-model tools, Higgsfield hosts **multiple generation engines** on one
platform — Kling 3.0/3.0 Omni/3.0 Motion Control, Google Veo 3.1/3.1 Lite, Wan 2.7/2.6/2.5,
Seedance 2.5/2.0/Pro, FLUX 3 Video, Minimax Hailuo 2.3/02, Higgsfield DoP (Lite/Standard/Turbo) for video; Soul 2.0, Soul Cinema Preview,
Soul Cast, Nano Banana Pro/2, Kling Image 3.0/Omni, Seedream 5.0 Pro/Lite/Flash + 4.5, GPT Image 2.0 / 2.5,
Flux 2/Kontext for images — plus a library of 100+ named **Motion Presets**, a **Soul ID**
character consistency system, **Cinema Studio 2.5**, **Cinema Studio 3.0** (Business/Team plan), and **Cinema Studio 3.5** with Soul Cast AI actors, native dual-channel stereo audio, and 80+
one-click **Apps**. **Sora 2 is retired from this skill's recommendations:** OpenAI shut the Sora 2 API down on 2026-09-24; Higgsfield only ever offered it in its web UI, and whether the UI still does is unconfirmed. For scale / physics shots use Seedance 2.0 or Minimax Hailuo 2.3 (`model-guide.md`). **Catalog check (2026-09-26):** Kling 3.0 Omni, Wan 2.5, Seedance Pro, Higgsfield DoP, Soul Cinema Preview and Kling Image 3.0 / Omni are not in the API catalog . They may be UI-only — verify in the live UI before recommending them, and prefer a catalog pick where `model-guide.md` names one. No catalog variant of Minimax Hailuo is named 02.

---

## Working Folders — file handling

The project has a `workspace/` folder with three subfolders. Use them for every
task that involves a user-provided document or a file you produce. This keeps
uploads and deliverables out of the project root.

| Folder | Role | Your behavior |
|--------|------|---------------|
| `workspace/input/` | Documents the user wants you to read (scripts, story bibles, briefs, character sheets, references). | Read from here first. If the user uploaded a file that landed elsewhere in the project root, **move it into `workspace/input/` before working with it**. When you need a document from the user, ask them to drop it in `workspace/input/`. |
| `workspace/output/` | Files you generate for the user (prompt packs, shot breakdowns, batch CSVs, reports, exported docs). | **Write every file deliverable here**, not to the project root. Tell the user the path when you finish. |
| `workspace/processed/` | Inputs you have finished consuming. | When a task is complete, **move the source from `input/` to `processed/`** so `input/` stays clean. Never delete the user's files — relocate them. |

Rules:
- Never scatter user uploads or generated files across the project root or skill folders — route them through `workspace/`.
- Treat `workspace/input/` as the canonical place to look when the user says "the script / bible / reference I gave you."
- These three folders' contents are local-only (git-ignored); do not assume anything in them is committed.

### Fast Path — Simple Creative Requests

If the user has selected Higgsfield and provides a clear creative intent
("write me a prompt for a car chase at night") with no specific constraints,
use these adjustable examples only where the brief leaves a choice open:

> **Fast Path still requires reading `skills/higgsfield-prompt/SKILL.md` first.** Ask only when a missing choice materially affects the result or cost.

| Parameter | Adjustable example |
|-----------|---------|
| Aspect ratio | 16:9 |
| Duration | 8s (Kling lanes — see Seedance exception below) |
| Style | Cinematic |
| Video model | Kling 3.0 (character-focused) or Seedance 2.0 (action/scale/references) |
| Image model | Soul 2.0 (portrait) or Nano Banana 2 (everything else) |

Ask only when a missing choice would materially change the result or cost.
Mention any assumptions used so the user can adjust them.

> **Seedance exception:** Seedance 2.0 never gets a silently defaulted runtime
> (`skills/higgsfield-seedance/SKILL.md` — always ask, never default). On Fast
> Path that means: if the user named no duration, route video to Kling 3.0;
> pick Seedance 2.0 only when the request names a duration — or when the user
> asked for Seedance by name, in which case ask for the runtime if it is
> required by the selected mode and absent from the brief.

> If you did not read `skills/higgsfield-prompt/SKILL.md` earlier in this conversation, read it now before writing the prompt.

### Full Path — Production Requests

For production work (Cinema Studio, multi-shot, specific model, budget constraints,
client work), read these fields from the request or approved project settings. Ask only
when a missing choice materially changes the output or cost:

**Required:**
- **Generation type**: Image / Video / App (one-click)
- **Video duration**: model-dependent enum — check the model's `duration` values in `specs/model-specs.yaml` before offering choices (e.g. Seedance 2.0 4–15s, Veo 3.1 4/6/8s; image-to-video clips trend short)
- **Aspect ratio**: 16:9 / 9:16 / 1:1 / 4:5 / 4:3 / 21:9-where-supported (default: 16:9) — enums per model in `specs/model-specs.yaml` (HARD RULE 7); anamorphic / 2.35:1 / 2.39:1 are **Look-line style register**, never output ratios
- **Model preference** (or ask Claude to recommend — see `skills/higgsfield-models/SKILL.md`)

**Optional (skip if user already provided):**
- Visual style: Cinematic / VHS / Super 8MM / Anamorphic / Abstract
- Reference image for image-to-video
- Motion preset preference

> Ask everything in one message — do not split across multiple rounds.

---

### Route to the Right Skill

For local generation, keep prompt craft and execution separate. A user-named provider, app, model, or existing project selection takes priority. The selected execution skill owns current syntax, media bindings, parameters, authorization, cost, submission, recovery, and delivery. Do not substitute Higgsfield catalog IDs, CLI commands, credit prices, or schemas for another platform's contract. Reuse a confirmed schema and job receipt; do not resubmit a job merely because status is uncertain. This library's model and production references remain available for creative planning when relevant.

| Selected task or platform | Route to |
|---------------------------|----------|
| RunningHub model or saved AI App | Installed `runninghub` skill; keep its region and saved app schema, and let it submit and recover the job. |
| Generation Service configured provider/model | Installed `generation-service:generation-service` skill; it selects its current vendor/model route and owns job tracking. RunningHub remains its own route. |
| 小云雀 / Pippit generation, processing, or Canvas | Installed `xyq-skill`; its CLI and current command docs own the operation. |
| LibTV canvas generation/editing | Current LibTV MCP connection and capabilities; use `libtv-to-treatment` only for a director treatment, `libtv-blender-live-action` for that named Blender workflow, or `music-driven-product-ad` for that named ad workflow. |
| Explicit Seed Audio / `seedaudio` standalone audio generation — SFX, ambience, music cues, speech, or mixed scenes | Installed `seedaudio` skill; its CLI and current Seed Audio/Qwen/StepAudio routes own the syntax, media handling, cost, recovery, and delivery. |
| New commercial AI project setup or explicit project-kit refresh | Installed `commercial-ai-project-kit`; it initializes/updates project material and does not choose a generation provider or run generation. |
| Cross-model identity, keyframe, face, surface-realism, or action-obedience failure | Installed `ai-video-realism` for diagnosis and repair, then the selected model writer for supported controls. |

If a local skill is unavailable, say so and resolve the intended platform before execution; do not silently change providers. For selected providers, go straight to their executor with the user's approved prompt and references. Prompt design may borrow relevant guidance here, but never force an emotion beat, edit cut, paid retry, or batch without a brief-specific reason and authorization.

**已有项目的连续性提炼：** 多镜头接续、空间轴线、双面道具、草稿／正片交接或局部重拍
需要补充制作方法时，按需读 `skills/shared/production-continuity.md`。LibTV 的占位符与素材
顺序由其当前执行器管理，保留已批准文本；不套用 Higgsfield 的标签改写约定。

| User wants | Route to |
|------------|----------|
| Write or improve a prompt for selected Higgsfield execution | `higgsfield-prompt` + relevant sub-skills |
| Develop a character / world / story / premise before prompting, build a character sheet / story bible, lock a visual style ("visual DNA"), keep a character consistent across many shots, or "I keep getting generic AI characters" | `higgsfield-character-design` |
| Audit or strengthen a scene / sequence / beat outline before generating it, or "is this scene working", "what's weak here", "why doesn't this land" | `higgsfield-scene-engine` |
| Cinematic still image prompt (shot framing, angles) | `higgsfield-image-shots` |
| GPT Image 2.0 / 2.5 / gpt-image-2 / gpt_image_2_5 prompt, Flare / Sunburst, transparent-background image, UI mockup, infographic, character/reference sheet, layout-dense image, or static-ad recreation | `higgsfield-gpt-image-2` |
| Choose the right model — incl. which lane edits existing footage, which model makes one clip longer than 15s, or motion transfer (Genjutsu vs Kling Motion Control) | `higgsfield-models` + `model-guide.md` (§ Edit-Lane Chooser, § Long-Take Chooser) |
| Camera movement guidance (video) | `higgsfield-camera` |
| Named motion preset (Explosion, Werewolf, etc.) | `higgsfield-motion` |
| Visual style selection | `higgsfield-style` |
| VFX presets (Air Bending, Plasma, etc.) | `higgsfield-motion` |
| Genre recipe (action, horror, ad, etc.) | `higgsfield-recipes` |
| Fix a failing generation | `higgsfield-troubleshoot` |
| A Seedance take came back wrong (not flagged) — reversal, babble, a third hand, gliding walk, choppy fight | `higgsfield-seedance` (`skills/higgsfield-seedance/FAILURE-MODES.md`) + `higgsfield-troubleshoot` (§ Stop-Rule Ladder) |
| Mixed Media presets (Noir, Sketch, Particles, etc.) | `higgsfield-mixed-media` |
| Photodump style preset / social-feed photo-dump aesthetic | `photodump-presets.md` (root reference) |
| Artistic style transformation, preset stacking | `higgsfield-mixed-media` |
| Cinema Studio 2.5 / Cinema Studio 3.0 / Cinema Studio 3.5 / Cinema Studio 4.0 / multi-shot sequence workflow / Soul Cast | `higgsfield-cinema` |
| Cinema Studio 4.0 — `cinematic_studio_video_4_0`, its four modes (t2v / omni_reference / video_edit / video_extension), camera / lens / aperture / era / genre / pacing ids, light and palette controls | `higgsfield-cinema` |
| Optical physics, camera bodies, lenses, Hero Frame | `higgsfield-cinema` |
| Elements system (@Characters/@Locations/@Props) | `higgsfield-cinema` |
| Director Panel, Speed Ramp, shot modes, Popcorn | `higgsfield-cinema` |
| Cinema Studio 3.0 Smart mode, @ references, native audio | `higgsfield-cinema` |
| Cinema Studio 3.5 — three-pill UI, Style Settings, Camera Settings, Manual Style, AI director toggle | `higgsfield-cinema` |
| Multi-shot workflow, chaining tools, full production pipeline | `higgsfield-pipeline` |
| Short film, branded content, Popcorn → video → assembly on Higgsfield | `higgsfield-pipeline` |
| Animated AD / brand promo on selected Higgsfield execution, built brief → storyboard sheet → video ("make a motion", "motion design ad", "animate my logo into a video", "promo/ad video", classicMD/highMD) | `higgsfield-motion-design` |
| Pre-generation memory check, apply past failure fixes | `higgsfield-recall` |
| User reports a generation result (kept/rejected/flagged) and this project uses the Higgsfield ledger | `higgsfield-recall` |
| Audio design, dialogue cues, SFX, ambient sound | `higgsfield-audio` |
| **Standalone audio generation** — soundtrack, ambience bed, multi-speaker scene audio, Seed Audio 1.0 (`seed_audio`), TTS voiceover / narration as its own deliverable | `higgsfield-audio` |
| Swap or revoice the speaker in a finished video (`voice_change`), or clone / create a reusable voice (`create_voice` → `voice_type: element`) | `higgsfield-audio` |
| **3D** — image→3D / multi-view→3D / text→3D mesh (GLB), rigging or animating a mesh, remesh / retexture, 3D Body, 3D Jutsu / Scene Builder 3D projects, a 3D turnaround as a multi-angle reference, a 3D blockout as a staging reference (`generate_3d`, `scene_builder_3d_*`) | `higgsfield-3d` |
| **Extend / continue an existing clip** — "make it longer", "what happens next / before", prequel, last-frame handoff, extension chains | a native forward/backward extension on 2.5 → `higgsfield-seedance-2-5` (`video_extension`); a 2.0 clip continued as a video reference → `higgsfield-seedance` (§ Extension Prompting); chaining across generations → `higgsfield-pipeline` (§ Continuation & Extension Handoff) |
| **Prep assets / reference sheets before video** — character sheet, prop three-view, location plate, "build my elements", variety sheet for crowds | `templates/ad-asset-prep.md` + `higgsfield-gpt-image-2` |
| Audition / screen-test a designed character (how they move, speak, react) before scene generation | `higgsfield-character-design` (§ Screen Test / Audition) |
| Seedance 2.0 / Pro prompt, flagged prompt, credit waste on Seedance | `higgsfield-seedance` |
| **Seedance 2.5** — user names 2.5 / Dreamina / Jimeng, wants a single clip longer than 15s, wants to **edit** or **extend** a video that already exists, or supplies many image/video/audio references (up to 30/10/10) | `higgsfield-seedance-2-5` |
| **2.0 vs 2.5** (both say "Seedance"): needs 4K, `mode=fast`, or a `genre` hint → `higgsfield-seedance`; needs >15s in one generation, video editing, forward/backward extension, or heavy multi-reference → `higgsfield-seedance-2-5`. Both do 1080p and platform start/end frames (2.5 only in `omni_reference`); 2.5 caps at 1080p | — |
| **Character performance** — acting, behavior, mannerisms, tics, a gait, subtext, "my characters look wooden / dead-eyed / AI", keeping a character themselves across many shots, an acting master profile | `higgsfield-acting` |
| **Feature-film production pipeline on Seedance** — headless character sheets, location sheets, a scene geography block reused across shots, dialogue construction, iteration discipline, giants / crowds / threshold transitions | `higgsfield-seedance` (`HELL-GRIND.md`) |
| **Transform footage the user already has** (video-to-video): "make a Seedance prompt for this video/clip", add a VFX element (set my head/hair on fire, transform my hand, make a limb invisible), swap the world/background around a preserved subject (desert, clouds, lava, neon city), put a giant creature behind me or on a landmark, relight/regrade to match, sync a crash-zoom/push-in to a line — a **real source clip** is the starting point | `higgsfield-seedance-vfx` |
| **Replace a VFX/3D pipeline with generation** — "can AI do this instead of VFX", put myself in this plate, put a creature in my footage, a dragon/monster shot without buying or rigging a 3D model, "how do I build a whole VFX shot", asset sheets → size-ref → locations → shots as one pipeline; also "my v2v keeps failing / turns to slop", scale drift between two subjects, which image model for faces vs creatures vs clothing vs locations | `higgsfield-seedance-2-5` (`VFX-PIPELINE.md`) |
| Precise facial expression / FACS / Action Unit codes (AU12, AU6…), forced or uncanny or mixed expression, close-up micro-performance, monologue/dialogue facial acting, "which AU code for anger/fear", FACS reference sheet | `higgsfield-facs` |
| "Make a shotlist", break a script/brief/treatment into many connected Seedance prompts, director's shotlist, global style prefix + `@`-glossary + named per-scene prompts as one editable HTML | `higgsfield-shotlist-director` |

---

### Load Map — how much to read

The routing table says *where*; this says *how much*. Loads are cumulative — every path starts from HARD RULE 2's mandatory reads.

| Situation | Load |
|-----------|------|
| Simple creative prompt (Fast Path) | root `SKILL.md` + `skills/higgsfield-prompt/SKILL.md` — nothing else |
| Any Seedance prompt | + `skills/higgsfield-seedance/SKILL.md` (+ the matching `templates/seedance/` file when the request is technique-shaped) |
| Multi-scene / sequence / script breakdown | + `higgsfield-shotlist-director` + `higgsfield-pipeline` |
| Model choice unclear or contested | + `higgsfield-models` + `specs/` (the generated spec for the output type) |
| User reports a generation result for a project using the Higgsfield ledger | + `higgsfield-recall` (ledger write) |
| A Seedance render failed (not filtered) | + `skills/higgsfield-seedance/FAILURE-MODES.md` + `skills/higgsfield-troubleshoot/SKILL.md` |
| Anything else | one routing-table row → that sub-skill; resist loading more than the row names |

### Check Templates for Genre Match

Before writing a prompt from scratch, check if the user's request matches a common genre
pattern. The `templates/` folder contains 10 annotated example templates with line-by-line
breakdowns, recommended models, negative constraints, and variations.

| User request matches | Check template |
|---------------------|----------------|
| Chase, pursuit, action, parkour | `templates/01-cinematic-action-chase.md` |
| Product, commercial, ad, UGC | `templates/02-product-ugc-showcase.md` |
| Horror, scary, creepy, dread | `templates/03-horror-atmosphere.md` |
| Fashion, editorial, lookbook | `templates/04-fashion-editorial.md` |
| Sci-fi, cyberpunk, VFX, space | `templates/05-sci-fi-vfx.md` |
| Portrait, character intro, close-up | `templates/06-portrait-character-intro.md` |
| Landscape, nature, establishing shot | `templates/07-landscape-establishing-shot.md` |
| Comedy, social media, TikTok, skit | `templates/08-comedy-social-media.md` |
| Romance, intimate, couple, wedding | `templates/09-romantic-intimate.md` |
| Dance, music, performance, concert | `templates/10-dance-music-performance.md` |

Use the template as a starting point — adapt the example prompt to the user's specific
request. The annotations explain WHY each element works, helping you make informed
substitutions.

**Technique templates** (`templates/seedance/`) — structure templates for Seedance
prompts where the user request is technique-shaped rather than genre-shaped:

| Technique need | Template |
|---|---|
| Pre-visualize multi-character spatial geometry before prompting | `templates/seedance/top-down-map.md` |
| Multi-character shot with cross-character relationships | `templates/seedance/multi-character-anchor.md` |
| Single-character shot with position + pose + contact-point locks | `templates/seedance/single-character-position.md` |
| Worked example: two-character anchoring end-to-end | `templates/seedance/worked-example-two-character.md` |
| Anime / stylized-2D animation — layered formula + style block + character turnaround | `templates/seedance/anime-animation.md` |
| Close-up facial acting via FACS Action Unit codes — beat-synced expression schedule | `templates/seedance/facs-expression-beats.md` |
| Seedance **2.5** multi-reference brief — role map + staged beats with end states | `templates/seedance/omni-reference-2-5.md` |
| Show the model WHERE figures stand — a front-on outline position reference attached LAST (one incomplete-record run: no bleed, NOT reliable at moving blocking) | `templates/seedance/staging-reference.md` |

**Text-overlay templates** (`templates/text-overlays/`) — paste-ready text-rendering
prompts for slogan / subtitle / speech-bubble overlays:

| Text overlay type | Template |
|---|---|
| Slogan / brand callout / opening title | `templates/text-overlays/slogan.md` |
| Subtitle (dialogue-synchronized) | `templates/text-overlays/subtitle.md` |
| Speech bubble (character-attributed) | `templates/text-overlays/speech-bubble.md` |

---

### Build the Prompt Using the MCSLA Formula

Full MCSLA definition and prompt structure → `skills/higgsfield-prompt/SKILL.md`

Quick summary — five layers, every prompt:

| M | C | S | L | A |
|---|---|---|---|---|
| Model | Camera | Subject | Look | Action |

**Core rules:**
- Be specific — name camera presets, describe VFX concretely
- Use 200 words as an optional editing cue for new short-form prompts; preserve approved text and apply only verified executor limits (HARD RULE 7).
- Subject → Action → Camera → Style is the most reliable order

---

### Output Format

**Single prompt:**
```
**Model**: [model name]
**Aspect ratio**: [ratio]  **Duration**: [Xs]  **Style**: [style]

[Prompt]

**Camera**: [camera control name]
**Motion preset** (if used): [preset name]
```

**Two versions (when style varies):**
```
### Version 1 — [Style Name]
[Prompt]

---
### Version 2 — [Style Name]
[Prompt]
```

**Output rules:**
- Output a clean, ready-to-paste prompt — no meta-commentary after
- Do not explain what every line does unless the user asks
- For a new Higgsfield video prompt, name a verified camera control or motion preset when it serves the brief

---

## Generation Ledger — when selected for the project

When this project's chosen record is the Higgsfield ledger, record each reported
generation attempt — kept, rejected, or filter-flagged — once in
`db/ledger/<project>.json`. RunningHub, Generation Service, and other executors
retain their own job receipts; do not duplicate them into this ledger. The
denominator (successes too, not just failures) supports takes-per-kept ratios.

**The 5-second rule for a selected ledger:** record a known verdict once. If
the take has not been selected, leave the verdict pending review instead of
asking a bookkeeping question. For a requested ledger row, use
`skills/higgsfield-recall/SKILL.md` § Log the Generation Result.

---

## @ Reference Rules

- User uploads a document (script, bible, brief, reference notes): read it from `workspace/input/`; if it landed elsewhere, move it there first (see Working Folders above)
- User uploads image: use `[reference image]` or describe it as "the provided reference"
- For video extension: note "extend from [reference video], continue with..."
- For style transfer: note "match the visual style of [reference image]"

---

## Shared Resources

| Resource | What it contains | When to use |
|----------|-----------------|-------------|
| `skills/shared/negative-constraints.md` | Generation artifacts + prevention phrases, by category | Consult for a relevant, concrete failure risk; append only the matching constraint |
| `skills/shared/provenance.md` | Repo-wide provenance legend — what [OFFICIAL]/[DEMO]/[FIELD]/[EMPIRICAL]/[HOUSE]/[MEASURED] mean and the evidence each requires | Before leaning on a tagged claim |
| `skills/shared/house-rulings.md` | Every contested doctrine question — ruling or OPEN, scope, both sides | When two skill files seem to disagree |
| `templates/` | 10 annotated genre templates with examples, models, annotations, variations | When user request matches a common genre — use as starting point |
| `templates/ad-asset-prep.md` | Ad asset preparation: product sheets, hero-character sheets, location plates — generate-many → test-in-motion → lock-the-winner | When an ad/product request needs reference assets built before video |
| `templates/character-design/` | 6 character-design worksheets (9-question sheet, story bible, visual DNA) | With `higgsfield-character-design` when developing characters before prompting |
| `templates/seedance/` | 10 Seedance technique templates: top-down-map, multi-character-anchor, single-character-position, worked-example-two-character, anime-animation, facs-expression-beats, footage-vfx-transform, global-style-prefix, omni-reference-2-5, staging-reference | When Seedance request is technique-shaped (spatial blocking, position references, multi-character anchoring, anime/stylized-2D, FACS acting, footage VFX, style prefix, 2.5 multi-reference) |
| `templates/text-overlays/` | 3 text-rendering templates: slogan, subtitle, speech-bubble | When user request includes on-screen text rendering |

---

## Sub-Skills (auto-loaded as needed)

| Skill | Trigger |
|-------|---------|
| `higgsfield-prompt` | New Higgsfield prompt writing or refinement request |
| `higgsfield-image-shots` | Cinematic image prompts — shot framing, angles, composition |
| `higgsfield-gpt-image-2` | GPT Image 2.0 / 2.5 prompts — when to prefer 2.5 (transparent background, xhigh/max), three-format taxonomy (JSON / prose / meta-prompt), UI mockups, infographics, reference sheets, static-ad recreation |
| `higgsfield-models` | "Which model should I use?" / model comparison / edit-lane, long-take (>15s) and motion-transfer choosers |
| `higgsfield-camera` | Camera movement questions (video) |
| `higgsfield-motion` | Named preset requests (Explosion, Werewolf, VFX, etc.) |
| `higgsfield-style` | Visual style / aesthetic questions |
| `higgsfield-character-design` | Pre-production story bible — premise / world / 9-question character / story spine / visual DNA (before prompting) |
| `higgsfield-scene-engine` | Optional scene/sequence structural audit — Goal / Obstacle / Tactic / Reversal / Value Shift |
| `higgsfield-recipes` | Genre scene templates |
| `higgsfield-troubleshoot` | Failed generations / quality issues |
| `higgsfield-mixed-media` | Artistic preset overlays (Noir, Sketch, Particles, etc.) |
| `higgsfield-cinema` | Cinema Studio / color grading / optical physics / multi-shot / Elements / Smart mode / @ references / Style Settings / Camera Settings / Manual Style |
| `higgsfield-pipeline` | Multi-shot workflow / tool chaining / full production pipeline |
| `higgsfield-motion-design` | Optional animated-ad storyboard flow; choose the video or code-motion executor from the brief |
| `higgsfield-recall` | Recall relevant past failures when requested, matched, or selected for the project |
| `higgsfield-audio` | Audio design, dialogue, SFX, ambient sound for audio-capable models |
| `higgsfield-seedance` | Seedance 2.0 / Pro prompt director + content-filter preflight linter (+ `HELL-GRIND.md`, Higgsfield's open-sourced feature-film pipeline) |
| `higgsfield-seedance-2-5` | Seedance 2.5 omni-reference dialect — generation/edit/extension modes, reference-role grammar, optional staging, keyframes, storyboards, blockouts, transitions, and VFX planning |
| `higgsfield-seedance-vfx` | Video-to-video footage transformation for a selected Seedance 2.0 route — preserve a real subject + camera move, add VFX / swap the environment / relight to match |
| `higgsfield-acting` | Character performance as behavior under pressure — objective / obstacle / tactics / subtext, with optional acting profile, beat and gaze detail |
| `higgsfield-shotlist-director` | Brief/script → one connected Seedance shotlist (style prefix + `@`-glossary + named per-scene prompts) as editable HTML |
| `higgsfield-facs` | FACS Action Unit codes for precise facial expressions in Seedance 2.0 — forced/uncanny/mixed expressions, close-up dialogue facial acting, emotion→AU recipes, FACS reference sheets |
| `higgsfield-3d` | 3D meshes (image / multi-view / text → GLB), rigging + animation, remesh / retexture, 3D Body, 3D Jutsu scene projects, 3D turnarounds and 3D staging blockouts |

> Full vocabulary in `vocab.md`
> Full motion preset library in `skills/higgsfield-motion/SKILL.md`
> Model comparison in `model-guide.md`
> Example prompts in `prompt-examples.md`
> Shared negative constraints in `skills/shared/negative-constraints.md`
> Genre-specific annotated templates in `templates/`
