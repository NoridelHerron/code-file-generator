# Code & HDL File Generator

## Overview
This repository contains a set of **interactive Python utilities** for generating boilerplate code and HDL files with **consistent structure, headers, and intent-driven templates**.

The generators are designed to:
- Reduce repetitive setup work
- Prevent structural mismatches in low-level designs
- Enforce clean, readable scaffolding
- Stay tool-agnostic and vendor-neutral

The goal is acceleration without abstraction — you still write the logic, the tools just give you a correct starting point.

## Repository Structure

.
├── gen_files  
├── gen_generator/  # C / C++ / Python file generator
│   ├── c_content.py
│   ├── dispatcher.py
│   ├── gen_file.py
│   ├── py_content.py
│   ├── std_lib.py
├── hdl_files 
└── hdl_generator/  # VHDL / Verilog / SystemVerilog generator
│   ├── dispatcher.py
│   ├── file_content.py
│   ├── function_helper.py
│   ├── hdl_genFile.py
│   ├── verilog_sv_templates
│   ├── vhdl_templates
├── utilities/      # Shared helpers and user prompts 
│   ├── shared_helpers.py
│   ├── user_prompt.py
│   ├── __init__.py
├── License
├── Makefile
├── Readme.md
├── run.py


Each folder has a single responsibility and no circular dependencies.

### gen_generator/ - Code File Generator

Generates standard C, C++, and Python source/header files.

**Supported Languages**

- C (.c, .h)
- C++ (.cpp, .hpp)
- Python (.py)

**Key Files**

- **gen_file.py**
    Interactive entry point (no template logic inside)
- **dispatcher.py**
    Dispatches language-specific content
- **std_lib.py**
    Conservative standard library includes
- **c_content.py**
    C / C++ source and header templates
- **py_content.py**
    Python module template

**Features**

- Interactive terminal prompts
- Auto-generated file banners with timestamps
- Optional author field with confirmation
- Header guards for .h / .hpp
- Minimal main() stubs (or __main__ for Python)
- Optional Function injection for Python function scaffolding
- No external dependencies

### hdl_generator/ — HDL Generator

Generates intent-driven HDL templates for RTL design and verification.

**Supported HDLs**

- VHDL (.vhd)
- Verilog (.v, .vh)
- SystemVerilog (.sv, .svh)

**Supported Unit Types**

- Combinational modules
- Sequential (clocked) modules
- Packages
    - VHDL packages
    - SystemVerilog
    - Verilog (include-style package)

**Key Files**

- **hdl_genFile.py**
    User interaction and orchestration
- **dispatcher.py**
    Language- and unit-type routing (no file I/O)
- **vhdl_templates.py**
    VHDL entity and package templates
- **verilog_sv_templates.py**
    Verilog / SystemVerilog module and package templates
- **file_content.py**
    Language-specific structural assembly
- **function_helpers.py**
    Port/body generation helpers

**Features**

- Explicit design-intent prompts
- Clear distinction between combinational and sequential logic
- Language-aware templates (VHDL vs Verilog vs SystemVerilog)
- Conservative, synthesizable skeletons
- No implicit latches
- No mixed logic styles
- No file I/O inside templates (generation is fully decoupled)

### utilities/

Shared helper functions used across all generators.

#### Contents

- **__init__.py**
    - Clean public API for shared utilities
- **shared_helpers.py**
    - Header/banner generation
    - Comment-style resolution per language
    - Separator utilities
    - Header guards
    - Add Function up to N (Python only at the moment)
    - File save abstraction
- **user_prompt.py**
    - Author confirmation logic
    - Output directory selection
    - Function count prompts

**Note:** I use the gen_files/ and hdl_files/ folders as temporary output targets during testing so generated files don’t mix with the generator’s core code while I iterate and validate behavior.

## How to use
**Generate C / C++ / Python Files**

From root directory

    Linux:   **make gen**

    Windows: **py run.py gen**

You will be prompted to: 
1. Enter file type
2. Enter file name (without extension)
3. Optionally enter an author name
4. Number of Function/s (Python only)
5. If you want to store it in the folder
    - If yes, it will prompt the path folder 
    - If no, it goes to the root directory

**Generate HDL Files**

From root directory

    Linux:   **make gen**

    Windows: **py run.py gen**

You will be prompted to:
1. Enter file type
2. Enter module / entity / package name
3. Select HDL unit type
    - for vhdl (.vhd), there's 3 options (c = combinational, s = sequential, p = package)
    - for Verilog (.v) and System Verilog (.sv) (c = combinational, s = sequential)
    - .vh and .svh 
4. Optionally enter an author name
5. If you want to store it in the folder
    - If yes, it will prompt the path folder 
    - If no, it goes to the root directory

All generated file will be created with the appropriate extension.

## Design Philosophy
Both generators follow the same core principles:
- **Intent first**: user explicitly chooses design type and language
- **Conservative defaults**: no implicit latches, no mixed logic styles
- **Minimal scaffolding**: correct starting point, not a full implementation
- **Tool-agnostic**: no vendor-specific constructs or pragmas

These tools are meant to **accelerate setup**, not replace engineering judgment.

## Why This Exists

I built this for myself to reduce structural overhead in the low-level work I do across HDL, C/C++, and Python. It enforces intent early and adds clear separators so I can focus on solving real problems instead of repeating setup tasks.

**Author:** Noridel Herron

**Email:**  github@noridel.com
