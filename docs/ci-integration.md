# CI integration

ChipPilot includes a manual GitHub Actions workflow that runs the investigation pipeline against repository artifacts.

The workflow checks out the repository, installs Icarus Verilog, installs ChipPilot, runs diagnosis plus isolated verification, and uploads a machine-readable evidence report.

It does not automatically push code or open pull requests. Automatic repository mutation should only be enabled after benchmark validation and explicit permissions.
