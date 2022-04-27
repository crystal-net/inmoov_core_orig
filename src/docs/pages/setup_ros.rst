
Setup ROS2 and Required Packages
================================



Support Packages
--------------------------
These packages are not part of ROS2 but are needed to install the binary packages


.. code-block:: console

sudo apt install apt-transport-https



Install VS Code.

.. code-block:: console

   wget https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64
   sudo dpkg -i code_1.63.2-1639562499_amd64.deb




Install Extra packages
----------------------

.. code:: console

   sudo apt install ros-galactic-rviz2
   sudo apt install ros-galactic-joint-state-publisher-gui ros-galactic-joint-state-publisher
   sudo apt install 



Colcon command line autocomplete

.. code:: console
   
   echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc




The code below will install the base ROS2 Packages

.. code-block:: console

   sudo apt install ros-galactic-desktop




We need these packages for Gazebo

.. code-block:: console

   sudo apt install ros-galactic-gazebo-ros2-control




Packages for Naviation (Nav2): 

.. code-block:: console

   sudo apt install ros-galactic-navigation2 ros-galactic-nav2-bringup




Packages for Gazebo ros-galactic-gazebo-ros2-control

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



