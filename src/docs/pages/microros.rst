
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
   


   


   

Install Extra packages
----------------------

