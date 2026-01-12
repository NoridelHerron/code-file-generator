
## ============================================================
## Project Name: 
## Description :
##
## File Name   : embedded_genFile.py
## Dependencies:
## Author      : Noridel Herron
## Date        : 2026-01-11 11:29:00
## ============================================================

from utilities.user_prompt import (
    ask_author_name,
    Out_directory
)

from utilities.shared_helpers import (
    save_file
)

from .thread_content import Thread_Info
from .user_prompts import Get_Purpose
from .helper_functions import Decode_Purpose
from .m1_process import Process_FileContent

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

    if purpose == "t" or ((purpose == "m1" or purpose == "m2") and num_threads > 0):
        # =========================================================
        # Save one output file per thread name + .h with all 
        # the thread names
        # =========================================================
        thread_names = Thread_Info( 
                            author,
                            folder_name,
                            purpose,
                            num_threads )
        
        # =========================================================
        # Save .c file if m1 or m2
        # =========================================================
        if purpose == "m1":
            process1 = Process_FileContent( 
                            "process1",
                            author,
                            purpose,
                            thread_names )

            save_file( "process1" + ".c", process1, folder_name)

        elif purpose == "m2":
            process2 = Process_FileContent( 
                            "process2",
                            author,
                            purpose,
                            thread_names )

            save_file( "process2" + ".c", process2, folder_name)
                
    
                
        
    
    

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

