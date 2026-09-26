import json, subprocess, sys
from pathlib import Path
from .ground_truth import CASES

TB={
 'FSM-001':('packet_controller.sv','tb_packet_controller.sv'),
 'WIDTH-001':('width_mismatch.sv','width_mismatch_tb.sv'),
 'RESET-001':('reset_bug.sv','reset_bug_tb.sv'),
 'COUNTER-001':('counter_bug.sv','counter_bug_tb.sv'),
 'HANDSHAKE-001':('handshake_bug.sv','handshake_bug_tb.sv'),
 'ASSERTION-001':('assertion_bug.sv','assertion_bug_tb.sv'),
 'LATCH-001':('latch_bug.sv','latch_bug_tb.sv'),
 'MUX-001':('mux_bug.sv','mux_bug_tb.sv'),
 'PARAM-001':('parameter_bug.sv','parameter_bug_tb.sv'),
 'CDC-001':('cdc_bug.sv','cdc_bug_tb.sv'),
}

def run():
 root=Path(__file__).parent/'cases'; results=[]
 for case,(rtl,tb) in TB.items():
  out=Path('/tmp')/(case+'.out')
  c=subprocess.run(['iverilog','-g2012','-o',str(out),str(root/rtl),str(root/tb)],capture_output=True,text=True)
  s=None if c.returncode else subprocess.run(['vvp',str(out)],capture_output=True,text=True)
  results.append({'id':case,'compile':'PASS' if c.returncode==0 else 'FAIL','simulation':'PASS' if s and s.returncode==0 else ('FAIL' if s else 'NOT_RUN'),'stdout':s.stdout if s else '','stderr':c.stderr if c.returncode else (s.stderr if s else '')})
 return results

if __name__=='__main__': print(json.dumps(run(),indent=2))
