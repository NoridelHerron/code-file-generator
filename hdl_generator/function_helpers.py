# ============================================================
# function_helpers.py
# Description:
#
# Author: Noridel Herron
# Date  : 2026-01-06 23:13:23
# ============================================================

from datetime import datetime

# ==============================================================================
def Get_time_and_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ==============================================================================
def Print_Sep():
    return "=" * 59

# ==============================================================================
def Get_author_name(author="", comment=""):
    return (
        f"Author      : {author}"
        if author else
        f"Author      :"
    )

# ==============================================================================
def Print_Header(entity_name, author, hdl_type, file_ext):
    timestamp = Get_time_and_date()
    sep       = Print_Sep()
    comment   = "--" if hdl_type == "vhdl" else "//"
    header    = f"""{comment} {sep}
{comment} Project Name: 
{comment} Description :
{comment}
{comment} File Name   : {entity_name}.{file_ext}
{comment} Dependencies:
{comment} {author}
{comment} Date        : {timestamp}
{comment} {sep}"""

    return header

# ==============================================================================
def Print_Port_comments(hdl_type):
    if hdl_type == "vhdl":
        result = """
        -- User/s
        -- add ports here
        """
        
    else:
        result = """
        // User/s
        // I/O
        """ 
    return result

# ==============================================================================
def Print_Seq_Port(hdl_type):
    if hdl_type == "vhdl":
        result = """
        clk : in std_logic;
        rst : in std_logic
    """
    else:
        result = """
    input clk,
    input rst
"""
    return result

# ==============================================================================
def Print_Seq_Body(hdl_type):
    if hdl_type == "vhdl":
        result = """
    process(clk, rst)
    begin
        if rst = '1' then
            -- reset logic
        elsif rising_edge(clk) then
            -- logic here
        end if;
    end process;
    """
        
    elif hdl_type == "sv":
        result = """
always_ff @(posedge clk or posedge rst) begin
    if (rst) begin
        // reset logic
    end else begin
        // logic here
    end
end
    """
    
    else:
        result = """
always @(posedge clk or posedge rst) begin
    if (rst) begin
        // reset logic
    end else begin
        // logic here
    end
end
    """  
    return result

# ==============================================================================
def Print_Comb_Body(hdl_type):
    if hdl_type == "vhdl":
        result = """
    -- Combinational logic
    -- If only simple concurrent assignments are needed,
    -- this process can be safely removed.
    process(all)
    begin
        -- logic here
    end process;
    """ 
        
    elif hdl_type == "sv":
        result = """
always_comb begin
    // logic here
end
    """
    
    else:
        result = """
always @(*) begin
    // logic here
end
"""  
    return result

# ==============================================================================
def Print_Package_Body(package_name, hdl_type):
    if hdl_type == "vhdl":
        result = f"""
package {package_name}_pkg is

    -- constants
    -- types
    -- subtypes
    -- function/procedure declarations

end package {package_name}_pkg;

package body {package_name}_pkg is

    -- function/procedure implementations

end package body {package_name}_pkg;
"""
    
    elif hdl_type == "sv":
        result = f"""

package {package_name}_pkg;

    // parameters
    // typedefs
    // localparams
    // functions

endpackage
"""
    else:
        result = f"""

`ifndef {package_name.upper()}_PKG_VH
`define {package_name.upper()}_PKG_VH

// parameters
// `define MACROS
// localparams

`endif
"""
    return result
# ==============================================================================



