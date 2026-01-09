
// ===========================================================
// Project Name: 
// Description :
//
// File Name   : svs.sv
// Dependencies:
// Author      : Nor
// Date        : 2026-01-09 11:12:40
// ===========================================================

module svs (
    
    input clk,
    input rst
    
);

// Add logic signal/s here


always_ff @(posedge clk or posedge rst) begin
    if (rst) begin
        // reset logic
    end else begin
        // logic here
    end
end
    
