
## ============================================================
## Project Name: 
## Description :
##
## File Name   : m1_process.py
## Dependencies:
## Author      : Noridel Herron
## Date        : 2026-01-12 12:10:08
## ============================================================

from utilities.shared_helpers import (
    Print_Header,
    Print_Sep
)

from gen_generator.std_lib import Standard_Lib

## ============================================================
##  Function/s Only
## ============================================================

def Pthread_Create_Function(thread_names):

    result = "\n\t".join(
        f"pthread_create(&{name}_t, NULL, {name}_thread, NULL);"
        for name in thread_names
    )

    # *************
    return result
    # *************

## ****************************************

def Pthread_Join_Function(thread_names):

    result = "\n\t".join(
        f"pthread_join({name}_t, NULL);"
        for name in thread_names
    )
    
    # *************
    return result
    # *************

## ****************************************

def Pthread_Decl_Function(thread_names):
    
    result = "\n\t".join(
        f"pthread_t {name}_t;"
        for name in thread_names
    )

    # *************
    return result
    # *************

## ****************************************

def Process_Content( 
        header, 
        lib,
        thread_decl,
        create_block,
        join_block,
        sep ):
    
    result = f"""
{header}
{lib}
int main(void)
{{
    {thread_decl}

    if (ipc_init() < 0) {{
        fprintf(stderr, "IPC init failed\\n");
        return 1;
    }}

    /* Start the Threads */
    {create_block}

    /* Wait for Threads */
    {join_block}

    /* Clean up */
    ipc_cleanup();

    return 0;
}}

// {sep}
// END OF FILE
// {sep}
    """

    # *************
    return result
    # *************

## ****************************************

def Process_FileContent( file_name,
                          author,
                          purpose,
                          thread_names):

    sep          = Print_Sep()
    lib          = Standard_Lib(purpose)

    header       = Print_Header(
                        file_name,
                        author,
                        "//",
                        ".c" )
    
    create_block = Pthread_Create_Function(thread_names)
    join_block   = Pthread_Join_Function(thread_names)
    thread_decl  = Pthread_Decl_Function(thread_names)

    result = Process_Content( 
                header, 
                lib,
                thread_decl,
                create_block,
                join_block,
                sep )
    
    # *************
    return result
    # *************

## ============================================================
##  End of File
## ============================================================

