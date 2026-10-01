from chippilot.coverage_feedback import CoveragePoint, CoverageSnapshot
from chippilot.coverage_runner import CoverageRunner


class FakeSimulator:
    root = "."
    def run(self, sources, top, timeout=120):
        return {"status":"PASS"}


class FakeAdapter:
    def collect(self, workspace, **kwargs):
        return CoverageSnapshot((CoveragePoint("fsm", covered=2, total=2),))


def test_runner_accepts_improved_coverage():
    before = CoverageSnapshot((CoveragePoint("fsm", covered=1, total=2),))
    result = CoverageRunner(FakeSimulator(), FakeAdapter()).run(
        sources=["tb.sv"], top="tb", before=before
    )
    assert result["status"] == "ACCEPTED"
    assert result["coverage_after"] > result["coverage_before"]


class FailingSimulator(FakeSimulator):
    def run(self, sources, top, timeout=120):
        return {"status":"FAIL"}


def test_runner_requires_passing_simulation():
    before = CoverageSnapshot((CoveragePoint("fsm", covered=1, total=2),))
    result = CoverageRunner(FailingSimulator(), FakeAdapter()).run(
        sources=["tb.sv"], top="tb", before=before
    )
    assert result["status"] == "SIMULATION_NOT_PASS"
