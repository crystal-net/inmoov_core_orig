
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



# Source the ROS 2 installation
.. code-block:: console

  source /opt/ros/$ROS_DISTRO/setup.bash


# Create a workspace and download the micro-ROS tools
.. code-block:: console

  mkdir microros_ws
  cd microros_ws
  git clone -b $ROS_DISTRO https://github.com/micro-ROS/micro_ros_setup.git src/micro_ros_setup


# Update dependencies using rosdep
.. code-block:: console

  sudo apt update && rosdep update
  rosdep install --from-path src --ignore-src -y



# Install pip
.. code-block:: console

  sudo apt-get install python3-pip


# Build micro-ROS tools and source them
.. code-block:: console

  colcon build
  source install/local_setup.bash

# now build the firmware
.. code-block:: console

  ros2 run micro_ros_setup create_firmware_ws.sh freertos nucleo_f446re



# Start the Agent (doesn't matter what the microcontroll is programmed for.  This is just a bridge)
.. code-block:: console
  
  ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyACM0





Summary
Create a microros Directory
Download microros from git
Build the project using for FreeRTOS on Nucleo446 board
This will create an nucleo_f446re.ioc file we will use to start the project
Startup STM32CubeIDE and create a new project using the IOC file in a new directory called uros (or something sensible)
Close STM32CubeIDE
Open STM32CubeMX
Chnage the project to use MakeFile
Update Make file with instructions from the repo at https://github.com/micro-ROS/micro_ros_setup.git
From here on in don't generate new code using IDE because the Makefile toolchain will get deleted.
Close CubeMX and load CubeIDE
Update the include paths





