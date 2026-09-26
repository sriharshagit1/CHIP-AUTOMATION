# Blind evaluation protocol

1. Give the agent only the public case view: RTL, regression/testbench artifacts, and case ID.
2. Keep `ground_truth.py` outside the agent context.
3. Record the agent's diagnosis and candidate patch before verification.
4. Apply the candidate in an isolated workspace.
5. Run compile, targeted test, and regression.
6. Score exact patch agreement separately from verified behavioral success.
7. Report failures and unsupported cases rather than silently excluding them.

This separation reduces benchmark leakage and distinguishes finding the exact reference patch from producing any behaviorally verified repair.
