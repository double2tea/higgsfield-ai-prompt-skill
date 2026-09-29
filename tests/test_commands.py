"""Slash-command contracts — the promises each .claude/commands/*.md must keep.

/validate declared "release-ready" from the NON-strict run while --strict was
red; /release told the agent to push to protected `main` and tag whatever HEAD
was, contradicting CLAUDE.md (branch → PR → merge → tag the MERGE commit; PDF
regenerate → MANIFEST → upload). These tests pin the corrected contracts.
"""
import re

from conftest import REPO

CMD = REPO / ".claude" / "commands"


def _code_blocks(text):
    return "\n".join(re.findall(r"```(?:bash)?\n(.*?)```", text, re.DOTALL))


def test_validate_command_readiness_needs_all_three_gates():
    text = (CMD / "validate.md").read_text(encoding="utf-8")
    code = _code_blocks(text)
    assert "python3 scripts/validate.py --strict" in code
    assert "python3 -m pytest tests/ -q" in code
    assert "python3 scripts/validate.py --evals" in code
    # the only unflagged validate.py invocation in the runnable block is strict
    assert re.findall(r"validate\.py(?! --)", code) == []
    assert "release-ready** ONLY when all three" in text


def test_release_command_follows_the_protected_main_ceremony():
    text = (CMD / "release.md").read_text(encoding="utf-8")
    assert "git push && git push --tags" not in text          # no direct push to main
    assert "git switch -c release/v$ARGUMENTS" in text
    assert "gh pr create --base main" in text
    assert "mergeCommit" in text and 'git tag -a v$ARGUMENTS "$MERGE"' in text
    assert "git push origin --delete release/v$ARGUMENTS" in text
    # regenerate → refresh MANIFEST → upload, in that order
    gen = text.index("generate_user_guide.py")
    manifest = text.index("--write-manifest")
    upload = text.index("gh release upload")
    assert gen < manifest < upload
    # tagging happens after the merge
    assert text.index("gh pr merge") < text.index('git tag -a v$ARGUMENTS')
