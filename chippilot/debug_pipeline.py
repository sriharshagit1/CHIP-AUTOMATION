from .agent_runtime import AgentRuntime
from .result import DebugResult

def debug(log_path,rtl_path,tb_path):
    result=AgentRuntime().run(log_path,rtl_path,tb_path)
    verification=result['verification']
    status='VERIFIED' if verification.get('status')=='VERIFIED' else 'UNVERIFIED'
    evidence=[{'type':'tool_trace','items':result['trace']},{'type':'verification','data':verification}]
    return DebugResult(status,result['diagnosis'].get('root_cause',''),result['patch'].get('status','UNKNOWN'),verification.get('status','NOT_RUN'),evidence,result['trace'])
