import subprocess, tempfile
from pathlib import Path

def verify_patch(rtl_path: str, tb_path: str, patched_content: str, timeout: int = 10):
    with tempfile.TemporaryDirectory(prefix="chippilot-") as d:
        root=Path(d)
        rtl=root/Path(rtl_path).name
        tb_src=Path(tb_path).read_text(encoding="utf-8")
        tb=root/Path(tb_path).name
        rtl.write_text(patched_content,encoding="utf-8")
        tb.write_text(tb_src,encoding="utf-8")
        out=root/"sim.out"
        compile_run=subprocess.run(["iverilog","-g2012","-o",str(out),str(rtl),str(tb)],capture_output=True,text=True,timeout=timeout)
        if compile_run.returncode:
            return {"status":"FAIL","stage":"compile","stdout":compile_run.stdout,"stderr":compile_run.stderr}
        sim=subprocess.run(["vvp",str(out)],capture_output=True,text=True,timeout=timeout)
        return {"status":"VERIFIED" if sim.returncode==0 else "FAIL","stage":"simulation","stdout":sim.stdout,"stderr":sim.stderr}
