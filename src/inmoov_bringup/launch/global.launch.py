import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    config = os.path.join(
      get_package_share_directory('inmoov_bringup'),
      'config',
      'inmoov_config.yaml'
    )

    return LaunchDescription([
        Node(
            package='demo_nodes_cpp',
            executable='talker',
            namespace='inmoov', # Namespace
            name='sim',                # Subnodename
            parameters=[config]
        ),
        Node(
            package='micro_ros_agent',
            executable='micro_ros_agent',
            name='micro_ros_agent',
            arguments=["serial", "--dev", "/dev/ttyACM0"]

            # namespace='inmoov', # Namespace
            # name='uros',                # Subnodename
            # parameters=[{'serial --dev /dev/ttyACM0'}]
        )])