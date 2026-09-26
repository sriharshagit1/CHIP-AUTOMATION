import subprocess, json
from pathlib import Path
from .extended_fixtures import CASES

def run():
 results=[]
 root=Path(__file__).parent
 for case,rtl,tb in CASES:
  out=Path('/tmp')/(case+'.out')
  c=subprocess.run(['iverilog','-g2012','-o',str(out),str(root/rtl),str(root/tb)],capture_output=True,text=True)
  if c.returncode: results.append({'id':case,'compile':'FAIL','simulation':'NOT_RUN','stderr':c.stderr}); continue
  s=subprocess.run(['vvp',str(out)],capture_output=True,text=True)
  results.append({'id':case,'compile':'PASS','simulation':'PASS' if s.returncode==0 else 'FAIL','stdout':s.stdout})
 return results

if __name__=='__main__': print(json.dumps(run(),indent=2))
