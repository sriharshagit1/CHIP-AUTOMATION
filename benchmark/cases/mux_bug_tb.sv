module tb;
logic a=0,b=1,sel=0,y;
mux_bug dut(a,b,sel,y);
initial begin #1;
  if(y !== b) begin $display("FAIL: expected y=1 observed %b",y); $finish(1); end
  $display("PASS"); $finish(0);
end
endmodule
