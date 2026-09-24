import argparse
from pathlib import Path
from .log_parser import parse_failure, to_dict
from .analyzer import diagnose
from .evidence import write_report
from .patcher import propose_fsm_patch
from .verify import verify_patch

def main():
    p=argparse.ArgumentParser(prog="chippilot",description="Regression failure investigator")
    p.add_argument("log")
    p.add_argument("--rtl",default="examples/fsm/packet_controller.sv")
    p.add_argument("--tb",default="examples/fsm/tb_packet_controller.sv")
    p.add_argument("--report",default="evidence/report.json")
    p.add_argument("--verify",action="store_true")
    a=p.parse_args()
    failure=parse_failure(Path(a.log).read_text(encoding="utf-8"))
    rtl=Path(a.rtl).read_text(encoding="utf-8")
    diagnosis=diagnose(failure,rtl)
    patch=propose_fsm_patch(a.rtl)
    verification={"status":"NOT_RUN","reason":"Use --verify to execute the proposed patch safely."}
    if a.verify and patch["status"]=="PROPOSED":
        verification=verify_patch(a.rtl,a.tb,patch["content"])
    write_report(a.report,to_dict(failure),diagnosis.__dict__,verification)
    print("\nCHIPPILOT INVESTIGATION")
    print(f"Failure: {failure.category} | {failure.file}:{failure.line}")
    print(f"Root cause: {diagnosis.root_cause}")
    print(f"Confidence: {diagnosis.confidence:.0%}")
    print(f"Patch: {patch['status']}")
    print(f"Verification: {verification['status']}")
    if verification["status"]=="VERIFIED":
        print("VERIFIED: proposed patch passed the executable testbench.")
    print(f"Evidence: {a.report}")

if __name__ == "__main__":
    main()
