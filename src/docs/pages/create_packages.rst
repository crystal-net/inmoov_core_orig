Building the packages for InMoov.
===============================


Keep in mind that you don't need to build these packages yourself.  You can also download the precompiled package binaries.

.. code-block:: console

   ros2 pkg create <pkg-name> --dependencies [deps] --build-type ament_cmake
   so
   ros2 pkg create inmoov_msgs --dependencies rclcpp --build-type ament_cmake
   ros2 pkg create inmoov_bringup --dependencies rclcpp --build-type ament_python
   ros2 pkg create inmoov_msgs --dependencies rclcpp --build-type ament_cmake
   ros2 pkg create inmoov_msgs --dependencies rclcpp --build-type ament_cmake
   ros2 pkg create inmoov_msgs --dependencies rclcpp --build-type ament_cmake
   ros2 pkg create inmoov_msgs --dependencies rclcpp --build-type ament_cmake