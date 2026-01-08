# ============================================================
# verilog_sv_templates.py
# Description:
#   Verilog and SystemVerilog template generators.
#
# Author: Noridel Herron
# Date  : 2026-01-06 16:57:12
# ============================================================

from function_helpers import (Get_author_name, Print_Seq_Port, Print_Seq_Body,
                              Print_Port_comments, Print_Comb_Body)
from verilogSV_helpers import Get_Complete_vSv, Get_Package_vSv

# ==============================================================================
# Generate Verilog / SystemVerilog module template
# ==============================================================================
def verilog_module_template(
    module_name,
    author="",
    hdl_lang="",
    is_sequential=True
):
    if hdl_lang == "sv":
        file_ext = "sv"
        note     = "// Add logic signal/s here"

    elif hdl_lang == "verilog":
        file_ext = "v"
        note     = "// Add wire or reg here"
    
    if is_sequential:
        ports = Print_Seq_Port(hdl_lang)
        body  = Print_Seq_Body(hdl_lang)
    else:
        ports = Print_Port_comments(hdl_lang)
        body  = Print_Comb_Body(hdl_lang)

    return Get_Complete_vSv(module_name, Get_author_name(author), ports, body, hdl_lang, file_ext, note) 

# ==============================================================================  
# Generate Verilog / SystemVerilog package template
# ==============================================================================
def verilog_package_template(package_name, author="", hdl_lang=""):
    return Get_Package_vSv(package_name, Get_author_name(author), hdl_lang)