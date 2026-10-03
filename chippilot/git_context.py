import subprocess

class GitContext:
    def __init__(self,root="."): self.root=root
    def log(self,path=None,limit=10):
        cmd=["git","log","-n",str(limit),"--format=%H%x09%an%x09%s"]
        if path: cmd += ["--",path]
        r=subprocess.run(cmd,cwd=self.root,text=True,capture_output=True)
        return r.stdout.strip().splitlines()
    def changed_files(self,base="HEAD~1"):
        return changed_files(self.root,base)

def _git(root,args):
    return {"returncode":(r:=subprocess.run(["git",*args],cwd=root,text=True,capture_output=True)).returncode,"stdout":r.stdout,"stderr":r.stderr}

def recent_commits(root=".",limit=10):
    return _git(root,["log","-n",str(limit),"--format=%H%x09%an%x09%s"])

def changed_files(root=".",base="HEAD~1"):
    result=_git(root,["diff","--name-only",base,"HEAD"])
    if result["returncode"] != 0:
        result=_git(root,["diff","--name-only","HEAD"])
    return result

def commit_diff(root=".",commit="HEAD"):
    return _git(root,["show","--stat","--oneline",commit])
