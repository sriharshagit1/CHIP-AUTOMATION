from dataclasses import dataclass
import hashlib

@dataclass
class Patch:
    file: str
    before: str
    after: str
    rationale: str = ''

    @property
    def id(self):
        raw=self.file+'\n'+self.before+'\n'+self.after
        return hashlib.sha256(raw.encode()).hexdigest()[:16]

    def apply(self,text):
        if self.before not in text:
            raise ValueError('patch context not found')
        return text.replace(self.before,self.after,1)

    def diff(self):
        return {'patch_id':self.id,'file':self.file,'before':self.before,'after':self.after,'rationale':self.rationale}
