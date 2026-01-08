# ============================================================
# vhdl_templates.py
# Description:
#   VHDL template generators for entities and packages.
#
# Author: Noridel Herron
# Date  : 2026-01-06 16:58:58
# ============================================================

from function_helpers import (Get_author_name, Print_Seq_Port, 
                              Print_Seq_Body,  Print_Comb_Body,
                              Print_Port_comments)
from vhdl_helpers import ( Get_Complete_VHDL, Get_Package_VHDL)

# Generate VHDL module templates
def vhdl_entity_template(entity_name, author="", is_sequential=True):
    author_line = Get_author_name(author)

    if is_sequential:
        ports = Print_Seq_Port("vhdl")
        body  = Print_Seq_Body("vhdl")
    else:
        ports = Print_Port_comments("vhdl")
        body  = Print_Comb_Body("vhdl")

    return Get_Complete_VHDL(author_line, entity_name, ports, body, "vhd" )

def vhdl_package_template(package_name, author):
    return Get_Package_VHDL(package_name, Get_author_name(author), "vhd")