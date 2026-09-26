from pathlib import Path
from .git_context import recent_commits, commit_diff
from .fixture_verify import verify

class RuntimeTools:
    def __init__(self,repo_root='benchmark/cases'):
        self.root=Path(repo_root).resolve()
    def read_rtl(self,path):
        p=(self.root/path).resolve()
        if self.root not in p.parents: raise PermissionError('path outside allowed repository')
        return {'path':str(p),'content':p.read_text(encoding='utf-8')}
    def git_history(self,limit=5): return recent_commits(str(self.root),int(limit))
    def git_diff(self,commit='HEAD'): return commit_diff(str(self.root),commit)
    def verify_case(self,case_id,patched_content): return verify(case_id,patched_content)
    def mapping(self): return {'read_rtl':self.read_rtl,'git_history':self.git_history,'git_diff':self.git_diff,'verify_case':self.verify_case}
