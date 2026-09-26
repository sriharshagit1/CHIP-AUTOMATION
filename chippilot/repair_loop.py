class RepairLoop:
    def __init__(self,agent,max_attempts=3): self.agent=agent; self.max_attempts=max_attempts

    def run(self,case_id,initial_messages,verify_fn):
        messages=list(initial_messages); attempts=[]
        for attempt in range(1,self.max_attempts+1):
            result=self.agent.run(messages)
            attempts.append({'attempt':attempt,'agent':result})
            patch=result.get('patch') if isinstance(result,dict) else None
            if not patch: return {'status':'NO_PATCH','attempts':attempts}
            verification=verify_fn(patch)
            attempts[-1]['verification']=verification
            if verification.get('status')=='VERIFIED': return {'status':'VERIFIED','attempts':attempts}
            feedback={'role':'tool','content':str({'verification_failure':verification,'instruction':'Revise using only observed verification evidence. Do not claim success.'})}
            messages=messages+[{'role':'assistant','content':str(result)},feedback]
        return {'status':'RETRY_EXHAUSTED','attempts':attempts}
