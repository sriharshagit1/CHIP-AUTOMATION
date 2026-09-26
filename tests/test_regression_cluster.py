import unittest
from chippilot.regression_cluster import cluster_failures
class TestRegressionCluster(unittest.TestCase):
    def test_groups_similar_failures(self):
        rows=[{'id':'A','log':'packet_controller.sv:6 state ERROR expected DONE'},{'id':'B','log':'packet_controller.sv:8 state ERROR expected DONE'},{'id':'C','log':'fifo.sv:2 width ERROR'}]
        c=cluster_failures(rows)
        self.assertEqual(c[0]['count'],2)
        self.assertTrue(c[0]['shared_root_cause_hypothesis'])
if __name__=='__main__': unittest.main()
