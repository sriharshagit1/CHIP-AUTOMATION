class VerificationGate:
    REQUIRED=('compile','target','regression')
    def evaluate(self,checks):
        missing=[x for x in self.REQUIRED if checks.get(x) is not True]
        return {'status':'VERIFIED' if not missing else 'NOT_VERIFIED','missing':missing}
