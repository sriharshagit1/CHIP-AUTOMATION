from .fingerprint import fingerprint

class FailureRetriever:
    def __init__(self,memory): self.memory=memory

    def find_similar(self,log,limit=5):
        fp=fingerprint(log)
        query=' '.join([fp.category,fp.module,fp.expected,fp.observed,fp.signal])
        hits=self.memory.search(query,limit=limit)
        return {'fingerprint':fp.to_dict(),'matches':[h.__dict__ for h in hits]}

    def investigation_context(self,log,limit=5):
        result=self.find_similar(log,limit)
        return ('FAILURE FINGERPRINT:\n'+str(result['fingerprint'])+
                '\nHISTORICAL MATCHES:\n'+str(result['matches']))
