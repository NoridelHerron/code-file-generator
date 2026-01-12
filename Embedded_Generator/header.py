
## ============================================================
## Project Name: 
## Description :
##
## File Name   : header.py
## Dependencies:
## Author      : Noridel Herron
## Date        : 2026-01-11 17:10:27
## ============================================================

from utilities.shared_helpers import (
    Print_Sep, 
    Print_Header
)

## ============================================================
##  Function/s Only
## ============================================================

def Thread_HeaderFile( opt, 
                       file_name,
                       author,
                       thread_names ):
    
    header = Print_Header(
                file_name, 
                author,
                "//",
                ".h" )
    
    sep          = Print_Sep()

    thread_block = "\n".join(
                        f"\tvoid* {name}_thread(void *arg);" 
                        for name in thread_names
                    )
    
    if opt == "t":
        result = f"""
{header}

#ifndef {file_name.upper()}_H
#define {file_name.upper()}_H

{thread_block}

#endif /* {file_name.upper()}_H */

// {sep}
//  End of File
// {sep}
"""
    else:
        result = ""

    # *************
    return result
    # *************

def Header_Content(opt):
    
    result = ""

    # *************
    return result
    # *************

## ============================================================
##  End of File
## ============================================================

