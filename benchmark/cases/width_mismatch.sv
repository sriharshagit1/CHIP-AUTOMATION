module width_mismatch(input logic [7:0] data, output logic [7:0] out);
  logic [7:0] nibble;
  assign nibble = {4'b0, data[3:0]}; // intentional truncation bug
  assign out = nibble;
endmodule
