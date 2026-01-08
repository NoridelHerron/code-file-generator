
// ===========================================================
// Project Name: 
// Description :
//
// File Name   : v_seq_test.v
// Dependencies:
// Author      :
// Date        : 2026-01-07 22:20:56
// ===========================================================
module v_seq_test (
    
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
    
