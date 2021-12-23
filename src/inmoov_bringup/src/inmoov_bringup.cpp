// #include "inmoov_bringup/inmoov_bringup.hpp"
#include "rclcpp/rclcpp.hpp"

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<rclcpp::Node>("inmoov_bringup");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}




