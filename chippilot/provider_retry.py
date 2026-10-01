class RetryingProvider:
    def __init__(self,provider,max_retries=2): self.provider=provider; self.max_retries=max_retries
    def next_action(self,**kwargs):
        last=None
        for _ in range(self.max_retries+1):
            try: return self.provider.next_action(**kwargs)
            except Exception as exc: last=exc
        raise last
