
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

def Thread_HeaderFile( file_name,
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

    # *************
    return result
    # *************

## ****************************************

def IPC_Header_FileContent(
        file_name,
        author,
        packet_type
    ):

    header = Print_Header(
                file_name,
                author,
                "//",
                ".h"
            )

    sep = Print_Sep()

    # Remove "_t" to get struct tag
    struct_tag = packet_type[:-2]

    result = f"""
{header}

#ifndef IPC_INTERFACE_H
#define IPC_INTERFACE_H

#include "ipc_pkg.h"

/* Initialize shared memory and synchronization primitives */
int  ipc_init(void);

/* Release IPC resources */
void ipc_cleanup(void);

/* Write latest packet into shared memory */
void ipc_send_packet(const {packet_type} *pkt);

/* Read latest packet from shared memory */
int  ipc_receive_packet({packet_type} *pkt);

#endif /* IPC_INTERFACE_H */

// {sep}
// End of File
// {sep}
"""
    # *************
    return result
    # *************


## ============================================================
##  End of File
## ============================================================

