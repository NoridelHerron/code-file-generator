# Code & HDL File Generator

## Overview
This repository contains a set of **interactive Python utilities** for generating boilerplate code and HDL files with **consistent structure, headers, and intent-driven templates**.

The tools are designed to reduce repetitive setup work while enforcing clean, conservative defaults suitable for **general programming, RTL design, and verification workflows**.

## What's Included
**Code File Generator** (gen_file.py)

Generates standard source and header files for general-purpose programming.

**Supported Languages**
- C      (.c,   .h)
- C++    (.cpp, .hpp)
- Python (.py)

**Features**
- Interactive terminal prompts
- Automatically generated file banner with timestamp
- Optional author field with confirmation
- Header guards for .h / .hpp files
- Minimal main() stubs for source files
- No external dependencies

**HDL Generator** (hdl_genFile.py)

Generates **intent-driven HDL templates** for digital design work.

**Supported HDLs**:
- VHDL          (.vhd)
- Verilog       (.v,  .vh)
- SystemVerilog (.sv, .svh)

**Supported unit types**:
- Combinational modules
- Sequential (clocked) modules
- Packages (Verilog packages are generated as include files: .vh)

**Features**:
- Interactive design-intent prompts
- Explicit distinction between combinational and sequential logic
- Language-aware templates (VHDL vs Verilog vs SystemVerilog)
- Conservative, synthesizable skeletons
- No file I/O inside templates (generation is fully decoupled)

## How to use
**Generate C / C++ / Python Files**

Run: **python gen_file.py**

You will be prompted to: 
1. Enter file type
2. Enter file name (without extension)
3. Optionally enter an author name

**Generate HDL Files**

Run: **python hdl_genFile.py**

You will be prompted to:
1. Select HDL language (VHDL / Verilog / SystemVerilog)
2. Select unit type (combinational / sequential / package)
3. Enter the module/entity/package name
4. Optionally enter an author name

All generated file will be created with the appropriate extension.
All generated files are stored in the **hdl_generated_files** directory.

## Design Philosophy
Both generators follow the same core principles:
- **Intent first**: user explicitly chooses design type and language
- **Conservative defaults**: no implicit latches, no mixed logic styles
- **Minimal scaffolding**: correct starting point, not a full implementation
- **Tool-agnostic**: no vendor-specific constructs or pragmas

These tools are meant to **accelerate setup**, not replace engineering judgment.

**Author:** Noridel Herron

**Email:**  github@noridel.com
