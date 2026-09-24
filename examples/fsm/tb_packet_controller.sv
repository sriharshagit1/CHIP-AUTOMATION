module tb;
  logic clk=0, rst=1, start=0, complete=0;
  logic done;
  packet_controller dut(.clk(clk),.rst(rst),.start(start),.complete(complete),.done(done));
  always #5 clk=~clk;
  initial begin
    #12 rst=0; #10 start=1; #10 start=0; #20 complete=1; #10 complete=0;
    if (!done) begin $display("FAIL: expected DONE observed IDLE"); $fatal; end
    $display("PASS: completion reached DONE");
    #10 $finish;
  end
endmodule
