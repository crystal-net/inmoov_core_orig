#!/usr/bin/env python3

# Source code taken from the youtube tutorial at: https://www.youtube.com/watch?v=l4Ph9DYqp9U

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class BaseMotorController(Node):
    def __init__ (self):
        super().__init__("base_motor_controller")
        self.twist_subscriber = self.create_subscription(Twist,"base/cmd_vel",self.send_cmd_vel,10)
        self.get_logger().info("base_motor_controller has started")

    def send_cmd_vel(self,msg):
        self.get_logger().info("trist:l Linear velocity: %f Angular velocity: %f" % (msg.linear.x, msg.angular.z))

def main(args=None):
    rclpy.init(args=args)
    node = BaseMotorController()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()