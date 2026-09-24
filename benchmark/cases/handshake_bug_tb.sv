module tb;
  logic clk=0,rst=1,valid=0,ready=0; logic accepted;
  handshake_bug dut(clk,rst,valid,ready,accepted);
  always #1 clk=~clk;
  initial begin #2; rst=0; valid=1; ready=1; #2;
    if(accepted !== 1'b1) begin $display("FAIL: expected accepted=1 observed %b",accepted); $finish(1); end
    $display("PASS"); $finish(0);
  end
endmodule
