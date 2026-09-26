module mux_bug(input logic a,b,sel, output logic y);
assign y = sel ? a : a;
endmodule
