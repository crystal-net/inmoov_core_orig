

    
ROS2 Cheatsheet
==================

Below is a list of available commands    
    
   - wstool - Manage many repos in workspace.
   - rqt dep - Displays package structure and dependencies.

   - action     Various action related sub-commands
   - bag        Various rosbag related sub-commands
   - component  Various component related sub-commands
   - daemon     Various daemon related sub-commands
   - doctor     Check ROS setup and other potential issues
   - interface  Show information about ROS interfaces
   - launch     Run a launch file
   - lifecycle  Various lifecycle related sub-commands
   - multicast  Various multicast related sub-commands
   - node       Various node related sub-commands
   - param      Various param related sub-commands
   - pkg        Various package related sub-commands
   - run        Run a package specific executable
   - security   Various security related sub-commands
   - service    Various service related sub-commands
   - wtf        Use `wtf` as alias to `doctor`
  
    
    
Working with topics 
---------------------


   - rostopic
   - rosbag - A tool for displaying information about ROS topics, including publishers, subscribers, publishing rate, and messages.
   - ros2 topic bw - Display bandwidth used by topic.
   - ros2 topic echo - Print messages to screen.
   - ros2 topic find - Find topics by type.
   - ros2 topic hz - Display publishing rate of topic.
   - ros2 topic info - Print information about an active topic.
   - ros2 topic list - List all published topics.
   - ros2 topic pub - Publish data to topic.
   - ros2 topic type - Print topic type.
    

Working with ROS bag files
--------------------------
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
    



RQT Data Visualization
----------------------


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




Working with Joint State
------------------------
This allows us to send fake joint states using a slider GUI.

.. code:: xml

   <!-- send fake joint values -->
   <node name="joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher">
      <param name="use_gui" value="true">
   </node>





URDF Geometry Definition
========================

    Links
    
      origin rpy="0 1.57075 0" xyz="0 0 -0.3" 
      All mesurements are in relation to the parent
      rpy (roll / pitch / yaw) rotates the link (part) measured in radians?
      xyz sets the location at

      Regarding the joint definition, origin xyz="0 -0.22 0.25"
      It is defined in terms of the parents reference frame. So we are -0.22 meters in the y direction (to our left, but to the right relative to the axes) and 0.25 meters in the z direction (up).
      
      
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
==================

The basic syntax is not that different from Markdown, but it also
has many more powerful features that Markdown doesn't have. We aren't
taking advantage of those yet though.

- Odometer readings
- GPS readings
- IMU readings
- Force sensor readings

