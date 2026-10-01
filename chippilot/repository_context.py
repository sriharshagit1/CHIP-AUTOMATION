class RepositoryContext:
    def __init__(self,index,git,failures):
        self.index=index; self.git=git; self.failures=failures
    def build(self,log=''):
        f=self.failures.extract(log)
        return {
            'failure':f.__dict__,
            'rtl_index':self.index.build(),
            'recent_changes':self.git.changed_files(),
            'history':{path:self.git.log(path,5) for path in f.files},
        }
