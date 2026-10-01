import subprocess

class GitContext:
    def __init__(self,root='.'): self.root=root
    def log(self,path=None,limit=10):
        cmd=['git','log','-n',str(limit),'--format=%H%x09%an%x09%s']
        if path: cmd += ['--',path]
        r=subprocess.run(cmd,cwd=self.root,text=True,capture_output=True)
        return r.stdout.strip().splitlines()
    def changed_files(self,base='HEAD~1'):
        r=subprocess.run(['git','diff','--name-only',base,'HEAD'],cwd=self.root,text=True,capture_output=True)
        return r.stdout.strip().splitlines()
