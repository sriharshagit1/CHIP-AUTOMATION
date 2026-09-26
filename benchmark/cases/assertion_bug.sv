module assertion_bug(input logic clk, input logic req, output logic ack);
always_ff @(posedge clk) ack <= req;
endmodule
