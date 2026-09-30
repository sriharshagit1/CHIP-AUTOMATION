from dataclasses import dataclass

@dataclass(frozen=True)
class EngineeringObjective:
    request: str
    success_conditions: tuple[str,...]
    constraints: tuple[str,...]=()

    def to_prompt(self):
        return {'request':self.request,'success_conditions':list(self.success_conditions),'constraints':list(self.constraints)}
