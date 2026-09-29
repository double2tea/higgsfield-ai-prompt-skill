"""CI workflows — the shell blocks are EXECUTED here, not just grepped.

Steps are extracted from the workflow text (stdlib only, no YAML library) and
run with `bash -e`, the runner's default shell, against controlled inputs:

  * validate.yml's lint self-check must demand the FAIL exit code AND the rule
    id (pre-v3.37 any non-zero exit — a traceback, an unknown-model exit 2 —
    passed as "expected FAIL").
"""
import os
import re
import shutil
import subprocess
import sys

import pytest

from conftest import REPO

WF = REPO / ".github" / "workflows"
BASH = shutil.which("bash")
pytestmark = pytest.mark.skipif(BASH is None, reason="bash not available")


def step_run(workflow: str, name_prefix: str) -> str:
    """The literal `run: |` block of the step whose name starts with prefix."""
    lines = (WF / workflow).read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^(\s*)- name: (.*)$", line)
        if not (m and m.group(2).startswith(name_prefix)):
            continue
        step_indent = len(m.group(1))
        for j in range(i + 1, len(lines)):
            r = re.match(r"^(\s*)run: \|\s*$", lines[j])
            if r:
                base = None
                body = []
                for k in range(j + 1, len(lines)):
                    ln = lines[k]
                    if ln.strip() == "":
                        body.append("")
                        continue
                    ind = len(ln) - len(ln.lstrip())
                    if ind <= len(r.group(1)):
                        break
                    base = ind if base is None else base
                    body.append(ln[base:])
                return "\n".join(body) + "\n"
            if re.match(rf"^\s{{0,{step_indent}}}- ", lines[j]):
                break
    raise AssertionError(f"{workflow}: no step starting with {name_prefix!r} with a run block")


def run_bash(script: str, cwd, env: dict):
    return subprocess.run([BASH, "-e", "-c", script], cwd=cwd, capture_output=True,
                          text=True, env={**os.environ, **env})


# ── validate.yml: known-FAIL needs the FAIL code AND the rule id ─────────────

FAKE_LINTER = '''import sys
args = " ".join(sys.argv[1:])
fail_case = "--mode fast" in args or "--ar 21:9" in args
MODE = {mode!r}
if fail_case and MODE == "crash":      # a traceback / unknown-model exit 2
    print("Traceback (most recent call last):\\n  KeyError: 'specs'", file=sys.stderr)
    sys.exit(2)
if fail_case and MODE == "wrong-rule":
    print("  x [FAIL] some-other-rule"); sys.exit(1)
if not fail_case and MODE == "pass-fails":
    print("  x [FAIL] mode-constraint"); sys.exit(1)
if fail_case:
    rule = "mode-constraint" if "--mode fast" in args else "ar-not-supported"
    print(f"  x [FAIL] {{rule}}"); sys.exit(1)
sys.exit(0)
'''


def _fake_repo(tmp_path, mode):
    (tmp_path / "scripts").mkdir()
    (tmp_path / "scripts" / "seedance_lint.py").write_text(FAKE_LINTER.format(mode=mode))
    return tmp_path


def test_lint_selfcheck_passes_on_the_real_linter():
    script = step_run("validate.yml", "Seedance lint self-check")
    r = run_bash(script, REPO, {})
    assert r.returncode == 0, r.stdout + r.stderr
    assert "lint self-check OK" in r.stdout


@pytest.mark.parametrize("mode", ["crash", "wrong-rule", "pass-fails"])
def test_lint_selfcheck_rejects_a_wrong_failure(tmp_path, mode):
    script = step_run("validate.yml", "Seedance lint self-check")
    r = run_bash(script, _fake_repo(tmp_path, mode), {})
    assert r.returncode != 0, f"{mode}: self-check passed a broken linter\n{r.stdout}"


def test_lint_selfcheck_positive_control_fake_linter_behaving(tmp_path):
    script = step_run("validate.yml", "Seedance lint self-check")
    r = run_bash(script, _fake_repo(tmp_path, "ok"), {})
    assert r.returncode == 0, r.stdout + r.stderr


def test_validate_yml_has_no_directory_scaffolding():
    text = (WF / "validate.yml").read_text(encoding="utf-8")
    assert "if [ -d tests ]" not in text and "if [ -d evals ]" not in text
    assert "python3 -m pytest -q" in text and "validate.py --evals" in text
