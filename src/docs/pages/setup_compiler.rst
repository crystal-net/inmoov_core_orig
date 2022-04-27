
Setup IDE and Compilers
=======================



VS Code IDE for building ROS2
--------------------------
Install VS Code.

.. code-block:: console

   wget https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64
   sudo dpkg -i code_1.63.2-1639562499_amd64.deb



Install STM32CubeIDE and STM32CubeMX
--------------------------
In order to build MicroROS for your STM32 microcontroller dev board, we will also be
using STM32CubeIDE in order to build and transfer our binaries and STM32CubeMX to
configure the HAL and CMSIS packages.  The two IDEs go hand in hand.

UPDATED 2022/01/11
First create a repository in your github account (or clone mine).  Then.

.. code-block:: console

   mkdir ~/ros2_ws
   cd ~ros2_ws
   git init 
   git add README.md 
   git commit -m "first commit"
   git branch -M main 
   git remote add origin https://github.com/crystal-net/inmoov_ros2.git  (or what ever your git repo is)
   git push -u origin main


   


Your directory structure should now look like the following

.. code-block:: console

   ~/catkin_ws
      .vscode/
      build/
      devel/
      src/
      ROS_WS.code-workspace

   


Colcon command line autocomplete

.. code:: console
   
   echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc



building with the Pi-Pico:   Follow these instructions:
   https://ubuntu.com/blog/getting-started-with-micro-ros-on-raspberry-pi-pico





