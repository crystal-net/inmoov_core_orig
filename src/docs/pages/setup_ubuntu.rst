
Setup Ubuntu and ROS2
=====================

Automated script
-----------------------------------
I have included here an unattend file for installing Ubuntu in a way that is going to work for this build.
Of course do NOT use this on a system that you already are using or has important data.

If you want to install Ubuntu Manually and pick your options this is perfectly acceptable.


Source info for setting up the workstation is at: https://github.com/RoboGnome/VS_Code_ROS
And here: https://github.com/athackst/vscode_ros2_workspace


Non-ROS packages
--------------------------
These packages are just used to support different aspects of the overall environment.  Mostly just to make life easier.


.. code-block:: console

sudo apt install apt-transport-https



Install VS Code.

.. code-block:: console

   wget https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64
   sudo dpkg -i code_1.63.2-1639562499_amd64.deb



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





