# ChipPilot API

V1 includes a local HTTP service for integration testing.

## Health

`GET /health`

## Investigate

`POST /investigate`

Request:

    {"log_path":"examples/fsm/regression.log","rtl_path":"examples/fsm/packet_controller.sv","tb_path":"examples/fsm/tb_packet_controller.sv"}

The response contains status, root cause, patch status, verification status, evidence and tool trace.

The current API intentionally accepts local repository paths. A production version should use authenticated repository IDs or uploaded artifacts instead of arbitrary filesystem paths.
