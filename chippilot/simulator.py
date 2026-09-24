import shutil, subprocess, tempfile
from pathlib import Path


def run_iverilog(rtl_path: str, tb_path: str, timeout: int = 10):
    iverilog = shutil.which("iverilog")
    vvp = shutil.which("vvp")
    if not iverilog or not vvp:
        return {"status":"SKIPPED","reason":"iverilog/vvp not installed"}
    with tempfile.TemporaryDirectory() as d:
        out = str(Path(d) / "sim.out")
        compile_run = subprocess.run([iverilog,"-g2012","-o",out,rtl_path,tb_path],capture_output=True,text=True,timeout=timeout)
        if compile_run.returncode != 0:
            return {"status":"FAIL","stage":"compile","stdout":compile_run.stdout,"stderr":compile_run.stderr}
        sim = subprocess.run([vvp,out],capture_output=True,text=True,timeout=timeout)
        return {"status":"PASS" if sim.returncode == 0 else "FAIL","stage":"simulation","stdout":sim.stdout,"stderr":sim.stderr}
