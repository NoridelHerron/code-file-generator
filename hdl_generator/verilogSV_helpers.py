# ============================================================
# verilogSV_helpers.py
# Description:
#
# Author: Noridel Herron
# Date  : 2026-01-07 11:57:25
# ============================================================

from utilities.shared_helpers import Print_Header, Print_Sep
from .function_helpers import Print_Package_Body

# ==============================================================================
# Combine the necessary content for the module
# ==============================================================================
def Get_Complete_vSv(module_name, author, ports, body, ext, note):
    
    header   = Print_Header(module_name, author, "//", ext) 

    complete = f"""
{header}
`timescale 1ns / 1ps

module {module_name} (
    {ports}
);

{note}
{body}
"""
    return complete

# ==============================================================================
# Combine the necessary content for the package
# ==============================================================================
def Get_Package_vSv(package_name, author, ext):
    header = Print_Header(package_name, author, "//", ext) 
    body   = Print_Package_Body(package_name, ext, Print_Sep())
    
    complete    = f"""
{header}{body}
"""
    return complete

# ==============================================================================