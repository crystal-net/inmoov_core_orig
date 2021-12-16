ROS2 Cheat Sheet
"""""""""""""""""


    
    Logging Tools rostopic
    rosbag - A tool for displaying information about ROS topics, including publishers, subscribers, publishing rate, and messages.
    Commands:
    ros2 topic bw - Display bandwidth used by topic.
    ros2 topic echo - Print messages to screen.
    ros2 topic find - Find topics by type.
    ros2 topic hz - Display publishing rate of topic.
    ros2 topic info - Print information about an active topic.
    ros2 topic list - List all published topics.
    ros2 topic pub - Publish data to topic.
    ros2 topic type - Print topic type.
    
    
    A set of tools for recording and playing back of ROS topics.
    Commands:
    rosbag record - Record a bag file with specified topics.
    rosbag play - Play content of one or more bag files.
    rosbag compress - Compress one or more bag files.
    rosbag decompress - Decompress one or more bag files.
    rosbag filter - Filter the contents of the bag.
    
    Examples:
    Record select topics:
    $ rosbag record topic1 topic2
    Replay all messages without waiting:
    $ rosbag play -a demo log.bag
    Replay several bag files at once:
    $ rosbag play demo1.bag demo2.bag
    Usage:
    
    Introspection and Command Tools
    $ rospack find [package]
    $ roscd [package[/subdir]]
    $ rosmsg/rossrv
    $ rospd [package[/subdir] | +N | -N]
    $ rosd - Displays Message/Service (msg/srv) data structure definitions.
    $ rosls [package[/subdir]]
    $ rosmsg show - Display the fields in the msg/srv.
    $ rosed [package] [file]
    $ rosmsg list - Display names of all msg/srv.
    $ roscp [package] [file] [destination]
    # rosmsg md5 - Display the msg/srv md5 sum.
    $ rosdep install [package]
    $ rosmsg package - List all the msg/srv in a package.
    $ roswtf or roswtf [file]
    



    ROS Galactic Cheatsheet
    rqt_console
    rqt_bag
    rqt_logger_level
    rqt_topic
    rqt_msg
    rqt_srv
    rqt_action
    rqt_publisher
    rqt_service_caller
    rqt_graph
    rqt_dep
    rqt_topic
    rqt_reconfigure
    rqt_shell
    rqt_py_console

    Data Visualization
    tf_echo
    view_frames
    rqt_plot
    rqt_image_view


    ROS Indigo Catkin Workspaces
    Create a catkin workspace
    Setup and use a new catkin workspace from scratch.
    Example:
    $ source /opt/ros/hydro/setup.bash
    $ mkdir -p ~/catkin ws/src
    $ cd ~/catkin ws/src
    $ catkin init workspace
    
    Checkout an existing ROS package
    Get a local copy of the code for an existing package and keep it up to date using wstool.
    Examples:
    $ cd ~/catkin ws/src
    $ wstool init
    $ wstool set tutorials --git git://github.com/ros/ros tutorials.git
    $ wstool update
    
    Create a new catkin ROS package
    Create a new ROS catkin package in an existing workspace with catkin create package. After using this you will need to
    edit the CMakeLists.txt to detail how you want your package built and add information to your package.xml.
    Usage:
    $ catkin create pkg <package name> [depend1] [depend2]
    Example:
    $ cd ~/catkin ws/src
    $ catkin create pkg tutorials std msgs rospy roscpp
    
    Build all packages in a workspace
    Use catkin make to build all the packages in the workspace and then source the setup.bash to add the workspace to the ROS PACKAGE PATH.
    Examples:
    $ cd ~/catkin ws
    $ ~/catkin make
    $ source devel/setup.bash

    Notes
      Joint Types
      There are three kinds of joints that move around in space. 
      Prismatic joint can only move along one dimension (in and out?)
      Planar joint can move around in a plane, or two dimensions. 
      Floating joints are unconstrained, and can move around in any of the three dimensions. These joints cannot be specified by just one number, and therefore aren’t included in this tutorial.

    
    rosparam load my_robot.urdf robot_description
      
    
    I want to just view a new URDF in rviz without my inmoov stuff
    
    roslaunch urdf_tutorial display.launch model:=urdf/easyjoint.urdf.xacro

    URDF Geometry Definition
    Links
    
      origin rpy="0 1.57075 0" xyz="0 0 -0.3" 
      All mesurements are in relation to the parent
      rpy (roll / pitch / yaw) rotates the link (part) measured in radians?
      xyz sets the location at

      Regarding the joint definition, origin xyz="0 -0.22 0.25"
      It is defined in terms of the parent’s reference frame. So we are -0.22 meters in the y direction (to our left, but to the right relative to the axes) and 0.25 meters in the z direction (up).
      
      
      With respect to the **LINK** while looking at the front of the model.
      Changing these values is independant of the joint (the RGB crosshairs).
      Technically the link(part) can be outside the joint but will still move in reference to it.
      Parameters are measured in meters and radians?
      (x)(RED) a positive value moves the part forward (closer) from the horizon, negative moves the part back
      (y)(GREEN) a positive value moves right, a negative value moves the part left
      (z)(BLUE) a positive vlue moves up, a negative value moves the part down
      
      (r) horizon, negative moves the part back
      (p) moves the part left
      (y) part down
      
      With respect to the **JOINT** while looking at the front of the model
      (x)(RED) a positive value moves the part forward (closer) from the horizon, negative moves the part back
      (y)(GREEN) a positive value moves right, a negative value moves the part left
      (z)(BLUE) a positive vlue moves up, a negative value moves the part down
      



Telemetry
----------

The basic syntax is not that different from Markdown, but it also
has many more powerful features that Markdown doesn't have. We aren't
taking advantage of those yet though.

- Odometer readings
- GPS readings
- IMU readings
- Force sensor readings


.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* InMoov Telemetry: http://www.crystal-net.org





Subtitle
...........

.. contents:: Overview
   :depth: 3


Section 1
===================

Text can be *italicized* or **bolded**  as well as ``monospaced``.
You can \*escape certain\* special characters.



Sub-subsection 1 (level 3)
--------------------------

Some more text.


Examples
=========


Comments
--------

.. This is a comment
   Special notes that are not shown but might come out as HTML comments


Images
------

Add an image with:

.. image:: screenshots/file.png
   :height: 100
   :width: 200
   :alt: alternate text

You can inline an image or other directive with the |customsub| command.

.. |customsub| image:: image/image.png
              :alt: (missing image text)


Lists
-----

- Bullet are made like this
- Point levels must be consistent
    * Sub-bullets
        + Sub-sub-bullets
- Lists

Term
    Definition for term
Term2
    Definition for term 2

:List of Things:
    item1 - these are 'field lists' not bulleted lists
    item2
    item 3

:Something: single item
:Someitem: single item

-----------------
Preformatted text
-----------------

A code example prefix must always end with double colon like it's presenting something::

    Anything indented is part of the preformatted block
   Until
  It gets back to
 Allll the way left

Now we're out of the preformatted block.

------------
Code blocks
------------

There are three equivalents: ``code``, ``sourcecode``, and ``code-block``.

.. code:: python

   import os
   print(help(os))

.. code:: C

   if (x=1, 1, 1) 

.. sourcecode::

  # Equivalent

.. code-block::

  # Equivalent

-----
Links
-----

Web addresses by themselves will auto link, like this: https://www.devdungeon.com

You can also inline custom links: `Google search engine <https://www.google.com>`_

This is a simple link_ to Google with the link defined separately.

.. _link: https://www.google.com

This is a link to the `Python website`_.

.. _Python website: http://www.python.org/

This is a link back to `Section 1`_. You can link based off of the heading name
within a document.

---------
Footnotes
---------

Footnote Reference [1]_

.. [1] This is footnote number one that would go at the bottom of the document.

Or autonumbered [#]

.. [#] This automatically becomes second, based on the 1 already existing.

-----------------
Lines/Transitions
-----------------

Any 4+ repeated characters with blank lines surrounding it becomes an hr line, like this.

====================================

------
Bill of Materials
------

+-------+-----+----------------------------+
| Screw | Qty | Link to suggested supplier |
+=======+=====+============================+
| M2    | 42  | 2                          |
+-------+-----+----------------------------+
| M3    | 23  | http://somesite.com        |
+-------+-----+----------------------------+
| M4    | 23  | http://somesite.com        |
+-------+-----+----------------------------+
| M5    | 23  | http://somesite.com        |
+-------+-----+----------------------------+
| M6    | 23  | http://somesite.com        |
+-------+-----+----------------------------+







Preserving line breaks
----------------------

Normally you can break the line in the middle of a paragraph and it will
ignore the newline. If you want to preserve the newlines, use the ``|`` prefix
on the lines. For example:

| These lines will
| break exactly
| where we told them to.


 

    You can use ``backticks`` for showing ``highlighted`` code.




