module tb;
logic [15:0] a=16'h1234,y;
parameter_bug #(.WIDTH(16)) dut(a,y);
initial begin #1;
  if(y !== a) begin $display("FAIL: expected y=1234 observed %h",y); $finish(1); end
  $display("PASS"); $finish(0);
end
endmodule
