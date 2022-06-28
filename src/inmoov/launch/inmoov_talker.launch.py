from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='micro_ros_agent',
            executable='micro_ros_agent',
            name='node1',
            output='screen'
        ),
        Node(
            package='demo_nodes_cpp',
            executable='talker'
        )
    
    ])