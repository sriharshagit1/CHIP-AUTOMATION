module latch_bug(input logic a,b,sel, output logic y);
always_comb begin
  if(sel) y=a;
end
endmodule
