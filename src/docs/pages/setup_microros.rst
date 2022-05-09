
Build MicroROS MCU Firmware
=====================


Create a build directory and download Docker image
--------------------------

Currently the build tools are based on Docker.  We will do it this way for now but I'd like to not use docker and not everybody is going to have docker installed

.. code-block:: console

   mkdir ~/micro_ros
   cd ~/micro_ros
   docker run -it --net=host -v /dev:/dev --privileged ros:galactic
   


   

Build steps
----------------------

We are going to use CubeMX to generate a CubeIDE project for the STM32 MCU as a make project.  This will also allow us to use whatever STM developement board we want.

- Import the template configuration file nucleof446re_uros_template.ioc 
  **** Note that there is a bit odf a chicken and egg issue here.  This file is generated from compiling the microros project but we need it to build the project.
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







Running a Working MicroROS Build
=====================


Now we have finally built a microros instance on our microcontroller and have the agent build and installed on the host.
Its finally time to run it and see if everything is working.


# Start the Agent (doesn't matter what the microcontroll is programmed for.  This is just a bridge)
.. code-block:: console
  
  ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyACM0

**Note this is easy to remember if you think about the fact you are running the micro_ros_agent package from within contains the micro_ros_agent executable and connecting by serial to /dev/ttyACM0


Alternatively, you can connect via the device ID which is a long string of characters and requires the ability to copy and paste into you terminal
.. code-block:: console

  ls /dev/serial/by-id/*




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

