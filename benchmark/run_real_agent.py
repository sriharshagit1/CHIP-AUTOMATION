import json, os
from pathlib import Path
from chippilot.http_provider import OpenAICompatibleProvider
from chippilot.provider_retry import RetryingProvider
from chippilot.agent_runtime import EngineeringAgentRuntime
from chippilot.tool_registry import ToolRegistry
from chippilot.tool_adapter import RegisteredTool
from chippilot.repository_adapter import RepositoryAdapter
from .metrics import summarize

def main():
    root=Path(os.getenv('CHIPILOT_REPO','.')).resolve()
    repo=RepositoryAdapter(root)
    registry=ToolRegistry()
    registry.register('repo.list',RegisteredTool('repo.list','List source files',lambda:repo.list_files()))
    registry.register('repo.read',RegisteredTool('repo.read','Read a repository file',lambda path:repo.read(path)))
    runtime=EngineeringAgentRuntime(RetryingProvider(OpenAICompatibleProvider(),2),registry,max_steps=int(os.getenv('CHIPILOT_MAX_STEPS','8')))
    rows=[]
    for case in json.loads(Path('benchmark/cases.json').read_text(encoding='utf-8')):
        try:
            _,state=runtime.run(case['objective'],case.get('stages',['rtl','verification']))
            rows.append({'id':case['id'],'status':'VERIFIED' if state.completed else 'FAILED','steps':len(state.steps),'seconds':0.0,'reason':state.reason})
        except Exception as exc:
            rows.append({'id':case['id'],'status':'ERROR','steps':0,'seconds':0.0,'reason':str(exc)})
    output={'benchmark_version':'real-agent-v1','model':os.getenv('CHIPILOT_LLM_MODEL','unset'),'summary':summarize(rows),'cases':rows}
    out=Path('evidence/experiments/real-agent-latest.json')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(output,indent=2),encoding='utf-8')
    print(json.dumps(output,indent=2))
    return output

if __name__=='__main__':
    main()
