from dataclasses import dataclass
from .log_parser import Failure

@dataclass
class Diagnosis:
    root_cause: str
    confidence: float
    suggested_change: str


def diagnose(failure: Failure, rtl: str) -> Diagnosis:
    text = rtl.lower()
    if "state" in text and "done" in text and "idle" in text:
        return Diagnosis(
            "FSM completion transition does not assert DONE before returning to IDLE.",
            0.86,
            "Inspect the completion condition and make the terminal transition explicit before IDLE."
        )
    if "assert" in failure.message.lower():
        return Diagnosis("An RTL assertion failed; inspect the referenced signal transition and preceding clock cycle.",0.62,"Review the failing assertion and the driving sequential logic.")
    return Diagnosis("The available evidence is insufficient for a deterministic root-cause classification.",0.25,"Collect the full regression log, RTL context, and recent Git diff.")
