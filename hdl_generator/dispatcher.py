# ============================================================
# dispatcher.py
# Description:
#   Returns HDL source text only (no file I/O).
#
# Author: Noridel Herron
# Date  : 2026-01-06 17:18:42
# ============================================================

from .vhdl_templates import ( 
    vhdl_entity_template,
    vhdl_package_template )

from .verilog_sv_templates import ( 
    verilog_module_template, 
    verilog_package_template )

# ============================================================
# Function only
# ============================================================

def generate_hdl_content( file_type, 
                          name, 
                          unit_type, 
                          author ):
    """
    Generate HDL source text based on language and unit type.

    Args:
        file_type (str): ".vhd", ".v", ".sv", ".vh", ".svh"
        unit_type (str): "comb", "seq", or "pkg"
        name      (str): entity/module/package name
        author    (str): optional author name

    Returns:
        str: HDL source content
    """

    # VHDL
    if file_type == ".vhd":
        if unit_type == "pkg":
            return vhdl_package_template(
                package_name = name,
                ext          = file_type,
                author       = author,
            )
        else:
            return vhdl_entity_template(
                entity_name=name,
                author        = author,
                is_sequential = (unit_type == "seq"),
            )

    # Verilog / SystemVerilog package/include files
    elif file_type in [".vh", ".svh"]:
        return verilog_package_template(
            package_name = name,
            author       = author,
            ext          = file_type )

    # Verilog / SystemVerilog modules
    elif file_type in [".v", ".sv"]:
        return verilog_module_template(
            module_name   = name,
            author        = author,
            ext           = file_type,
            is_sequential = (unit_type == "seq") )

    # Safety net
    else:
        raise ValueError(f"Unsupported HDL file type: {file_type}")

# ================================================================
# END OF FILE
# ================================================================