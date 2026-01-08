# ============================================================
# vhdl_helpers.py
# Description:
#
# Author: Noridel Herron
# Date  : 2026-01-07 11:04:53
# ============================================================

from function_helpers import (Print_Header, Print_Package_Body)

# ==============================================================================
# VHDL library
# ==============================================================================
def Print_Lib():
    return """
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- CUSTOMIZED PACKAGE
-- library work;
-- use work.xxxxxxx.all;
"""

# ==============================================================================
# Combine the necessary content for the module
# ==============================================================================
def Get_Complete_VHDL(author, entity_name, ports, body, file_ext):
    lib         = Print_Lib()
    header      = Print_Header(entity_name, author, "vhdl", file_ext)
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
"""
    return complete

# ==============================================================================
# Combine the necessary content for the package
# ==============================================================================
def Get_Package_VHDL(package_name, author, file_ext):
    lib      = Print_Lib()
    header   = Print_Header(package_name + "_pkg", author, "vhdl", file_ext)
    body     = Print_Package_Body(package_name, "vhdl")
    complete = f"""
{header}
{lib}{body}
"""
    return complete

# ==============================================================================