module tb;
  logic clk=0,rst=1,enable=0; logic [3:0] count;
  counter_bug dut(clk,rst,enable,count);
  always #1 clk=~clk;
  initial begin #2; rst=0; enable=1; #2;
    if(count !== 4'd1) begin $display("FAIL: expected count=1 observed %0d",count); $finish(1); end
    $display("PASS"); $finish(0);
  end
endmodule
