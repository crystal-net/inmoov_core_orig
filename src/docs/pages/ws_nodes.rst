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
    
    
