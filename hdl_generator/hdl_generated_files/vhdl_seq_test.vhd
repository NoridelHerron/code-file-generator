-- ===========================================================
-- Project Name: 
-- Description :
--
-- File Name   : vhdl_seq_test.vhd
-- Dependencies:
-- Author      : Nori
-- Date        : 2026-01-07 22:25:47
-- ===========================================================

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- CUSTOMIZED PACKAGE
-- library work;
-- use work.xxxxxxx.all;

entity vhdl_seq_test is
    port (

        clk : in std_logic;
        rst : in std_logic
    
    );
end vhdl_seq_test;

architecture rtl of vhdl_seq_test is

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
