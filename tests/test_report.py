import json

from conftest import HOME
from hinglish_toolbench.dataset import load
from hinglish_toolbench.providers import FakeProvider
from hinglish_toolbench.report import build, export_hf
from hinglish_toolbench.runner import run, score_run


class Oracle(FakeProvider):
    name = "oracle"


def test_leaderboard_build_and_hf_export():
    items = load()
    by_q = {i["query"]: i for i in items}
    score_run(run(Oracle("oracle-a", items=by_q), items, workers=1, progress=False), items)
    score_run(run(Oracle("oracle-b", items=by_q, fail_every=3), items, workers=1, progress=False), items)
    score_run(run(Oracle("lite-c", items=by_q), items, workers=1, progress=False, limit=1), items)
    (HOME / "README.md").write_text("x\n<!-- leaderboard:start -->\nold\n<!-- leaderboard:end -->\ny\n")
    (HOME / "DATASET_CARD.md").write_text("card")
    out = build()
    assert out["models"][0] == "oracle-a" and len(out["models"]) == 2
    lb = json.loads((HOME / "leaderboard.json").read_text())
    assert lb["full"][0]["indic_full_acc"] == 1.0
    assert any(r["partial"] for r in lb["lite"]) and len(lb["lite"]) == 3
    readme = (HOME / "README.md").read_text()
    assert "| 1 | oracle-a | **100.0%**" in readme and "old" not in readme and "lite split" in readme
    for f in ("leaderboard.svg", "by_language.svg", "gap.svg", "banner.svg", "five_ways.svg", "inside.svg", "judged.svg", "pipeline.svg", "slips.svg"):
        svg = (HOME / "docs" / "img" / f).read_text()
        assert svg.startswith("<svg") and "prefers-color-scheme: dark" in svg
    assert "Hinglish ToolBench" in (HOME / "docs" / "index.html").read_text()
    hf = export_hf()
    rows = [json.loads(l) for l in open(f"{hf}/data/test.jsonl")]
    assert len(rows) == 15 and isinstance(rows[0]["expected"], str)
