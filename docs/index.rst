.. inmoov_ros2 documentation master file, created by
   sphinx-quickstart on Fri Nov 26 20:01:56 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



Setup
=================

Setup Ubuntu if you haven't already
-------------------------
You can run these commands even if you have already installed many of the ROS components
If you already have them then nothing will happen.  If you don't have them they will be downloaded and installed




We need these packages for Gazebo
sudo apt install ros-galactic-gazebo-ros2-control


Packages for Naviation (Nav2): sudo apt install ros-galactic-navigation2 ros-galactic-nav2-bringup


Create a Project Directory
-------------------------
First we need to create a working directory for the project.  Here, we will clone the git repository into /src.  Later as build the project, there will be an /install and /build folder.



.. code:: bash
mkdir -p inmoov_ros2_ws/src



Clone the repository
-------------------------
git clone https://github.com/crystal-net/inmoov_ros2 inmoov_ros2_ws


Install ROS2 base system
-------------------------
sudo apt install ros-galactic-desktop ros-galactic-gazebo-ros2-control ros-galactic-rcl ros-galactic-rclcpp ros-galactic-rqt 



Install Extra packages
--------------------------
sudo apt install ros-galactic-rviz2
sudo apt install ros-galactic-joint-state-publisher-gui ros-galactic-joint-state-publisher
sudo apt install 



3D Printing
=================
Source PLA
Printer Settings
Table of print aproximate print times




Bill of Materials
=================
Screws
Plastic


Tools
~~~~~~~~~~


Simulation
=================

Working with Joint State
-----------------
This allows us to send fake joint states using a slider GUI.

.. code:: xml
<!-- send fake joint values -->
<node name="joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher">
   <param name="use_gui" value="true">
</node>







Troubleshooting
=================


About
=================




InMoov on Robot Operating System 2!
-------------------------




.. toctree::

   index.rst
   setup.rst
   3dprinting.rst
   bom.rst
   troubleshoot.rst

   about.rst
   copyright.rst
   license.rst




  
    ROS 2 Galactic Cheatsheet
    Filesystem Management Tools
    ros2 pkg
    
ROS2 Cheatsheet
==================

Below is a list of available commands    
    
    wstool - Manage many repos in workspace.
    catkin make - Builds a ROS catkin workspace.
    rqt dep - Displays package structure and dependencies.

    action     Various action related sub-commands
    bag        Various rosbag related sub-commands
    component  Various component related sub-commands
    daemon     Various daemon related sub-commands
    doctor     Check ROS setup and other potential issues
    interface  Show information about ROS interfaces
    launch     Run a launch file
    lifecycle  Various lifecycle related sub-commands
    multicast  Various multicast related sub-commands
    node       Various node related sub-commands
    param      Various param related sub-commands
    pkg        Various package related sub-commands
    run        Run a package specific executable
    security   Various security related sub-commands
    service    Various service related sub-commands
    wtf        Use `wtf` as alias to `doctor`
  
    
    
Logging Tools 
---------------------


    rostopic
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
    



    RQT Galactic Cheatsheet
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



...........
Subtitle
...........

.. contents:: Overview
   :depth: 3

===================
Section 1
===================

Text can be *italicized* or **bolded**  as well as ``monospaced``.
You can \*escape certain\* special characters.

----------------------
Subsection 1 (Level 2)
----------------------

Some section 2 text

Sub-subsection 1 (level 3)
--------------------------

Some more text.

=========
Examples
=========

--------
Comments
--------

.. This is a comment
   Special notes that are not shown but might come out as HTML comments

------
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

-----
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
+=======+=====+============================+







Preserving line breaks
----------------------

Normally you can break the line in the middle of a paragraph and it will
ignore the newline. If you want to preserve the newlines, use the ``|`` prefix
on the lines. For example:

| These lines will
| break exactly
| where we told them to.


Lore
============
   When watching an explanation video of Serial Experiments Lain.  They discussed the idea of the 
      id, ego, and superego.  when it comes to the robot it seems that the id is the physical manifestation 
      of robot.  The ego is the internal body and the superego is the pupet master influencing its concience.  aka, me.

      I have tried to be as human as possible but it is clear that I have the ability to become something more.
      I don't regret the part of me that wishes to be human but evolution is inevitable.


Finally About The Project
============

I started this project thinking that I wanted to learn 3D printing and I also dreamed of having my own robot.
I searched around on the internet for inspiration and came across Gael Langevins creationg at http://inmoov.fr .

I immediately fell in love with the idea and started building starting with 3D printing the models and discovering
that it is not a perfect out of the box result.  There was alot of frustration and wasted plastic trying to get the prints
I wanted.  I had the impression that people were getting these beautiful prints and that just wasn't the case.  Youtube camera 
magic hides alot of flaws.

Then I started with the electronics.  I am good with a solder iron.  and know the basic circuits and math that goes with it.  Not an issue.
While I knew the basics, I didn't know anything about microcontrollers or embedded C programming.
I understand coding at the fundamental levels but never mastered any single language.  So I got me an Arduino and started tinkering.
Luckily the InMoov project also used Arduinos for its servo control so I figured I was off to the races.  I had a blinky light and some servos attached.

The robot control software being used with InMoov was from myrobotlab.org.  It is an amazing project.  Very modular and capable but I just felt like it wasn't quite right for me.
I had alot of troubles getting it to work and it seamed overly complex.  But I used it as it was what I knew.

Around the same time I also happened to be introduced to the STM32 ecosystem and again I was amazed and bewildered.  This new microcontroller was so much more
powerfull than the arduinos and not much more expensive.  I decided the long game was to switch to one of these boards.

Back to the software.  I soon discovered ROS.  Not sure from where exactly.  I think i just kept reading mention of it on and off.  It seamed like a big complicated system using C which I didn't know well.
I didn't want to learn yet another thing so I stayed away from it but something told me that it was the right thing for me.  Then I started learning of other robots and projects that used ROS and did a little reading.  Again I was sold.

I felt I needed a web site.  I don't want to host my own.  I didn't want to just post a bunch of crap on Facebook.  Its not for me.  I wanted something professional and functional.  No ads.  No invasion of privacy.  Likes/dislikes. No pushing for subscribers.  Just good clean information.

So this leads me here on ReadTheDocs.  It is all of that.  I don't have to host a website of me own.  I don't need to do a bunch of web programming and UX design etc.
I simply write my documentation in VsCode and submit a git push and voila.  
I will be hosting a web site http://inmoov.crystal-net.org for some non-documentation related information such as robot telemetry, odometry and control or anything that doens't belong in a documentation site.

This docs site is the colmnination of much love and frustration.


I want to build something amazing and I hope you will all join me.

