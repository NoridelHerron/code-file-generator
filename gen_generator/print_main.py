## ===========================================================
## Project Name: File Generator
## Description :
##
## File Name   : print_main.py
## Dependencies: 
## Author      : Noridel Herron
## Date        : 2026-01-09 04:59:46
## ===========================================================

from .std_lib import Standard_Lib
from .py_content import Print_Py_Content
from .c_content import Print_C_Sources, Print_C_headers
from utilities.shared_helpers import Print_Sep, Add_Function
# ============================================================
# Function only
# ============================================================

def main_stub(ext, file_name, num):
    lib = Standard_Lib(ext)
    sep = Print_Sep()

    # Python
    if ext == ".py":
        func   = Add_Function(num, "##")
        result = Print_Py_Content(lib, sep, func)

    # C / C++ headers
    elif ext in (".h", ".hpp"):
        suffix = "HPP" if ext == ".hpp" else "H"
        guard  = f"{file_name.upper()}_{suffix}"
        result = Print_C_headers(ext, guard, lib, sep)
        
    # C / C++ source
    else:
        result = Print_C_Sources(lib, sep)

    # ************
    return result
    # ************

# ================================================================
# END OF FILE
# ================================================================
