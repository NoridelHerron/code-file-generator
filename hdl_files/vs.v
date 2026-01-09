
// ===========================================================
// Project Name: 
// Description :
//
// File Name   : vs.v
// Dependencies:
// Author      : skjdjkf
// Date        : 2026-01-09 10:47:02
// ===========================================================

module vs (
    
    input clk,
    input rst
    
);

// Add wire or reg here


always @(posedge clk or posedge rst) begin
    if (rst) begin
        // reset logic
    end else begin
        // logic here
    end
end
    
