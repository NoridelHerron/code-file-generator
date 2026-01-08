# ============================================================
# hdl_genFile.py
# Description: User prompt utilities for HDL code generation.
#   Collects explicit design intent (language, unit type,
#   combinational vs sequential, package usage, etc.).
#
# Author: Noridel Herron
# Date  : 2026-01-06 14:56:11
# ============================================================

from dispatcher import generate_hdl_content

# ==============================================================================
# Ask the user which HDL language to generate.
# ==============================================================================
def ask_hdl_language():
    while True:
        choice = input(
            "Select HDL language (vhdl / v / sv): "
        ).strip().lower()

        if choice == "vhdl":
            return "vhdl"
        elif choice in ["v", "verilog"]:
            return "verilog"
        elif choice in ["sv", "systemverilog"]:
            return "sv"
        else:
            print(
                "Invalid input. Please enter "
                "'vhdl', 'v' (verilog), or 'sv' (systemverilog)."
            )

# ==============================================================================
# Ask the user what type of HDL unit to generate.
# Module (clocked or not clocked) or a package
# ==============================================================================
def ask_hdl_unit_type():
    while True:
        choice = input(
            "Select HDL unit type "
            "(c = combinational, s = sequential, p = package): "
        ).strip().lower()

        if choice in ["c", "comb", "combinational"]:
            return "comb"
        elif choice in ["s", "seq", "sequential"]:
            return "seq"
        elif choice in ["p", "pkg", "package"]:
            return "pkg"
        else:
            print(
                "Invalid input. Please enter "
                "'c' (combinational), 's' (sequential), or 'p' (package)."
            )

# ==============================================================================
# Ask the user for the HDL unit name (entity/module/package).
# ==============================================================================
def ask_module_or_entity_name():
    while True:
        name = input(
            "Enter module / entity / package name: "
        ).strip()

        if name:
            return name
        else:
            print("Name cannot be empty.")

# ==============================================================================
# Ask for an optional author name.
# Confirms if user wants to leave it empty.
# ==============================================================================
def ask_author_name():
    """
    Ask for an optional author name.
    Confirms if user wants to leave it empty.

    Returns:
        str: author name or empty string
    """
    while True:
        author = input(
            "Enter author name (optional): "
        ).strip()

        if author:
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

# ==============================================================================
# Verilog does not support packages.
# Confirm behavior if user selects package + Verilog.
# if TRUE generation should proceed, else cancel the process
# ==============================================================================
def confirm_verilog_package_choice(hdl_language, unit_type):
    """
    Verilog does not support packages.
    Confirm behavior if user selects package + Verilog.

    Returns:
        bool: True if generation should proceed, False otherwise
    """
    if hdl_language == "verilog" and unit_type == "pkg":
        print(
            "\nNOTE: Verilog does not support packages.\n"
            "A Verilog include file (.vh) will be generated instead."
        )
        while True:
            choice = input("Proceed? (y/n): ").strip().lower()
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("Please enter 'y' or 'n'.")
    return True

# ==============================================================================
# Save generated HDL content to a file.
# ==============================================================================
def save_hdl_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

    print(f"\nFile generated: {filename}")

# ==============================================================================
# Main
# ==============================================================================
if __name__ == "__main__":

    print("=== HDL Generator Setup ===")

    hdl_language = ask_hdl_language()
    unit_type    = ask_hdl_unit_type()
    name         = ask_module_or_entity_name()
    author       = ask_author_name()

    if not confirm_verilog_package_choice(hdl_language, unit_type):
        print("Generation cancelled.")
    else:
        print("\nSummary:")
        print(f"  HDL Language : {hdl_language}")
        print(f"  Unit Type    : {unit_type}")
        print(f"  Name         : {name}")
        print(f"  Author       : {author if author else '(none)'}")

        # ----------------------------------------------------
        # Generate HDL content
        # ----------------------------------------------------
        content = generate_hdl_content(
            hdl_language=hdl_language,
            unit_type=unit_type,
            name=name,
            author=author
        )

        # Decide file extension and name
        if unit_type == "pkg":
            base = f"{name}_pkg"
        else:
            base = name

        if hdl_language == "vhdl":
            filename = f"{base}.vhd"
        elif hdl_language == "sv":
            if unit_type == "pkg":
                filename = f"{base}.svh"
            else:
                filename = f"{base}.sv"
        else:  # verilog
            if unit_type == "pkg":
                filename = f"{base}.vh"
            else:
                filename = f"{base}.v"

        save_hdl_file(filename, content)


