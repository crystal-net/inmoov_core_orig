
Setup Ubuntu and ROS2
=====================

Setup Ubuntu if you haven't already
-----------------------------------
These are modified instructions I created from this tutorial: https://micro.ros.org/docs/tutorials/core/first_application_rtos/freertos/

Currently the instructions are using Docker to downlaod the build system.  I think this is silly and will be attempting to remove this later but for now we will keep it till I know more.



Create a Project Directory
--------------------------
The code below will install the base ROS2 Packages

UPDATED 2022/01/11
First create a repository in your github account (or clone mine).  Then.

.. code-block:: console

   mkdir ~/micro_ros
   cd ~/micro_ros
   docker run -it --net=host -v /dev:/dev --privileged ros:galactic
   


   


   

Basic Steps
----------------------

- Use CubeMX to generate a CubeIDE project for the STM32 MCU as a make project.  
- Import the template configuration file nucleof446re_uros_template.ioc 
  **** Note that there is a bit of a chicken and egg issue here.  This file is generated from compiling the microros project but we need it to build the project.
  **** For the purpose of this project I am going to provide my modified file already setup for you.

- Click Generate Code in the top left
- Open CubeIDE
- Open project we just generated code for




docker pull microros/micro_ros_static_library_builder:galactic && docker run --rm -v ${workspace_loc:/${ProjName}}:/project --env MICROROS_LIBRARY_FOLDER=micro_ros_stm32cubemx_utils/microros_static_library_ide microros/micro_ros_static_library_builder:galactic