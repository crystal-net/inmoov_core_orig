reStructured Test Cheat Sheet
"""""""""""""""""""""""""""""

Joint states are what ROS uses to communicate the state or movement of each joint between nodes.



    This is basically where our robot it created.

We provide it some joint data and it calculates and publishes the transforms data. We don't see the transforms directly.

To run the robot_state_publisher we use the following command

```console
ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(xacro /inmoov/ros2_ws/urdf/description/inmoov.urdf.xacro)"
```

The components of this command are as follows

| Arguement | Value |
| --- | --- |
| ROS execution | ros2 |
| ROS run package | run |
| Package to run | robot_state_publisher |
| Package executable | robot_state_publisher |
| Args list flag | --ros-args -p |
| robot description path | robot_description:= |
| path to our xacro/urdf file | /inmoov/example.urdf.xacro |

ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$( xacro /inmoov/ros2_ws/src/inmoov_description/description/example_robot.urdf.xacro)"

ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$( xacro /inmoov/alan_inmoov_ros/inmoov_description/robots/inmoov.urdf.xacro)"