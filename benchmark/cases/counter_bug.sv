module counter_bug(input logic clk, rst, enable, output logic [3:0] count);
  always_ff @(posedge clk) begin
    if (rst) count <= 0;
    else if (enable) count <= count + 2; // intentional off-by-one
  end
endmodule
