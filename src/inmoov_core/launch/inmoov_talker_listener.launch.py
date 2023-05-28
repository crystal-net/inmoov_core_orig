import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro


def generate_launch_description():
   # In this part of the function we define objects inmoov_node and rviz_node
   # to be later launched in the return function below

   inmoov_talker = Node (
      package='inmooov_bringup.py',
      namespace='inmoov',
      executable='inmoov_talker.py',
      name='inmoov_talker'
   ),
   inmoov_listener = Node (
      package='inmooov_bringup.py',
      namespace='inmoov',
      executable='inmoov_listener.py',
      name='inmoov_listener'
   ),
   rviz_node = Node (
      package='rviz2',
      namespace='inmoov',
      executable='rviz2',
      name='inmoov_rviz2'
   )

   # This takes our objects defined above and launches them
   return LaunchDescription([
      inmoov_talker,
      inmoov_listener,
      rviz_node
   ])










# # =========================

#     # Use xacro to process the file
#     xacro_file = os.path.join(get_package_share_directory(pkg_name),file_subpath)
#     robot_description_raw = xacro.process_file(xacro_file).toxml()


#     # Configure the node
#     node_robot_state_publisher = Node(
#         package='robot_state_publisher',
#         executable='robot_state_publisher',
#         output='screen',
#         parameters=[{'robot_description': robot_description_raw}] # add other parameters here if required
#     )


#     # node_rviz2 = Node(package='rviz2', node_executable='rviz2', output='screen')


#     # Run the node
#     return LaunchDescription([
#         node_robot_state_publisher
#     ])

#     # Run the rviz2
#     # return LaunchDescription([
#     #     node_rviz2
#     # ])



