# ============================================================
# dispatcher.py
# Description:
#   Returns HDL source text only (no file I/O).
#
# Author: Noridel Herron
# Date  : 2026-01-06 17:18:42
# ============================================================

from vhdl_templates import (
    vhdl_entity_template,
    vhdl_package_template
)

from verilog_sv_templates import (
    verilog_module_template,
    verilog_package_template
)

# ==============================================================================
def generate_hdl_content(
    hdl_language,
    unit_type,
    name,
    author=""
):
    """
    Generate HDL source text based on language and unit type.

    Args:
        hdl_language (str): "vhdl", "verilog", or "sv"
        unit_type    (str): "comb", "seq", or "pkg"
        name         (str): entity/module/package name
        author       (str): optional author name

    Returns:
        str: HDL source content
    """

    # -------------------------------
    # VHDL
    # -------------------------------
    if hdl_language == "vhdl":

        if unit_type == "pkg":
            return vhdl_package_template(
                package_name=name,
                author=author
            )

        else:
            return vhdl_entity_template(
                entity_name=name,
                author=author,
                is_sequential=(unit_type == "seq")
            )

    # -------------------------------
    # SystemVerilog
    # -------------------------------
    elif hdl_language == "sv":

        if unit_type == "pkg":
            return verilog_package_template(
                package_name=name,
                author=author,
                hdl_lang=hdl_language
            )

        else:
            return verilog_module_template(
                module_name=name,
                author=author,
                hdl_lang=hdl_language,
                is_sequential=(unit_type == "seq")
            )

    # -------------------------------
    # Verilog
    # -------------------------------
    elif hdl_language == "verilog":

        if unit_type == "pkg":
            # Verilog has no packages → generate include (.vh)
            return verilog_package_template(
                package_name=name,
                author=author,
                hdl_lang=hdl_language
            )

        else:
            return verilog_module_template(
                module_name=name,
                author=author,
                hdl_lang=hdl_language,
                is_sequential=(unit_type == "seq")
            )

    else:
        raise ValueError("Unsupported HDL language")
# ==============================================================================