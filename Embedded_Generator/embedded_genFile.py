
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

from .ipc_content import (
    IPC_FileContent, 
    IPC_packageContent
)

from .header                  import IPC_Header_FileContent
from utilities.shared_helpers import save_file
from .thread_content          import Thread_Info
from .user_prompts            import Get_Purpose    
from .helper_functions        import Decode_Purpose
from .m1_process              import Process_FileContent

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
    
    elif purpose == "ipc":
                
        shm_name     = input( "Enter shared memory / semaphore name: " ).strip()
        packet_type  = input( "Enter shared packet type (struct type name | name_packet_t): " ).strip()
        magic_define = input( "Enter shared memory magic macro: " ).strip().upper()
        mem_addr     = input( "Enter memory address (0x46494F4E): " ).strip()

        # remove leading slash if present
        if shm_name.startswith("/"):
            shm_name = shm_name[1:]

        # normalize base name
        if shm_name.endswith("_shm"):
            base = shm_name[:-4]
        else:
            base = shm_name

        shm_name = base + "_shm"
        sem_name = base + "_sem"

        if not packet_type.endswith("_t"):
            packet_type += "_t"

        ipc_h = IPC_Header_FileContent( 
                            "ipc", 
                            author,
                            packet_type )  

        content = IPC_FileContent(
                        purpose,
                        author,
                        shm_name,
                        sem_name,
                        packet_type,
                        magic_define
                    )
        
        ipc_pkg = IPC_packageContent( "ipc_pkg", 
                        author,
                        packet_type, 
                        magic_define,
                        mem_addr)

        save_file( "ipc" + ".h", ipc_h, folder_name)
        save_file( "ipc_pkg" + ".h", ipc_pkg, folder_name)
        save_file( "ipc" + ".c", content, folder_name)

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

