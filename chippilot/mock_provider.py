class ScriptedProvider:
    def __init__(self,decisions): self.decisions=list(decisions); self.i=0
    def next_action(self,**_):
        if self.i>=len(self.decisions): return {'action':'finish','evidence':['script exhausted']}
        x=self.decisions[self.i]; self.i+=1; return x
