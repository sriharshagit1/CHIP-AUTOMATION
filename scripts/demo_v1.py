import json
from pathlib import Path
from chippilot.v1_runtime import ChipPilotV1

CASES=['WIDTH-001','RESET-001','COUNTER-001','HANDSHAKE-001']

def main():
    out=Path('evidence/demo'); out.mkdir(parents=True,exist_ok=True)
    pilot=ChipPilotV1()
    rows=[]
    for case in CASES:
        report=pilot.investigate(case,str(out/f'{case}.json'))
        rows.append({'case_id':case,'verdict':report['evidence']['verdict'],'verification':report['verification']['status']})
    (out/'summary.json').write_text(json.dumps({'cases':rows},indent=2),encoding='utf-8')
    print(json.dumps({'cases':rows},indent=2))
if __name__=='__main__': main()
