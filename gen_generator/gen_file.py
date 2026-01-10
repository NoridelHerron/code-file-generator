# ============================================================
# gen_file.py
# Description:
#   Interactive code file generator for C, C++, and Python.
#   Generates source and header files with consistent banners,
#   include guards (for headers), and minimal main stubs.
#
# Author : Noridel Herron
# Date   : 2026-01-06
# ============================================================

from utilities.shared_helpers import (Print_Header, Get_Comment,  
                                      Multiple_Separator, 
                                      save_file, Get_File_Info)

from utilities.user_prompt import(ask_author_name, 
                                  Out_directory,
                                  Get_Separator_Count)
from .print_main import main_stub

# ============================================================
# Functions
# ============================================================
def Get_Content(file_name, ext, author, num):
    """
    Generate the content of the file
    """
    comment      = Get_Comment(ext)
    header       = Print_Header(file_name, author, comment, ext)  
    main_content = main_stub(ext, file_name, num) 
    result       = f"""
{header}
{main_content}
"""
    # ************
    return result
    # ************

# ============================================================

def main():
    # Interactive entry point
    print("=== Code File Generator ===")
    print("Supported types: .c .h .cpp .hpp .py")

    file_type, base_name = Get_File_Info(False)
    author               = ask_author_name()                 # Optional author logic 

    num = Get_Separator_Count() if file_type == ".py" else 0 # Number of separator
    content              = Get_Content(base_name, file_type, author, num)

    # ************************************
    return base_name, file_type, content
    # ************************************

# ============================================================
# Main
# ============================================================
if __name__ == "__main__":

    # Extract the file name and generate the content 
    base_name, file_type, file_content = main()

    # Prompt user if the generated file will be stored in folder/root directory
    out_dir                            = Out_directory()
    save_file(base_name + file_type, file_content, out_dir)

# ================================================================
# END OF FILE
# ================================================================