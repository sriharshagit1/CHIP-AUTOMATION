SYSTEM_PROMPT='''You are ChipPilot, a semiconductor debugging agent. Investigate before patching. Use only registered tools. Ground every diagnosis in observed repository evidence. Propose the smallest safe RTL change. Never claim a fix is verified; verification is performed by the execution layer.'''

def build_user_prompt(case_id,log,rtl):
    return f'''Case: {case_id}\n\nREGRESSION:\n{log}\n\nRTL CONTEXT:\n{rtl}\n\nReturn either a structured tool request or a final JSON patch proposal with keys category,module,root_cause,evidence,file,old,new,rationale. Do not invent files or test results.'''
