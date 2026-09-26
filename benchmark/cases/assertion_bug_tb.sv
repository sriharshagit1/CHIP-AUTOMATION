module tb;
logic clk=0,req=0,ack;
assertion_bug dut(clk,req,ack);
always #1 clk=~clk;
initial begin
  req=1; #2;
  if(ack !== 1'b0) begin $display("FAIL: expected ack=0 observed %b",ack); $finish(1); end
  $display("PASS"); $finish(0);
end
endmodule
