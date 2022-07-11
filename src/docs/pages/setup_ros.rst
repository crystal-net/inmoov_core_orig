
Setup ROS2 and Required Packages
================================



Install Extra packages
----------------------


Install ros-galactic-rviz2

.. code:: console

   sudo apt install ros-galactic-rviz2
   


Colcon command line autocomplete

.. code:: console
   
   echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc




The code below will install the base ROS2 Packages

.. code-block:: console

   sudo apt install ros-galactic-desktop



For manual control of the joints during development, we need the robot_state_publiser and joint_state_publisher

.. code-block:: console
   
   sudo apt install ros-galactic-robot-state-publisher
   sudo apt install ros-galactic-joint-state-publisher
   sudo apt install ros-galactic-joint-state-publisher-gui
   




Packages for Naviation (Nav2): 

.. code-block:: console

   sudo apt install ros-galactic-navigation2 ros-galactic-nav2-bringup



Install Ignition-Fortress 
Instructions from: https://gazebosim.org/docs/fortress/install_ubuntu

.. code-block:: console

   sudo apt-get update
   sudo apt-get install lsb-release wget gnupg
   sudo wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
   sudo apt-get update
   sudo apt-get install ignition-fortress



Packages for old Gazebo ros-galactic-gazebo-ros2-control

.. code-block:: console

   sudo apt install ros-galactic-gazebo-ros2-control ros-galactic-gazebo-ros2-control-demos



Packages for building micro-ros-agent

.. code-block:: console

   sudo apt install build-essential cmake gcc-arm-none-eabi libnewlib-arm-none-eabi doxygen git python3



building with the Pi-Pico:   Follow these instructions:
   https://ubuntu.com/blog/getting-started-with-micro-ros-on-raspberry-pi-pico



Other packages

.. code-block:: console

   sudo apt-get install ros-$ROS_DISTRO-osrf-testing-tools-cpp
   sudo apt-get install ros-$ROS_DISTRO-test-msgs





Colcon command line autocomplete

.. code:: console
   
   echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc




Inmoov Message Publisher and Subscriber node
--------------------------------------------

This was developed with the tutorial located at: https://docs.ros.org/en/rolling/Tutorials/Writing-A-Simple-Cpp-Publisher-And-Subscriber.html
I realize this is for the rolling branch but I figure it won't change much and if it does change we want the latest information
The author for this info is at https://www.allisonthackston.com/.  I think it is worth having a look at some of her material.  I have no affiliation otherwise.

Info: Publisher and subscriber nodes are a many to many transport.  
There can be many subscribers that don't know who will be getting the messages or that anybody is actually receiving them.
There can also be many subscribers that don't always know who published the message on the topic.
This is good for constant data where it does not need to be ephemeral.


Inmoov Service Message Nodes
----------------------------
This was developed with the tutorial located at: https://docs.ros.org/en/rolling/Tutorials/Writing-A-Simple-Cpp-Service-And-Client.html

Sevices in ROS2 differ from topics in that they are are procedures that can be requested on a synchronous 1-on-1 basis.  
Meaning that the client requests that service and waits for the response.

We will be using services to request data that requires some kind of calcualtion or processing.
I don't believe we will be relying on this much as I don't want to make any part of the robot reliant on any piece of data and may otherwise fail.



