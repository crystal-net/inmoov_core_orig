#! /bin/bash

clear

xacro -o inmoov.urdf "$(find inmoov_description)/robots/inmoov.urdf.xacro"

ros2 run xacro xacro -o inmoov.urdf "$(find inmoov_description)/robots/inmoov.urdf.xacro"

#ros2 run xacro xacro -o inmoov.urdf "$(find inmoov_description)/robots/example_robot.urdf.xacro"

#ros2 run xacro xacro -o inmoov.urdf "/inmoov/ros2_ws/src/inmoov_description/robots/example_robot.urdf.xacro"

#