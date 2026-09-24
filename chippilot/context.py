from pathlib import Path

def collect_context(log_path, rtl_path, max_chars=12000):
    log=Path(log_path).read_text(encoding="utf-8")
    rtl=Path(rtl_path).read_text(encoding="utf-8")
    return {"log":log[-max_chars:],"rtl":rtl[:max_chars],"files":[str(log_path),str(rtl_path)]}

def build_context_prompt(context):
    return f"""Repository debugging context.
REGRESSION LOG:
{context["log"]}

RTL:
{context["rtl"]}

Determine the earliest actionable failure, affected logic, likely root cause, and the smallest safe change. Do not claim verification without executable evidence."""
