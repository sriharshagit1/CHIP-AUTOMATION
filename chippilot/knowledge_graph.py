from collections import defaultdict

class EngineeringKnowledgeGraph:
    def __init__(self): self.nodes={}; self.edges=defaultdict(set)
    def add_node(self,node_id,kind,**attrs): self.nodes[node_id]={'kind':kind,**attrs}
    def link(self,a,relation,b): self.edges[a].add((relation,b))
    def neighbors(self,node_id,relation=None):
        return [b for r,b in self.edges[node_id] if relation is None or r==relation]
    def export(self):
        return {'nodes':self.nodes,'edges':{k:list(v) for k,v in self.edges.items()}}
