# image-prompt-spec

Thin still-image skill. Lives on branch `image-prompt-spec` of the fork so `main` can still fast-forward from OSideMedia.

Install this folder only. Do not point an agent at the repo root.

## Internal references (all relative, one level)

| From | To | Exists |
|---|---|---|
| SKILL.md | references/models.md | yes |
| SKILL.md | references/edit.md | yes |
| SKILL.md | references/examples.md | yes |
| references/models.md | ../SKILL.md skeleton | yes |
| references/edit.md | ../SKILL.md KEEP block | yes |
| references/examples.md | models.md dialect notes | yes |

No links into `skills/higgsfield-*`, CLI, or catalog files.

Upstream sync:

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

Do not merge `main` into this skill folder automatically. Discipline changes belong in a reviewed edit of `SKILL.md`.
