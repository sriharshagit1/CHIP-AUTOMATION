import unittest
from chippilot.orchestrator import EngineeringOrchestrator
from chippilot.eda_tooling import EDAToolCatalog
from chippilot.stage_registry import StageRegistry
from chippilot.execution_policy import ExecutionPolicy

class TestOrchestrator(unittest.TestCase):
    def test_plan_has_approval_boundary(self):
        o=EngineeringOrchestrator(EDAToolCatalog())
        p=o.plan('debug timing regression',['rtl','sta'])
        self.assertEqual(p.approval_points,['merge_or_apply_design_change'])
    def test_stages_are_explicit(self):
        self.assertEqual([s.name for s in StageRegistry().all()],['rtl','verification','synthesis','sta','dft','post_silicon'])
    def test_policy_blocks_writes_by_default(self):
        d=ExecutionPolicy().decide('modify_rtl')
        self.assertFalse(d.allowed); self.assertTrue(d.requires_approval)
if __name__=='__main__': unittest.main()
