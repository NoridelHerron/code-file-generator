
// ============================================================
// Project Name: 
// Description :
//
// File Name   : verilog_s.v
// Dependencies:
// Author      : Noridel
// Date        : 2026-01-09 22:10:42
// ============================================================
`timescale 1ns / 1ps

module verilog_s (
    
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
    
