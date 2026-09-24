from .memory import FailureMemory
from .git_context import recent_commits, changed_files, commit_diff

class EngineeringKnowledge:
    def __init__(self,memory=None): self.memory=memory or FailureMemory()

    def retrieve(self,root,query,commit='HEAD'):
        historical=self.memory.search(query,limit=5)
        return {
            'historical_failures':[r.__dict__ for r in historical],
            'recent_commits':recent_commits(root,5),
            'changed_files':changed_files(root,commit),
            'commit_diff':commit_diff(root,commit),
        }

    def build_context(self,data):
        return ('HISTORICAL FAILURES:\n'+str(data['historical_failures'])+
                '\nRECENT COMMITS:\n'+data['recent_commits']['stdout']+
                '\nCHANGED FILES:\n'+data['changed_files']['stdout']+
                '\nCOMMIT DIFF:\n'+data['commit_diff']['stdout'])
