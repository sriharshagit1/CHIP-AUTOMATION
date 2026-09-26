module parameter_bug #(parameter WIDTH=8)(input logic [WIDTH-1:0] a, output logic [WIDTH-1:0] y);
assign y = a[7:0];
endmodule
