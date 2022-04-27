.. inmoov_ros2 documentation master file, created by
   sphinx-quickstart on Fri Nov 26 20:01:56 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MoveIt 2 Documentation
======================

Welcome to the unified MoveIt documentation, which includes tutorials, how-to-guides, core concepts, and more.

MoveIt 2 is the robotic manipulation platform for ROS 2, and incorporates the latest advances in motion planning, manipulation, 3D perception, kinematics, control, and navigation. MoveIt 2 was first released in 2019; for ROS 1 documentation, see `MoveIt 1 tutorials <https://ros-planning.github.io/moveit_tutorials>`_.

.. image:: https://moveit.ros.org/assets/images/roadmap.png
   :width: 400px




ROS is one of the best open source projects for robots that exists with extensive development contributers around the world.  
The aim of this project is to develop ROS2 modules for the InMoov https://inmoov.fr project.  To date, as far as I am aware, there is no working ROS2 modules.
An attempt was made with ROS1 https://github.com/alansrobotlab/inmoov_ros which seems to be abondoned.  I also decided to abandon as ROS2 is clearly the way to move forward.



.. toctree::
   :maxdepth: 1
   :caption: ROS2

   pages/setup_ros_workspace
   pages/setup_ros
   pages/setup_toolchain
   pages/setup_ubuntu




.. toctree::
   :maxdepth: 1
   :caption: MicroROS

   pages/3dprinting.rst
   pages/inmoov_modules.rst
   pages/microros.rst
   pages/ros-cheatsheet.rst
   pages/rst-cheetsheet.rst
   pages/troubleshoot.rst
   pages/upython.rst
   pages/ws_nodes.rst




.. toctree::
   :maxdepth: 1
   :caption: Controll and Visualization

   pages/moveit2
   pages/joystick



.. toctree::
   :maxdepth: 1
   :caption: A.I.

   pages/gpt4
   pages/yolov4




.. toctree::
   :maxdepth: 1
   :caption: Extras

   pages/why
   pages/lore

