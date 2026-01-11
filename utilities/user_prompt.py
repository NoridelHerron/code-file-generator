# ============================================================
# user_prompt.py
# Description:
#
# Author: Noridel Herron
# Date  : 2026-01-09 04:16:00
# ============================================================

# =============================================================
# Functions only
# =============================================================

def ask_author_name():
    """
    Prompt for an optional author name.

    Returns:
        str: Author name, or empty string if omitted.
    """
    while True:
        author = input("Enter author name (optional): ").strip()

        if author != "":
            return author

        confirm = input(
            "Author name is empty. Are you sure? (y/n): "
        ).strip().lower()

        if confirm == "y":
            return ""
        elif confirm == "n":
            continue
        else:
            print("Please enter 'y' or 'n'.")
    
# ================================================================

def Get_Function_Count():
    """
    Prompt for number of separators.

    Returns:
        int: Number of separators (0 if invalid or empty input)
    """
    num_str = input("Number of Function/s: ").strip()

    if not num_str.isdigit():
        result = 0
    else:
        result = int(num_str)
    # ************
    return result
    # ************

# ================================================================

def Out_directory():
    is_true = input("Do You want to store it in the folder? (y/n): ").strip()
    if is_true == "y":
        result =  input("Enter the folder name?: ").strip()   
    else:
        result = ""
    # ************
    return result
    # ************

# ================================================================
# END OF FILE
# ================================================================