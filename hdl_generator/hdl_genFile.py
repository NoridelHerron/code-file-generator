# ============================================================
# hdl_genFile.py
# Description: User prompt utilities for HDL code generation.
#   Collects explicit design intent (language, unit type,
#   combinational vs sequential, package usage, etc.).
#
# Author: Noridel Herron
# Date  : 2026-01-06 14:56:11
# ============================================================

from utilities.user_prompt import (ask_author_name, Out_directory)
from utilities.shared_helpers import (Get_File_Info, save_file)
from .dispatcher import generate_hdl_content

# ============================================================
# Functions
# ============================================================
def ask_hdl_unit_type(ext):
    """
    Ask the user what type of HDL unit to generate.
    Module (clocked or not clocked) or a package
    """
    if ext in [".vhd", ".v", ".sv"]:
        while True:
            if ext == ".vhd":
                choice = input(
                    "Select HDL unit type "
                    "(c = combinational, s = sequential, p = package): "
                ).strip().lower()
            else:
                choice = input(
                    "Select HDL unit type "
                    "(c = combinational, s = sequential): "
                ).strip().lower()

            if choice in ["c", "comb", "combinational"]:
                result = "comb"
            elif choice in ["s", "seq", "sequential"]:
                result = "seq"
            elif choice in ["p", "pkg", "package"]:
                result = "pkg"
            else:
                if ext == ".vhd":
                    print(
                        "Invalid input. Please enter "
                        "'c' (combinational), 's' (sequential), or 'p' (package)."
                    )
                else:
                    print(
                        "Invalid input. Please enter "
                        "'c' (combinational) or 's' (sequential)"
                    )

            # ************
            return result
            # ************

# ===============================================================
# Main
# ===============================================================
def main():
    print("=== HDL File Generator ===")
    print("Supported types/extensions: .vhd .v .vh .sv .svh")

    # Extract the file name needed to generate the content
    file_type, module_name = Get_File_Info(True)
    unit_type              = ask_hdl_unit_type(file_type)
    author                 = ask_author_name()

    # Generate HDL content
    content = generate_hdl_content(
            file_type = file_type,
            name      = module_name,
            unit_type = unit_type,
            author    = author
        )
    
    # Prompt user if the generated file will be stored in folder/root directory
    out_dir = Out_directory()
    save_file(module_name + file_type, content, out_dir)

# ================================================================
# Main
# ================================================================
if __name__ == "__main__":
        main()

# ================================================================
# END OF FILE
# ================================================================