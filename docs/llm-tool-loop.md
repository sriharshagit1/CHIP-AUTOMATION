# LLM tool loop

The model-facing protocol uses structured tool requests.

Example:

    {"action":"read_rtl","arguments":{"path":"packet_controller.sv","start":1,"end":80}}

ChipPilot validates the request, executes only registered tools, records the result, and returns the observation to the reasoning layer.

The model is not granted arbitrary shell access. Verification remains a separate controlled execution path.
