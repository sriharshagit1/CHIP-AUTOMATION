class ToolRegistry:
    def __init__(self): self._tools={}
    def register(self,name,tool):
        if name in self._tools: raise ValueError(f'duplicate tool: {name}')
        self._tools[name]=tool
    def get(self,name): return self._tools[name]
    def names(self): return sorted(self._tools)
    def describe(self): return {n:getattr(t,'description',t.__class__.__name__) for n,t in self._tools.items()}
