from pathlib import Path


def propose_fsm_patch(rtl_path: str):
    p=Path(rtl_path)
    original=p.read_text(encoding="utf-8")
    old="PROCESS: if (complete) state <= IDLE; // intentional regression bug"
    new="PROCESS: if (complete) state <= DONE; // ChipPilot proposed fix"
    if old not in original:
        return {"status":"NO_PATCH","reason":"Known V1 FSM pattern not found"}
    patched=original.replace(old,new,1)
    return {"status":"PROPOSED","file":str(p),"diff":{"before":old,"after":new},"content":patched}
