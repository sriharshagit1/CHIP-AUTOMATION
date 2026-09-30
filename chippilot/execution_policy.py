from dataclasses import dataclass

@dataclass
class ExecutionDecision:
    allowed: bool
    requires_approval: bool
    reason: str

class ExecutionPolicy:
    def __init__(self,allow_write=False,allow_external=False):
        self.allow_write=allow_write
        self.allow_external=allow_external

    def decide(self,action):
        write=action in {'modify_rtl','apply_patch','merge_pr'}
        external=action in {'run_eda','submit_cluster_job','access_lab_data'}
        if write and not self.allow_write:
            return ExecutionDecision(False,True,'design modification requires human approval')
        if external and not self.allow_external:
            return ExecutionDecision(False,True,'external execution requires explicit environment approval')
        return ExecutionDecision(True,False,'policy permits action')
