import unittest, tempfile
from pathlib import Path
from chippilot.dependency_graph import build_graph, reverse_dependents
class TestDependencyGraph(unittest.TestCase):
    def test_graph(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d,'child.sv').write_text('module child; endmodule')
            Path(d,'top.sv').write_text('module top; child u(); endmodule')
            g=build_graph(d)
            self.assertIn('child',g['edges']['top'])
            self.assertEqual(reverse_dependents(g,'child'),['top'])
if __name__=='__main__': unittest.main()
