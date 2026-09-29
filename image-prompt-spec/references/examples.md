# Examples

Dialect adjustments are in `models.md`. Edit lines are in `edit.md`.

## Weak

`beautiful cinematic 8k masterpiece woman, ultra realistic, trending`

## Shared brief

```text
FINISH: keyframe
SUBJECT: a woman with a wet bob and a dark wool coat, standing still, looking off-camera left
PLACE: night alley after rain, neon sign behind her right shoulder
CAMERA: eye-level medium shot, background falling soft
LIGHT: cool sign light from camera-right, warm practical from a doorway camera-left
STYLE: 35mm night photograph, muted teal and amber, visible grain
TEXT: none
REFS:
  Image 1 — IDENTITY. Face and build only.
```

## Edit

```text
CHANGE: replace the coat with the ivory satin dress in Image 2
KEEP: face, hair, pose, alley, crop
MATCH: the existing neon and doorway light on the new cloth
```

## GPT poster

```json
{
  "type": "vertical exhibition poster",
  "style": "Swiss editorial, off-white paper, black and one red",
  "layout": {
    "top": { "kicker": "NIGHT STUDY" },
    "center": "the woman from the identity reference, coat, wet alley",
    "bottom": { "title": "AFTER RAIN" }
  }
}
```
