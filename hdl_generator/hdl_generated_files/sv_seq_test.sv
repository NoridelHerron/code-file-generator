
// ===========================================================
// Project Name: 
// Description :
//
// File Name   : sv_seq_test.sv
// Dependencies:
// Author      : Hhjafhfd ahdhjdsj
// Date        : 2026-01-07 22:24:20
// ===========================================================
module sv_seq_test (
    
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
    
