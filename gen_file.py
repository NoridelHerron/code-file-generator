# ============================================================
# gen_file.py
# Description:
#   Interactive code file generator for C, C++, and Python.
#   Generates source and header files with consistent banners,
#   include guards (for headers), and minimal main stubs.
#
# Author : Noridel Herron
# Version: v1.0
# Date   : 2026-01-06
# ============================================================

from datetime import datetime
import os

# ============================================================
# Banner generator
# ============================================================
def file_banner(filename, author, comment_prefix):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    author_line = (
        f"{comment_prefix} Author: {author}\n"
        if author else
        f"{comment_prefix} Author:\n"
    )

    return f"""{comment_prefix} ============================================================
{comment_prefix} {filename}
{comment_prefix} Description:
{comment_prefix}
{author_line}{comment_prefix} Date  : {timestamp}
{comment_prefix} ============================================================
"""

# ============================================================
# Header guard generator
# ============================================================
def header_guard(guard):
    return f"""
#ifndef {guard}
#define {guard}

#endif // {guard}
"""

# ============================================================
# Main stub generator
# ============================================================
def main_stub(ext):
    if ext == ".c":
        return """
int main(void)
{
    return 0;
}
"""
    elif ext == ".cpp":
        return """
int main()
{
    return 0;
}
"""
    elif ext == ".py":
        return """

if __name__ == "__main__":
    pass
"""
    return ""

# ============================================================
# File generator 
# ============================================================
def generate_file(filename, author=""):
    _, ext = os.path.splitext(filename)

    supported = [".c", ".h", ".cpp", ".hpp", ".py"]
    if ext not in supported:
        raise ValueError("Unsupported file type")

    comment_prefix = "#" if ext == ".py" else "//"
    content = file_banner(filename, author, comment_prefix)

    if ext in [".h", ".hpp"]:
        guard = filename.replace(".", "_").upper()
        content += header_guard(guard)
    else:
        content += main_stub(ext)

    with open(filename, "w") as f:
        f.write(content)

    print(f"\nGenerated: {filename}")

# ============================================================
# Interactive entry point
# ============================================================
def main():
    print("=== Code File Generator ===")
    print("Supported types: .c .h .cpp .hpp .py")

    file_type = input("Enter file type: ").strip()
    if file_type not in [".c", ".h", ".cpp", ".hpp", ".py"]:
        print("Error: Unsupported file type")
        return

    base_name = input("Enter file name (without extension): ").strip()
    if not base_name:
        print("Error: File name cannot be empty")
        return

    # ---- Optional author logic ----
    while True:
        author = input("Enter author name (optional): ").strip()

        if author:
            break

        confirm = input("Author name is empty. Are you sure? (y/n): ").strip().lower()
        if confirm == "y":
            author = ""
            break
        elif confirm == "n":
            continue
        else:
            print("Please enter 'y' or 'n'.")

    generate_file(base_name + file_type, author)

# ============================================================
# Run
# ============================================================
if __name__ == "__main__":
    main()
