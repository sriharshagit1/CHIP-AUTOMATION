import json

from chippilot.coverage_adapter import JsonCoverageAdapter, StaticCoverageAdapter
from chippilot.coverage_feedback import CoveragePoint, CoverageSnapshot


def test_static_adapter_normalizes_rows():
    snap = StaticCoverageAdapter().collect(".", rows=[{"name":"a","covered":2,"total":4}])
    assert snap.points[0].name == "a"
    assert snap.points[0].percentage == 0.5


def test_json_adapter_reads_generic_report(tmp_path):
    (tmp_path/"coverage.json").write_text(json.dumps({"coverage":[{"name":"a","covered":3,"total":4}]}))
    snap = JsonCoverageAdapter().collect(tmp_path, report="coverage.json")
    assert snap.total_coverage == 0.75
