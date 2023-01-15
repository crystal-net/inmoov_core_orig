import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
import xacro

# For more example code see: https://github.com/joshnewans/articubot_one/tree/main/launch

def generate_launch_description():


    # use_sim_time = LaunchConfiguration('use_sim_time')
    # use_ros2_control = LaunchConfiguration('use_ros2_control') 

    # Build configuration variables by passing the package share path each time.  We do this in order to use
    # different package share directory paths but requires extra processing
    inmoov_config = os.path.join(get_package_share_directory('inmoov_bringup'),'config','inmoov_config.yaml')
    rviz_config = os.path.join(get_package_share_directory('inmoov_bringup'),'config','conf.rviz')
    # xacro_config = os.path.join(get_package_share_directory('inmoov_description'),'robots','inmoov.urdf.xacro')
    xacro_config = os.path.join(get_package_share_directory('inmoov_description'),'robots','articubot_one','robot.urdf.xacro')
    robot_description_raw = xacro.process_file(xacro_config).toxml()


    # Got this from tutorial and modified as below: robot_description_config = Command(['xacro ', xacro_file, ' use_ros2_control:=', use_ros2_control, ' sim_mode:=', use_sim_time])
    # I believe this is just a way of specifying the parameters without a bunch of currly brace operations later
    # robot_description_config = Command(['use_ros2_control:=', use_ros2_control, ' sim_mode:=', use_sim_time])
    




    # I think alternatively to the method above, we can get a "pkg_share" path and use that in the above definitions
    # It certainly makes things a little shorter and possible runs faster as it doesn't constantly interprate the package share path
    # Using share paths in other packages will require creating more than one pkg_share path variable
    # 
    # pkg_share = os.path.join(get_package_share_directory('inmoov_bringup'))
    # inmoov_config = os.path.join(pkg_share,'config','inmoov_config.yaml')
    # rviz_config = os.path.join(pkg_share,'config','conf.rviz')
    # xacro_config = os.path.join(pkg_share,'description','example_robot.urdf.xacro')
    # default_urdf_model_path = os.path.join(pkg_share, 'urdf/example_robot.urdf.xacro')


    # There are a couple ways of defining a launch file.
    # The first is to define actions right inside the LaunchDescription() constructor
    #     Node(
    #             package='package_name',
    #             executable='executable inside package',
    #             name='name_of_the_node?'
    #     )
    # 
    # The next way is to create a LaunchDescription object and then trigger the actions later.
    #     ld = LaunchDescription()            # Create an object called ld
    #     some_node = Node(
    #         package='some_package',
    #         executable='some_executable',
    #         name='some_name'
    #     )
    # 
    #     ld.add_action(some_node)
    #     return ld


    #   LaunchDescription([
    #        ...,
    #        GroupAction(
    #            condition=IfCondition(use_gui),
    #            actions = [
    #                ...,
    #                SetParametersFromFile('path/to/file.yaml'),
    #                ...,
    #                Node(...),  // the Node will be started when the condition is fullfilled and params will be passed to this node
    #                ...,
    #            ]
    #        ),
    #        Node(...),  // This node is not dependent on the condition and the parameters will not be passed, as it is not in the same scope
    #        ...
    #    ])






    return LaunchDescription([
        # Node(
        #     package='demo_nodes_cpp',
        #     executable='talker',
        #     namespace='inmoov', # Namespace
        #     name='sim',                # Subnodename
        #     parameters=[inmoov_config]
        # ),
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
            package='robot_state_publisher',
            executable='robot_state_publisher',
            # name='robot_state_publisher',
            output='screen',
            # parameters=[{'robot_description': robot_description_raw, 'use_ros2_control': use_ros2_control, ' sim_mode': use_sim_time }] # add other parameters here if required
            parameters=[{'use_sim_time': True, 'robot_description': robot_description_raw}] # add other parameters here if required
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config]
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare("gazebo_ros"), '/launch', '/gazebo.launch.py'])
        ),
        Node(package='gazebo_ros', executable='spawn_entity.py',
                    arguments=['-topic', 'robot_description',
                                '-entity', 'my_bot'],
                    output='screen'
        ),


    ])


        

        # ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/model/vehicle_blue/cmd_vel

        # Node(
        #     package='micro_ros_agent',
        #     executable='micro_ros_agent',
        #     name='micro_ros_agent',
        #     arguments=["serial", "--dev", "/dev/ttyACM0"]
        # ),