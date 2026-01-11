# ============================================================
# __init__.py
# Description: Shared helper utilities used across generators
#
# Author: Noridel Herron
# Date  : 2026-01-08 16:33:35
# ============================================================

from .shared_helpers import (
    Get_time_and_date,
    Print_Sep,
    Get_author_name,
    Get_Comment,
    header_guard,
    Print_Header,
    save_file,
    Multiple_Separator,
    Get_File_Info,
)

from .user_prompt import (
    ask_author_name,
    Get_Function_Count, 
    Out_directory,
)

__all__ = [
    "Get_time_and_date",
    "Print_Sep",
    "Get_author_name",
    "Get_Comment",
    "header_guard",
    "Print_Header",
    "save_file",
    "Multiple_Separator",
    "Get_File_Name",

    "ask_author_name",
    "Get_Function_Count",
    "Out_directory"
]
