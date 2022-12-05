#! /bin/bash

clear

xacro -o inmoov.urdf "$(find inmoov_description)/robots/inmoov.urdf.xacro"

ros2 run xacro xacro -o inmoov.urdf "$(find inmoov_description)/robots/inmoov.urdf.xacro"