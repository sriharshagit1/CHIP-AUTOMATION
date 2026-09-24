module packet_controller(input logic clk, rst, start, complete, output logic done);
  typedef enum logic [1:0] {IDLE, PROCESS, DONE} state_t;
  state_t state;
  always_ff @(posedge clk) begin
    if (rst) state <= IDLE;
    else case (state)
      IDLE:    if (start) state <= PROCESS;
      PROCESS: if (complete) state <= IDLE; // intentional regression bug
      DONE:    state <= IDLE;
    endcase
  end
  assign done = (state == DONE);
endmodule
