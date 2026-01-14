
## ============================================================
## Project Name: 
## Description :
##
## File Name   : helper_functions.py
## Dependencies:
## Author      : Noridel Herron
## Date        : 2026-01-11 13:32:47
## ============================================================

## from <add the source> import <add what's need to be imported>

## ============================================================
##  Function/s Only
## ============================================================

def Decode_Purpose(purpose_code):
    """
    Decode the encoded purpose string returned by Get_Purpose().

    Args:
        purpose_code (str): Encoded purpose string.
                            Examples:
                                "m12"  -> Main Process 1, 2 threads
                                "m2"   -> Main Process 2
                                "t4"   -> Thread-only file, 4 threads
                                "ipc"  -> IPC file

    Returns:
        tuple:
            purpose (str): One of ("m1", "m2", "t", "ipc")
            num_threads (int): Number of threads (0 if not applicable)
    """

    # Defaults
    purpose     = ""
    num_threads = 0

    # Normalize input
    code = purpose_code.strip().lower()

    # ============================================================
    # Switch-style decoding
    # ============================================================

    if code.startswith("m1"):
        purpose     = "m1"
        num_threads = int(code[2:])

    elif code.startswith("m2"):
        purpose     = "m2"
        num_threads = int(code[2:])

    elif code.startswith("t"):
        purpose     = "t"
        num_threads = int(code[1:])

    elif code in ("ipc"):
        purpose     = "ipc"
        num_threads = 0

    else:
        print(f"[ERROR] Invalid purpose code: {purpose_code}")

    # **************************
    return purpose, num_threads
    # **************************


def Function_Name():
    # *************
    return
    # *************

## ****************************************

def Function_Name():
    # *************
    return
    # *************

## ****************************************

def Function_Name():
    # *************
    return
    # *************

## ****************************************

def Function_Name():
    # *************
    return
    # *************
    
## ============================================================
##  End of File
## ============================================================

