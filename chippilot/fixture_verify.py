import subprocess, tempfile
from pathlib import Path

CASES={'WIDTH-001':('width_mismatch.sv','width_mismatch_tb.sv'),'RESET-001':('reset_bug.sv','reset_bug_tb.sv'),'COUNTER-001':('counter_bug.sv','counter_bug_tb.sv'),'HANDSHAKE-001':('handshake_bug.sv','handshake_bug_tb.sv')}

def verify(case_id,patched_content,fixture_dir='benchmark/cases'):
    rtl_name,tb_name=CASES[case_id]
    with tempfile.TemporaryDirectory() as d:
        root=Path(d); rtl=root/rtl_name; tb=root/tb_name
        rtl.write_text(patched_content,encoding='utf-8'); tb.write_text((Path(fixture_dir)/tb_name).read_text(encoding='utf-8'),encoding='utf-8')
        out=root/'sim.out'
        c=subprocess.run(['iverilog','-g2012','-o',str(out),str(rtl),str(tb)],capture_output=True,text=True,timeout=10)
        if c.returncode: return {'status':'FAIL','stage':'compile','stderr':c.stderr}
        s=subprocess.run(['vvp',str(out)],capture_output=True,text=True,timeout=10)
        return {'status':'VERIFIED' if s.returncode==0 else 'FAIL','stage':'simulation','stdout':s.stdout,'stderr':s.stderr}
