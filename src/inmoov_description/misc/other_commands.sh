#!/bin/bash

ros2 launch urdf_tutorial display.launch model:=inmoov_grey.urdf gui:=True

# ros2 launch ros_gz_sim_demos air_pressure.launch.py

# ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/model/vehicle_blue/cmd_vel