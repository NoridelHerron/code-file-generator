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
)

from .verilogSV_helpers import (
    Get_Complete_vSv,
    Get_Package_vSv,
)

# ============================================================
# Functions Only
# ============================================================

# Generate Verilog / SystemVerilog module template
def verilog_module_template(
    module_name,
    author="",
    ext=".v",
    is_sequential=True,
):
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

    complete = Get_Complete_vSv(
        module_name,
        author,
        ports,
        body,
        ext,
        note,
    )
    # **************
    return complete
    # **************

# ================================================================
# Generate Verilog / SystemVerilog package / include template
def verilog_package_template(package_name, author="", ext=".svh"):
    complete = Get_Package_vSv(package_name, author, ext)
    # **************
    return complete
    # **************    

# ================================================================
# END OF FILE
# ================================================================