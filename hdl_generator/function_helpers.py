# ============================================================
# function_helpers.py
# Description:
#
# Author: Noridel Herron
# Date  : 2026-01-06 23:13:23
# ============================================================

from utilities.shared_helpers import (
    Print_Sep )

# ==============================================================================
# ==============================================================================

def Print_Port_comments(ext):
    if ext == "vhdl":
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
# ==============================================================================

def Print_Seq_Port(ext):
    if ext == "vhdl":
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
# ==============================================================================

def Print_Seq_Body(ext):
    if ext == "vhdl":
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
    elif ext == ".sv":
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
# ==============================================================================

def Print_Comb_Body(ext):
    if ext == "vhdl":
        result = """
    -- Combinational logic
    -- If only simple concurrent assignments are needed,
    -- this process can be safely removed.
    process(all)
    begin
        -- logic here
    end process;
    """   
    elif ext == ".sv":
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
# ==============================================================================
def Print_Package_Body( package_name, 
                        ext, 
                        sep ):
    
    star = Print_Sep(True)
    
    if ext == ".vhd":
        result = f"""
package {package_name} is

    -- constants
    -- types
    -- subtypes
    -- function/procedure declarations

end package {package_name};

-- {star}

package body {package_name} is

    -- function/procedure implementations

end package body {package_name};

-- {sep}
-- END OF FILE
-- {sep}
""" 
    elif ext == ".svh":
        result = f"""

package {package_name}_pkg;

    // parameters
    // typedefs
    // localparams
    // functions

endpackage

// {sep}
// End of File
// {sep}
"""
    else:
        result = f"""

`ifndef {package_name.upper()}_VH
`define {package_name.upper()}_VH

// parameters
// `define MACROS
// localparams

`endif

// {sep}
// END OF FILE
// {sep}
"""
    return result
