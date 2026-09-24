module tb;
  logic clk=0,rst=0,d=0; logic q;
  reset_bug dut(clk,rst,d,q);
  always #1 clk=~clk;
  initial begin rst=1; #2;
    if(q !== 1'b0) begin $display("FAIL: expected q=0 observed q=%b",q); $finish(1); end
    $display("PASS"); $finish(0);
  end
endmodule
