"""Where things live. HTB_HOME overrides the repo root (tests use a temp dir)."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(os.environ.get("HTB_HOME", Path(__file__).resolve().parents[2]))
DATA = ROOT / "data"
BUILD = DATA / "build"          # generation cache (not shipped)
VERSION = "v1"
DATASET = DATA / VERSION        # the released dataset
RESULTS = ROOT / "results"      # raw model outputs, one folder per run
REVIEWS = DATA / "reviews"      # native-speaker reviews
DOCS = ROOT / "docs"
