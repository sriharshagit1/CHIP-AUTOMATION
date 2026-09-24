module reset_bug(input logic clk, rst, input logic d, output logic q);
  always_ff @(posedge clk) begin
    if (rst) q <= 1'b1; // intentional bug: expected reset value is 0
    else q <= d;
  end
endmodule
