"""Shared fixtures for the tooling test suite.

The scripts/ directory is added to sys.path so the flat-module tooling
(seedance_lint, higgsfield_memory, validate) imports directly.
DB redirection uses the HF_DB_DIR env var (see scripts/higgsfield_memory.py)
because it works identically for in-process imports and subprocess CLI
invocations.
"""

import json
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "scripts"
FIXTURES = Path(__file__).parent / "fixtures"

sys.path.insert(0, str(SCRIPTS))


@pytest.fixture
def tmp_db(tmp_path, monkeypatch):
    """Empty filter/quality DBs in a temp dir, exported via HF_DB_DIR."""
    db = tmp_path / "db"
    db.mkdir()
    for name in ("filter-memory.json", "quality-memory.json"):
        (db / name).write_text(
            json.dumps({"entries": [], "_total_entries": 0}), encoding="utf-8")
    monkeypatch.setenv("HF_DB_DIR", str(db))
    return db


@pytest.fixture(scope="session")
def mini_spec():
    """Committed model specs for linter checks; no removed generator needed."""
    path = REPO / "specs" / "model-specs.json"
    return json.loads(path.read_text(encoding="utf-8")), path
