module width_mismatch(input logic [7:0] data, output logic [7:0] out);
  logic [3:0] nibble;
  assign nibble = data;
  assign out = {4'b0, nibble};
endmodule
