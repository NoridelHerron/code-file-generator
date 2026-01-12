# ============================================================
# verilog_sv_templates.py
# Description:
#   Verilog and SystemVerilog template generators.
#
# Author: Noridel Herron
# Date  : 2026-01-06 16:57:12
# ============================================================

from .function_helpers import (
    Print_Seq_Port,
    Print_Seq_Body,
    Print_Port_comments,   # consider renaming to Print_Port_Placeholder
    Print_Comb_Body,
    Print_Package_Body
)

from utilities.shared_helpers import ( 
    Print_Header, 
    Print_Sep )

from .file_content import Get_Verilog_Content

# ============================================================
# Functions Only
# ============================================================

# Generate Verilog / SystemVerilog module template
def verilog_module_template( module_name   = "",
                             author        = "",
                             ext           = ".v",
                             is_sequential = True ):

    if ext == ".sv":
        note = "// Add logic signal/s here"
    else:
        note = "// Add wire or reg here"

    if is_sequential:
        ports = Print_Seq_Port(ext)
        body  = Print_Seq_Body(ext)
    else:
        ports = Print_Port_comments(ext)
        body  = Print_Comb_Body(ext)

    header   = Print_Header( module_name, 
                             author, 
                             "//", 
                             ext ) 
    
    complete = Get_Verilog_Content( 
                    is_package  = False, 
                    module_name = module_name,
                    header      = header, 
                    body        = body,
                    ports       = ports, 
                    note        = note )
    # **************
    return complete
    # **************

# ================================================================

# Generate Verilog / SystemVerilog package / include template
def verilog_package_template( package_name = "", 
                              author       = "", 
                              ext          = ".svh"):
    
    header   = Print_Header( 
                    package_name, 
                    author, 
                    "//", 
                    ext ) 
    
    body     = Print_Package_Body( 
                    package_name, 
                    ext, 
                    Print_Sep())
    
    complete = Get_Verilog_Content( 
                    is_package  = True, 
                    module_name = package_name,
                    header      = header, 
                    body        = body,
                    ports       = "", 
                    note        = "" )
    
    # **************
    return complete
    # **************    

# ================================================================
# END OF FILE
# ================================================================