
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

from gen_generator.std_lib import Standard_Lib
from utilities.shared_helpers import save_file
from .header import Thread_HeaderFile
from .user_prompts import Get_Thread_Names

## ============================================================
##  Function/s Only
## ============================================================

def Thread_FileContent(
        fileName = "",
        fileType = "",
        author   = ""
):
    header = Print_Header(
                fileName + "_thread", 
                author, 
                "//", 
                ".c" )
    
    body   = Thread_Content(fileName)
    lib    = Standard_Lib(fileType)

    result = f"""{header}
{lib}{body}

    """
    
    # *************
    return result
    # *************

## ****************************************

def Thread_Content(name):

    sep = Print_Sep()

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

## ****************************************

def Thread_Info( author,
                 folder_name,
                 purpose,
                 num_threads ):

    # =========================================================
    # Collect thread names if applicable
    # =========================================================

    if num_threads > 0:
        thread_names = Get_Thread_Names(num_threads)

        # =====================================================
        # Generate one output file per thread name 
        # =====================================================

        for name in thread_names:
            content  = Thread_FileContent(
                            fileName = name,
                            fileType = purpose,
                            author   = author )

            # Unique file per thread (prevents overwriting)
            file_name = f"{name}_thread.c"

            save_file( file_name, 
                       content, 
                       folder_name )

        file_h = Thread_HeaderFile( 
                    "threads",
                    author,
                    thread_names )
        
        save_file( "threads.h", file_h, folder_name)

    else:
        thread_names = []

    # ******************
    return thread_names
    # ******************
    
## ============================================================
##  End of File
## ============================================================

