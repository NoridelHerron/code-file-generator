
## ============================================================
## Project Name: 
## Description :
##
## File Name   : user_prompts.py
## Dependencies:
## Author      : Noridel Herron
## Date        : 2026-01-11 11:37:31
## ============================================================


## ============================================================
##  Function/s Only
## ============================================================

def Get_Purpose():
    """
    Prompt the user to specify the purpose/type of the generated file.

    Options:
        M1  = Main Process 1 (may contain multiple threads)
        M2  = Main Process 2
        T   = Thread-only file
        IPC = IPC-related file

    Returns:
        str: Encoded purpose string.
             Examples:
                "m12"  -> Main Process 1 with 2 threads
                "m2"   -> Main Process 2
                "t4"   -> Thread file with 4 threads
                "ipc"  -> IPC file
    """

    # *************
    while True:

        # ==============================================================
        # Prompt user to select the purpose of the file being generated
        # ==============================================================
        purpose = input(
            "M1  = Main Process 1\n"
            "M2  = Main Process 2\n"
            "T   = Thread\n"
            "IPC = IPC\n"
            "Select purpose: "
        ).strip().lower()

        # =========================================================
        # Purposes that require a thread count
        # =========================================================
        if purpose in ["m1", "t"]:
            num_thread = input(
                "Enter number of thread(s): "
            ).strip()

            if not num_thread.isdigit() or int(num_thread) <= 0:
                print("[ERROR] Thread count must be a positive number.\n")
                continue

            # **************************
            return purpose + num_thread
            # **************************

        # =========================================================
        # Purposes without thread counts
        # =========================================================
        elif purpose in ["m2", "ipc"]:

            # *************
            return purpose
            # *************
        # =========================================================
        # Invalid selection
        # =========================================================
        else:
            print("\n[ERROR] Invalid selection. Please choose again.\n")


## ****************************************

def Get_Thread_Names(num_threads):
    """
    Prompt user for thread names and return a list of names.

    Args:
        num_threads (int): Number of threads to name

    Returns:
        list[str]: Thread names (length == num_threads)
    """
    names = []

    if num_threads <= 0:
        return names

    use_names = input("Do you want to name the threads? (y/n): ").strip().lower()

    if use_names != "y":
        # Auto-generate default names
        # *************************************************
        return [f"thread_{i}" for i in range(num_threads)]
        # *************************************************

    for i in range(num_threads):
        while True:
            name = input(f"Name for thread {i} (No need to include '_thread'): ").strip()

            if not name:
                print("Name cannot be empty.")
                continue

            if name in names:
                print("Duplicate thread name. Choose a unique name.")
                continue

            names.append(name)
            break

    # *************
    return names
    # *************

## ****************************************

def Thread_Command(cmd=False):
    result = ""
    # *************
    return result
    # *************

## ****************************************

def Function_Name():
    # *************
    return
    # *************

    
## ============================================================
##  End of File
## ============================================================

