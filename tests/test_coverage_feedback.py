from chippilot.coverage_feedback import CoveragePoint, CoverageSnapshot, compare_coverage, prioritize_gaps, snapshot_from_rows

def test_snapshot_and_gap_priority():
    snap = snapshot_from_rows([{"name":"fsm","kind":"branch","covered":2,"total":4},{"name":"reset","kind":"assertion","covered":1,"total":1}])
    assert snap.total_coverage == 0.75
    assert prioritize_gaps(snap)[0].name == "fsm"

def test_compare_rejects_regression():
    before = CoverageSnapshot((CoveragePoint("a", covered=1, total=2),))
    after = CoverageSnapshot((CoveragePoint("a", covered=0, total=2),))
    delta = compare_coverage(before, after)
    assert delta.regressed == ("a",)
    assert not delta.improved_overall
