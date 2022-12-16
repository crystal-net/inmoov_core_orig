# Author: Addison Sears-Collins
# Date: September 14, 2021
# Description: Launch a two-wheeled robot URDF file using Rviz.
# https://automaticaddison.com

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource

# This was an example from a video from the channel Articulated Robotics
# generate_launch_description is a parent function.
# Useful tutorials: 
#   https://roboticscasual.com/tutorial-ros2-launch-files-all-you-need-to-know/
#   https://roboticsbackend.com/ros2-launch-file-example/
#   http://design.ros2.org/articles/node_lifecycle.html
#
# the Node section is an Action imported from launch_ros.actions module
# Node is added to LaunchDescription which is a method imported from the launch py module
# Node is an action.  That means, this launch file will start the node as if you would execute
#  $ ros2 run turtlesim turtlesim_node

#
# ld in this example launcher is an object of LaunchDescription
# 





def generate_launch_description():
  # The current configuration of variables only works for a robot with one package.
  # See inmoov.launch.py for a custom version
  # Set the path to this package.
  pkg_share = FindPackageShare(package='inmoov_bringup').find('inmoov_bringup')
  print (pkg_share)

  desc_share = FindPackageShare(package='inmoov_description').find('inmoov_description')
  print (desc_share)

  # Set the path to the RViz configuration settings
  default_rviz_config_path = os.path.join(pkg_share, 'config/conf.rviz')
  print (default_rviz_config_path)

  # Set the path to the URDF file
  default_urdf_model_path = os.path.join(desc_share, 'robots/inmoov.urdf.xacro')
  print (default_urdf_model_path)

  ########### YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE ##############  
  # Launch configuration variables specific to simulation
  # I believe these create empty LaunchConfiguration objects that need to be
  #  further declared and configured
  gui = LaunchConfiguration('gui')
  urdf_model = LaunchConfiguration('urdf_model')
  rviz_config_file = LaunchConfiguration('rviz_config_file')
  use_robot_state_pub = LaunchConfiguration('use_robot_state_pub')
  use_rviz = LaunchConfiguration('use_rviz')
  use_sim_time = LaunchConfiguration('use_sim_time')


  # Declare the launch arguments  
  # These are command line arguements.
  # They all have defaults so nothing has to be specified
  # However they can be overridden using the name key
  declare_urdf_model_path_cmd = DeclareLaunchArgument(
    name='urdf_model', 
    default_value=default_urdf_model_path, 
    description='Absolute path to robot urdf file')
    
  declare_rviz_config_file_cmd = DeclareLaunchArgument(
    name='rviz_config_file',
    default_value=default_rviz_config_path,
    description='Full path to the RVIZ config file to use')
    
  declare_use_joint_state_publisher_cmd = DeclareLaunchArgument(
    name='gui',
    default_value='True',
    description='Flag to enable joint_state_publisher_gui')
  
  declare_use_robot_state_pub_cmd = DeclareLaunchArgument(
    name='use_robot_state_pub',
    default_value='True',
    description='Whether to start the robot state publisher')

  declare_use_rviz_cmd = DeclareLaunchArgument(
    name='use_rviz',
    default_value='True',
    description='Whether to start RVIZ')
    
  declare_use_sim_time_cmd = DeclareLaunchArgument(
    name='use_sim_time',
    default_value='True',
    description='Use simulation (Gazebo) clock if true')
   

  # Specify the actions
  # Publish the joint state values for the non-fixed joints in the URDF file.
  start_joint_state_publisher_cmd = Node(
    condition=UnlessCondition(gui),
    package='joint_state_publisher',
    executable='joint_state_publisher',
    name='joint_state_publisher')

  # A GUI to manipulate the joint state values
  start_joint_state_publisher_gui_node = Node(
    condition=IfCondition(gui),
    package='joint_state_publisher_gui',
    executable='joint_state_publisher_gui',
    name='joint_state_publisher_gui')

  # Subscribe to the joint states of the robot, and publish the 3D pose of each link.
  start_robot_state_publisher_cmd = Node(
    condition=IfCondition(use_robot_state_pub),
    package='robot_state_publisher',
    executable='robot_state_publisher',
    parameters=[{'use_sim_time': use_sim_time, 
    'robot_description': Command(['xacro ', urdf_model])}],
    arguments=[default_urdf_model_path])

  # Launch RViz
  start_rviz_cmd = Node(
    condition=IfCondition(use_rviz),
    package='rviz2',
    executable='rviz2',
    name='rviz2',
    output='screen',
    arguments=['-d', rviz_config_file])
  



  # Create the launch description and populate
  ld = LaunchDescription()

  # Declare the launch options
  ld.add_action(declare_urdf_model_path_cmd)
  ld.add_action(declare_rviz_config_file_cmd)
  ld.add_action(declare_use_joint_state_publisher_cmd)
  ld.add_action(declare_use_robot_state_pub_cmd)  
  ld.add_action(declare_use_rviz_cmd) 
  ld.add_action(declare_use_sim_time_cmd)

  # Add any actions
  ld.add_action(start_joint_state_publisher_cmd)
  ld.add_action(start_joint_state_publisher_gui_node)
  ld.add_action(start_robot_state_publisher_cmd)
  ld.add_action(start_rviz_cmd)

  return ld

  IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare("gazebo_ros"), '/launch', '/gazebo.launch.py'])
    )