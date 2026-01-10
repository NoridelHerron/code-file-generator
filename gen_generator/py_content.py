
## ===========================================================
## Project Name: File Generator
## Description :
##
## File Name   : py_content.py
## Dependencies:
## Author      : Noridel Herron
## Date        : 2026-01-09 13:07:19
## ===========================================================

## ===========================================================
## Function only
## ===========================================================

def Print_Py_Content(lib, sep, func):
    content = f"""
{lib}
## from <add the source> import <add what's need to be imported>

## {sep}
##  Function/s Only
## {sep}
{func}
def main():
    pass
    
## {sep}
##  Main Only
## {sep}

if __name__ == "__main__":
    main()
    
## {sep}
##  End of File
## {sep}
"""
    # ************
    return content
    # ************

## ===========================================================
## End of File
## ===========================================================
