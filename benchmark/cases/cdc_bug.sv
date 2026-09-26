module cdc_bug(input logic clk, async_in, output logic sync_out);
always_ff @(posedge clk) sync_out <= async_in;
endmodule
