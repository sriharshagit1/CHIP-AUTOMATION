from pathlib import Path
import shutil
import subprocess
import tempfile

class Simulator:
    def __init__(self,root='.'):
        self.root=Path(root).resolve()
        self.verilator=shutil.which('verilator')

    def available(self):
        return bool(self.verilator)

    def run(self,sources,top,timeout=120):
        if not self.verilator:
            return {'status':'UNAVAILABLE','reason':'verilator not installed'}
        src=[str((self.root/p).resolve()) for p in sources]
        with tempfile.TemporaryDirectory(prefix='chippilot-') as td:
            exe=Path(td)/'sim'
            cmd=[self.verilator,'--binary','--timing','--top-module',top,'-o',str(exe),*src]
            try:
                build=subprocess.run(cmd,cwd=self.root,text=True,capture_output=True,timeout=timeout)
                if build.returncode:
                    return {'status':'COMPILE_FAIL','stdout':build.stdout[-4000:],'stderr':build.stderr[-4000:]}
                run=subprocess.run([str(exe)],cwd=self.root,text=True,capture_output=True,timeout=timeout)
                return {'status':'PASS' if run.returncode==0 else 'FAIL','returncode':run.returncode,'stdout':run.stdout[-4000:],'stderr':run.stderr[-4000:]}
            except subprocess.TimeoutExpired:
                return {'status':'TIMEOUT'}
