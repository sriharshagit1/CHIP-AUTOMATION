from chippilot.coverage_feedback import CoveragePoint, CoverageSnapshot
from chippilot.eda_execution import EDAExecutionAdapter
from chippilot.evidence import EvidenceStore
from chippilot.execution_policy import ExecutionPolicy
from chippilot.uvm_context import UVMContext, UVMSequence
from chippilot.uvm_execution import UVMExecutionPlanner
from chippilot.verification_dispatch import VerificationDispatcher
from chippilot.verification_execution import VerificationExecutionPlanner
from chippilot.verification_planner import VerificationPlanner
from chippilot.verification_run import VerificationRunOrchestrator

def make_runner(tmp_path):
    return VerificationRunOrchestrator(VerificationPlanner(max_candidates=1), VerificationExecutionPlanner(UVMExecutionPlanner()), VerificationDispatcher(EDAExecutionAdapter()), EvidenceStore(tmp_path))

def test_run_has_single_id_and_persists_evidence(tmp_path):
    r=make_runner(tmp_path).run(objective='cover fsm',coverage=CoverageSnapshot((CoveragePoint('fsm',covered=1,total=2),)),uvm_context=UVMContext(tests=('smoke_test',),sequences=(UVMSequence('seq'),),confidence='medium'),simulator='vcs',binary='./simv',policy=ExecutionPolicy(allow_external=True))
    assert r.run_id and r.final_status=='DRY_RUN'
    assert any(e['kind']=='evidence_saved' for e in r.events)

def test_low_confidence_is_blocked(tmp_path):
    r=make_runner(tmp_path).run(objective='cover',coverage=CoverageSnapshot((CoveragePoint('fsm',covered=1,total=2),)),uvm_context=UVMContext(confidence='low'),simulator='vcs',binary='./simv',policy=ExecutionPolicy())
    assert r.final_status=='BLOCKED'
