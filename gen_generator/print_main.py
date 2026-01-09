## ===========================================================
## Project Name: 
## Description :
##
## File Name   : print_main.py
## Dependencies:
## Author      : Noridel Herron
## Date        : 2026-01-09 04:59:46
## ===========================================================

from .std_lib import Standard_Lib
from .py_content import Print_Py_Content
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

        result = f"""#ifndef {guard}
#define {guard}

{lib}

#endif /* {guard} */
"""

    # C / C++ source
    else:
        main_sig = "int main(void)" if ext == ".c" else "int main()"
        result = f"""{lib}
{main_sig}
{{
    return 0;
}}
"""

    # ************
    return result
    # ************

# ================================================================
# END OF FILE
# ================================================================
