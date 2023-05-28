import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration

def generate_launch_description():


    use_sim_time = LaunchConfiguration('use_sim_time')


    # Build configuration variables by passing the package share path each time.  We do this in order to use
    # different package share directory paths but requires extra processing
    inmoov_config = os.path.join(get_package_share_directory('inmoov_bringup'),'config','inmoov_config.yaml')
    rviz_config = os.path.join(get_package_share_directory('inmoov_bringup'),'config','conf.rviz')
    xacro_config = os.path.join(get_package_share_directory('inmoov_description'),'description','example_robot.urdf.xacro')
    default_urdf_model_path = os.path.join(get_package_share_directory('inmoov_description'), 'urdf/example_robot.urdf.xacro')




    # I think alternatively to the method above, we can get a "pkg_share" path and use that in the above definitions
    # It certainly makes things a little shorter and possible runs faster as it doesn't constantly interprate the package share path
    # Using share paths in other packages will require creating more than one pkg_share path variable
    # 
    # pkg_share = os.path.join(get_package_share_directory('inmoov_bringup'))
    # inmoov_config = os.path.join(pkg_share,'config','inmoov_config.yaml')
    # rviz_config = os.path.join(pkg_share,'config','conf.rviz')
    # xacro_config = os.path.join(pkg_share,'description','example_robot.urdf.xacro')
    # default_urdf_model_path = os.path.join(pkg_share, 'urdf/example_robot.urdf.xacro')




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
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'use_sim_time': use_sim_time, 
            'robot_description': Command(['xacro ', xacro_config])}],
            arguments=[default_urdf_model_path]
        ),
    ])


# Other possible Node() parameters
#   Don't know why these seem to be duplicates
#   node_executeable
#   node_namespace
#   node_name
# 
#   remappings=[]