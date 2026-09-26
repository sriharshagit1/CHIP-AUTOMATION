import json, unittest
from unittest.mock import patch
from chippilot.http_provider import SimpleJSONProvider
class Resp:
    def read(self): return json.dumps({'output':'{"action":"FINAL","arguments":{}}'}).encode()
    def __enter__(self): return self
    def __exit__(self,*a): pass
class TestHTTPProvider(unittest.TestCase):
    @patch('chippilot.http_provider.urlopen',return_value=Resp())
    def test_contract(self,m):
        p=SimpleJSONProvider('https://example.invalid'); out=p.generate([],[]); self.assertIn('FINAL',out); m.assert_called_once()
if __name__=='__main__': unittest.main()
