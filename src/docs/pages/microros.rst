
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
source /opt/ros/$ROS_DISTRO/setup.bash

# Create a workspace and download the micro-ROS tools
mkdir microros_ws
cd microros_ws
git clone -b $ROS_DISTRO https://github.com/micro-ROS/micro_ros_setup.git src/micro_ros_setup

# Update dependencies using rosdep
sudo apt update && rosdep update
rosdep install --from-path src --ignore-src -y

# Install pip
sudo apt-get install python3-pip

# Build micro-ROS tools and source them
colcon build
source install/local_setup.bash

# now build the firmware
ros2 run micro_ros_setup create_firmware_ws.sh freertos nucleo_f446re

