# ============================================================
# vhdl_templates.py
# Description:
#   VHDL template generators for entities and packages.
#
# Author: Noridel Herron
# Date  : 2026-01-06 16:58:58
# ============================================================

from .function_helpers import ( 
    Print_Seq_Port,    
    Print_Seq_Body,  
    Print_Comb_Body,   
    Print_Port_comments,
    Print_Package_Body )

from .file_content import Get_VHDL_Content 

from utilities.shared_helpers import ( 
    Print_Header, 
    Print_Sep )

# ================================================================
# Functions only
# ================================================================

# Generate VHDL module templates
def vhdl_entity_template( entity_name, 
                          author        = "", 
                          is_sequential = True):

    if is_sequential:
        ports = Print_Seq_Port("vhdl")
        body  = Print_Seq_Body("vhdl")

    else:
        ports = Print_Port_comments("vhdl")
        body  = Print_Comb_Body("vhdl")

    header   = Print_Header(
                    entity_name, 
                    author, 
                    "--", 
                    ".vhd")

    complete = Get_VHDL_Content(
                    is_package  = False, 
                    header      = header, 
                    body        = body,
                    entity_name = entity_name,
                    ports       = ports )
    
    # **************
    return complete
    # **************

# ================================================================
# Generate VHDL package template
def vhdl_package_template( package_name = "", 
                           ext          = "", 
                           author       = ""):
    
    header   = Print_Header( package_name, 
                             author, 
                             "--",  
                             ext )
    
    sep      = Print_Sep()
    body     = Print_Package_Body( package_name + "_pkg", 
                                   ext, 
                                   sep ) 
    
    complete = Get_VHDL_Content(
                    is_package  = True, 
                    header      = header, 
                    body        = body,
                    entity_name = "",
                    ports       = "" )
    
    # **************
    return complete
    # ************** 

# ================================================================
# END OF FILE
# ================================================================