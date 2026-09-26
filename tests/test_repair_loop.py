import unittest
from chippilot.repair_loop import RepairLoop
class FakeAgent:
 def __init__(self): self.n=0
 def run(self,m): self.n+=1; return {'patch':{'new':str(self.n)}}
class TestRepairLoop(unittest.TestCase):
 def test_retries_until_verified(self):
  a=FakeAgent(); r=RepairLoop(a,3).run('X',[],lambda p:{'status':'VERIFIED' if p['new']=='2' else 'FAIL'})
  self.assertEqual(r['status'],'VERIFIED'); self.assertEqual(len(r['attempts']),2)
if __name__=='__main__': unittest.main()
