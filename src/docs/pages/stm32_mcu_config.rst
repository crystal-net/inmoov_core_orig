
Setup the microcontroller using STMCubeMX
=====================

Objective
-----------------------------------
Next we need to setup our microcontroller.  The microros project officially supports a small number of boards.
We are currently developing with one of these boards but I thing it would be prudent to make this as portable as possible.

Here, we are going to aim at supporting most STM32 microcontroller dev boards.

The micro_ros instructions also don't go into great detail on how to get a working STM32CubeIDE working.  I think this is a fantastic tool and so below are the instructions to get it configured.

And yes.  This means that we are going to work with two different IDE's  I like VSCode but unfortunately support for STM32 MCU's is not great.  I might explore this later but for now we are going to use CubeIDE.



- Create a new project using your microcontroller.
- Select Yes to initialize the defaults.  I do this because it sets up most periferals including the push button which we will use to test microros
- Configure:
    * USART
    * freeRTOS
    * Project / Makefile
- Save the project to your cubeIDE workspace folder

- open CubeMX and import as a Makefile project (select the folder) and close CubeMX
- Edit the make file - AT this point i opened CubeMX and tested a build by selecting the main.c file and building.  Everything should build complete.  I am going to close it and add in the extras and see what happens.
    - At this point I think we may need to do a build from the command line but maybe not?  I don't want to use docker but it looks like I have to?
    - At this poing I did a backup and compiled as is.  I got an error about something like Multithread missing.  Its an ifdef so I don't think its needed. but maybe it won't compile becasue the extra packages are missing
- change into that workspace folder (ex. uros_nucleo_f466re)
- Clone the cubeMX utils into the folder ( git clone https://github.com/micro-ROS/micro_ros_stm32cubemx_utils )
- enter into that folder
- Fix ^m if needed


