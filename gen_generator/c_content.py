
## ============================================================
## Project Name: File Generator
## Description :
##
## File Name   : c_content.py
## Dependencies:
## Author      : Noridel Herron
## Date        : 2026-01-09 16:51:04
## ============================================================

## ============================================================
##  Function/s Only
## ============================================================

def Print_C_Sources( lib, 
                     sep ):
    
    result = f"""{lib}
int main(void)
{{
    return 0;
}}

// {sep}
//  End of File
// {sep}
"""
    # *************
    return result
    # *************

## ************************************************************

def Print_C_headers( guard, 
                     lib, 
                     sep ):
    result = f"""#ifndef {guard}
#define {guard}
{lib}

#endif /* {guard} */

// {sep}
//  End of File
// {sep}
"""
    # *************
    return result
    # *************

## ============================================================
##  End of File
## ============================================================

