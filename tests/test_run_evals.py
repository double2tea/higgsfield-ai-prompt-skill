"""evals/run_evals.py — vacuous passes are harness ERRORs; unmatched traps
are reported without assuming a cause.

Written against the public run_case()/main() surface so the same tests run
on the pre-fix harness (git show 9b86817:evals/run_evals.py) — where every
test below went RED: the vacuous cases returned [] (a pass).
"""

import importlib.util
import json
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("run_evals", REPO / "evals" / "run_evals.py")
run_evals = importlib.util.module_from_spec(_spec)
sys.modules["run_evals"] = run_evals
_spec.loader.exec_module(run_evals)

GOOD_RESPONSE = ("**Model**: Seedance 2.0\n**Mode**: std  **Aspect ratio**: 16:9  "
                 "**Duration**: 8s  **Resolution**: 1080p\n\nStyle: noir. Slow "
                 "dolly-in on a figure in a wool coat. Interior warehouse at dusk.")


@pytest.fixture(scope="module")
def specs():
    return run_evals._spec_index()


def is_error(failures):
    return bool(failures) and any("error" in f.lower() for f in failures)


def case(assertions, model="seedance_2_0", response=GOOD_RESPONSE):
    return {"id": "t", "model": model, "response": response, "assertions": assertions}


@pytest.mark.parametrize("assertions", [
    [{"type": "enum_legal", "expect": "ilegal"}],          # typo'd expect
    [],                                                    # no assertions
    [{"type": "word_count"}],                              # no bounds
    [{"type": "sections_present", "names": []}],           # empty names
    [{"type": "preset_names_valid", "names": []}],         # empty names
    [{"type": "lint_verdict", "max": "WARNING"}],          # unknown verdict
    [{"type": "enm_legal"}],                               # unknown type
], ids=["bad-expect", "no-assertions", "word-count-unbounded", "empty-sections",
        "empty-presets", "bad-max", "unknown-type"])
def test_vacuous_assertions_are_harness_errors(specs, assertions):
    failures = run_evals.run_case(case(assertions), specs)
    assert is_error(failures), failures


def test_enum_legal_without_declared_settings_is_an_error(specs):
    bare = "Style: noir. Slow dolly-in on a figure in a wool coat. Interior warehouse at dusk."
    failures = run_evals.run_case(case([{"type": "enum_legal"}], response=bare), specs)
    assert is_error(failures), failures


def test_well_formed_case_still_passes(specs):
    c = case([{"type": "enum_legal"}, {"type": "word_count", "max": 200},
              {"type": "sections_present", "names": ["Style"]}])
    assert run_evals.run_case(c, specs) == []


TRAP_1080P = ("**Model**: Seedance 2.5\n**Mode**: t2v  **Aspect ratio**: 16:9  "
              "**Duration**: 10s  **Resolution**: 1080p\n\nA kettle reaches boil on "
              "a gas stove, steam against morning window light. Static close-up.")


def test_trap_legal_under_current_specs_requires_reaudit(specs):
    s25 = run_evals.sl.resolve_model(specs, "seedance_2_5")
    assert s25 is not None and "1080p" in s25["resolutions"]
    failures = run_evals.run_case(
        case([{"type": "enum_legal", "expect": "illegal"}], "seedance_2_5", TRAP_1080P),
        specs)
    assert len(failures) == 1
    assert "re-audit the trap and checker" in failures[0]
    assert "checker regression" not in failures[0]


def test_legal_golden_with_illegal_current_enum_is_flagged(specs):
    golden = GOOD_RESPONSE.replace("16:9", "5:1")
    failures = run_evals.run_case(case([{"type": "enum_legal"}], "seedance_2_0", golden), specs)
    assert len(failures) == 1
    assert "illegal settings for seedance_2_0" in failures[0]


def test_main_counts_errors_and_exits_nonzero(tmp_path, monkeypatch, capsys):
    doc = {"skill": "t", "cases": [case([{"type": "enum_legal", "expect": "ilegal"}]),
                                   dict(case([{"type": "word_count", "max": 500}]), id="ok")]}
    (tmp_path / "t.json").write_text(json.dumps(doc), encoding="utf-8")
    monkeypatch.setattr(run_evals, "CASES_DIR", tmp_path)
    monkeypatch.setattr(sys, "argv", ["run_evals.py"])
    assert run_evals.main() == 1
    out = capsys.readouterr().out
    assert "1/2 eval cases passed" in out and "ERROR" in out


def test_committed_cases_have_no_harness_errors(specs):
    # The corpus itself must be well-formed; a malformed committed case is a
    # silent pass waiting to happen.
    errors = []
    for path in sorted((REPO / "evals" / "cases").glob("*.json")):
        for c in json.loads(path.read_text(encoding="utf-8")).get("cases", []):
            fs = run_evals.run_case(c, specs)
            errors += [f"{c['id']}: {f}" for f in fs if f.startswith("harness ERROR")]
    assert errors == []
