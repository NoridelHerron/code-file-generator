
## ============================================================
## Project Name: 
## Description :
##
## File Name   : embedded_genFile.py
## Dependencies:
## Author      : Noridel Herron
## Date        : 2026-01-11 11:29:00
## ============================================================

from utilities.shared_helpers import (
    save_file,
)

from utilities.user_prompt import (
    ask_author_name,
    Out_directory
)

from .user_prompts import (
    Get_Purpose,
    Get_Thread_Names )

from .helper_functions import (
    Decode_Purpose
)

from .thread_content import (
    Thread_FileContent,
)

from .header import (
    Thread_HeaderFile
)

## ============================================================
##  Function
## ============================================================

def main():
    """
    Entry point for the code / Embedded generator.
    Dispatches generation logic based on selected purpose.
    """

    # =========================================================
    # Get purpose and decode configuration
    # =========================================================
    author               = ask_author_name()
    folder_name          = Out_directory()
    purpose_code         = Get_Purpose()
    purpose, num_threads = Decode_Purpose(purpose_code)

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
                    purpose, 
                    "threads",
                    author,
                    thread_names )
        
        save_file( "threads.h", file_h, folder_name)

    else:
        thread_names = []

    

    # ============================================================
    # Switch-style dispatch
    # ============================================================

    # ============================================================
    # Done
    # ============================================================

    print("[INFO] Generation complete")

    
## ============================================================
##  Main Only
## ============================================================

if __name__ == "__main__":
    main()
    
## ============================================================
##  End of File
## ============================================================

