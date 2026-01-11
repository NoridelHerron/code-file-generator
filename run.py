# ============================================================
# run.py
# Description:
#
# Author: Noridel Herron
# Date  : 2026-01-08 22:51:24
# ============================================================

import sys
import subprocess

TARGETS = {
    "hdl": ["-m", "hdl_generator.hdl_genFile"],
    "gen": ["-m", "gen_generator.gen_file"],
    "emb": ["-m", "Embedded_Generator.embedded_genFile"],
}

if len(sys.argv) != 2 or sys.argv[1] not in TARGETS:
    print("Usage:")
    print("  py run.py hdl   # Run HDL generator")
    print("  py run.py gen   # Run general code generator")
    print("  py run.py emb   # Run embedded code generator")
    sys.exit(1)

cmd = ["py"] + TARGETS[sys.argv[1]]
subprocess.run(cmd)
