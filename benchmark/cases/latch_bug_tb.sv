module tb;
logic a=0,b=1,sel=1,y;
latch_bug dut(a,b,sel,y);
initial begin #1; sel=0; #1;
  if(y !== 1'b0) begin $display("FAIL: expected y=0 observed %b",y); $finish(1); end
  $display("PASS"); $finish(0);
end
endmodule
