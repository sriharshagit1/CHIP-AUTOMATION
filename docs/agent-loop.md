# ChipPilot agent loop

The model proposes actions; the runtime owns execution.

1. Provider receives the objective, context, history and registered-tool manifest.
2. Provider proposes one structured action.
3. Runtime validates and executes the registered tool.
4. Tool output becomes new context.
5. The provider may re-plan.
6. Completion is accepted only when evidence is supplied.
7. Step budgets and tool errors terminate the run safely.

This separation lets the same execution layer work with different model providers and keeps verification outside the model's authority.
