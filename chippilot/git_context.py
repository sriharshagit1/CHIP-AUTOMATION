import subprocess
from pathlib import Path

def run_git(root,args):
    p=subprocess.run(['git','-C',root,*args],capture_output=True,text=True,timeout=10)
    return {'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}

def recent_commits(root,limit=5):
    return run_git(root,['log',f'-{limit}','--oneline','--decorate'])

def changed_files(root,commit='HEAD'):
    return run_git(root,['diff-tree','--no-commit-id','--name-only','-r',commit])

def commit_diff(root,commit='HEAD'):
    return run_git(root,['show','--format=fuller','--stat','--patch',commit])

def blame_lines(root,path,start=1,end=50):
    return run_git(root,['blame','-L',f'{start},{end}','--',path])
