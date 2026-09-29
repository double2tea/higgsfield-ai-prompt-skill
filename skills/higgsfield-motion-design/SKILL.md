---
name: higgsfield-motion-design
description: "Use for a Higgsfield motion-design or animated-ad video when Higgsfield is the selected platform. Offers a storyboard-first path from brief to reference sheet to generated clip. For crisp editable text or logos, route to an installed code-motion executor. The chosen executor owns current models, upload, cost, and job status."
user-invocable: true
metadata:
  tags: [higgsfield, motion-design, animated-ad, logo-animation, brand, motion-graphics, storyboard, classicMD, highMD]
  version: 1.0.1
  updated: 2026-06-22
  parent: higgsfield
---

# Higgsfield Motion Design

A motion-design planning example originally written for the Higgsfield MCP connector.
Use its storyboard and visual-direction techniques when relevant; the selected
executor owns current tools, models, permissions, costs, and job state. Preserve
the user's requested pace, cuts, and output format. New prompt text defaults to
Simplified Chinese unless the user requests another language; preserve supplied
copy and machine syntax.
For the named camera/motion preset library (Explosion, Werewolf, Air Bending,
etc.) use `higgsfield-motion` instead.

> **Not a spec sheet.** Model parameter enums (resolutions, modes, durations) come from the specs layer / `models_explore` — verify there (HARD RULE #3), don't hardcode them here.

## QUICK FACTS
- Two example flows: **classicMD** (smooth, elegant, cinematic) vs **highMD** (fast cuts, extreme dynamics, CGI energy) — use the one the brief calls for [→](#step-0--determine-the-flow-type)
- Ask only for missing decisions that affect the brief, grouped in one message when practical [→](#step-1--brief-intake-one-message)
- The original example uses one GPT Image 2 storyboard grid; choose reference format with the selected executor [→](#step-3--generate-the-storyboard)
- The original example uses Seedance 2.0; confirm the selected model and schema with the executor [→](#step-4--generate-the-video)
- highMD rule: no realistic humans — silhouettes, chrome figures, or 3D abstract shapes only [→](#notes--rules)
- A highMD logo hold can scale to the clip length when the approved edit calls for one [→](#step-4--generate-the-video)

---

## STEP 0 — Determine the flow type

Identify which workflow applies before anything else:

- **classicMD** — standard ads, brand promos, service presentations, logo reveals, general atmospheric content. Smooth transitions, elegant typography, cinematic feel.
- **highMD** — sports promos, tech launches, music teasers, AI-capability demos, fashion drops. Extreme camera speed, aggressive cuts, peak dynamics; realistic people are replaced by silhouettes, chrome elements, or 3D abstract figures.

If the request makes the flow obvious, proceed silently. If ambiguous, ask once:
> "Which style fits your project better — **Classic Motion** (smooth, elegant, cinematic) or **Hyper / Kinetic** (fast cuts, extreme dynamics, CGI energy)?"

---

## STEP 1 — Brief intake (one message)

Confirm only decisions missing from the brief. Group related questions when
practical; do not ask again for an approved choice:

1. **Existing assets?** — Yes (upload logo / product photo / reference) · No (help me create the visual)
2. **Duration** — use the requested runtime; 5s / 10s / 15s are examples only
3. **Frame format** — 16:9 (horizontal) · 9:16 (vertical Reels/TikTok/Stories) · 1:1 (square feed)
4. **Mood / style** *(free input)* — e.g. energetic, minimalist, luxury, technological, atmospheric, aggressive, cinematic
5. **Brand / product name and tagline** *(if any)*
6. **Storyboard frames** — choose a count only if the brief calls for a sheet; 6 / 8 / 9 are examples

---

## STEP 2 — Asset handling

**If the user has assets:** use the selected executor's current upload or
reference workflow and preserve the approved asset roles.

**If the user has no assets:** plan a base visual from brand name, mood, style,
palette, and aspect ratio if the project needs one. Generate it only through
the selected executor with the required cost and submission authorization.

---

## STEP 3 — Generate the storyboard

For a storyboard-led brief, one sheet with N panels is a useful example.
Choose the format and panel count from the approved production plan.

In the original GPT Image 2 example, one storyboard grid uses the approved asset as a reference. If a grid fits the brief, keep panels visually consistent and give each a distinct moment and clear subject state. Choose the image tool, panel count, and any caption with the selected executor and user brief.

- **classicMD panels:** smooth compositions, elegant typography zones, cinematic lighting.
- **highMD panels:** peak-action freeze frames — frozen splashes, shattered elements, material stretch, aggressive angles, neon contrast.

Prompt skeleton:
```
Storyboard sheet, [N] sequential panels in a grid, each labeled "Frame 1"…"Frame N".
Panel 1: [scene]. Panel 2: [scene]. … Panel N: [logo lock / brand name].
Each panel: [camera angle], [motion state], [mood/lighting]. Style: [cinematic / kinetic].
Consistent color palette throughout. Clean storyboard design, thin borders between panels.
```

Present a short storyboard summary (Frame 1…N one-liners + Mood + Motion +
Ending). Revise or render the sheet when the user asks; use the selected
executor for any generation and its job receipt.

---

## STEP 4 — Generate the video

For an approved video plan, draft the prompt from the scene sequence, flow
type, duration, aspect ratio, mood/style, and any requested brand reveal.
The selected executor chooses the current model, schema, cost check, submission,
and job display. Seedance 2.0 is the original example, not a required model.

- **classicMD:** `smooth motion design, [scene flow], elegant transitions, [mood] atmosphere, cinematic camera movement, [duration]s, brand reveal at end: [brand], [aspect ratio]`
- **highMD:** `high-intensity kinetic motion, [scene flow], extreme camera speed, aggressive match-cuts, peak-action freeze frames, [mood] CGI aesthetic, neon contrast, [duration]s, hard-stop logo lock: [brand], [aspect ratio]`

For highMD, a final static brand/logo hold is an option when the brief calls for one; scale it to the clip length.

If a start frame is part of the approved plan, supply the approved asset
through the selected executor's reference mechanism. For Seedance 2.0, a
`genre` hint can support the intended mood when useful.

> **Resolution note:** Seedance 2.0 reaches 4K only in `mode=std`; `mode=fast` caps at 720p. See `higgsfield-seedance` / the specs layer.

---

## STEP 5 — Review & iterate

Present the render and collect specific feedback. Revise the plan or submit
another paid generation only when the user requests it.

---

## Notes & rules

- Ask only for the missing Step 1 decisions.
- A single storyboard grid is one useful format, not a required generation step.
- GPT Image 2 (`gpt_image_2`) and Seedance 2.0 (`seedance_2_0`) are original examples; the selected executor owns model choice.
- **highMD:** silhouettes, chrome figures, and 3D abstract shapes are available styles; add a logo hold only if the brief calls for it.
- **classicMD logo** can appear as opener, closer, or both — ask if unspecified.
- Use the selected executor's current tools for upload, generation, cost,
  status, and recovery. Explain a failed generation; submit another attempt
  only when the user approves it.

## Related skills
- `higgsfield-motion` — the named camera/motion preset library (different skill)
- For crisp, editable text and logo animation, route to an installed code-motion tool with its current schema.
- `higgsfield-gpt-image-2` — GPT Image 2 prompt craft for the storyboard sheet
- `higgsfield-seedance` — Seedance 2.0 prompt formula, modes, and preflight linter
- `higgsfield-pipeline` — product-ad workflow planning
- The selected executor — media upload, job status, and balance
