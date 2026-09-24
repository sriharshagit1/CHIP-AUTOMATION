import re
from dataclasses import dataclass, asdict

@dataclass
class Failure:
    raw: str
    file: str | None
    line: int | None
    message: str
    category: str

def parse_failure(log: str) -> Failure:
    patterns = [
        (r"(?P<file>[\\w./-]+\\.(?:sv|v)):(?P<line>\\d+).*?(?P<msg>(?:ERROR|Error|error).*)", "simulation_error"),
        (r"(?P<file>[\\w./-]+\\.(?:sv|v)):(?P<line>\\d+).*?(?P<msg>expected.*?observed.*)", "assertion"),
    ]
    for pattern, category in patterns:
        m = re.search(pattern, log, re.S)
        if m:
            return Failure(log, m.group("file"), int(m.group("line")), m.group("msg").strip(), category)
    return Failure(log, None, None, log.strip().splitlines()[-1] if log.strip() else "No failure text", "unknown")

def to_dict(f: Failure):
    return asdict(f)
