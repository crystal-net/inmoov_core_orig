Moveit2
=================

*** Instructions from https://moveit.ros.org/install-moveit2/source/

export COLCON_WS=~/ws_moveit2/
mkdir -p $COLCON_WS/src
cd $COLCON_WS/src



git clone https://github.com/ros-planning/moveit2.git -b $ROS_DISTRO
for repo in moveit2/moveit2.repos $(f="moveit2/moveit2_$ROS_DISTRO.repos"; test -r $f && echo $f); do vcs import < "$repo"; done

rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
