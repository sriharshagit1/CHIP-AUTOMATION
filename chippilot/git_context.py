import subprocess

class GitContext:
    def __init__(self,root="."): self.root=root
    def log(self,path=None,limit=10):
        return subprocess.run(["git","log","-n",str(limit),"--format=%H%x09%an%x09%s"]+([ "--",path] if path else []),cwd=self.root,text=True,capture_output=True).stdout.strip().splitlines()
    def changed_files(self,base="HEAD~1"):
        return subprocess.run(["git","diff","--name-only",base,"HEAD"],cwd=self.root,text=True,capture_output=True).stdout.strip().splitlines()

def _git(root,args):
    r=subprocess.run(["git",*args],cwd=root,text=True,capture_output=True)
    return {"returncode":r.returncode,"stdout":r.stdout,"stderr":r.stderr}

def recent_commits(root="."):
    return _git(root,["log","-n","10","--format=%H%x09%an%x09%s"])

def changed_files(root="."):
    return _git(root,["diff","--name-only","HEAD~1","HEAD"])

def commit_diff(root=".",commit="HEAD"):
    return _git(root,["show","--stat","--oneline",commit])
