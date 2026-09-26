module tb;
logic clk=0,async_in=0,sync_out;
cdc_bug dut(clk,async_in,sync_out);
always #1 clk=~clk;
initial begin
 async_in=1; #2;
 if(sync_out !== 1'b0) begin $display("FAIL: expected synchronized latency, observed immediate propagation"); $finish(1); end
 $display("PASS"); $finish(0);
end
endmodule
