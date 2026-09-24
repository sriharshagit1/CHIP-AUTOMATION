module tb;
  logic [7:0] data; logic [7:0] out;
  width_mismatch dut(data,out);
  initial begin data=8'hAB; #1;
    if(out !== 8'hAB) begin $display("FAIL: expected AB observed %h",out); $finish(1); end
    $display("PASS"); $finish(0);
  end
endmodule
