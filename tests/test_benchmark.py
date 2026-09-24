import unittest
from chippilot.benchmark import summary

class TestBenchmark(unittest.TestCase):
    def test_catalog(self):
        s=summary()
        self.assertGreaterEqual(s["total"],10)
        self.assertGreaterEqual(s["implemented"],1)

if __name__=="__main__":
    unittest.main()
