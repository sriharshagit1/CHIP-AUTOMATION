import argparse, json
from .v1_runtime import ChipPilotV1

def main():
    p=argparse.ArgumentParser(description='ChipPilot V1')
    p.add_argument('case_id',choices=['FSM-001','WIDTH-001','RESET-001','COUNTER-001','HANDSHAKE-001','ASSERTION-001','LATCH-001','MUX-001','PARAM-001','CDC-001'])
    p.add_argument('--report',default='evidence/chippilot-v1.json')
    args=p.parse_args(); result=ChipPilotV1().investigate(args.case_id,args.report); print(json.dumps(result,indent=2))
if __name__=='__main__': main()
