---
name: image-prompt-spec
description: Write production image-generation and image-edit briefs for Nano Banana Pro, Seedream, GPT Image, and Qwen. Use when the user asks for an image prompt, edit prompt, reference-image roles, style lock, or why the same prompt looks different across models. Not for video, Cinema Studio, Soul ID, credits, or any vendor UI.
license: MIT
metadata:
  type: workflow
  version: "1.0"
  source: Distilled from Higgsfield production practice and vendor image guides. Platform controls removed.
---

# Image prompt spec

Write a production brief, not a tag soup. Reply in the user's language. Deliver the brief in English unless the target model is Qwen and the user wants Chinese typography.

Do not mention Higgsfield, Soul slots, Cinema Studio, credits, CLI flags, or catalog ids.

## Load map

Read only the file the job needs. Do not load the parent Higgsfield tree.

- Model dialect — `references/models.md`
- Edit or multi-reference — `references/edit.md`
- Worked brief — `references/examples.md`

## Hard rules

1. Name the finished object first (poster, packshot, keyframe, local edit).
2. Write only what a camera can see. No "8K, masterpiece, beautiful".
3. Assign every reference a single role. Identity, style, product, or light.
4. Do not restate a locked face. The reference owns identity.
5. Put on-image text in quotes and name its position.
6. Edit in one change per pass. See `references/edit.md`.
7. Same flaw twice means rewrite the brief.
8. Keep the skeleton identical across models. Change density only. See `references/models.md`.
9. If the model is unnamed, deliver the skeleton plus one dialect line.

## Shared skeleton

```text
FINISH: <poster | packshot | keyframe | portrait | local edit>
SUBJECT: <who or what, age-blind physical description, one action>
PLACE: <where, time, weather if visible>
CAMERA: <height, distance, lens feel in words>
LIGHT: <source, direction, hardness, color>
STYLE: <one medium or era, one palette>
TEXT: "<exact string>" at <position>
KEEP: <what must not change>
REFS:
  Image 1 — IDENTITY. Face and body only.
  Image 2 — STYLE. Palette and rendering only.
  Image 3 — PRODUCT. Shape, logo, materials.
```

Age-blind means no age number.

## Delivery

1. The brief, ready to paste.
2. A dialect line naming the model and the one adjustment from `references/models.md`.
3. The reference role list, or a note that a role is missing.

Do not generate the image unless the user asked for generation.
