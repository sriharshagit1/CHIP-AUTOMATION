from .tool_adapter import RegisteredTool
from .simulator import Simulator

def simulator_tool(root='.'):
    sim=Simulator(root)
    return RegisteredTool('sim.run','Run a bounded Verilator simulation',lambda sources,top,timeout=120:sim.run(sources,top,timeout))
