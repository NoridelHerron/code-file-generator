-- ===========================================================
-- Project Name: 
-- Description :
--
-- File Name   : vhdl_comb_test.vhd
-- Dependencies:
-- Author      : Noridel
-- Date        : 2026-01-07 22:25:26
-- ===========================================================

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- CUSTOMIZED PACKAGE
-- library work;
-- use work.xxxxxxx.all;

entity vhdl_comb_test is
    port (

        -- User/s
        -- add ports here
        
    );
end vhdl_comb_test;

architecture rtl of vhdl_comb_test is

begin

    -- Combinational logic
    -- If only simple concurrent assignments are needed,
    -- this process can be safely removed.
    process(all)
    begin
        -- logic here
    end process;
    
end rtl;
