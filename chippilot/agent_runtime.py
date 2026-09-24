from .controller import AgentController
from .planner import DebugPlanner
from .analyzer import diagnose
from .patcher import propose_fsm_patch
from .verify import verify_patch

class AgentRuntime:
    def __init__(self,max_tool_calls=8):
        self.tools=AgentController(max_tool_calls)
        self.planner=DebugPlanner()

    def run(self,log_path,rtl_path,tb_path):
        trace=[]
        for step in self.planner.plan(log_path,rtl_path,tb_path):
            result=self.tools.call(step.tool,*step.args)
            trace.append({'tool':step.tool,'result':str(result)[:1000]})
        log=self.tools.call('read_log',log_path)
        rtl=self.tools.call('read_rtl',rtl_path)
        failure=type('Failure',(),{'message':log})()
        diagnosis=diagnose(failure,rtl)
        patch=propose_fsm_patch(rtl_path)
        verification={'status':'NOT_RUN'}
        if patch['status']=='PROPOSED':
            verification=verify_patch(rtl_path,tb_path,patch['content'])
        return {'diagnosis':diagnosis.__dict__,'patch':patch,'verification':verification,'trace':trace+self.tools.trace()}
