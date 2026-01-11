
## ============================================================
## Project Name: 
## Description :
##
## File Name   : file_content.py
## Dependencies:
## Author      : Noridel Herron
## Date        : 2026-01-10 09:37:36
## ============================================================

from utilities.shared_helpers import (
    Print_Sep
)

## ============================================================
##  Function/s Only
## ============================================================

## VHDL library
def Print_Lib():
    vhdl_lib = """
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- CUSTOMIZED PACKAGE
-- library work;
-- use work.xxxxxxx.all;
"""
    # **************
    return vhdl_lib
    # **************

## ********************************************

## VHDL
def Get_VHDL_Content( is_package  = False, 
                      header      = "", 
                      body        = "",
                      entity_name = "",
                      ports       = "" ):
    
    lib = Print_Lib()
    sep = Print_Sep()
    
    if is_package:
        complete = f"""
{header}
{lib}{body}
"""
    # ***********************************
    else: 
        complete    = f"""{header}
{lib}
entity {entity_name} is
    port (
{ports}
    );
end {entity_name};

architecture rtl of {entity_name} is

begin
{body}
end rtl;

-- {sep}
-- END OF FILE
-- {sep}
"""
    # *************
    return complete
    # *************

## ********************************************

## Verilog
def Get_Verilog_Content( is_package  = False, 
                         module_name = "",
                         header      = "", 
                         body        = "",
                         ports       = "", 
                         note        = ""):
    
    complete = ""
    sep      = Print_Sep()

    if is_package:
        complete = f"""
{header}{body}
"""
    # *****************
    else:
       complete = f"""
{header}
`timescale 1ns / 1ps

module {module_name} (
    {ports}
);

    {note}
{body}
// {sep}
// END OF FILE
// {sep}
""" 
       
    # **************
    return complete
    # **************
    
## ============================================================
##  End of File
## ============================================================

