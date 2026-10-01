import unittest
from chippilot.provider_retry import RetryingProvider

class Failing:
    def __init__(self): self.n=0
    def next_action(self,**kwargs):
        self.n+=1
        if self.n<2: raise RuntimeError('transient')
        return {'action':'finish','evidence':['ok']}

class TestRetry(unittest.TestCase):
    def test_retry(self):
        p=Failing()
        self.assertEqual(RetryingProvider(p,2).next_action()['action'],'finish')
        self.assertEqual(p.n,2)

if __name__=='__main__':
    unittest.main()
