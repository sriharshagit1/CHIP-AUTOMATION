import unittest, json
from chippilot.api import Handler

class TestAPIContract(unittest.TestCase):
    def test_health_contract(self):
        self.assertTrue(hasattr(Handler,'do_GET'))
        self.assertTrue(hasattr(Handler,'do_POST'))

if __name__=='__main__': unittest.main()
