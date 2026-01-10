-- ============================================================
-- Project Name: 
-- Description :
--
-- File Name   : vhdl_s.vhd
-- Dependencies:
-- Author      : jksdjk
-- Date        : 2026-01-10 11:54:49
-- ============================================================

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- CUSTOMIZED PACKAGE
-- library work;
-- use work.xxxxxxx.all;

entity vhdl_s is
    port (

        clk : in std_logic;
        rst : in std_logic
    
    );
end vhdl_s;

architecture rtl of vhdl_s is

begin

    process(clk, rst)
    begin
        if rst = '1' then
            -- reset logic
        elsif rising_edge(clk) then
            -- logic here
        end if;
    end process;
    
end rtl;
