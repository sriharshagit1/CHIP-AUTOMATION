import argparse, json
from pathlib import Path
from .log_parser import parse_failure, to_dict
from .analyzer import diagnose
from .evidence import write_report

def main():
    p=argparse.ArgumentParser(prog="chippilot",description="Regression failure investigator")
    p.add_argument("log",help="path to regression log")
    p.add_argument("--rtl",default="examples/fsm/packet_controller.sv")
    p.add_argument("--report",default="evidence/report.json")
    a=p.parse_args()
    log=Path(a.log).read_text(encoding="utf-8")
    rtl=Path(a.rtl).read_text(encoding="utf-8")
    failure=parse_failure(log)
    diagnosis=diagnose(failure,rtl)
    verification={"status":"NOT_RUN","reason":"V1 is diagnosis-first; simulator integration is isolated for safe execution."}
    write_report(a.report,to_dict(failure),diagnosis.__dict__,verification)
    print("\nCHIPPILOT INVESTIGATION")
    print(f"Failure: {failure.category} | {failure.file}:{failure.line}")
    print(f"Root cause: {diagnosis.root_cause}")
    print(f"Confidence: {diagnosis.confidence:.0%}")
    print(f"Suggested action: {diagnosis.suggested_change}")
    print(f"Evidence: {a.report}")

if __name__ == "__main__": main()
