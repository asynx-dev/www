---
description: MIG "init_calib_complete" signal does not go high during simulation
author: Yunus Esergün
date: 2020-10-21
---
# MIG "init_calib_complete" signal does not go high

For a project, which utilizes 7-Series, I should use PL memory and **MIG** is
the best IP choice for this purpose. In many websites, including [Xilinx
documents](https://www.xilinx.com/support/documentation/ip_documentation/mig_7series/v4_1/ug586_7Series_MIS.pdf),
you can find how to configure MIG IP. Even if there are many configuration
parameters in MIG IP, if you know where to look, it is so easy to build it.

After configuring your 7-Series MIG, you will notice that there is an important
signal called `init_calib_complete`. Calibration is the first stage of MIG if
you run the code. MIG arranges phasors, clocks, etc and small write-read test
with the help of 200 MHz reference clock in calibration stages, which detailed
information can be found via [this
link](https://www.xilinx.com/support/answers/51954.html).

However, if you debug your code,regardless of whether you choose "**Debug
Signals for Memory Controller**" Mode On or not, and if `init_calib_complete`
signal is not high, you cannot reach your PL memory (Even your PS memory), so
AXI transaction error can show up. Therefore, there are some checkpoints that
you should be sure about. I have listed step by step what you should check to
correct calibration stage and use your PL memory:

**1)** **Check MIG Parameters** → As stated before, in MIG, there are tons of
parameters especially PL memory port configuration, which can confuse a person
so much. Therefore, if you have a problem with `init_calib_complete` signal,
you should check your MIG configuration. I have listed the most important
parameters and stages that you should be careful about below:
<!--markdownlint-disable MD013-->
Page Name|Setting Name|Instruction
---------------|-----------|---------------------------------------------------------
**Options for Controller**|**Clock Period Parameter**|You should know which frequency at most your PL memory can reach. Otherwise, because if your PL memory does not support the frequency that it can, probably you will not be able to make your memory work.
**Options for Controller**|**Memory Part**| For your FPGA, there are many Xilinx documents that you can learn which memory part your FPGA's PL memory utilizes. You should search and choose the right one.
**Memory Options for Controller**|**Input Clock Period**|In addition to the memory part, you should also search about the system clock frequency and choose the right period.
**Pin Selection for Controller**|-|This part is the most confusing and important part for MIG configuration. Again, you should search about the ports and connect ports correctly. This situation is the same for when you choose the ports for `sys_clk`, `clk_ref` and `sys_rst` signals in "**System Signals Selection**" part.
<!--markdownlint-enable MD013-->
**2)** **Check All Resets** → There are 3 resets in MIG, which are `sys_rst`,
`aresetn` and `ui_clk_sync_rst`. If you do not connect `sys_rst pin` to a port
from your FPGA and you want to give it a signal, do not choose `ui_clk_sync_rst`
because if you choose it, `sys_rst` will never be high (if it is chosen as
active-low) and so `ui_clk_sync_rst` will never be low (because it is
active-high). As a result, this can cause that "`init_calib_complete`" signal
will stay low.

**3)** **Check All Clocks** → If you do not connect your reference clock to a
port (If you choose no buffer option for `clk_ref`), please be sure that you
give 200 MHz to it. Otherwise, calibration stage will start but never finish
because of the clock.

**4)** **Check Data Mask** → In the Options for Controller page of MIG
interface, there is an option called **Data Mask**. If you do not utilize AXI4
user interface feature, you have a chance to change this option and please
choose the option. If you use AXI4 user interface with 72 data width, it is
automatically unselected. In this situation, please decrease data width bits and
select **Data Mask** option. People utilize 72 bits data width feature
generally for using ECC (Error Correction Code). If you really have to use this
option, then you cannot select **Data Mask** option and you should write a
logic, which I do not know how much it can be hard, because AXI has byte enables
which requires DM pins. This situation is mentioned in [this Xilinx forum
thread](https://forums.xilinx.com/t5/Memory-Interfaces-and-NoC/MIG-7-Series-2018-2-Cannot-disable-data-mask-dm/td-p/974993).

Finally, after checking this corner case situations, if your MIG does not still
work, you should check the situations over and over to finally make it work.
