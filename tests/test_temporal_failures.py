import unittest
from chippilot.temporal_failures import parse_timestamped_failures, primary_candidates
class TestTemporalFailures(unittest.TestCase):
    def test_orders_by_timestamp(self):
        e=parse_timestamped_failures([{'id':'B','log':'[2.0] x.sv:9 ERROR'}, {'id':'A','log':'[1.0] x.sv:4 ERROR'}])
        self.assertEqual(primary_candidates(e)[0]['test_id'],'A')
        self.assertIn('causal confirmation',primary_candidates(e)[0]['reason'])
if __name__=='__main__': unittest.main()
