module handshake_bug(input logic clk, rst, valid, ready, output logic accepted);
  always_ff @(posedge clk) begin
    if (rst) accepted <= 0;
    else accepted <= valid & ~ready; // intentional bug
  end
endmodule
