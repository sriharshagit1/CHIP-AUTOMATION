import unittest
from chippilot.engineering_plan import EngineeringPlan
from chippilot.eda_tooling import EDATool, EDAToolCatalog
from chippilot.knowledge_graph import EngineeringKnowledgeGraph

class TestVisionFoundations(unittest.TestCase):
    def test_plan(self):
        p=EngineeringPlan('debug silicon issue'); p.add('rtl','inspect RTL','repo'); p.add('sta','analyze timing','sta'); p.require_approval('apply RTL patch')
        self.assertEqual(p.approval_points,['apply RTL patch'])
    def test_catalog(self):
        c=EDAToolCatalog(); c.register(EDATool('sim','verification','simulation',lambda:None))
        self.assertEqual(c.for_stage('verification')[0].name,'sim')
    def test_graph(self):
        g=EngineeringKnowledgeGraph(); g.add_node('x','failure'); g.add_node('y','commit'); g.link('x','caused_by','y')
        self.assertEqual(g.neighbors('x','caused_by'),['y'])
if __name__=='__main__': unittest.main()
