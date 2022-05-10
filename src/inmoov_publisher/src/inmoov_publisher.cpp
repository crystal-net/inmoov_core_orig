#include "rclcpp/rclcpp.hpp" //add include path to /opt/ros/galactic/include in c_cpp_properties.json if this doesn't resolve

// Next we are going to create an executable that creates a node and this is the starting main function.  This has nothing to do with any other main function from other modules.

int main(int argc, char **argv)
{
    //Initialize ROS communication node
    rclcpp::init(argc, argv);

    //Create the ROS Node called inmoov_publisher
    auto node = std::make_shared<rclcpp::Node>("inmoov_publisher");

    RCLCPP_INFO(node->get_logger(), "hello cpp publisher node");

    //Shutdown ROS communication for this node
    rclcpp::shutdown(); 

    return 0;

}