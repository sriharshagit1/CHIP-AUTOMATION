import subprocess, sys
from pathlib import Path

CASES=[
 ("WIDTH-001","width_mismatch.sv","width_mismatch_tb.sv"),
 ("RESET-001","reset_bug.sv","reset_bug_tb.sv"),
 ("COUNTER-001","counter_bug.sv","counter_bug_tb.sv"),
 ("HANDSHAKE-001","handshake_bug.sv","handshake_bug_tb.sv"),
]

def run():
    results=[]
    for case,rtl,tb in CASES:
        out=Path("/tmp")/(case+".out")
        p=subprocess.run(["iverilog","-g2012","-o",str(out),str(Path(__file__).parent/rtl),str(Path(__file__).parent/tb)],capture_output=True,text=True)
        if p.returncode:
            results.append({"id":case,"compile":"FAIL","simulation":"NOT_RUN","stderr":p.stderr}); continue
        s=subprocess.run(["vvp",str(out)],capture_output=True,text=True)
        results.append({"id":case,"compile":"PASS","simulation":"PASS" if s.returncode==0 else "FAIL","stdout":s.stdout})
    return results

if __name__=="__main__":
    import json
    print(json.dumps(run(),indent=2))
