---
name: higgsfield-shotlist-director
description: "Use when the user requests a connected shotlist for a selected Seedance 2.0 production. Can produce one editable HTML artifact with shared style and asset references plus numbered scene prompts. The 15-second envelope and CUT blocks are workflow options, not requirements for every scene; preserve the requested duration, format, and approved edit plan."
user-invocable: true
metadata:
  tags: [higgsfield, seedance, seedance-2.0, shotlist, director, style-prefix, ad, commercial, artifact, html]
  version: 1.3.0
  updated: 2026-09-26
  parent: higgsfield
---

# Higgsfield Shotlist Director

**Scope:** The 15-second prompts and `CUT` blocks below describe a Seedance 2.0
shotlist workflow. Keep a requested or approved duration and edit plan; one
uninterrupted shot is valid. Confirm current limits with the selected executor.

Turn a brief into **one connected shotlist** — not a pile of separate prompts.
The deliverable is a single editable HTML artifact the user opens in a browser,
ticks scenes off as they shoot, and comes back to you to revise. This is the
artifact-shaped workflow a fully-AI commercial actually runs on: lock a global
look once, declare the cast/props/locations once, then emit named per-scene
prompts that all inherit both.

> **This skill is the connected layer on top of `higgsfield-seedance`.** It does
> not reinvent the prompt grammar — every per-scene prompt obeys the six-slot
> formula and the Prompt-Craft Laws in `../higgsfield-seedance/SKILL.md`, and
> every prompt is preflight-linted before delivery. What this skill adds is the
> *document*: the global Style Prefix, the `@`-glossary, the per-scene numbering,
> and the edit-once / per-scene-override semantics that keep 25 prompts in sync.

## QUICK FACTS
- Output = **one self-contained HTML file** (inline CSS/JS, no deps), not loose prompts [→](#what-you-produce)
- Three structural layers, top to bottom: **Global Style Prefix → `@`-asset glossary → named per-scene prompts** [→](#the-three-layers)
- Example per-scene structure: `Style → Characters → Scene`, with `CUT` blocks only for planned edits; the 15s envelope and `3a/3b/3c` split are optional [→](#per-scene-prompt-law)
- [OFFICIAL] Density heuristic for a planned multi-shot sequence: group related rows within the selected model's length limits; split only where a requested edit or real continuity change calls for it [→](#prompt-density--grouping-shot-rows-into-15s-envelopes)
- For a planned edit sequence, check that stated cut durations fit the requested runtime and look for accidental visual repetition [→](#sequence-tempo-and-variety)
- Continuity carries exits too: an **Off-screen line** (exit side + last state) per just-departed character keeps re-entry direction legal [→](#per-scene-prompt-law)
- **Edit-once-propagates**: change the prefix once → it changes in every prompt; per-scene **override** lets one scene break the global look [→](#edit-once-and-per-scene-override)
- Differentiators over a bare shotlist generator: **preflight linter**, **reference-role lanes**, **Elements `@`-auto-attach**, **failure-mode awareness**, and optional acceptance-rate logging [→](#what-makes-this-outclass-a-bare-generator)
- Default to Simplified Chinese for new prompt text; preserve user text and machine syntax. Translate for execution only when the selected mode has a verified language requirement [→](#workflow)

---

## What you produce

A single `shotlist.html` (saved to the user's outputs and presented). It is
**self-contained** — inline CSS, inline JS, zero external dependencies — so the
user can open it offline and it just works. Structure:

1. **Title bar** — project name (infer from the brief; "Untitled" if unclear).
2. **Global Style Prefix** — collapsible block at top, applied to every prompt.
3. **`@`-asset glossary** — the cast/props/locations declared once.
4. **Scene list** — numbered scenes, each with a checkbox (progress saved in
   `localStorage`), a one-line scene description, and one or more copy-ready
   prompt blocks labeled with their planned durations.
5. A short "how to use" note (checkboxes auto-save; ask Claude to revise).

The Style Prefix appears **once** in the collapsible block **and** is prepended
verbatim to every prompt's copy-block — so the user copies one prompt into
Seedance and it works standalone, no reassembly.

---

## The three layers

### 1. Global Style Prefix

A single style block glued to every prompt in the document — edit it once and it
changes everywhere. It locks the film's global look: format/resolution, lighting
doctrine, colour ratio, lens/shutter, skin realism, acting register, physics,
composition, continuity, frame rate, and audio convention.

Ship the reusable fill-in-the-blanks block from
[`../../templates/seedance/global-style-prefix.md`](../../templates/seedance/global-style-prefix.md).
**Always check the conversation first** — if the user pasted a custom prefix, use
that one verbatim. Otherwise use the template default.

### 2. `@`-asset glossary

Declare every recurring asset once, with a stable `@`-name, then register each
under **Elements** in Higgsfield with the **same name** so pasting a prompt
auto-attaches the right images:

```
@hero — main character          @boss — side character
@headphones — product           @sneakers · @bag · @skydancer — props
@kitchen · @stadium · @street — locations
@s_hero — athletic-look hero     @s_hero_wet — sweaty post-run hero
@music_track (audio_1.wav) — motion locks to this beat
@staging_ACME_street_v1 — front-on position reference, attached LAST
```

A position map in the glossary is always the **front-on staging reference**
(`../../templates/seedance/staging-reference.md`: outline figures, position only,
attached after the photo references), named by that template's § Tag naming
(`@staging_[PROJECT]_[scene]_[version]`; `ACME` above is a placeholder project). No
slot filename goes beside it: slots are assigned by upload order, so a staging
reference filed as `image_1` would sit in the character's slot. Elements
auto-attach finds the right images, but nothing in this repo documents the order
it attaches them in — when the staging reference must land last, check the
attach order before firing, or attach it by hand after the photo references. A **top-down** floor plan is never
registered or attached — it is an authoring aid whose output travels into the
prompt as a written blocking note (`../../templates/seedance/top-down-map.md`).

The slot→role discipline (`@Image1` = character, `@Image2` = costume, `@Audio1`
= rhythm…) comes from `../higgsfield-seedance/SKILL.md` § Reference Roles →
Per-Image Role Convention. **Multi-state variants get their own locked entry**
(`@s_hero_wet`), built on purpose up front — asking the model to "sweat him up"
later makes it improvise and the face drifts.

**Each glossary entry also carries a fidelity grade** — a role says what job the
asset does, the grade says how much of it must survive into the pixels:
*full-preserve* / *partial-preserve (name the parts)* / *attribute-transfer (name
the target it lifts onto)* / *loose-guide*. One word per line is enough
(`@headphones — product, full-preserve`); the grades and their prompt phrasing
live in `../higgsfield-seedance-2-5/SKILL.md` § Reference Roles → Fidelity.
Without a grade, "use @image4 for the coat" silently means whatever the model
felt like keeping that day.

### 3. Named per-scene prompts

Number scenes (`1`, `2`, `3`…) and split a scene into named prompts (`1a`, `1b`)
only when its planned edits or the selected model's duration limit require it.
Use one checkbox per **scene**, including when that scene has multiple prompts.

---

## Per-scene prompt law

The following is an example layout for a planned multi-cut prompt; keep only
the blocks the approved shot needs. This verbatim-prefix shape is the
**connected-shotlist regime** `[FIELD — 13-project harvest]`;
a standalone block-scaffold prompt instead distributes style into its home
blocks and opens on SCENE CONTEXT — `../higgsfield-seedance/SKILL.md`
§ Distributed style. Which shape ships is decided by the workflow: shotlist →
this law; single standalone brief → distributed.)

```
[STYLE PREFIX — full block, verbatim (or the per-scene override)]

Characters:
[Only the characters in this prompt. @names + locked physical descriptors +
carried state — wet hair from the prior scene, strap on one shoulder, same
wardrobe unless it changed on screen.]

Off-screen (only when someone just left):
[Anyone in the PREVIOUS prompt but absent here: exit side + last visible state —
"Bo — exited frame-left, still carrying the crate." Carry for one prompt, drop
after two consecutive absent prompts.]

Scene:
[1–2 sentences. Where, when, and the geo-spatial blocking — where each character
sits relative to the location and to each other. "Hero at the kitchen island,
back to camera; the moka pot is on the left burner."]

CUT 1 — [framing, lens/FOV, camera move]:
[Beat-accurate action: gesture, eye-line, breath, micro-pause; what the camera
does; what the light does; diegetic SFX if relevant.]

CUT 2 — …
```

In this example workflow, prompts may **target 15s** when the selected mode supports
that duration and the brief calls for it; plan cuts only if the scene needs them. Many 15s prompts hold 1–3 cuts —
that is the **live-action narrative norm**; stylized registers run denser by
design (3D-animated 6 shots/15s, product montage 8–10 sections with 0.3s macro
cuts — `../higgsfield-style/SKILL.md` § Style Recipes), and the flash-establish
/ insert durations in `../higgsfield-camera/SKILL.md` § Shot duration by type
are what make dense shapes fit. If a scene runs longer, split it across
`3a/3b/3c` only when needed, each with the full Style Prefix and Characters
block, continuity holding across them.

**Beat-by-beat choreography, not "he dances."** Generic motion verbs mean nothing
to Seedance — spell the move out: *"two crisp head nods on the beat, shoulders
rolling back one at a time, a soft knee-dip, a loose finger-snap, finishing on a
quarter-spin."* (Full pattern: `../../templates/10-dance-music-performance.md`.)

**The Off-screen line is what keeps re-entries legal.** Carried state covers who
is in frame; it says nothing about who just left, and re-entry from the wrong
side is a classic continuity break the viewer feels before they can name it.
One line per departed character buys the next prompt the correct entering side
and hand-state for free. `[EMPIRICAL — MiniMax H3 skill corpus; re-derived]`

**Match-cut via a repeated anchor action.** When independently-generated scenes
must cut together, end and begin neighboring scenes on the **same gesture** (the
ear-cup tap) — the reused motion lets them "cut on action" most of the time.
When those clips then sit on one timeline, plan the unifying finish pass and cut
placement per `../higgsfield-audio/SKILL.md` § Cutting to music.

---

## Prompt density — grouping shot rows into 15s envelopes

`[OFFICIAL — Higgsfield shotlist-builder + seedance-2-pro-director skills,
2026-07]` — the shotlist's hardest judgment call is how many script beats
share one prompt within the approved runtime. There is no fixed ratio (canonical productions ran
anywhere from 1.4 rows per prompt to 4.7); decide per scene with this
heuristic:

**Consider grouping shot rows when these conditions hold:**

1. Same character set in frame
2. Same location (or sub-area of it)
3. One continuous emotional/temporal unit — no time skip, no mood pivot
4. Stageable within the requested duration and selected model's limits
5. The combined prompt stays inside practical length limits (ZH: the
   1,800-char hard cap; EN block prompts run much longer — see
   `../higgsfield-seedance/SKILL.md` § Field calibration)

**Consider a split when the approved edit plan or model limit calls for it:**

1. Hard cut between locations (apartment → flashback)
2. A major character entrance/exit changes the handle list
3. A lens/setup change that needs its own envelope (wide establish → tight
   insert)
4. A performance arc that needs a separate shot; preserve a requested
   continuous performance even if the script lists several beats.
5. A planned insert/cutaway to a prop or screen

**Complexity budget per prompt** (possible split signals): more than 2 strong
actions · more than 2 camera moves · more than 3 important characters ·
more than 1 complex VFX event · more than 1 location change — any of these
may call for another envelope when the plan allows it. Duration ladder: 4–8s = one strong
action · 8–12s = one action + a reveal · 12–15s = 2–3 simple beats ·
complex fight/chase/transformation = multiple prompts. **Reconciling the
ladder with a 15s example:** use the requested runtime and the selected
model's current limits. A short scene need not be padded to fill an envelope.

Split an overloaded prompt only when the brief and edit plan support the split.

**Thin briefs.** Keep unspecified action, emotion, camera, and sound open
unless a concrete production choice is needed to make the requested scene
work. Ask when that choice would alter approved intent. A neutral-to-portrait
lens (63°/47° FOV in Seedance block prompts; 29° for a needed close-up) and
motivated practical light are available techniques, not automatic additions
(`../higgsfield-seedance/SKILL.md` § FOV anchors). Confirm runtime rather than
silently inserting a 15s target.

---

## Sequence tempo and variety

`[EMPIRICAL — third-party director-skill evaluations 2026-08-09; re-derived
heuristics, unmeasured here]` — two whole-sequence checks that no per-prompt
rule can catch, run once before delivery:

**Tempo budget — the arithmetic gate.** Budget the piece before writing it:
total runtime at ~4–6s average per cut can estimate the cut count when cuts
are already part of the edit plan. A longer hero hold (6–8s) is one option.
Rough bands: ≤15s → ~3 cuts · ~20s → 4–5 · ~30s → ~6 · ~45s → 7–8 · ~60s →
9–11. When cut durations are stated, check that they add up to the requested
runtime. A mismatch can hide dead air or an impossible edit.

**Monotony audit — read the column, not the prompt.** After drafting, read only
the framing + camera-move line of every cut, top to bottom, as one column. No
run of **three consecutive cuts** may share the same shot size *and* the same
camera move; when every cut reads "medium, slow push-in", vary the shot's
*function and scale* — not just its duration. Per-prompt review can't see this
failure at all; it only shows when the column is read as a sequence, and it is
the single most common tell of a generated shotlist.

---

## Edit-once and per-scene override

Talk to the user's revisions like an editor of one connected document, never 20
loose chats:

- **"Edit prompt 1a, do X"** → change only that prompt.
- **"Change the style prefix to Y, apply everywhere"** → propagate to every
  prompt's copy-block in one pass.
- **Per-scene override** → one scene can break the global look. Replace just that
  prompt's Style Prefix lighting line (e.g. Scene 2 stadium: *"bright, genuinely
  sunny midday, strong frontal sun, deep blue sky, hard-edged shadows"*) while
  every other scene keeps the soft global prefix. The override is a local edit to
  one prompt's prefix, not a change to the global block.

When revising, **re-render the same HTML file with the change applied** — don't
describe the change in chat. Preserve scene numbering where possible (don't
renumber everything for a one-prompt edit), preserve the Style Prefix unless told
to change it. The user's checkbox state survives via `localStorage` keyed by
scene number, so stable numbering = no lost progress.

---

## What makes this outclass a bare generator

A plain "script → prompts" generator stops at the document. This skill is wired
into the rest of the repo, which is the whole point:

1. **Preflight prompts for the selected Higgsfield model.** Before delivering the shotlist, run each prompt's
   copy-block through the linter — `python3 scripts/seedance_lint.py --preflight
   --regime block --model seedance_2_0 "<prompt>"`
   (`../higgsfield-seedance/SKILL.md` § Pre-flight Linter). Copy-blocks are
   block-scaffold regime: the linter usually auto-detects this, but pin
   `--regime block` so the short-form word caps can never fire on a
   full-density scene prompt. Real names, brand/IP, age markers, conflicting instructions, shot-
   count drift, and out-of-enum aspect/resolution/mode can be caught. A shotlist of 25 prompts is 25 chances to ship a flagged
   one. In the same pass run the § Sequence tempo and variety checks — the
   linter sees one prompt at a time; the sum check and monotony audit see the
   sequence.
2. **Reference-role lanes.** The `@`-glossary uses the stable slot→role
   convention so `@Image1` = character holds across all 25 prompts and nobody
   re-checks which face the model expects at shot 47.
3. **Failure-mode awareness.** Flag high-risk shots at authoring time (reflections,
   same-character doubles, crowds, compound camera moves, door-entry geometry) per
   `../higgsfield-seedance/ENGINE-RULES.md` and
   `../higgsfield-seedance/FAILURE-MODES.md`, rather than
   letting them silently break a scene.
4. **Acceptance-rate honesty.** The finished ad is the best few seconds out of
   many takes — keep candidates, test in motion, lock the winner, and log
   kept/rejected outcomes only if the project chose the Higgsfield ledger (`higgsfield-recall`). The shotlist is the
   plan; iteration is still the skill.
5. **Audio as a driver.** When a `@music_track` locks the choreography, write the
   beat-sync mapping per `../higgsfield-audio/SKILL.md` § Audio as a Conditioning
   Input; keep the prompt body diegetic-only and layer score in post.

---

## Workflow

1. **Read the brief as a director, not a transcriber.** Find the dramatic shape —
   where each scene turns, lands, and breathes.
2. **Lock the Style Prefix.** Custom from the conversation, or the template
   default.
3. **Build the `@`-glossary.** One entry per recurring asset; multi-state variants
   get their own locked entry.
4. **Block the scenes.** Number them; divide a long beat only when the requested
   duration and selected mode require it.
5. **Write each prompt** with the style, characters, and scene detail it needs.
   Use `CUT` blocks only for planned edits. Default to Simplified Chinese;
   preserve user copy and machine syntax. Translate for execution only when
   the selected mode has a verified language requirement.
6. **Preflight every prompt** and flag high-risk shots.
7. **Generate the HTML** (skeleton below) and present it.
8. **On revisions**, re-render the file with edits applied; preserve numbering.

---

## HTML skeleton

Self-contained, dark directing-room aesthetic. Inline everything. Checkbox state
persists in `localStorage`; each prompt has a Copy button; the Style Prefix is in
a collapsible block at the top **and** prepended to every prompt's `<pre>`.

```html
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>{{PROJECT_TITLE}} — Director's Shotlist</title>
<style>
  :root{--bg:#0e0e10;--panel:#17171a;--panel-2:#1d1d21;--border:#2a2a30;
        --text:#e8e8ea;--dim:#9a9aa2;--accent:#d4a259;--done:#4ade80}
  *{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--text);
    font-family:-apple-system,system-ui,sans-serif;line-height:1.5;padding:32px 24px 80px}
  .container{max-width:980px;margin:0 auto} h1{font-size:28px;margin:0 0 4px}
  .howto,details.style-prefix,.scene{background:var(--panel);border:1px solid var(--border);
    border-radius:8px;padding:14px 18px;margin-bottom:18px}
  details.style-prefix summary{cursor:pointer;font-weight:600;color:var(--accent)}
  pre{white-space:pre-wrap;font-family:"SF Mono",Menlo,monospace;font-size:12.5px;margin:0}
  .scene-header{display:flex;gap:12px;align-items:flex-start;margin-bottom:14px}
  .scene-num{font-weight:700;color:var(--accent);min-width:48px}
  .scene.done .scene-desc{text-decoration:line-through;color:var(--dim)}
  .prompt-block{background:var(--panel-2);border:1px solid var(--border);
    border-radius:6px;margin-top:12px;overflow:hidden}
  .prompt-label{display:flex;justify-content:space-between;padding:8px 14px;
    border-bottom:1px solid var(--border);font-size:12px;color:var(--dim);text-transform:uppercase}
  .copy-btn{background:transparent;color:var(--accent);border:1px solid var(--border);
    border-radius:4px;padding:4px 10px;font-size:11px;cursor:pointer}
  .copy-btn.copied{color:var(--done);border-color:var(--done)}
  pre.prompt{padding:14px 16px}
</style></head><body><div class="container">
  <h1>{{PROJECT_TITLE}}</h1>
  <div class="howto">Tick scenes as you finish — progress saves automatically.
    Copy any prompt with the approved scene details and planned cuts, if any. Ask for revisions.</div>
  <details class="style-prefix"><summary>Global Style Prefix (applied to every prompt)</summary>
    <pre>{{STYLE_PREFIX_TEXT}}</pre></details>
  {{SCENES_HTML}}
</div><script>
  document.querySelectorAll('.scene input[type=checkbox]').forEach(cb=>{
    const k='shotlist-scene-'+cb.dataset.scene+'-done';
    if(localStorage.getItem(k)==='1'){cb.checked=true;cb.closest('.scene').classList.add('done')}
    cb.addEventListener('change',()=>{localStorage.setItem(k,cb.checked?'1':'0');
      cb.closest('.scene').classList.toggle('done',cb.checked)})});
  document.querySelectorAll('.copy-btn').forEach(b=>b.addEventListener('click',()=>{
    const p=b.closest('.prompt-block').querySelector('pre.prompt');
    navigator.clipboard.writeText(p.textContent).then(()=>{b.classList.add('copied');
      const t=b.textContent;b.textContent='Copied';
      setTimeout(()=>{b.classList.remove('copied');b.textContent=t},1500)})}));
</script></body></html>
```

Each scene block in `{{SCENES_HTML}}` (one checkbox per scene, `data-scene` =
scene number as a string):

```html
<div class="scene">
  <div class="scene-header">
    <input type="checkbox" data-scene="3">
    <div class="scene-num">3.</div>
    <div class="scene-desc">Hero grooves across the kitchen — the world goes quiet.</div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label"><span>Prompt 3a · [planned duration]</span><button class="copy-btn">Copy</button></div>
    <pre class="prompt">[FULL PROMPT — Style Prefix, Characters, Scene; CUT blocks only for planned edits]</pre>
  </div>
  <div class="prompt-block">
    <div class="prompt-label"><span>Prompt 3b · [planned duration]</span><button class="copy-btn">Copy</button></div>
    <pre class="prompt">[SECOND PROMPT only if scene 3 needs a split]</pre>
  </div>
</div>
```

---

## Related skills

- `higgsfield-seedance` — the prompt grammar this skill emits (six-slot formula,
  Prompt-Craft Laws, Reference Roles, preflight linter, engine + failure modes)
- `higgsfield-pipeline` — upstream multi-shot production planning the shotlist
  slots into
- `higgsfield-audio` — `@music_track` beat-sync + diegetic-only convention
- `higgsfield-character-design` — character sheets the `@`-glossary points at
- `higgsfield-recall` — recall prior outcomes; log kept/rejected takes only when this project uses the Higgsfield ledger
- `../../templates/seedance/global-style-prefix.md` — the reusable prefix block +
  a per-scene override example
