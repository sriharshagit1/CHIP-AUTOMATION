# End-to-end agent

`E2EAgent` connects a model provider to the bounded tool loop and repository tools.

The included `LocalRuleProvider` is only a credential-free pipeline test. It must not be used as evidence of LLM performance.

A real deployment supplies an implementation of the provider interface. The same tool registry, sandbox and verifier are then reused for model evaluation.
