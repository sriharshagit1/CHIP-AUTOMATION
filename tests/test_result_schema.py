import unittest
from benchmark.result_schema import validate_run
class TestResultSchema(unittest.TestCase):
    def test_valid(self):
        run={'results':{'cases':[{'id':'X','attempts':[{'attempt':1,'agent_status':'PATCH_PROPOSED','patch':{},'verification':{'status':'VERIFIED'}}],'final_status':'VERIFIED','seconds':1.0}]}}
        self.assertEqual(validate_run(run),[])
if __name__=='__main__': unittest.main()
