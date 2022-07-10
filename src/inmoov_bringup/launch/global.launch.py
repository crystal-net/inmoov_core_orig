# example.launch.py
# from https://docs.ros.org/en/humble/How-To-Guides/Launch-file-different-formats.html

import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.actions import GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace
import xacro
from glob import glob
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():


    rviz_path = os.path.join(get_package_share_directory('inmoov_bringup'), 'launch/conf.rviz')


    # Xacro robot definition
    # xacro_file = os.path.join(get_package_share_directory(pkg_name),file_subpath)
    file_subpath = 'description/example_robot.urdf.xacro'
    xacro_file = os.path.join(get_package_share_directory('inmoov_bringup'),file_subpath)
    robot_description_raw = xacro.process_file(xacro_file).toxml()



    # args that can be set from the command line or a default will be used
    background_r_launch_arg = DeclareLaunchArgument(
        "background_r", default_value=TextSubstitution(text="0")
    )
    background_g_launch_arg = DeclareLaunchArgument(
        "background_g", default_value=TextSubstitution(text="255")
    )
    background_b_launch_arg = DeclareLaunchArgument(
        "background_b", default_value=TextSubstitution(text="0")
    )
    chatter_ns_launch_arg = DeclareLaunchArgument(
        "chatter_ns", default_value=TextSubstitution(text="my/chatter/ns")
    )


    # include another launch file
    launch_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('demo_nodes_cpp'),
                'launch/topics/talker_listener.launch.py'))
    )


    # include another launch file in the chatter_ns namespace
    launch_include_with_namespace = GroupAction(
        actions=[
            # push_ros_namespace to set namespace of included nodes
            PushRosNamespace('chatter_ns'),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory('demo_nodes_cpp'),
                        'launch/topics/talker_listener.launch.py'))
            ),
        ]
    )


    # start a turtlesim_node in the turtlesim1 namespace
    turtlesim_node = Node(
        package='turtlesim',
        namespace='turtlesim1',
        executable='turtlesim_node',
        name='sim'
    )


    # start another turtlesim_node in the turtlesim2 namespace
    # and use args to set parameters
    turtlesim_node_with_parameters = Node(
        package='turtlesim',
        namespace='turtlesim2',
        executable='turtlesim_node',
        name='sim',
        parameters=[{
            "background_r": LaunchConfiguration('background_r'),
            "background_g": LaunchConfiguration('background_g'),
            "background_b": LaunchConfiguration('background_b'),
        }]
    )


    # perform remap so both turtles listen to the same command topic
    forward_turtlesim_commands_to_second_turtlesim_node = Node(
        package='turtlesim',
        executable='mimic',
        name='mimic',
        remappings=[
            ('/input/pose', '/turtlesim1/turtle1/pose'),
            ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
        ]
    )

# Joint State Functions
# ###############################

  # Publish the joint state values for the non-fixed joints in the URDF file.
    start_joint_state_publisher_cmd = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher')
 
  # A GUI to manipulate the joint state values
    start_joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui')
 
  # Subscribe to the joint states of the robot, and publish the 3D pose of each link.
    start_robot_state_publisher_cmd = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'use_sim_time': use_sim_time, 
        'robot_description': Command(['xacro ', urdf_model])}],
        arguments=[default_urdf_model_path])









    start_rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=[('-d'+ rviz_path),('-f', 'world')]    
        )



    # Configure the node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        name='sim',
        parameters=[{'robot_description': robot_description_raw}] # add other parameters here if required
    )

    return LaunchDescription([
        background_r_launch_arg,
        background_g_launch_arg,
        background_b_launch_arg,
        chatter_ns_launch_arg,
        launch_include,
        launch_include_with_namespace,
        turtlesim_node,
        turtlesim_node_with_parameters,
        forward_turtlesim_commands_to_second_turtlesim_node,
        start_rviz2,
        node_robot_state_publisher
    ])


# todo
#  ros2 run teleop_twist_keyboard teleop_twist_keyboard

