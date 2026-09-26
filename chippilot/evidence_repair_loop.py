from .repair_context import build_feedback

class EvidenceRepairLoop:
    def __init__(self,agent,max_attempts=3): self.agent=agent; self.max_attempts=max_attempts
    def run(self,case_id,messages,verify_fn):
        attempts=[]
        for n in range(1,self.max_attempts+1):
            result=self.agent.run(messages); patch=result.get('patch') if isinstance(result,dict) else None
            if not patch:
                attempts.append({'attempt':n,'agent':result,'verification':{'status':'NO_PATCH'}}); return {'status':'NO_PATCH','attempts':attempts}
            verification=verify_fn(patch); attempts.append({'attempt':n,'agent':result,'verification':verification})
            if verification.get('status')=='VERIFIED': return {'status':'VERIFIED','attempts':attempts}
            messages=messages+[{'role':'tool','content':str(build_feedback(case_id,verification))}]
        return {'status':'RETRY_EXHAUSTED','attempts':attempts}
