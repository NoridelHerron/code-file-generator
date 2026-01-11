
## ============================================================
## Project Name: 
## Description :
##
## File Name   : thread_content.py
## Dependencies:
## Author      : Noridel Herron
## Date        : 2026-01-11 13:54:23
## ============================================================

from utilities.shared_helpers import (
    Print_Header,
    Print_Sep
)

from .lib_contents import (
    Print_Lib
)

## ============================================================
##  Function/s Only
## ============================================================

def Thread_FileContent(
        fileName = "",
        fileType = "",
        author   = ""
):
    header = Print_Header(
                fileName, 
                author, 
                "//", 
                ".c" )
    
    body   = Thread_Content(fileName)
    lib    = Print_Lib(fileType)

    result = f"""{header}
{lib}{body}

    """
    
    # *************
    return result
    # *************

## ****************************************

def Thread_Content(name):

    sep    = Print_Sep()

    result = f"""
void* {name}_thread(void *arg)
{{
    (void)arg;

    // 
    for (;;) {{
        sleep(1);
    }}
    return NULL;
}}

// {sep}
// END OF FILE
// {sep}
    """

    # *************
    return result
    # *************
    
## ============================================================
##  End of File
## ============================================================

