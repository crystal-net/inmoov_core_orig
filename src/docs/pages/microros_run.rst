
Running a Working MicroROS Build
=====================


Now we have finally built a microros instance on our microcontroller and have the agent build and installed on the host.
Its finally time to run it and see if everything is working.


# Start the Agent (doesn't matter what the microcontroll is programmed for.  This is just a bridge)
.. code-block:: console
  
  ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyACM0

**Note this is easy to remember if you think about the fact you are running the micro_ros_agent package from within contains the micro_ros_agent executable and connecting by serial to /dev/ttyACM0


Alternatively, you can connect via the device ID which is a long string of characters and requires the ability to copy and paste into you terminal
.. code-block:: console

  ls /dev/serial/by-id/*

