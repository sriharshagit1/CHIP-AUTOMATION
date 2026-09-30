from dataclasses import dataclass

@dataclass(frozen=True)
class Stage:
    name: str
    purpose: str
    maturity: str

DEFAULT_STAGES=(
    Stage('rtl','design source and structural reasoning','foundation'),
    Stage('verification','simulation, assertions, coverage and regression','foundation'),
    Stage('synthesis','mapping RTL into implementation structures','adapter'),
    Stage('sta','timing analysis and constraint reasoning','adapter'),
    Stage('dft','testability and manufacturing-test reasoning','adapter'),
    Stage('post_silicon','lab traces, logs and silicon failure correlation','adapter'),
)

class StageRegistry:
    def __init__(self,stages=DEFAULT_STAGES): self._stages={s.name:s for s in stages}
    def get(self,name): return self._stages[name]
    def all(self): return list(self._stages.values())
    def maturity(self): return {s.name:s.maturity for s in self._stages}
