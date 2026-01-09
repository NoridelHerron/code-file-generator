# ============================================================
# Makefile
# Code File Generator
#
# Supports:
#   - Linux / macOS
#   - Windows (Git Bash or MSYS2)
#
# NOTE:
#   PowerShell does NOT include `make`.
#   On Windows PowerShell, use:  py run.py hdl | py run.py gen
#
# Author: Noridel Herron
# ============================================================

# ------------------------------------------------------------
# OS detection
# ------------------------------------------------------------
ifeq ($(OS),Windows_NT)
	PYTHON := py
	PLATFORM := Windows
else
	PYTHON := python3
	PLATFORM := Unix
endif

# ------------------------------------------------------------
# Phony targets
# ------------------------------------------------------------
.PHONY: help info hdl gen run-hdl run-gen

# ------------------------------------------------------------
# Help target
# ------------------------------------------------------------
help:
	@echo ""
	@echo "Code File Generator"
	@echo "==================="
	@echo ""
	@echo "Available targets:"
	@echo ""
	@echo "  make hdl        Run HDL generator"
	@echo "  make gen        Run general generator"
	@echo "  make info       Show environment info"
	@echo "  make help       Show this help"
	@echo ""
	@echo "Windows users:"
	@echo "  - Use Git Bash to run make"
	@echo "  - Or use PowerShell:"
	@echo "      py run.py hdl"
	@echo "      py run.py gen"
	@echo ""

# ------------------------------------------------------------
# Info / diagnostics
# ------------------------------------------------------------
info:
	@echo "Platform : $(PLATFORM)"
	@echo "Python   : $(PYTHON)"
	@echo "PWD      : $(CURDIR)"

# ------------------------------------------------------------
# Run targets (module-based execution)
# ------------------------------------------------------------
run-hdl:
	$(PYTHON) -m hdl_generator.hdl_genFile

run-gen:
	$(PYTHON) -m gen_generator.gen_file

# ------------------------------------------------------------
# Short aliases
# ------------------------------------------------------------
hdl: run-hdl
gen: run-gen
