import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():


    # Build configuration variables
    inmoov_config = os.path.join(get_package_share_directory('inmoov_bringup'),'config','inmoov_config.yaml')
    rviz_config = os.path.join(get_package_share_directory('inmoov_bringup'),'config','conf.rviz')
    xacro_config = os.path.join(get_package_share_directory('inmoov_description'),'description','example_robot.urdf.xacro')




    return LaunchDescription([
        Node(
            package='demo_nodes_cpp',
            executable='talker',
            namespace='inmoov', # Namespace
            name='sim',                # Subnodename
            parameters=[inmoov_config]
        ),
        Node(
            package='micro_ros_agent',
            executable='micro_ros_agent',
            name='micro_ros_agent',
            arguments=["serial", "--dev", "/dev/ttyACM0"]
        ),
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher'
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config]
        )
    ])


        #     Node(
        #     package='robot_state_publisher',
        #     executable='robot_state_publisher',
        #     parameters=[{'use_sim_time': use_sim_time, 
        #     'robot_description': Command(['xacro ', urdf_model])}],
        #     arguments=[default_urdf_model_path]
        # ),