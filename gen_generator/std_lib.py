
## ===========================================================
## Project Name: File Generator
## Description :
##
## File Name   : std_lib.py
## Dependencies:
## Author      : Noridel Herron
## Date        : 2026-01-09 12:33:05
## ===========================================================

# ============================================================
# Function only
# ============================================================

def Standard_Lib(ext):
    if ext in [".c", ".h"]:
        lib = """
// C STANDARD LIBRARY
#include <stdio.h>    // printf, scanf, file I/O
#include <stdlib.h>   // malloc, free, rand, exit
#include <stdint.h>   // fixed-width integers
#include <stdbool.h>  // bool type
#include <string.h>   // memcpy, memset, strcmp
#include <stddef.h>   // size_t, NULL, offsetof
#include <math.h>     // math functions
#include <time.h>     // time, clock, srand seed
#include <errno.h>    // error codes
#include <assert.h>   // assertions
#include <float.h>    // Floating-point limits
#include <limits.h>   // Integer limits
#include <ctype.h>
"""
    # *****************************************
    elif ext in [".cpp", ".hpp"]:
        lib = """
// C++ STANDARD LIBRARY 
#include <iostream>    // console I/O
#include <string>      
#include <vector>      // dynamic arrays
#include <array>       // fixed-size arrays
#include <algorithm>   // sort, find, transform
#include <cstdint>     // fixed-width integers
#include <memory>      // smart pointers
#include <chrono>      // time utilities
#include <random>      // RNG
#include <iomanip>      // control data format
#include <iostream>
#include <fstream>
#include <sstream>
"""
    # *********************************************
    elif ext == ".py":
        lib = """## Libraries
import sys
import pathlib
import time
import numpy as np
import cv2
"""
    else:
        lib = ""
    # ************
    return lib
    # ************

# ================================================================
# END OF FILE
# ================================================================