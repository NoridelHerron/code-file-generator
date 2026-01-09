# ============================================================
# shared_helpers.py
# Description:
#
# Author: Noridel Herron
# Date  : 2026-01-08 19:30:50
# ============================================================

from datetime import datetime
import os

# =============================================================
# Functions only
# =============================================================

def Get_time_and_date():
    result = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # ************
    return result
    # ************

# =============================================================

def Print_Sep(star=False):
    if star:
        result = "*" * 60
    else:
        result = "=" * 60
    # ************
    return result
    # ************

# ==============================================================

def Get_author_name(author=""):
    result =  (
        f"Author      : {author}"
        if author else
        f"Author      :"
    )
    # ************
    return result
    # ************

# ==============================================================

def Get_Comment(ext):
    result = "//"
    if ext == ".vhd":
        result = "--"
    elif ext == ".py":
        result = "##"
    # ************
    return result
    # ************

# ==============================================================

def Get_Extension(lang="", is_pkg=""):
    
    if lang == "vhdl":
        result = ".vhd"
    elif lang == "sv":
        if is_pkg == "pkg":
            result = ".svh"
        else:
            result = ".sv"
    else:
        if is_pkg == "pkg":
            result = ".vh"
        else:
            result = ".v"
    # ************
    return result
    # ************

# ===============================================================

def header_guard(guard):
    result = f"""
`ifndef {guard.upper()}_PKG_VH
`define {guard.upper()}_PKG_VH

// parameters
// `define MACROS
// localparams

`endif
"""
    # ************
    return result
    # ************

# ===============================================================

def Print_Header(file_name, author, comment, file_ext):
    timestamp = Get_time_and_date()
    sep       = Print_Sep()

    header    = f"""{comment} {sep}
{comment} Project Name: 
{comment} Description :
{comment}
{comment} File Name   : {file_name}{file_ext}
{comment} Dependencies:
{comment} {Get_author_name(author)}
{comment} Date        : {timestamp}
{comment} {sep}"""

    # ************
    return header
    # ************

# ================================================================
def save_file(filename, content, out_dir=None):
    """
    Save generated content to a file.

    Args:
        filename (str): Name of the file to create
        content (str): File contents
        out_dir (str | None): Output directory.
                              If None, save in current directory.
    """
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        file_path = os.path.join(out_dir, filename)
    else:
        file_path = filename

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\nFile generated: {file_path}")

# ================================================================

def Multiple_Separator(num, comment):
    result = ""

    for _ in range(num):
        result += f"\n{comment} {Print_Sep(True)}\n"

    # ************
    return result
    # ************

# ================================================================

def Add_Function(num, comment):
    result = ""

    for _ in range(num):
        result += (
            "\ndef Function_Name():\n"
            "    pass\n\n"
            f"{comment} {Print_Sep(True)}\n"
        )

    # ************
    return result
    # ************


def Get_File_Info(is_hdl: bool):
    """
    Prompt for file type and base file name.

    Returns:
        tuple[str, str]: (file_type, base_name)
    """
    if is_hdl:
        valid_types = [".vhd", ".v", ".vh", ".sv", ".svh"]
    else:
        valid_types = [".c", ".h", ".cpp", ".hpp", ".py"]

    while True:
        file_type = input("Enter file type: ").strip()

        if file_type not in valid_types:
            print(f"Error: Unsupported file type. Valid types: {', '.join(valid_types)}")
            continue

        if is_hdl:
            base_name = input("Enter module / entity / package name: ").strip()
        else:
            base_name = input("Enter file name (without extension): ").strip()
            
        if not base_name:
            if is_hdl:
                print("Error: Module or Entity name cannot be empty")
            else:
                print("Error: File name cannot be empty")
            continue   
        # **************************
        return file_type, base_name
        # **************************

# ================================================================
# END OF FILE
# ================================================================