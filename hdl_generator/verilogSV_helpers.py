# ============================================================
# verilogSV_helpers.py
# Description:
#
# Author: Noridel Herron
# Date  : 2026-01-07 11:57:25
# ============================================================

from function_helpers import (Print_Header, Print_Package_Body)

# ==============================================================================
# Combine the necessary content for the module
# ==============================================================================
def Get_Complete_vSv(module_name, author, ports, body, hdl_type, file_ext, note):
    
    header   = Print_Header(module_name, author, hdl_type, file_ext)
    complete = f"""
{header}
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
def Get_Package_vSv(package_name, author, hdl_type):
    file_ext = "sv" if hdl_type == "sv" else "v"
    header   = Print_Header(package_name + "_pkg", author, file_ext, file_ext + "h")
    body     = Print_Package_Body(package_name, file_ext)
    
    complete    = f"""
{header}{body}
"""
    return complete

# ==============================================================================