class RegisteredTool:
    def __init__(self,name,description,runner):
        self.name=name
        self.description=description
        self._runner=runner
    def run(self,**kwargs):
        return self._runner(**kwargs)
