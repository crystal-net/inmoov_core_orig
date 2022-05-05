
Setup Ubuntu and Build a Workspace
==================================


Source info for setting up the workstation is at: https://github.com/RoboGnome/VS_Code_ROS



Create a Project Directory
--------------------------
The code below will install the base ROS2 Packages

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





