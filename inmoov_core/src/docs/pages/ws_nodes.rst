.. code-block:: console

   ros2 pkg create --build-type ament_cmake inmoov_awaken
   
   
   
   
We need to creates some nodes inside our package.  This takes the format  
      
   ros2 pkg create --build-type ament_cmake --node-name my_node my_package

.. code-block:: console

    ros2 pkg create --build-type ament_cmake --node-name inmoov_nodes sight
    ros2 pkg create --build-type ament_cmake --node-name inmoov_nodes listen
    ros2 pkg create --build-type ament_cmake --node-name inmoov_nodes speach
    ros2 pkg create --build-type ament_cmake --node-name inmoov_nodes sensation
    ros2 pkg create --build-type ament_cmake --node-name inmoov_nodes telemetry
    ros2 pkg create --build-type ament_cmake --node-name inmoov_nodes 
    
    
These are the nodes that I think I'll need to create eventually.
   
   my_robot
   my_robot_base
   my_robot_bringup 
   my_robot_description
   my_robot_gazebo
   my_robot_kinematics
   my_robot_localization
   my_robot_manipulation
   my_robot_moveit_config
   my_robot_msgs 
   my_robot_navigation
   my_robot_teleop
   my_robot_tests
   my_robot_rviz_plugins