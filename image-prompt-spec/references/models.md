# Model dialects

Skeleton is in `../SKILL.md`. Do not change block order. Examples are in `examples.md`.

House styles differ because each model has a different prior and reads a reference as features, not pixels. Lock style in a style-only reference.

## Nano Banana Pro / Banana 2

Narrative, short, one or two sentences plus the blocks.

- Prefer physical light and place over artist names.
- Lens numbers are weak. Say "tight portrait, background falling soft".
- Best at identity match and one-line corrections.
- Label every reference. Roles are in `edit.md`.

## Seedream 5 Pro

Physical and material-heavy. Stronger on stylized and non-human subjects. Weaker when the same sentence also demands exact layout.

## GPT Image 2 / 2.5

- One scene, no chrome: dense prose (Format B).
- Panels, labels, UI: one JSON object (Format A). Tie goes to A.
- Theme only: short meta brief (Format C).
- Do not say "photorealistic" for faces. Say film photograph, grain, flash.
- Quote exact text. Shape is in `examples.md`.

## Qwen Image

A school or medium name is allowed. Chinese strings stay in quotes with a position. Still assign roles from `edit.md`.

## Routing

| Job | First try |
|---|---|
| Face lock, small fix | Banana |
| Fantasy / stylized still | Seedream |
| Poster, UI, quoted text, clothing | GPT Image |
| Chinese layout, named school | Qwen |
