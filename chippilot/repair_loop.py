from .patch import Patch
from .verification import VerificationGate

class RepairLoop:
    def __init__(self,max_attempts=3):
        self.max_attempts=max_attempts
        self.gate=VerificationGate()

    def evaluate(self,attempts):
        history=[]
        for i,attempt in enumerate(attempts[:self.max_attempts],1):
            checks=attempt.get('checks',{})
            verdict=self.gate.evaluate(checks)
            event={'attempt':i,'patch_id':attempt.get('patch_id'),'verification':verdict,'reason':attempt.get('reason','')}
            history.append(event)
            if verdict['status']=='VERIFIED':
                return {'status':'VERIFIED','attempts':history,'accepted_patch':attempt}
        return {'status':'NOT_VERIFIED','attempts':history,'accepted_patch':None}
