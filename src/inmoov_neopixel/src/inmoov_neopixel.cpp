/* ****************************
This module is a publisher template for InMoov.
We intend to use it as a building block for more complicated message data.
*******************************/

// add include path to /opt/ros/galactic/include in c_cpp_properties.json if this doesn't resolve
#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class InmoovNeoPixelNode
  : public rclcpp::Node  // MODIFY NAME  Ex. if this was a led controller node it would be called LedControllerNode
{
public:
  InmoovNeoPixelNode()
    : Node("inmoov_neopixel_node"), robot_name_("Inmoov1")  // MODIFY NAME  node_name would be similar to led_controller
  {
    publisher_ = this->create_publisher<example_interfaces::msg::String>("inmoov_state", 10);
    timer_ = this->create_wall_timer(std::chrono::microseconds(500), std::bind(&InmoovNeoPixelNode::publishPixelState, this));
    RCLCPP_INFO(this->get_logger(), "neopixel node initialized");
    
  }

private:
  void publishPixelState()
  {
    auto msg = example_interfaces::msg::String();
    msg.data = std::string("This is ") + robot_name_ + std::string("inmoov_neopixel_node");
    publisher_->publish(msg);
  }

  std::string robot_name_;

  rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
};

// Next we are going to create an executable that creates a node and this is the starting main function.
// This has nothing to do with any other main function from other modules.
int main(int argc, char** argv)
{
  // Initialize ROS communication node
  rclcpp::init(argc, argv);

  // Create the ROS Node called InmoovNeoPixelNode
  // rclcpp::Node is a type
  // make_shared is used heavily by ROS and is part of CPP for managing pointers
  auto node = std::make_shared<InmoovNeoPixelNode>();  // MODIFY NAME

  // Spinning the node will run the node object and log using RCLCPP_INFO repeatedly till you press CTRL-C.
  // At this time the node will be shutdown and the pointer destroyed as we are using make_shared
  rclcpp::spin(node);

  // Shutdown ROS communication for this node when CTRL-C is pressed.
  // Because we used make_shared, prointers will be destroyed appropriately.
  rclcpp::shutdown();
  return 0;
}
// Ensure to modify CMakeLists.txt to create compile and create the executable.