/* This module is a publisher template for InMoov.  We intend to use it as a building block for more complicated message data. */


//add include path to /opt/ros/galactic/include in c_cpp_properties.json if this doesn't resolve
#include "rclcpp/rclcpp.hpp" 
#include "example_interfaces/msg/string.hpp"


// OOP Methode
class publisherNode: public rclcpp::Node
{
    public:
        publisherNode(): Node("inmoov_publisher")
        {
            // RCLCPP_INFO(this->get_logger(), "Hello World");
            publisher_ = create_publisher<example_interfaces::msg::String>("robot_news",10);
            
        }

    private:
        rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
        
};

// Next we are going to create an executable that creates a node and this is the starting main function.  This has nothing to do with any other main function from other modules.
int main(int argc, char **argv)
{
    //Initialize ROS communication node
    rclcpp::init(argc, argv);

    //Create the ROS Node called inmoov_publisher
    // rclcpp::Node is a type
    // inmoov_publisher is just an abitrary name for the node
    // make_shared is used heavily by ROS and is part of CPP for managing pointers
    auto node = std::make_shared<rclcpp::Node>("inmoov_publisher");

    //RCLCPP_INFO is part of RCLCPP
    RCLCPP_INFO(node->get_logger(), "hello cpp publisher node");

    //Spinning the node will run the node object and log using RCLCPP_INFO repeatedly till you press CTRL-C.
    //At this time the node will be shutdown and the pointer destroyed as we are using make_shared
    rclcpp::spin(node);


    //Shutdown ROS communication for this node
    rclcpp::shutdown(); 
    return 0;
}
// Ensure to modify CMakeLists.txt to create compile and create the executable.